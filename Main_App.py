import streamlit as st
from streamlit_option_menu import option_menu

import Price_Predictor
import  Analysis_App
import Home
import Recommend_Appartments

# Configure page
st.set_page_config(page_title="My Dashboard", layout="wide")

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Price Predictor", "Analysis App"],
        icons=["house", "graph-up", "bar-chart"],
        menu_icon="cast",
        default_index=0,
    )

# Main content based on selection
if selected == "Home":
    # Home.show()
    st.title("🏠 Home")
    st.write("Welcome to your dashboard!")

elif selected == "Price Predictor":
    st.title("💰 Price Predictor")
    Price_Predictor.show()



elif selected == "Analysis App":
    # Analysis_App.show()
    st.title("📊 Analysis App")
    Recommend_Appartments.recommend()