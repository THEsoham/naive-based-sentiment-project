import re

class CleaningAgent:
    def clean(self, text):
        # From your notebook: HTML removal, Lowercasing, Normalization
        text = re.sub(r'<[^>]+>', ' ', text)
        text = text.lower()
        # Normalizes "goooood" to "good"
        text = re.sub(r'(.)\1{2,}', r'\1\1', text)
        text = re.sub(r'[^a-z\s]', ' ', text)
        return " ".join(text.split())