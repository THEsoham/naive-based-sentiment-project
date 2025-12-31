import pandas as pd

class DataAgent:
    def collect_data(self, file_path):
        texts, scores = [], []
        current_text, current_score = None, None

        with open(file_path, "r", encoding="latin-1") as f:
            for line in f:
                line = line.strip()
                if line.startswith("review/score:"):
                    current_score = float(line.split(":")[1])
                elif line.startswith("review/text:"):
                    current_text = line.split(":")[1]
                
                if current_text and current_score:
                    texts.append(current_text)
                    scores.append(current_score)
                    current_text, current_score = None, None
        
        df = pd.DataFrame({"text": texts, "score": scores})
        if df.empty:
            print("Data Agent: Warning! No data collected.")
        return df