import streamlit as st
import pandas as pd


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
    if st.session_state.choice and st.session_state.habitable:
        st.write("Correct! You chose right!")
        st.write(st.session_state.reason)
    elif st.session_state.choice and not st.session_state.habitable:
        st.write("Oh No! You chose wrong!")
        st.write(st.session_state.reason)
        st.button("Next Planet", on_click=load_next_row)
    elif not st.session_state.choice and st.session_state.habitable: 
        st.write("Oh No! You chose wrong!")
        st.write(st.session_state.reason)
    elif not st.session_state.choice and not st.session_state.habitable: 
        st.write("Correct! You chose right!")
        st.write(st.session_state.reason)
        st.button("Next Planet", on_click=load_next_row)
    

st.title("Exoplanet Exploration")
if not st.session_state.game:
    st.write("Zombies have taken over your planet! You need to find a new planet to live on. Explore the exoplanets below to find a new home.")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.button("Blast off!", on_click=start_game)
else:     
        st.header(f"Planet: {st.session_state['id']}")
        st.image(st.session_state.image)
        
        st.write(st.session_state["prompt"])
    
        col1, col2 = st.columns(2)
    
        with col1:
            if st.button("Not Habitable"):
                st.session_state.choice = False
                check()

        with col2:
            if st.button("Habitable"):
                st.session_state.choice = True
                check()

st.markdown("""
            <style>
            img {
            border: 2px solid #ffffff;
            width: 100%;
            }
            </style>
            """, unsafe_allow_html=True)


