import streamlit as st

with st.sidebar:
    st.page_link('streamlit_app.py', label='Exoplanet Exploration', icon='🚀')
    st.page_link('pages/home.py', label='Exoplanet Home', icon='🏠')
    st.page_link('pages/resources.py', label='Exoplanet Resources', icon='📖')

st.markdown("<h1 style='text-align: center;'>Exoplanet</h1>", unsafe_allow_html=True)
st.write("")
st.markdown("<p style='text-align: center; font-size: 20px;'>A planet outside of our solar system that usually orbits another star in our galaxy.</p>", unsafe_allow_html=True)

st.image("images/exoplanets.jpg")

st.write("## What makes it habitable?")
with st.expander("### Presence of Liquid Water"):
    st.write("- Must exist in a stable form on the surface")
    st.write("- Ideally within the habitable zone of its star")

with st.expander("### Suitable Temperature Range"):
    st.write("- Temperatures should generally be between -15°C and 122°C to support liquid water")

with st.expander("### Atmospheric Composition"):
    st.write("- Should have a breathable atmosphere with nitrogen and oxygen")
    st.write("- Protects against harmful radiation")

with st.expander("### Planetary Characteristics"):
    planetary_chars = {
        "Size and Mass": "Ideally similar to Earth to retain an atmosphere",
        "Magnetic Field": "Protects the atmosphere from stellar radiation",
        "Geological Activity": "Helps regulate temperature and atmospheric composition"
    }
    for char, desc in planetary_chars.items():
        st.write(f"- **{char}**: {desc}")

with st.expander("### Stellar Characteristics"):
    st.write("- The host star should be stable, long-lived, and emit suitable radiation levels")

with st.expander("### Orbital and Rotational Factors"):
    st.write("- A stable, circular orbit")
    st.write("- A rotation rate that allows for moderate temperature variations")

with st.expander("### Elemental Composition"):
    st.write("- Presence of essential elements like carbon, hydrogen, nitrogen, oxygen, phosphorus, and sulfur")
