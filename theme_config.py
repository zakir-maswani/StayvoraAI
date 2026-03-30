"""
Unified Theme Configuration for Stayvora Hotel AI Engine

This module provides centralized theme styling for the Streamlit dashboard.
All color, typography, and styling values are defined here to ensure consistency.
Light Orange Theme with Professional Aesthetics.
"""

from dataclasses import dataclass
from typing import Tuple

# COLOR PALETTE - LIGHT ORANGE THEME
@dataclass
class ThemeColors:
    """Centralized color definitions for the entire application."""
    
    # Primary Colors - Light Orange Theme
    header_light: str = "#aad0fe"       # Light blue-orange
    header_dark: str = "#fdbf60"        # Medium orange
    header_medium: str = "#f59e0b"      # Darker orange
    
    # Background Colors
    page_bg_light: str = "#fef3e2"      # Very light cream
    page_bg_medium: str = "#fde8d0"     # Light cream
    card_bg: str = "#ffffff"            # Pure white
    
    # Text Colors
    text_dark: str = "#3a3a3a"          # Dark gray (body text)
    text_header: str = "#5a3a1a"        # Dark brown (headers)
    text_label: str = "#7a4a2a"         # Medium brown (labels)
    text_metric: str = "#b45309"        # Brown (metric values)
    text_light: str = "#ffffff"         # White (on dark backgrounds)
    
    # Accent Colors
    border_orange: str = "#fdbf60"      # Orange border
    button_hover: str = "#fed7aa"       # Light orange hover
    
    # Sentiment Status Colors
    sentiment_positive: str = "#10b981" # Green
    sentiment_neutral: str = "#f59e0b"  # Orange
    sentiment_negative: str = "#ef4444" # Red
    
    # Background Colors (lighter versions)
    sentiment_positive_bg: str = "#d1fae5"   # Light green
    sentiment_neutral_bg: str = "#fef3c7"    # Light yellow
    sentiment_negative_bg: str = "#fee2e2"   # Light red
    
    # Alert Colors
    alert_success: str = "#dcfce7"      # Light green
    alert_warning: str = "#fef3c7"      # Light yellow
    alert_danger: str = "#fee2e2"       # Light red
    alert_info: str = "#dbeafe"         # Light blue
    
    # Border Colors
    alert_success_border: str = "#16a34a"   # Green border
    alert_warning_border: str = "#d97706"   # Orange border
    alert_danger_border: str = "#dc2626"    # Red border
    alert_info_border: str = "#0284c7"      # Blue border

# TYPOGRAPHY CONFIGURATION
@dataclass
class ThemeTypography:
    """Typography settings for consistent font styling."""
    
    font_sans: str = "sans-serif"
    font_mono: str = "monospace"
    
    size_xs: str = "0.75rem"
    size_sm: str = "0.875rem"
    size_base: str = "1rem"
    size_lg: str = "1.125rem"
    size_xl: str = "1.25rem"
    size_2xl: str = "1.5rem"
    size_3xl: str = "1.875rem"
    size_4xl: str = "2.25rem"
    
    weight_normal: int = 400
    weight_medium: int = 500
    weight_semibold: int = 600
    weight_bold: int = 700
    weight_extrabold: int = 800
    weight_black: int = 900
    
    line_tight: str = "1.25"
    line_normal: str = "1.5"
    line_relaxed: str = "1.75"
    line_loose: str = "2"

# SPACING CONFIGURATION
@dataclass
class ThemeSpacing:
    """Spacing values for consistent layout."""
    
    xs: str = "0.25rem"
    sm: str = "0.5rem"
    md: str = "1rem"
    lg: str = "1.5rem"
    xl: str = "2rem"
    xxl: str = "3rem"

# BORDER RADIUS CONFIGURATION
@dataclass
class ThemeBorderRadius:
    """Border radius values for consistent rounding."""
    
    sm: str = "4px"
    md: str = "8px"
    lg: str = "12px"
    xl: str = "16px"
    full: str = "9999px"

