import pickle
import pandas as pd

diagonosis_model = pickle.load(open('./telemedicine_model', 'rb'))
   

def predict_disease(csvFile):
    
    df = pd.read_csv(csv_file)
    predictions = diagonosis_model.predict(csvFile)
    return decoded_final[predictions[0]]