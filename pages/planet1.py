import streamlit as st

st.session_state.answer_habitable = True
st.session_state.habitable_explanation = "This planet is habitable. Congratulations! You found the exoplanet to live on!"
st.session_state.not_habitable_explanation = "This planet is not habitable. You need to find another one."
st.session_state.image_url = ""


st.session_state.choice_habitable = False
st.session_state.show_habitable_section = False
st.session_state.show_not_habitable_section = False


st.title("Exoplanet X")
st.write("Here are the features of Exoplanet X:")
st.write("- It is a rocky planet.")
st.write("- It has a thin atmosphere.")
st.write("- It has a large moon.")
st.write("- It has a ring system.")
st.write("- It has a magnetic field.")
st.write("- It has a large canyon.")
st.write("- It has a large volcano.")
st.write("- It has a large ocean.")
st.write("- It has a large mountain.")

col1, col2, col3 = st.columns(3)

def check():
    if st.session_state.choice_habitable and st.session_state.answer_habitable:
        st.write("Correct! You chose right!")
        st.write("Something about the planet that makes it habitable.")    
    elif st.session_state.choice_habitable and not st.session_state.answer_habitable:
        st.write("Oh No! You chose wrong!")
        st.write("Something about the planet that makes it not habitable.")
        if st.button("Next Planet"):
            st.switch_page("pages/planet2.py")
    elif not st.session_state.choice_habitable and st.session_state.answer_habitable: 
        st.write("Oh No! You chose wrong!")
        st.write("Something about the planet that makes it habitable.")
    elif not st.session_state.choice_habitable and not st.session_state.answer_habitable: 
        st.write("Correct! You chose right!")
        st.write("Something about the planet that makes it not habitable.")
        if st.button("Next Planet"):
            st.switch_page("pages/planet2.py")

with col1:
    if st.button("Not Habitable"):
        st.session_state.choice_habitable = False
        check()

with col2:
    if st.button("Habitable"):
        st.session_state.choice_habitable = True
        check()
