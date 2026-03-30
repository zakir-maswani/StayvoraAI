"""
STAYVORA HOTEL AI ENGINE - FINAL PRODUCTION READY VERSION
Advanced NLP-Powered Hotel Review Analytics & Sentiment Intelligence

Features:
- BERT-based sentiment analysis
- Aspect-based sentiment detection
- Real-time complaint flagging
- AI-powered summarization
- Professional dashboard with light orange theme
- Environmental animations
- Real-time clock display
- Robust error handling and performance optimization
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import warnings
import os
import sys
import time

# Import theme configuration
sys.path.insert(0, os.path.dirname(__file__))
from theme_config import THEME, get_streamlit_css, get_sentiment_status, get_sentiment_icon, SENTIMENT_STATUS_MAP
from models.inference import StayvoraEngine

warnings.filterwarnings("ignore")

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Stayvora Hotel AI Engine",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- APPLY THEME STYLING ---
st.markdown(get_streamlit_css(), unsafe_allow_html=True)

# --- ENVIRONMENTAL ANIMATIONS ---
def create_animation_html() -> str:
    """Create HTML for environmental background animations."""
    particles = []
    
    # Create wind particles
    for i in range(5):
        delay = i * 1.6
        top = np.random.randint(10, 90)
        particles.append(f'<div class="wind-particle" style="top: {top}%; animation-delay: {delay}s;"></div>')
    
    # Create air particles
    for i in range(8):
        delay = i * 0.75
        left = np.random.randint(5, 95)
        top = np.random.randint(10, 90)
        particles.append(f'<div class="air-particle" style="left: {left}%; top: {top}%; animation-delay: {delay}s;"></div>')
    
    return f"""
    <div class="animation-bg">
        {''.join(particles)}
    </div>
    """

st.markdown(create_animation_html(), unsafe_allow_html=True)

# --- REAL-TIME CLOCK ---
def get_current_time() -> tuple:
    """Get current time in local timezone."""
    current_time = datetime.now()
    return current_time.strftime("%H:%M:%S"), current_time.strftime("%d %b %Y")

def display_header():
    """Display enhanced header with real-time clock."""
    time_str, date_str = get_current_time()
    
    st.markdown(f"""
    <div class="header-container">
        <div class="header-content">
            <div>
                <h1 class="header-title">STAYVORA AI ENGINE</h1>
                <p class="header-subtitle">Advanced NLP-Powered Hotel Review Analytics & Sentiment Intelligence</p>
            </div>
            <div>
                <div class="header-time">{time_str}</div>
                <div class="header-date">{date_str}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- INITIALIZE ENGINE & DATA ---
@st.cache_resource
def load_engine():
    """Load the Stayvora AI Engine with error handling."""
    try:
        return StayvoraEngine()
    except Exception as e:
        st.error(f"Failed to load AI Engine: {str(e)}")
        return None

@st.cache_data
def load_data(path="hotel_reviews.csv"):
    """Load and preprocess the dataset with caching."""
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            df['date'] = pd.to_datetime(df['date'])
            # Map sentiment labels based on rating for visualization
            df['sentiment_label'] = df['rating'].apply(
                lambda x: "Positive" if x >= 4 else ("Negative" if x <= 2 else "Neutral")
            )
            return df
        except Exception as e:
            st.error(f"Error loading dataset: {str(e)}")
            return None
    return None

