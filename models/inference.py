import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StayvoraEngine:
    """
    Stayvora AI Engine: A production-ready NLP pipeline for hotel review analysis.
    Features: Sentiment Analysis, Aspect Detection, Summarization, and Complaint Detection.
    """
    def __init__(self):
        # Determine device (GPU if available, else CPU)
        self.device = 0 if torch.cuda.is_available() else -1
        logger.info(f"Initializing StayvoraEngine on device: {'GPU' if self.device == 0 else 'CPU'}")
        
        try:
            # Sentiment Analysis Model: nlptown/bert-base-multilingual-uncased-sentiment
            # This model is pre-trained specifically for star ratings (1-5).
            self.sentiment_model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
            self.sentiment_pipeline = pipeline(
                "sentiment-analysis", 
                model=self.sentiment_model_name,
                device=self.device
            )
            
            # Summarization: Using text-generation as a robust fallback
            # This avoids 'Unknown task summarization' errors in some environments.
            self.summarizer = pipeline(
                "text-generation", 
                model="gpt2",
                device=self.device
            )
            
            # Aspects to monitor
            self.aspects = ["Room", "Staff", "Food", "Cleanliness", "Price", "Location", "Service", "Wifi"]
            logger.info("StayvoraEngine initialized successfully.")
            
        except Exception as e:
            logger.error(f"Error initializing StayvoraEngine: {str(e)}")
            raise e

    def get_sentiment(self, text: str):
        """Analyze sentiment and map to Positive, Neutral, or Negative."""
        if not text or len(text.strip()) == 0:
            return "Neutral", 0.0
            
        try:
            # Truncate text to fit model limits
            result = self.sentiment_pipeline(text[:512])[0]
            
            # Mapping star labels (e.g., '1 star', '5 stars') to sentiment
            label = result['label']
            score = result['score']
            star_rating = int(label.split()[0])
            
            if star_rating >= 4:
                return "Positive", score
            elif star_rating <= 2:
                return "Negative", score
            else:
                return "Neutral", score
        except Exception as e:
            logger.warning(f"Sentiment analysis failed for text: {text[:50]}... Error: {str(e)}")
            return "Neutral", 0.0

    def detect_aspects(self, text: str):
        """Detect hotel-related aspects in the review text."""
        detected = {}
        text_lower = text.lower()
        
        # Simple keyword-based aspect detection for performance
        # In a full production system, this could be a zero-shot classifier.
        for aspect in self.aspects:
            if aspect.lower() in text_lower:
                # Get a localized sentiment for the aspect (simplified here as overall sentiment)
                sentiment, _ = self.get_sentiment(text)
                detected[aspect] = sentiment
        return detected

    def summarize_reviews(self, reviews_list: list, max_reviews: int = 5):
        """Generate a concise summary of multiple reviews using a text-generation prompt."""
        if not reviews_list:
            return "No reviews available to summarize."
            
        try:
            # Combine reviews (limit total length)
            combined_text = " ".join(reviews_list[:max_reviews])
            if len(combined_text) < 50:
                return combined_text
                
            # Use a prompt-based summarization approach
            prompt = f"Summarize the key points of these hotel reviews: {combined_text[:500]} \nSummary:"
            
            summary = self.summarizer(
                prompt, 
                max_new_tokens=50, 
                do_sample=False,
                pad_token_id=50256 # GPT-2 specific pad token
            )
            
            # Extract only the generated summary part
            generated_text = summary[0]['generated_text']
            if "Summary:" in generated_text:
                return generated_text.split("Summary:")[-1].strip()
            return generated_text[:100] + "..."
            
        except Exception as e:
            logger.warning(f"Summarization failed. Error: {str(e)}")
            return "Summary generation unavailable at the moment."

    def detect_complaints(self, text: str, sentiment: str):
        """Identify if a review is a critical complaint requiring immediate action."""
        # Critical keywords
        critical_keywords = [
            "worst", "disgusting", "rude", "dirty", "unacceptable", 
            "terrible", "never again", "stolen", "scam", "refund"
        ]
        
        text_lower = text.lower()
        has_critical_keyword = any(kw in text_lower for kw in critical_keywords)
        
        # A review is a complaint if it's negative OR contains critical keywords
        return (sentiment == "Negative") or has_critical_keyword

if __name__ == "__main__":
    # Test block
    try:
        engine = StayvoraEngine()
        test_text = "The room was very dirty and the staff was extremely rude. I will never come back here."
        sentiment, score = engine.get_sentiment(test_text)
        aspects = engine.detect_aspects(test_text)
        is_complaint = engine.detect_complaints(test_text, sentiment)
        
        print(f"--- Test Results ---")
        print(f"Text: {test_text}")
        print(f"Sentiment: {sentiment} ({score:.2f})")
        print(f"Aspects: {aspects}")
        print(f"Is Complaint: {is_complaint}")
    except Exception as e:
        print(f"Initialization test failed: {e}")
