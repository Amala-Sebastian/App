
import pickle
import numpy as np
import  streamlit as st 

import tensorflow as tf
load=pickle.load(open('train_model.sav','rb'))
st.title("FAKE NEWS DETECTION")
input_text=st.text_input("Enter news article")
