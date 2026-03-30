import pandas as pd
import re
import string
from sklearn.model_selection import train_test_split

def clean_text(text):
    text = str(text).lower()
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    text = re.sub('\s+', ' ', text).strip()
    return text

def preprocess_dataset(file_path):
    df = pd.read_csv(file_path)
    df['cleaned_text'] = df['review_text'].apply(clean_text)
    
    # Map rating to sentiment labels
    def map_sentiment(rating):
        if rating >= 4: return "Positive"
        elif rating <= 2: return "Negative"
        else: return "Neutral"
    
    df['sentiment'] = df['rating'].apply(map_sentiment)
    
    # Split for training (though we'll use pre-trained BERT, this is for demonstration)
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    
    train.to_csv("train_reviews.csv", index=False)
    test.to_csv("test_reviews.csv", index=False)
    
    print("Data preprocessed and saved as train_reviews.csv and test_reviews.csv")
    return df

if __name__ == "__main__":
    preprocess_dataset("hotel_reviews.csv")
