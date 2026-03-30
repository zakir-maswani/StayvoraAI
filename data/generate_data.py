import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_hotel_reviews(num_reviews=1000):
    aspects = {
        "Room": ["spacious", "dirty", "comfortable", "small", "quiet", "noisy", "clean", "bed"],
        "Staff": ["friendly", "rude", "helpful", "slow", "professional", "unwelcoming", "kind"],
        "Food": ["delicious", "cold", "tasty", "limited", "breakfast", "buffet", "expensive"],
        "Cleanliness": ["spotless", "dusty", "hygienic", "dirty", "moldy", "fresh"]
    }
    
    customer_types = ["Business", "Solo", "Couple", "Family", "Group"]
    sentiments = ["Positive", "Negative", "Neutral"]
    
    reviews = []
    start_date = datetime(2025, 1, 1)
    
    for i in range(num_reviews):
        # Pick a random aspect and sentiment
        aspect = random.choice(list(aspects.keys()))
        sentiment = random.choices(sentiments, weights=[0.5, 0.3, 0.2])[0]
        
        if sentiment == "Positive":
            adj = random.choice([a for a in aspects[aspect] if a not in ["dirty", "small", "noisy", "rude", "slow", "unwelcoming", "cold", "limited", "expensive", "dusty", "moldy"]])
            text = f"The {aspect.lower()} was {adj}. Really enjoyed my stay!"
            rating = random.randint(4, 5)
        elif sentiment == "Negative":
            adj = random.choice([a for a in aspects[aspect] if a in ["dirty", "small", "noisy", "rude", "slow", "unwelcoming", "cold", "limited", "expensive", "dusty", "moldy"]])
            text = f"The {aspect.lower()} was {adj}. Very disappointed with the service."
            rating = random.randint(1, 2)
        else:
            text = f"The {aspect.lower()} was okay. Nothing special but met basic needs."
            rating = 3
            
        # Add some variety
        if random.random() > 0.7:
            text += " I would consider coming back if things improve."
            
        date = start_date + timedelta(days=random.randint(0, 400))
        customer_type = random.choice(customer_types)
        
        reviews.append({
            "review_text": text,
            "rating": rating,
            "date": date.strftime("%Y-%m-%d"),
            "customer_type": customer_type
        })
        
    df = pd.DataFrame(reviews)
    df.to_csv("hotel_reviews.csv", index=False)
    print(f"Generated {num_reviews} reviews and saved to hotel_reviews.csv")

if __name__ == "__main__":
    generate_hotel_reviews()
