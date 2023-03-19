import streamlit as st
import secrets, string
import os
import spacy
import moviepy.editor as mp
import speech_recognition as sr

#Loading NLP to detect nouns in sentence
nlp = spacy.load("en_core_web_sm")

##Creating the temp directories if not present already
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
GenText = []
if option == 'Text':
    userText = st.text_area('Enter your Symptoms to Get Started', ''' ''')

    # Using nlp model for generating the nouns

    Nouns=nlp(userText)
    GenText = [token.text for token in Nouns if token.pos_ == "NOUN"]
    st.write(GenText)

elif option == 'Video':

    user_video = st.file_uploader("Upload Your Video describing your Symptoms", type=['mov','mp4'])

    temp_name = '_'+''.join(secrets.choice(string.ascii_uppercase + string.digits)for i in range(8))

    ### Reading Video from User

    if user_video is not None:
        video = user_video.read()
        st.video(video)
        ##Write video to the temp directory
        with open('assets/video/temp'+temp_name+'.mp4', "wb") as temp_vid:
            temp_vid.write(video)

        ##Get the duration of the video

        clip = mp.VideoFileClip('assets/video/temp'+temp_name+'.mp4')
        duration = int(clip.duration)

        ##Convert to audio

        clip = mp.VideoFileClip('assets/video/temp'+temp_name+'.mp4').subclip(0,duration)
        clip.audio.write_audiofile("assets/audio/temp"+temp_name+'.wav', codec='pcm_s16le')


        r = sr.Recognizer()
        with sr.AudioFile("assets/audio/temp"+temp_name+'.wav') as source:
            audio_text = r.listen(source)
            ##Speech To Text here
            genText = r.recognize_google(audio_text, language='en-IN')
            print('Converting audio transcripts into text ...')
            
            print(genText)

        Nouns=nlp(genText)
        GenText = [token.text for token in Nouns if token.pos_ == "NOUN"]

        st.write(GenText)


if (GenText is not None) or (userText is not None):
    st.button('Submit')  
else:
    st.error('This is an error', icon="🚨")