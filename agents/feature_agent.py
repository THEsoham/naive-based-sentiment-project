from collections import Counter

class FeatureAgent:
    def __init__(self):
        self.vocab = set()
        self.pos_word_counts = Counter()
        self.neg_word_counts = Counter()
        self.pos_total_count = 0
        self.neg_total_count = 0

    # Ensure this name is exactly 'update_features'
    def update_features(self, tokens, sentiment):
        words = tokens.split()
        self.vocab.update(words)
        if sentiment == "positive":
            self.pos_word_counts.update(words)
            self.pos_total_count += len(words)
        else:
            self.neg_word_counts.update(words)
            self.neg_total_count += len(words)