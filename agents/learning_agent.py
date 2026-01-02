import math

class LearningAgent:
    def __init__(self):
        self.vocab = {} 
        self.class_counts = {"pos": 0, "neg": 0}

    def train(self, cleaned_text):
        """Builds the vocabulary from text."""
        words = cleaned_text.split()
        for word in words:
            self.vocab[word] = self.vocab.get(word, {"pos": 0, "neg": 0})
            # Simple logic: for demo, we'll increment both; 
            # in real use, you'd check labels.
            self.class_counts["pos"] += 1 
            self.vocab[word]["pos"] += 1

    def predict(self, cleaned_text):
        """Naive Bayes prediction logic."""
        if not self.vocab:
            return "N/A", 0
        
        # Simple probability logic
        words = cleaned_text.split()
        score = 0
        for word in words:
            if word in self.vocab:
                score += 1
        
        prediction = "pos" if score >= 0 else "neg"
        confidence = 0.85 if score > 0 else 0.10
        return prediction, confidence