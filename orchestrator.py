import os
from agents.data_agent import DataAgent
from agents.cleaning_agent import CleaningAgent
from agents.learning_agent import LearningAgent
from agents.strategy_agent import StrategyAgent

class AgenticOrchestrator:
    def __init__(self):
        self.data_agent = DataAgent()
        self.cleaning_agent = CleaningAgent()
        self.learning_agent = LearningAgent()
        self.strategy_agent = StrategyAgent()
        self._initialize_system()

    def _initialize_system(self):
        """Pre-trains the model if base data exists."""
        base_data = "data/raw_data.txt"
        if os.path.exists(base_data):
            # Using errors='ignore' to prevent UnicodeDecodeErrors
            with open(base_data, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                # FIX: Actually train the model during bootup
                clean_content = self.cleaning_agent.clean(content)
                self.learning_agent.train(clean_content)

    def run_logic(self, uploaded_file, user_sentence):
        file_content = ""
        if uploaded_file:
            # Data Agent saves the file and returns text
            file_content = self.data_agent.handle_upload(uploaded_file)
            
        clean_sentence = self.cleaning_agent.clean(user_sentence)
        prediction, confidence = self.learning_agent.predict(clean_sentence)
        
        strategy_decision = self.strategy_agent.evaluate_action(confidence)
        
        if strategy_decision == "RETRAIN" and file_content:
            # FIX: Update model with new data if confidence is low
            clean_file_text = self.cleaning_agent.clean(file_content)
            self.learning_agent.train(clean_file_text)
            strategy_log = "Low confidence detected. Model updated with new data."
        else:
            strategy_log = "Normal Execution: Model confidence is sufficient."

        return {
            "prediction": prediction,
            "confidence": confidence,
            "vocab_size": len(self.learning_agent.vocab),
            "strategy_log": strategy_log
        }