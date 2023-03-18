# HEALTH BRIDGE

## Project Overview

The goal of this project is to develop a machine learning algorithm that can accurately diagnose patients through telemedicine appointments using video input (or text as a fallback option). With the COVID-19 pandemic limiting in-person visits, telemedicine has become increasingly important for providing healthcare to patients. However, accurately diagnosing patients through telemedicine can be challenging due to the limitations of virtual visits. By developing a machine learning algorithm that can analyze patient data from video input and provide accurate diagnoses, we hope to improve patient outcomes and reduce the strain on healthcare systems.

## Data

We will be using a dataset of patients' symptoms that have been gathered from various sources. The data gathered from the sources will be used to train the model, and then we will use natural language processing (NLP) techniques to extract relevant information from the patient.

## Methods

Our approach will be to use speech-to-text technology to convert the patient videos to text data. We will preprocess the text data to extract relevant features and use various NLP techniques to build and train our machine learning model. Then we will be predicting the disease using one of the machine learning algorithms like Naive Bayes, Decision Tree, Random Forest, and K-nearest neighbor (KNN). 

## Results

We will evaluate our model's performance using various metrics such as accuracy, precision, recall, and F1 score. We will also perform cross-validation to ensure that our model is robust and can generalize to new data.

## Getting Started

To get started with this application, you will need to have the dependencies installed on your system. You can install the dependencies using pip:

## Installing Dependencies
```python
pip install -r requirements.txt
```

Once you have installed the dependencies, you can run the application by executing the following command in the root directory 

```python
python -m health-bridge
```

## Conclusion

Through this project, we aim to develop a machine learning algorithm that can accurately diagnose patients through telemedicine appointments using video input. By improving the accuracy of virtual diagnoses, we hope to improve patient outcomes and reduce the strain on healthcare systems. The use of speech-to-text technology and NLP techniques to extract information from patient videos has the potential to revolutionize the way telemedicine appointments are conducted and improve the quality of care provided to patients.
