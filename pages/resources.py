import streamlit as st

with st.sidebar:
    st.page_link('streamlit_app.py', label='Exoplanet Exploration', icon='🚀')
    st.page_link('pages/home.py', label='Exoplanet Home', icon='🏠')
    st.page_link('pages/resources.py', label='Exoplanet Resources', icon='📖')


st.markdown("<h1 style='text-align: center;'>Resources</h1>", unsafe_allow_html=True)
st.write("")
st.markdown("""
<div style='font-size:20px; text-align:center;'>
    <a href="https://science.nasa.gov/exoplanets/">NASA Exoplanets</a><br>
    <a href="https://exoplanetarchive.ipac.caltech.edu/">NASA Exoplanet Archive</a><br>
    <a href="https://hackanexoplanet.esa.int/">Hack an Exoplanet</a>
</div>
""", unsafe_allow_html=True)