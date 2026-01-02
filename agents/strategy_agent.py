class StrategyAgent:
    def __init__(self, confidence_threshold=0.6):
        # The threshold determines when the agent gets "worried"
        self.confidence_threshold = confidence_threshold

    def evaluate_action(self, confidence):
        """
        Decides whether to simply report the result or trigger a retrain.
        """
        # If the model is not sure (confidence is low), trigger a retrain
        if confidence < self.confidence_threshold:
            return "RETRAIN"
        
        # Otherwise, keep current model state
        return "REPORT"