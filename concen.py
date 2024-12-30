# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 13:18:00 2024

@author: pushpa
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu


#loading the models

concentarte_model = pickle.load(open('C:/jaswanth/model.pkl,'rb'))


with st.sidebar:
    
    selected =  option_menu('Concrete Strength Prediction System ',
                            ['concentarte'],
                            
                           
                            
                            default_index = 0)