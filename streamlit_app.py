import streamlit as st
import pandas as pd

st.set_page_config(page_title="Exo-Exo", page_icon="🚀", initial_sidebar_state="collapsed")

with st.sidebar:
    st.page_link('streamlit_app.py', label='Exoplanet Exploration', icon='🚀')
    st.page_link('pages/home.py', label='Exoplanet Home', icon='🏠')
    st.page_link('pages/resources.py', label='Exoplanet Resources', icon='📖')

st.markdown("""
<style>

.stApp {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

.stApp > .main > div {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)


data = pd.read_csv('data.csv')

# Initialize session state if not already done
if 'index' not in st.session_state:
    st.session_state.index = 0

if 'game' not in st.session_state:
    st.session_state.game = False

if 'choice' not in st.session_state:
    st.session_state.choice = False

# Load the first row of the dataset into session state
def init_game():
    if st.session_state.index == 0:
        for col in data.columns:
            st.session_state[col] = data.iloc[st.session_state.index][col]

# Function to load the next row into session state
def load_next_row():
    if st.session_state.index < len(data) -1:
        st.session_state.index += 1
    else:
        st.session_state.index = 0  # Reset to the first row if we reach the end
    for col in data.columns:
        st.session_state[col] = data.iloc[st.session_state.index][col]
    
def start_game():
    st.session_state.game = True
    init_game()

def check():
    # Ensure the result spans the full page width
    st.write("")  # Adds a little separation from the buttons
    st.write("<div style='width: 100%; text-align: center;'>", unsafe_allow_html=True)

    if st.session_state.choice and st.session_state.habitable:
        st.write("<h2>🚀 Super job! You did it! 🚀 </h2>", unsafe_allow_html=True)
        st.write(st.session_state.reason)
        st.button("Restart ↻", on_click=load_next_row)

    elif st.session_state.choice and not st.session_state.habitable:
        st.write("Great try! Unfortunately, it is not habitable.")
        st.write(st.session_state.reason)
        st.button("Next Planet", on_click=load_next_row)

    elif not st.session_state.choice and st.session_state.habitable:
        st.write("Good try! Interestingly, it is potentially habitable!")
        st.write(st.session_state.reason)

    elif not st.session_state.choice and not st.session_state.habitable:
        st.write("Awesome, you got it right!")
        st.write(st.session_state.reason)
        st.button("Next Planet", on_click=load_next_row)

    st.write("</div>", unsafe_allow_html=True)
    

st.title("Exo-Exo")
if not st.session_state.game:
    st.write("Zombies have taken over your planet! You need to find a new planet to live on. Explore the exoplanets below to find a new home.")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.button("Blast off!", on_click=start_game)
else:     
    st.header(st.session_state['id'])
    st.image(st.session_state.image, use_column_width=True)

    for p in st.session_state["prompt"].split('.'):
        st.write(f"{p}.")
    
    col1, col2 = st.columns(2)

    # Initialize a flag to track button clicks
    button_clicked = False
    
    with col1:
        if st.button("Not Habitable"):
            st.session_state.choice = False
            button_clicked = True

    with col2:
        if st.button("Potentially Habitable"):
            st.session_state.choice = True
            button_clicked = True

    # If a button was clicked, call `check()` outside the columns
    if button_clicked:
        check()

st.markdown("""
            <style>
            img {
            border: 2px solid #ffffff;
            width: 100%;
            }
            </style>
            """, unsafe_allow_html=True)