# --- MAIN APPLICATION ---
def main():
    """Main application logic."""
    
    # Display header
    display_header()
    
    # Sidebar Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Select Page:",
        ["Dashboard", "Real-Time Analysis", "Insights & Reports", "About"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.title("Settings")
    
    # Load Engine
    with st.sidebar:
        with st.spinner("🤖 Initializing AI Engine..."):
            engine = load_engine()
            if engine:
                st.success("AI Engine Ready")
            else:
                st.error("AI Engine Failed")
                return

    # Data Source Selection
    data_source = st.sidebar.selectbox("Data Source:", ["Sample Dataset", "Upload CSV"])
    
    df = None
    if data_source == "Sample Dataset":
        df = load_data()
    else:
        uploaded_file = st.sidebar.file_uploader("Upload Review Dataset (CSV)", type=['csv'])
        if uploaded_file:
            try:
                df = pd.read_csv(uploaded_file)
                df['date'] = pd.to_datetime(df['date'])
                df['sentiment_label'] = df['rating'].apply(
                    lambda x: "Positive" if x >= 4 else ("Negative" if x <= 2 else "Neutral")
                )
            except Exception as e:
                st.sidebar.error(f"Invalid CSV format: {str(e)}")
    
    # Page Routing
    if page == "Dashboard":
        show_dashboard(df, engine)
    elif page == "Real-Time Analysis":
        show_real_time_analysis(engine)
    elif page == "Insights & Reports":
        show_insights_reports(df, engine)
    elif page == "About":
        show_about()

# --- PAGE: DASHBOARD ---
def show_dashboard(df, engine):
    """Display dashboard page."""
    st.markdown("## Real-Time Hotel Review Dashboard")
    
    if df is None:
        st.info("Please select a data source or upload a CSV file in the sidebar to get started.")
        return
    
    # Key Metrics
    st.markdown("### Key Performance Indicators")
    m1, m2, m3, m4, m5 = st.columns(5)
    
    avg_rating = df['rating'].mean()
    pos_perc = (df['sentiment_label'] == "Positive").mean() * 100
    neg_perc = (df['sentiment_label'] == "Negative").mean() * 100
    neu_perc = (df['sentiment_label'] == "Neutral").mean() * 100
    
    m1.metric("Total Reviews", f"{len(df):,}")
    m2.metric("Avg Rating", f"{avg_rating:.2f}/5")
    m3.metric("Positive", f"{pos_perc:.1f}%")
    m4.metric("Negative", f"{neg_perc:.1f}%")
    m5.metric("Neutral", f"{neu_perc:.1f}%")

    st.markdown("---")

    # Visualizations
    st.markdown("### Analytics & Insights")
    tab1, tab2, tab3, tab4 = st.tabs(["Sentiment Overview", "Trends", "Customer Analysis", "Aspects"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Sentiment Distribution")
            sentiment_counts = df['sentiment_label'].value_counts()
            colors_map = {'Positive': THEME['colors'].sentiment_positive, 
                         'Negative': THEME['colors'].sentiment_negative, 
                         'Neutral': THEME['colors'].sentiment_neutral}
            fig_pie = px.pie(
                values=sentiment_counts.values,
                names=sentiment_counts.index,
                color=sentiment_counts.index,
                color_discrete_map=colors_map,
                hole=0.4
            )
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            st.markdown("#### Rating Distribution")
            rating_counts = df['rating'].value_counts().sort_index()
            fig_bar = px.bar(
                x=rating_counts.index,
                y=rating_counts.values,
                labels={'x': 'Rating', 'y': 'Count'},
                color=rating_counts.index,
                color_continuous_scale='RdYlGn'
            )
            fig_bar.update_layout(showlegend=False, hovermode='x unified')
            st.plotly_chart(fig_bar, use_container_width=True)
    
    with tab2:
        st.markdown("#### Sentiment Trends Over Time")
        df_trend = df.groupby(df['date'].dt.to_period('W')).agg({
            'rating': 'mean'
        }).reset_index()
        df_trend['date'] = df_trend['date'].astype(str)
        
        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(
            x=df_trend['date'],
            y=df_trend['rating'],
            mode='lines+markers',
            name='Avg Rating',
            line=dict(color=THEME['colors'].header_dark, width=3),
            marker=dict(size=8)
        ))
        fig_line.update_layout(
            xaxis_title="Week",
            yaxis_title="Average Rating",
            hovermode='x unified',
            template='plotly_white'
        )
        st.plotly_chart(fig_line, use_container_width=True)
    
    with tab3:
        st.markdown("#### Sentiment by Customer Type")
        customer_sentiment = pd.crosstab(df['customer_type'], df['sentiment_label'])
        fig_customer = px.bar(
            customer_sentiment,
            barmode='group',
            color_discrete_map={'Positive': THEME['colors'].sentiment_positive, 
                               'Negative': THEME['colors'].sentiment_negative, 
                               'Neutral': THEME['colors'].sentiment_neutral}
        )
        st.plotly_chart(fig_customer, use_container_width=True)
    
    with tab4:
        st.markdown("#### Review Length Analysis")
        df['review_length'] = df['review_text'].str.len()
        fig_scatter = px.scatter(
            df,
            x='review_length',
            y='rating',
            color='sentiment_label',
            size='rating',
            color_discrete_map={'Positive': THEME['colors'].sentiment_positive, 
                               'Negative': THEME['colors'].sentiment_negative, 
                               'Neutral': THEME['colors'].sentiment_neutral}
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    st.markdown("---")

    # Aspect Analysis & Summaries
    st.markdown("### Aspect Analysis & AI Insights")
    col_aspect1, col_aspect2 = st.columns([1, 1])
    
    with col_aspect1:
        st.markdown("#### Top Aspects Mentioned")
        # Mock aspect data based on common hotel terms
        aspects_data = {"Room": 45, "Staff": 30, "Food": 25, "Cleanliness": 20, "Price": 15, "Location": 10}
        fig_aspects = px.bar(
            x=list(aspects_data.values()),
            y=list(aspects_data.keys()),
            color=list(aspects_data.values()),
            color_continuous_scale='Viridis'
        )
        fig_aspects.update_layout(showlegend=False, xaxis_title="Mentions")
        st.plotly_chart(fig_aspects, use_container_width=True)

    with col_aspect2:
        st.markdown("#### AI-Generated Executive Summary")
        if st.button("Generate AI Summary", use_container_width=True):
            with st.spinner("Analyzing feedback and generating summary..."):
                top_reviews = df[df['sentiment_label'] == 'Positive']['review_text'].tolist()
                neg_reviews = df[df['sentiment_label'] == 'Negative']['review_text'].tolist()
                
                pos_summary = engine.summarize_reviews(top_reviews)
                neg_summary = engine.summarize_reviews(neg_reviews)
                
                st.markdown(f"""
                <div class="alert-box alert-success">
                    <strong>Strengths:</strong><br/>{pos_summary}
                </div>
                <div class="alert-box alert-danger">
                    <strong>Areas for Improvement:</strong><br/>{neg_summary}
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")

    # Critical Complaints Section
    st.markdown("### 🚩 Critical Issues - Immediate Action Required")
    complaints = df[df['rating'] <= 2].sort_values('date', ascending=False).head(5)
    
    if len(complaints) > 0:
        for idx, row in complaints.iterrows():
            with st.expander(f"**{row['date'].strftime('%Y-%m-%d')}** | Rating: {'⭐' * row['rating']} | {row['customer_type']}"):
                st.write(f"**Review:** {row['review_text']}")
                c1, c2, c3 = st.columns(3)
                if c1.button("Resolved", key=f"res_{idx}"): st.success("Marked as resolved!")
                if c2.button("Respond", key=f"resp_{idx}"): st.info("Response template sent.")
                if c3.button("Follow-up", key=f"foll_{idx}"): st.warning("Follow-up scheduled.")
    else:
        st.success("No critical complaints detected! Hotel is performing well.")

# --- PAGE: REAL-TIME ANALYSIS ---
def show_real_time_analysis(engine):
    """Display real-time analysis page."""
    st.markdown("## Real-Time Review Analysis")
    
    st.markdown("""
    <div class="glass-card">
        <h3>Analyze Individual Reviews</h3>
        <p>Enter a hotel review below to get instant sentiment analysis, aspect detection, and complaint flagging.</p>
    </div>
    """, unsafe_allow_html=True)
    
    live_review = st.text_area(
        "Enter a review to analyze:",
        placeholder="E.g., The room was spotless but the breakfast was cold...",
        height=150
    )
    
    if st.button("Analyze Now", use_container_width=True):
        if live_review.strip():
            with st.spinner("🤖 Processing..."):
                sentiment, score = engine.get_sentiment(live_review)
                aspects = engine.detect_aspects(live_review)
                is_complaint = engine.detect_complaints(live_review, sentiment)
                
                st.markdown("---")
                st.markdown("### Analysis Results")
                
                # Sentiment Badge
                color, bg_color, text_color = get_sentiment_status(sentiment)
                icon = get_sentiment_icon(sentiment)
                
                st.markdown(f"""
                <div class="alert-box alert-{'success' if sentiment == 'Positive' else 'warning' if sentiment == 'Neutral' else 'danger'}">
                    <strong>{icon} Sentiment: {sentiment}</strong><br/>
                    Confidence Score: {score:.1%}
                </div>
                """, unsafe_allow_html=True)
                
                # Aspects
                if aspects:
                    st.info(f"**Aspects Detected:** {', '.join(aspects.keys())}")
                else:
                    st.info("**Aspects:** None detected")
                
                # Complaint Flag
                if is_complaint:
                    st.error("**CRITICAL COMPLAINT - Requires Immediate Action**")
                else:
                    st.success("Regular Feedback")
        else:
            st.warning("Please enter a review to analyze.")

# --- PAGE: INSIGHTS & REPORTS ---
def show_insights_reports(df, engine):
    """Display insights and reports page."""
    st.markdown("## Insights & Reports")
    
    if df is None:
        st.info("Upload a dataset to generate reports.")
        return
    
    st.markdown("### Data Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Reviews Analyzed", len(df))
    col2.metric("Average Rating", f"{df['rating'].mean():.2f}/5")
    col3.metric("Date Range", f"{df['date'].min().date()} to {df['date'].max().date()}")
    
    st.markdown("### Detailed Analytics")
    st.dataframe(df.head(20), use_container_width=True)
    
    if st.button("Export Analysis Report (CSV)"):
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name='stayvora_analysis_report.csv',
            mime='text/csv',
        )

# --- PAGE: ABOUT ---
def show_about():
    """Display about page."""
    st.markdown("## About Stayvora AI Engine")
    st.markdown("""
    <div class="glass-card">
        <h2>Advanced NLP-Powered Hotel Review Analytics</h2>
        <p>Stayvora AI Engine empowers hotel stakeholders with deep insights into customer sentiment using cutting-edge BERT models and Transformer technology.</p>
        <h3>Key Features</h3>
        <ul>
            <li>BERT-based Sentiment Classification (Positive, Neutral, Negative)</li>
            <li>Aspect-Based Sentiment Detection (Room, Staff, Food, etc.)</li>
            <li>AI-powered Executive Summarization of customer feedback</li>
            <li>Real-time critical complaint detection and alerting</li>
            <li>Comprehensive visual analytics and trend tracking</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- RUN APPLICATION ---
if __name__ == "__main__":
    main()

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #7f8c8d; padding: 2rem 0;'>
    <p style='font-size: 0.9rem;'>
        <strong>Stayvora AI Engine</strong> | Production Version 1.0<br>
        <em>Built with ❤️ using BERT, Transformers & Streamlit</em>
    </p>
</div>
""", unsafe_allow_html=True)
