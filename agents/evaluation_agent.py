class EvaluationAgent:
    def get_metrics(self, scores):
        """Computes confidence and prediction (Blueprint 5.5)."""
        # Confidence is the absolute difference between log scores
        confidence = abs(scores['positive'] - scores['negative'])
        
        if scores['positive'] > scores['negative']:
            prediction = "positive"
        else:
            prediction = "negative"
            
        return prediction, confidence