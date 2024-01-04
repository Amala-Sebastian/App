
import pickle
import numpy as np
import  streamlit as st 


#model=tf.keras.models.load_model("/content/drive/MyDrive/DeepLearning/my_model.keras")
#load=pickle.load(open('train_model.sav','rb'))
#up=st.file_uploader("hdhf",type="jpg")
st.title("FAKE NEWS DETECTION")
input_text=st.text_input("Enter news article")
