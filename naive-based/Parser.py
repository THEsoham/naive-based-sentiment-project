def parse_reviews_txt(file_path, add_sentiment=True):

    texts = []
    scores = []

    current_text = None
    current_score = None

    # Read file line by line
    with open(file_path, "r", encoding="latin-1") as file:
        for line in file:
            line = line.strip()

            # Extract score
            if line.startswith("review/score:"):
                try:
                    current_score = float(line.split("review/score:")[1].strip())
                except ValueError:
                    current_score = None

            # Extract review text
            elif line.startswith("review/text:"):
                current_text = line.split("review/text:")[1].strip()

            # Store review once both are available
            if current_text is not None and current_score is not None:
                if current_text != "":   # avoid empty reviews
                    texts.append(current_text)
                    scores.append(current_score)

                current_text = None
                current_score = None

    # Create DataFrame
    df = pd.DataFrame({
        "text": texts,
        "score": scores
    })

    # Optional: convert score to sentiment label
    if add_sentiment:
        df["sentiment"] = df["score"].apply(
            lambda x: "positive" if x >= 4
            else "negative" if x <= 2
            else "neutral"
        )

    return df


# ------------------------
# Run & Preview
# ------------------------
df = parse_reviews_txt("/content/foods.txt")
print(df.head())
print("\nDataset shape:", df.shape)