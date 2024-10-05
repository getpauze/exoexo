import streamlit as st
import pandas as pd


st.title("Exoplanet Exploration")
st.write("Your planet has been invaded by aliens! You need to find the exoplanet where they came from.")

col1, col2, col3 = st.columns(3)

data = pd.read_csv('/Users/meghanadravidas/workspace/nasa-space-apps/exoexo/data.csv')

# Initialize session state if not already done
if 'index' not in st.session_state:
    st.session_state.index = 0

# Load the first row of the dataset into session state
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
    

# Check if the button is clicked
if st.button("Submit Answer"):
    load_next_row()

# Display the current row data
st.write("Current Exoplanet Data:")
for col in data.columns:
    st.write(f"{col}: {st.session_state[col]}")


with col2:
    if st.button("Bleh"):
        st.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center;">
                <p>Button clicked!</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.switch_page("pages/planet2.py")