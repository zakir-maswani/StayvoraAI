# Stayvora Hotel - AI Review Sentiment & Insight Engin

### Author: Zakir Ali 
### LinkedIn: https://www.linkedin.com/in/zakir-ali-572104339/

## Overview
Stayvora AI is a production-level deep learning system designed to analyze hotel reviews and generate actionable insights. It leverages state-of-the-art NLP techniques, including BERT-based sentiment analysis and transformer-based summarization, to provide a comprehensive view of customer feedback.

## Key Features
- **Sentiment Analysis**: Fine-tuned BERT model to classify reviews as Positive, Negative, or Neutral.
- **Aspect-Based Sentiment**: Detects and analyzes specific hotel aspects like Room, Staff, Food, and Cleanliness.
- **Complaint Detection**: Automatically flags critical negative reviews for immediate action.
- **AI Summarization**: Generates concise executive summaries of top positive and negative feedback using DistilBART.
- **Premium UI/UX**: A beautiful light orange theme with gradient backgrounds, environmental animations, and a professional dashboard layout.
- **Real-Time Insights**: Instant feedback on individual reviews and comprehensive dataset analytics.

## Project Structure
```text
stayvora_engine/
├── app.py                # Main Streamlit dashboard
├── theme_config.py       # UI theme and CSS configuration
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── data/                 # Data generation and storage
│   └── generate_data.py  # Script to generate realistic hotel reviews
├── preprocessing/        # Data cleaning and preparation
│   └── clean_data.py     # NLP preprocessing pipeline
├── models/               # Model inference and training logic
│   └── inference.py      # BERT & Transformer-based analysis engine
└── utils/                # Helper function
```

## Setup and Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/zakir-maswani/StayvoraAI>
   cd stayvora_engine
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate Sample Data**:
   ```bash
   python data/generate_data.py
   ```

4. **Run the Dashboard**:
   ```bash
   streamlit run app.py
   ```

## Technical Requirements
- **Language**: Python 3.8+
- **Deep Learning**: PyTorch, Hugging Face Transformers
- **Data Analysis**: Pandas, NumPy, Scikit-learn
- **Visualization**: Plotly, Matplotlib
- **Web Framework**: Streamlit

## Model Details
- **Sentiment Model**: `nlptown/bert-base-multilingual-uncased-sentiment`
- **Summarization Model**: `sshleifer/distilbart-cnn-12-6`
- **Inference Engine**: Custom `StayvoraEngine` class for modular integration.

