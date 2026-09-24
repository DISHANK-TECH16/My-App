import streamlit as st
from google import genai
from dotenv import load_dotenv
import time

load_dotenv()
client = genai.Client()
st.set_page_config(
    page_title="Dishank's App",  # Changes the tab name
    page_icon="🚀",               # Changes the tab emoji/icon
    layout="wide"                 # Optional: "centered" or "wide"
)
# st.title("🌍 Travel Assistant ✈️")
st.markdown(
    """
    <style>
    /* --- 1. DARKER FULL-SCREEN LIVE WEBSITE BACKGROUND FOR TEXT VISIBILITY --- */
    .stApp {
        background: linear-gradient(135deg, #030712 0%, #0f172a 35%, #064e3b 70%, #1e1b4b 100%);
        background-size: 400% 400%;
        animation: dark-coastal-gradient 18s ease infinite;
    }

    @keyframes dark-coastal-gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Make Streamlit top header transparent so background flows seamlessly */
    .stApp > header {
        background-color: transparent !important;
    }

    /* --- 2. BRIGHTER FULL-WIDTH TROPICAL BEACH BANNER STYLES --- */
    @keyframes shimmer {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes bounce-subtle {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
    }

    .full-width-beach-banner {
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
        width: 100vw;
        min-height: 42vh;
        padding: 6.5rem 2rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        /* Lighter overlay to make the beach background look much brighter and sunnier */
        background: linear-gradient(rgba(5, 15, 30, 0.25), rgba(5, 15, 30, 0.45)), 
                    url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
        color: white;
        margin-top: -4.5rem;
        margin-bottom: 2.5rem;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
    }

    .travel-title-full {
        font-size: 3.8rem;
        font-weight: 900;
        margin: 0;
        text-shadow: 2px 4px 12px rgba(0,0,0,0.7);
    }

    .travel-icon-full {
        display: inline-block;
        animation: bounce-subtle 2.5s ease-in-out infinite;
    }

    .travel-subtitle-full {
        font-size: 1.4rem;
        font-weight: 500;
        margin-top: 1rem;
        max-width: 700px;
        text-shadow: 1px 2px 8px rgba(0,0,0,0.7);
        opacity: 0.98;
    }

    .badge-full {
        display: inline-block;
        background: linear-gradient(270deg, #ff7e5f, #feb47b, #ff7e5f);
        background-size: 200% 200%;
        animation: shimmer 5s ease infinite;
        color: white;
        padding: 6px 18px;
        border-radius: 30px;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 1rem;
        box-shadow: 0 4px 15px rgba(255, 126, 95, 0.5);
    }

    /* --- Force sharp text contrast for Streamlit widgets --- */
    .stTextInput label, .stSelectbox label, .stSlider label, h3 {
        color: #f8fafc !important;
        font-weight: 600;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    </style>

    <!-- Full-Width Tropical Beach Hero Banner Component -->
    <div class="full-width-beach-banner">
        <div>
            <div class="badge-full">🌴 Make Your Vacation Special 🥥</div>
            <h1 class="travel-title-full">
                <span class="travel-icon-full">✈️</span> Travel Asssistant
            </h1>
            <p class="travel-subtitle-full">
                Discover hidden paradises, luxury retreats, and epic getaways tailored entirely to you.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
        
st.caption(" Your personal planner ")

location = st.text_input("🗺️ Where is your destination ?")

days_nr = st.number_input("📅 What is the duration (days) of trip", min_value=1, max_value=30)

activities = st.multiselect("What kind of Activities you would prefer during Trip", 
                            ["🏞️Adventure & Outdoor","🏛️Sightseeing & Exploration",
                             "🌊Relaxation & Leisure","🍜Food & Culture","🎢Entertainment"])

budget = st.selectbox("Select Budget", ["👑Luxury","💎Premium","💳Standard","💸Economy"])

travel_type = st.radio("🤝Who are you travelling with",["Family","Friends","Solo"])

prompt = f"""You are a Travel Planner, User is saying that client wants to
go to {location} for {days_nr} days , client is on budget of type {budget},
also he will like to perform activities like{activities} during trip,
Travel type is: {travel_type}
Plan a trip and share answer in bullet format  
"""


st.markdown(
    """
    <style>
    /* Target the Streamlit button */
    .stButton > button {
        background: linear-gradient(45deg, #ff007f, #7f00ff);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: bold;
        box-shadow: 0 0 15px rgba(255, 0, 127, 0.6);
        transition: all 0.3s ease-in-out;
    }

    /* Glowing effect on hover */
    .stButton > button:hover {
        background: linear-gradient(45deg, #ff3399, #9933ff);
        box-shadow: 0 0 25px rgba(255, 51, 153, 0.9), 0 0 35px rgba(153, 51, 255, 0.7);
        color: white;
        border: none;
        transform: scale(1.02);
    }
    
    /* Active/Click state */
    .stButton > button:active {
        transform: scale(0.98);
    }
    </style>
    """,
    unsafe_allow_html=True,
)
if st.button("🏖️Plan Trip"):
    st.balloons()
    interaction = client.interactions.create(   
        model="gemini-3.5-flash-lite",
        input=prompt
      )   
    with st.spinner("✈️Launching towards Peace..."):
        time.sleep(5)   
    st.success("🧳 Your Trip Plan Is Ready")
    st.write(interaction.output_text)