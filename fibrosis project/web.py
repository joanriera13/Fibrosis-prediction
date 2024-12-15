import streamlit as st

st.set_page_config(
    page_title = "LFPP", 
    page_icon = "diagnosis.png"  
)

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
    
if st.session_state.current_page == "Home":
    from Home import show_home
    show_home()
    
elif st.session_state.current_page == "Questionnaire":
    from Questionnaire import show_questionnaire
    show_questionnaire()
