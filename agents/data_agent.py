import pandas as pd

class DataAgent:
    def collect_data(self, file_path):
        # Based on your notebook's parse_reviews_txt function
        texts, scores = [], []
        current_text, current_score = None, None

        with open(file_path, "r", encoding="latin-1") as file:
            for line in file:
                line = line.strip()
                if line.startswith("review/score:"):
                    current_score = float(line.split("review/score:")[1])
                elif line.startswith("review/text:"):
                    current_text = line.split("review/text:")[1]
                
                if current_text and current_score:
                    texts.append(current_text)
                    scores.append(current_score)
                    current_text, current_score = None, None

        df = pd.DataFrame({"text": texts, "score": scores})
        # Detect noise: Check for empty reviews or missing labels
        if df.isnull().values.any():
            print("Data Agent: Warning! Missing labels detected.")
        return df