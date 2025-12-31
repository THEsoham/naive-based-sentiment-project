from agents.data_agent import DataAgent
from agents.cleaning_agent import CleaningAgent
from agents.feature_agent import FeatureAgent
from agents.learning_agent import LearningAgent
from agents.evaluation_agent import EvaluationAgent
from agents.strategy_agent import StrategyAgent

class Orchestrator:
    def __init__(self):
        # Initializing all agents defined in your blueprint
        self.data_agent = DataAgent()
        self.cleaning_agent = CleaningAgent()
        self.feature_agent = FeatureAgent()
        self.learning_agent = LearningAgent()
        self.evaluation_agent = EvaluationAgent()
        self.strategy_agent = StrategyAgent()

    def boot_up(self, file_path):
        raw_df = self.data_agent.collect_data(file_path)
        
        for _, row in raw_df.iterrows():
            clean_text = self.cleaning_agent.clean(row['text'])
            sentiment = "positive" if row['score'] > 3.0 else "negative"
            
            # CHECK THIS LINE: Does it match the name in feature_agent.py?
            self.feature_agent.update_features(clean_text, sentiment)
        
        print(f"Orchestrator: Boot-up complete. Vocab Size: {len(self.feature_agent.vocab)}")

    def run_inference(self, raw_input, true_label=None):
        """Phase 2: Prediction and Adaptation Loop (Blueprint 6.V - 6.VIII)"""
        # 1. Cleaning
        clean = self.cleaning_agent.clean(raw_input)
        # 2. Learning Agent calculates scores
        scores = self.learning_agent.get_log_likelihoods(self.feature_agent, clean)
        # 3. Evaluation Agent gets confidence
        pred, conf = self.evaluation_agent.get_metrics(scores)
        
        print(f"Prediction: {pred} | Confidence Score: {conf:.2f}")

        # 4. Strategy Agent decides on autonomous adaptation
        action = self.strategy_agent.decide_action(conf)
        if action == "ADAPT_MODEL" and true_label:
            print("Strategy Agent: Low confidence detected. Updating features autonomously...")
            self.feature_agent.update_features(clean, true_label)
            
        return pred