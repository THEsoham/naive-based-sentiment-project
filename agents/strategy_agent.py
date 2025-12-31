class StrategyAgent:
    def decide_action(self, confidence_score, threshold=1.5):
        """Triggers adaptation autonomously (Blueprint 5.6)."""
        if confidence_score < threshold:
            return "ADAPT_MODEL"
        return "STAY_STABLE"