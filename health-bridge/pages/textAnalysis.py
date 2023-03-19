import streamlit as st
import secrets, string
import os
import moviepy.editor as mp
import speech_recognition as sr

##Creating the temp directories
if not os.path.exists('assets/video'):
    os.makedirs('assets/video')
if not os.path.exists('assets/audio'):
    os.makedirs('assets/audio')

st.set_page_config(page_title='Health Bridge', page_icon = 'assets/logo.png', initial_sidebar_state = 'auto')

st.title("Welcome to Health Bridge")
st.info('Please choose the option to communicate with our ML Model', icon="ℹ️")

option = st.selectbox(
    'How would you like to communicate ?',
    ('Enter your Choice','Text', 'Video'))

st.write('You selected:', option)

userText = ""
GenText = ""
if option == 'Text':
    userText = st.text_area('Enter your Symptoms to Get Started', ''' ''')
elif option == 'Video':
    user_video = st.file_uploader("Upload Your Video describing your Symptoms", type=['mov','mp4'])

    temp_name = '_'+''.join(secrets.choice(string.ascii_uppercase + string.digits)for i in range(8))

    ### Reading Video from User

    if user_video is not None:
        video = user_video.read()
        st.video(video)
        with open('assets/video/temp'+temp_name+'.mp4', "wb") as temp_vid:
            temp_vid.write(video)

        clip = mp.VideoFileClip('assets/video/temp'+temp_name+'.mp4').subclip(0,5)
        clip.audio.write_audiofile("assets/audio/temp"+temp_name+'.wav', codec='pcm_s16le')

        r = sr.Recognizer()
        with sr.AudioFile("assets/audio/temp"+temp_name+'.wav') as source:
            audio_text = r.listen(source)
            genText = r.recognize_google(audio_text, language='en-IN', show_all=True)
            print('Converting audio transcripts into text ...')
            print(GenText)