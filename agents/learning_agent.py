import json
import os

class LearningAgent:
    def __init__(self, model_path="data/models/weights.json"):
        self.model_path = model_path
        self.vocab = {}  # {word: {pos: count, neg: count}}
        self.class_counts = {"pos": 0, "neg": 0}
        self.load_model()

    def load_model(self):
        if os.path.exists(self.model_path):
            with open(self.model_path, 'r') as f:
                data = json.load(f)
                self.vocab = data['vocab']
                self.class_counts = data['counts']

    def save_model(self):
        with open(self.model_path, 'w') as f:
            json.dump({'vocab': self.vocab, 'counts': self.class_counts}, f)

    def train_incremental(self, text, label):
        # Update your Naive Bayes dictionaries here
        # ... (your existing logic) ...
        self.save_model() # Save after learning