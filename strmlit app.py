import pandas as pd
import streamlit as st

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
modelTrain = st.beta_container()

with header:
    st.title('Loan Prediction')
    st.text('In this project, we will determine customers who are going to be granted their loan request on the basis that they would be able to pay them')

with dataset:
    st.header('Loan Prediction dataset')
    st.text('The datasets are;')
    st.markdown('* **train.csv** - The dataset for the model to be trained on consisting of past loans and their approval status')
    trdata = pd.read_csv('train.csv')
    st.write(trdata.head())

    st.markdown('* **test.csv** - The new applicants with loan requests awaiting consideration')
    tdata = pd.read_csv('test.csv')
    st.write(tdata.head())

with features:
    st.header('The features I created')
    st.markdown('* **Total Income** - I created this from the sum of applicant and co-applicant income so the total earnings of the household can be seen in one glance')

with modelTrain:
    st.header('Model Training')
    st.text('The best performing model out of five selections was used to design this application interface')

    sel_col, disp_col = st.beta_columns(2)
    
    max_depth = sel_col.slider('What should be the max depth of the model?', min_value = 0, max_value = 20, value = 4, step = 2)

    n_estimators = sel_col.selectbox('How many trees should there be?', options=[0, 100,200,300,400], index = 1)