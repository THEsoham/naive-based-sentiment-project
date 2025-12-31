import math

class LearningAgent:
    def get_log_likelihoods(self, feature_agent, tokens):
        """Calculates probabilities using Laplace smoothing (Blueprint 5.4)."""
        words = tokens.split()
        v_size = len(feature_agent.vocab)
        
        # Start with log(0.5) for priors (neutral starting point)
        pos_score = math.log(0.5)
        neg_score = math.log(0.5)
        
        for word in words:
            # Laplace Smoothing: (count + 1) / (total_words + vocab_size)
            # Probability of word given Positive
            pos_count = feature_agent.pos_word_counts[word]
            p_w_pos = (pos_count + 1) / (feature_agent.pos_total_count + v_size)
            pos_score += math.log(p_w_pos)
            
            # Probability of word given Negative
            neg_count = feature_agent.neg_word_counts[word]
            p_w_neg = (neg_count + 1) / (feature_agent.neg_total_count + v_size)
            neg_score += math.log(p_w_neg)
            
        return {"positive": pos_score, "negative": neg_score}