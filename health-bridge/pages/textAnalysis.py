import streamlit as st
import secrets, string
import os
import spacy
import moviepy.editor as mp
import speech_recognition as sr
import csv
import pandas as pd
import pickle

symptoms = ['itching', 'skin rash', 'nodal skin eruptions', 'continuous sneezing', 'shivering', 'chills', 'joint pain', 'stomach pain', 'acidity', 'ulcers on tongue', 'muscle wasting', 'vomiting', 'burning micturition', 'spotting  urination', 'fatigue', 'weight gain', 'anxiety', 'cold hands and feets', 'mood swings', 'weight loss', 'restlessness', 'lethargy', 'patches in throat', 'irregular sugar level', 'cough', 'high fever', 'sunken eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish skin', 'dark urine', 'nausea', 'loss of appetite', 'pain behind the eyes', 'back pain', 'constipation', 'abdominal pain', 'diarrhoea', 'mild fever', 'yellow urine', 'yellowing of eyes', 'acute liver failure', 'fluid overload', 'swelling of stomach', 'swelled lymph nodes', 'malaise', 'blurred and distorted vision', 'phlegm', 'throat irritation', 'redness of eyes', 'sinus pressure', 'runny nose', 'congestion', 'chest pain', 'weakness in limbs', 'fast heart rate', 'pain during bowel movements', 'pain in anal region', 'bloody stool', 'irritation in anus', 'neck pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen legs', 'swollen blood vessels', 'puffy face and eyes', 'enlarged thyroid', 'brittle nails', 'swollen extremeties', 'excessive hunger', 'extra marital contacts', 'drying and tingling lips', 'slurred speech', 'knee pain', 'hip joint pain', 'muscle weakness', 'stiff neck', 'swelling joints', 'movement stiffness', 'spinning movements', 'loss of balance', 'unsteadiness', 'weakness of one body side', 'loss of smell', 'bladder discomfort', 'foul smell of urine', 'continuous feel of urine', 'passage of gases', 'internal itching', 'toxic look (typhos)', 'depression', 'irritability', 'muscle pain', 'altered sensorium', 'red spots over body', 'belly pain', 'abnormal menstruation', 'dischromic  patches', 'watering from eyes', 'increased appetite', 'polyuria', 'family history', 'mucoid sputum', 'rusty sputum', 'lack of concentration', 'visual disturbances', 'receiving blood transfusion', 'receiving unsterile injections', 'coma', 'stomach bleeding', 'distention of abdomen', 'history of alcohol consumption', 'fluid overload', 'blood in sputum', 'prominent veins on calf', 'palpitations', 'painful walking', 'pus filled pimples', 'blackheads', 'scurring', 'skin peeling', 'silver like dusting', 'small dents in nails', 'inflammatory nails', 'blister', 'red sore around nose', 'yellow crust ooze']

new_symptoms = []

new_list = [0]*len(symptoms)

def pred():
    diagonosis_model = pickle.load(open('models/telemedicine_model', 'rb'))
    decoded_final = {15: "Fungal Infection",4:"Allergy",16:"GERD",9:"Chronic cholestasis",14:'Drug Reaction'
    ,33:'Peptic ulcer diseae'
    ,1:'AIDS'
    ,12:'Diabetes' 
    ,17:'Gastroenteritis'
    ,6:'Bronchial Asthma'
    ,23:'Hypertension' 
    ,30:'Migraine'
    ,7:'Cervical spondylosis'
    ,32:'Paralysis (brain hemorrhage)'
    ,28:'Jaundice'
    ,29:'Malaria'
    ,8:'Chicken pox'
    ,11:'Dengue'
    ,37:'Typhoid'
    ,40:'hepatitis A'
    ,19:'Hepatitis B'
    ,20:'Hepatitis C'
    ,21:'Hepatitis D'
    ,22:'Hepatitis E'
    ,3:'Alcoholic hepatitis'
    ,36:'Tuberculosis'
    ,10:'Common Cold'
    ,34:'Pneumonia'
    ,13:'Dimorphic hemmorhoids(piles)'
    ,18:'Heart attack'
    ,39:'Varicose veins'
    ,26:'Hypothyroidism'
    ,24:'Hyperthyroidism'
    ,25:'Hypoglycemia'
    ,31:'Osteoarthristis'
    ,5:'Arthritis'
    ,0:'(vertigo) Paroymsal  Positional Vertigo'
    ,2:'Acne'
    ,38:'Urinary tract infection',35:'Psoriasis',27:'Impetigo'
    }
    csv_file = "models/predict.csv"
    df = pd.read_csv(csv_file)
    predictions = diagonosis_model.predict(df)
    return decoded_final[predictions[0]]


def validate(text):
    # Using nlp model for generating the nouns

    Nouns=nlp(text)
    GenText = [chunk.text for chunk in Nouns.noun_chunks]
    common_elements = [element for element in GenText if element in symptoms]
    common_elements = [string.replace(' ', '_') for string in common_elements]
    return common_elements

def generate_csv(iter):
    new_symptoms = [string.replace(' ', '_') for string in symptoms]
    for i in iter:
        ind = new_symptoms.index(i)
        print(ind)
        new_list[ind] = 1
    print(new_list)
    with open("models/predict.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(new_symptoms)
        writer.writerow(new_list)


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
common_elements = ""
if option == 'Text':
    userText = st.text_area('Enter your Symptoms to Get Started', ''' ''')
    common_elements = validate(userText)
    st.write(common_elements)
    generate_csv(common_elements)
    
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
        genText = ""
        with sr.AudioFile("assets/audio/temp"+temp_name+'.wav') as source:
            audio_text = r.listen(source)
            ##Speech To Text here
            genText = r.recognize_google(audio_text, language='en-IN')
            print('Converting audio transcripts into text ...')

            print(genText)
            print(type(genText))

        common_elements = validate(genText)
        st.write(common_elements)
        generate_csv(common_elements)


if (GenText is not None) or (userText is not None):
    if st.button('Submit Result'):
        disease = pre()
        st.write("You are suffering from:", disease)
else:
    st.error('This is an error', icon="🚨")

if __name__=="__main__":
    pass