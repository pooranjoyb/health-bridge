import streamlit as st

st.set_page_config(page_title='Health Bridge', page_icon = '../assets/logo.png', initial_sidebar_state = 'auto')

st.title("Welcome to Health Bridge")

txt = st.text_area('Enter your Symptoms to Get Started', ''' ''')

user_video = st.file_uploader("Or Upload Your Video describing your Symptoms", type=['mov','mp4'])

### Reading Video from User

if user_video is not None:
    video = user_video.read()
    st.video(video)
