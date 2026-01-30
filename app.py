import streamlit as st
import pandas as pd
import pickle
import numpy as np
import os

st.set_page_config(page_title="Iris Classifier",page_icon="🌸") # flower = windows + dot

@st.cache_resource
def load_model():

  model_path="iris_model.pkl"
  if os.path.exists(model_path):
    with open(model_path,'rb')as file:
      return pickle.load(file)
  else:
    st.error(f"Model file'{Model_path}' not found!")
    return None
model=load_model()

st.title("🌸 Iris Species Predictor")
st.markdown(""" This app uses a ** logistic Regression** model to predict the species of an Iris flower based on its physical measurement.""")
st.sidebar.header("Input Floral Features")
