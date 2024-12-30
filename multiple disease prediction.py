# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:47:19 2024

@author: pushpa
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu


#loading the models

diabetes_model = pickle.load(open('C:/Users/pushpa/OneDrive/Desktop/Multiple disease predictar/sample models/diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('C:/Users/pushpa/OneDrive/Desktop/Multiple disease predictar/sample models/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('C:/Users/pushpa/OneDrive/Desktop/Multiple disease predictar/sample models/parkinsons_model.sav','rb'))


with st.sidebar:
    
    selected =  option_menu('Multiple Disease Prediction System',
                            ['Diabetes Predictions',
                             'Heart Disease Prediction',
                             'Parkinsons Predictions'],
                            
                            icons = ['activity','heart','person'],
                            
                            default_index = 2)

#Diabates Prediction Page
    
if(selected == 'Diabetes Predictions'):
         
    st.title('Diabetes Predictions using ML')
    
    col1,col2 = st.columns(2)
    
    with col1:
        Pregancies = st.text_input('Number of Pregancies')
    with col2:
        Glucose = st.text_input('Gulcose Level')
    with col1:
        BloodPressure = st.text_input('Number of Blood Pressure value')
    with col2:
        SkinThickness = st.text_input('Skin Thickness value')
    with col1:
        Insulin = st.text_input('Insulin Level')
    with col2:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')
    
    
    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        
        diab_prediction = diabetes_model.predict([[Pregancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is not Diabrtic'
            
    st.success(diab_diagnosis)
    
    
        
if(selected == 'Heart Disease Prediction'):
    
    st.title('Heart Disease Predictions using ML')
    
    col1,col2 = st.columns(2)
    
    with col1:
        age = st.text_input('Age of the person')
    with col2:
        sex = st.text_input('Enter gender')
    with col1:
        cp = st.text_input('Cerebral Palsy')
    with col2:
        trestbps = st.text_input('Resting Blood Pressure')
    with col1:
        chol  = st.text_input('Cholesterol')
    with col2:
        fbs = st.text_input('Fasting Blood Sugar')
    with col1:
        restecg = st.text_input('Resting electrocardiographic')
    with col2:
        thalach = st.text_input('Maximum Teart Rate')
    with col1:
        exang = st.text_input('Exchange Transfusion')
    with col2:
        oldpeak = st.text_input('ST depression')
    with col1:
        slope = st.text_input('ST/HR')
    with col2:
        ca = st.text_input('Coronary artery')
    with col1:
        thal  = st.text_input('Thalassemia')
    with col2:
        target = st.text_input("Target value")
        
        
    heart_test = ''
    
    if st.button('Your Heart Testing Results:'):
        heart_prediction = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target]])
        
        if(heart_test[0]==1):
            heart_test = 'The person Having Heart Diseses'
        else:
            heart_test = 'The person Having NO Heart Diseses'
            
    st.success(heart_test)
         
    
    
    
    
if(selected == 'Parkinsons Predictions'):
    
    
    st.title('Parkinsons Disease Predictions using ML')
        

    col1,col2 = st.columns(2)
    
    with col1:
        name = st.text_input('name')
    with col2:
        MDVP_Fo = st.text_input('Fo(Hz)')
    with col1:
        MDVP_Fhi = st.text_input('Fhi(Hz)')
    with col2:
        MDVP_Flo = st.text_input('Flo(Hz)')
    with col1:
        MDVP_Jitter  = st.text_input('Jitter(%)')
    with col2:
        MDVP_Jitter  = st.text_input('Jitter(Abs)')
    with col1:
        MDVP_RAP = st.text_input('RAP')
    with col2:
        MDVP_PPQ = st.text_input('PPQ')
    with col1:
        Jitter_DDP = st.text_input('value')
    with col2:
        MDVP_Shimmer = st.text_input('DDP')
    with col1:
        MDVP_Shimmer1 = st.text_input('Shimmer')
    with col2: 
        Shimmer_APQ3 = st.text_input('Shimmer(db)')
    with col1: 
        Shimmer_APQ5 = st.text_input('Apo')
    with col2:
        Shimmer_DDA = st.text_input('APQ3')
    with col1:
        NHR  = st.text_input('NHR')
    with col2:
        HNR  = st.text_input('HNR') 
    with col1:
        status = st.text_input('status')
    with col2:
        RPDE  = st.text_input('RPDE')
    with col1:
        DFA  = st.text_input('DFA')
    with col2:
        spread1  = st.text_input('Spread1')
    with col1:
        spread2 = st.text_input('Spread2')
    with col2:
        D2  = st.text_input('D2')
    with col1:
        PPE = st.text_input('PPE') 
        
   
    Parkinsons_test = ''
 
    if st.button('Your Parkinsons Testing Results:'):
        
        Parkinsons_prediction = parkinsons_model.predict([[MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_Jitter,MDVP_Jitter,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer1,Shimmer_APQ3,Shimmer_APQ5,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
     
      
        if(Parkinsons_test[0]==1):
            
           Parkinsons_test = 'The person Having Parkinsons Diseses'
        else:
            
           Parkinsons_test = 'The person Having NO Parkinsons Diseses'
         
    st.success(Parkinsons_prediction)
   
      
 