# SHADOW CONFIGURATION
@dataclass
class ThemeShadows:
    """Shadow definitions for depth and elevation."""
    
    sm: str = "0 1px 2px 0 rgba(253, 191, 96, 0.05)"
    md: str = "0 4px 6px -1px rgba(253, 191, 96, 0.1), 0 2px 4px -1px rgba(253, 191, 96, 0.06)"
    lg: str = "0 10px 15px -3px rgba(253, 191, 96, 0.1), 0 4px 6px -2px rgba(253, 191, 96, 0.05)"
    xl: str = "0 20px 25px -5px rgba(253, 191, 96, 0.1), 0 10px 10px -5px rgba(253, 191, 96, 0.04)"
    
    button_default: str = "0 2px 8px rgba(253, 191, 96, 0.15)"
    button_hover: str = "0 6px 20px rgba(253, 191, 96, 0.4)"

# ANIMATION CONFIGURATION
@dataclass
class ThemeAnimations:
    """Animation timing and easing functions."""
    
    duration_fast: str = "150ms"
    duration_base: str = "300ms"
    duration_slow: str = "500ms"
    
    easing_ease_in: str = "ease-in"
    easing_ease_out: str = "ease-out"
    easing_ease_in_out: str = "ease-in-out"
    easing_linear: str = "linear"

# COMPLETE THEME OBJECT
THEME = {
    'colors': ThemeColors(),
    'typography': ThemeTypography(),
    'spacing': ThemeSpacing(),
    'border_radius': ThemeBorderRadius(),
    'shadows': ThemeShadows(),
    'animations': ThemeAnimations(),
}

# SENTIMENT STATUS MAPPING
SENTIMENT_STATUS_MAP = {
    'POSITIVE': {
        'color': THEME['colors'].sentiment_positive,
        'bg_color': THEME['colors'].sentiment_positive_bg,
        'text_color': '#15803d',
        'icon': '😊',
    },
    'NEUTRAL': {
        'color': THEME['colors'].sentiment_neutral,
        'bg_color': THEME['colors'].sentiment_neutral_bg,
        'text_color': '#92400e',
        'icon': '😐',
    },
    'NEGATIVE': {
        'color': THEME['colors'].sentiment_negative,
        'bg_color': THEME['colors'].sentiment_negative_bg,
        'text_color': '#7f1d1d',
        'icon': '😞',
    }
}

# UTILITY FUNCTIONS
def get_sentiment_status(sentiment: str) -> Tuple[str, str, str]:
    """
    Get sentiment status styling.
    
    Args:
        sentiment: Sentiment label ('Positive', 'Neutral', 'Negative')
        
    Returns:
        Tuple of (color, background_color, text_color)
    """
    sentiment_upper = sentiment.upper()
    if sentiment_upper in SENTIMENT_STATUS_MAP:
        config = SENTIMENT_STATUS_MAP[sentiment_upper]
        return config['color'], config['bg_color'], config['text_color']
    return THEME['colors'].text_dark, THEME['colors'].card_bg, THEME['colors'].text_dark

def get_sentiment_icon(sentiment: str) -> str:
    """Get emoji icon for sentiment."""
    sentiment_upper = sentiment.upper()
    if sentiment_upper in SENTIMENT_STATUS_MAP:
        return SENTIMENT_STATUS_MAP[sentiment_upper]['icon']
    return '❓'

