import streamlit as st
import secrets, string
import os

##Creating the temp directories
if not os.path.exists('../assets/video'):
    os.makedirs('../assets/video')
if not os.path.exists('../assets/audio'):
    os.makedirs('../assets/audio')

st.set_page_config(page_title='Health Bridge', page_icon = '../assets/logo.png', initial_sidebar_state = 'auto')

st.title("Welcome to Health Bridge")

txt = st.text_area('Enter your Symptoms to Get Started', ''' ''')

user_video = st.file_uploader("Or Upload Your Video describing your Symptoms", type=['mov','mp4'])

temp_name = '_'+''.join(secrets.choice(string.ascii_uppercase + string.digits)
              for i in range(8))

### Reading Video from User

if user_video is not None:
    video = user_video.read()
    st.video(video)
    with open('../assets/video/temp'+temp_name+'.mp4', "wb") as temp_vid:
        temp_vid.write(video)
