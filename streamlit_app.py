import streamlit as st


st.title("Exoplanet Exploration")
st.write("Your planet has been invaded by aliens! You need to find the exoplanet where they came from.")

col1, col2, col3 = st.columns(3)

with col2:
    if st.button("Get Started"):
        st.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center;">
                <p>Button clicked!</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.switch_page("pages/planet1.py")