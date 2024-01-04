
import pickle
import numpy as np
import  streamlit as st 
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Embedding, GRU, LSTM, RNN, SpatialDropout1D
import tensorflow as tf

#model=tf.keras.models.load_model("/content/drive/MyDrive/DeepLearning/my_model.keras")
load=pickle.load(open('train_model.sav','rb'))
#up=st.file_uploader("hdhf",type="jpg")
st.title("FAKE NEWS DETECTION")
input_text=st.text_input("Enter news article")