# STREAMLIT CSS STYLES
def get_streamlit_css() -> str:
    """
    Get complete CSS styling for Streamlit application.
    Includes animations, button styles, and theme colors.
    """
    colors = THEME['colors']
    shadows = THEME['shadows']
    animations = THEME['animations']
    
    return f"""
    <style>
        /* ENVIRONMENTAL ANIMATIONS */
        
        @keyframes windflow {{
            0% {{ transform: translateX(-100%); opacity: 0; }}
            10% {{ opacity: 0.3; }}
            50% {{ opacity: 0.5; }}
            90% {{ opacity: 0.3; }}
            100% {{ transform: translateX(100%); opacity: 0; }}
        }}
        
        @keyframes airflow {{
            0% {{ transform: translateY(0px); opacity: 0; }}
            50% {{ opacity: 0.2; }}
            100% {{ transform: translateY(-20px); opacity: 0; }}
        }}
        
        @keyframes subtle-pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.8; }}
        }}
        
        @keyframes float {{
            0%, 100% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
        }}
        
        /* Background animation container */
        .animation-bg {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
            overflow: hidden;
        }}
        
        .wind-particle {{
            position: absolute;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, transparent, rgba(253, 191, 96, 0.1), transparent);
            animation: windflow 8s infinite;
        }}
        
        .air-particle {{
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(253, 191, 96, 0.2);
            border-radius: 50%;
            animation: airflow 6s infinite;
        }}
        
        /* MAIN CONTAINER */
        
        .main {{
            background: linear-gradient(135deg, {colors.page_bg_light} 0%, {colors.page_bg_medium} 100%);
            padding: 0;
        }}
        
        /* HEADER STYLING */
        
        .header-container {{
            background: linear-gradient(90deg, {colors.header_light} 0%, {colors.header_dark} 100%);
            padding: 2.5rem;
            border-radius: 0;
            color: {colors.text_header};
            margin-bottom: 2rem;
            box-shadow: {shadows.lg};
            position: relative;
            overflow: hidden;
        }}
        
        .header-container::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 20% 50%, rgba(255,255,255,0.1), transparent),
                        radial-gradient(circle at 80% 80%, rgba(255,255,255,0.05), transparent);
            pointer-events: none;
        }}
        
        .header-content {{
            position: relative;
            z-index: 1;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .header-title {{
            font-size: 2.8rem;
            font-weight: 900;
            margin: 0;
            letter-spacing: -0.5px;
            color: {colors.text_header};
            flex: 1;
        }}
        
        .header-subtitle {{
            font-size: 1.1rem;
            font-weight: 400;
            margin-top: 0.5rem;
            opacity: 0.95;
            color: {colors.text_label};
        }}
        
        .header-time {{
            font-size: 1.2rem;
            font-weight: 700;
            color: {colors.text_header};
            text-align: right;
            min-width: 200px;
            animation: subtle-pulse 2s ease-in-out infinite;
        }}
        
        .header-date {{
            font-size: 0.9rem;
            color: {colors.text_label};
            text-align: right;
        }}
        
        /* CARD STYLING */
        
        .metric-card {{
            background: {colors.card_bg};
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: {shadows.md};
            border-left: 5px solid {colors.border_orange};
            margin-bottom: 1rem;
            transition: all {animations.duration_base} {animations.easing_ease_in_out};
        }}
        
        .metric-card:hover {{
            transform: translateY(-4px);
            box-shadow: {shadows.lg};
        }}
        
        .metric-card h3 {{
            color: {colors.text_metric};
            font-weight: 700;
            margin-bottom: 0.5rem;
        }}
        
        .metric-card p {{
            color: {colors.text_dark};
            font-size: 1rem;
            margin: 0;
        }}
        
        .glass-card {{
            background: rgba(255, 255, 255, 0.99);
            border-radius: 12px;
            padding: 1.8rem;
            box-shadow: {shadows.md};
            margin-bottom: 1.5rem;
            border: 2px solid {colors.border_orange};
            transition: all {animations.duration_base} {animations.easing_ease_in_out};
        }}
        
        .glass-card:hover {{
            box-shadow: {shadows.lg};
            border-color: {colors.header_dark};
        }}
        
        .glass-card h2 {{
            color: {colors.text_metric};
            font-weight: 800;
            margin-top: 0;
            margin-bottom: 1rem;
        }}
        
        .glass-card h3 {{
            color: {colors.header_medium};
            font-weight: 700;
            margin-top: 1rem;
        }}
        
        .glass-card p {{
            color: {colors.text_dark};
            line-height: 1.7;
            font-size: 0.95rem;
        }}
        
        /* BUTTON STYLING */
        
        .stButton > button {{
            background: linear-gradient(90deg, {colors.header_dark} 0%, {colors.header_light} 100%);
            color: {colors.text_header};
            border: none;
            border-radius: 10px;
            padding: 0.85rem 1.5rem;
            font-weight: 700;
            transition: all {animations.duration_base} {animations.easing_ease_in_out};
            width: 100%;
            font-size: 0.95rem;
            box-shadow: {shadows.button_default};
            position: relative;
            overflow: hidden;
        }}
        
        .stButton > button::before {{
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transform: translate(-50%, -50%);
            transition: width {animations.duration_base}, height {animations.duration_base};
        }}
        
        .stButton > button:hover {{
            transform: translateY(-3px);
            box-shadow: {shadows.button_hover};
            background: linear-gradient(90deg, {colors.header_light} 0%, {colors.header_dark} 100%);
        }}
        
        .stButton > button:hover::before {{
            width: 300px;
            height: 300px;
        }}
        
        .stButton > button:active {{
            transform: translateY(-1px);
        }}
        
        /* ALERT STYLING */
        
        .alert-box {{
            border-radius: 10px;
            padding: 1.3rem;
            margin-bottom: 1.2rem;
            font-weight: 500;
            font-size: 0.95rem;
            transition: all {animations.duration_base} {animations.easing_ease_in_out};
        }}
        
        .alert-success {{
            background-color: {colors.alert_success};
            border-left: 5px solid {colors.alert_success_border};
            color: #15803d;
        }}
        
        .alert-warning {{
            background-color: {colors.alert_warning};
            border-left: 5px solid {colors.alert_warning_border};
            color: #92400e;
        }}
        
        .alert-danger {{
            background-color: {colors.alert_danger};
            border-left: 5px solid {colors.alert_danger_border};
            color: #7f1d1d;
        }}
        
        .alert-info {{
            background-color: {colors.alert_info};
            border-left: 5px solid {colors.alert_info_border};
            color: #0c2d6b;
        }}
        
        /* TEXT STYLING */
        
        h1, h2, h3 {{
            color: {colors.text_metric};
            font-weight: 800;
        }}
        
        p {{
            line-height: 1.7;
            color: {colors.text_dark};
            font-size: 0.95rem;
        }}
        
        label {{
            color: {colors.text_header};
            font-weight: 700;
        }}
        
        /* METRIC VALUES */
        
        [data-testid="stMetricValue"] {{
            font-size: 2.5rem;
            font-weight: 900;
            color: {colors.text_metric};
            animation: float 3s ease-in-out infinite;
        }}
        
        [data-testid="stMetricLabel"] {{
            font-size: 0.9rem;
            color: {colors.text_label};
            font-weight: 700;
        }}
        
        /* SIDEBAR */
        
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {colors.page_bg_light} 0%, {colors.page_bg_medium} 100%);
        }}
        
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {{
            color: {colors.text_metric};
        }}
        
        /* TABS */
        
        .stTabs [data-baseweb="tab-list"] {{
            gap: 0.5rem;
        }}
        
        .stTabs [data-baseweb="tab"] {{
            border-radius: 8px 8px 0 0;
            padding: 0.75rem 1.5rem;
            background: #f5f5f5;
            border: none;
            color: {colors.text_header};
            font-weight: 600;
            transition: all {animations.duration_base} {animations.easing_ease_in_out};
        }}
        
        .stTabs [aria-selected="true"] {{
            background: linear-gradient(90deg, {colors.header_dark} 0%, {colors.header_light} 100%);
            color: {colors.text_header};
        }}
        
        /* EXPANDER */
        
        .streamlit-expanderHeader {{
            background: {colors.page_bg_light};
            border-radius: 8px;
            padding: 0.75rem;
            color: {colors.text_metric};
            font-weight: 700;
            transition: all {animations.duration_base} {animations.easing_ease_in_out};
        }}
        
        .streamlit-expanderHeader:hover {{
            background: {colors.page_bg_medium};
        }}
        
        /* FOOTER */
        
        footer {{
            visibility: hidden;
        }}
    </style>
    """
