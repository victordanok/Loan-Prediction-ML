import pandas as pd
import streamlit as st
import pickle
from sklearn.ensemble import RandomForestClassifier

header = st.container()
dataset = st.container()
features = st.container()
modelTrain = st.container()

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
    st.text('Random Forest Classification Algorithm was used to design this application interface')
    st.text('For the best performance, max_depth of 4 and n_estimators of 100 give the highest accuracy and precision')

    sel_col, disp_col = st.columns(2)
    
    #max_depth = sel_col.slider('What should be the max depth of the model?', min_value = 0, max_value = 20, value = 4, step = 2)
    #n_estimators = sel_col.selectbox('How many trees should there be?', options=[0, 100,200,300,400], index = 1)
    
    
    def user_input_features():

        gender = sel_col.selectbox('Gender', options=['Male', 'Female'])
        if gender == 'Male':
            gender = 0
        else:
            gender = 1
        
        married = sel_col.selectbox('Marital Status', options=['Yes', 'No'])
        if married == 'Yes':
            married = 1
        else:
            married = 0

        kids = sel_col.selectbox('Number of children', options=['0', '1', '2', '3+'])
        if kids == '0':
            kids = 0
        elif kids == '1':
            kids = 1
        elif kids == '2':
            kids = 2
        else:
            kids = 3

        degree = sel_col.selectbox('What is your level of Education', options=['Graduate', 'Not Graduate'])
        if degree == 'Graduate':
            degree = 1
        else:
            degree = 0
    
        employ = sel_col.selectbox('Self Employed', options=['No', 'Yes'])
        if employ == 'Yes':
            employ = 1
        else:
            employ = 0

        property = sel_col.selectbox('Housing Area designation', options=['Urban', 'Rural', 'Semiurban'])
        if property == 'Urban':
            property = 3
        elif property == 'Semiurban':
            property = 2
        else:
            property = 1

        credit = sel_col.selectbox('Credit History', ('Yes', 'No'))
        if credit == 'Yes':
            employ = 1
        else:
            credit = 0

        CoapplicantIncome = sel_col.number_input('Enter your partners income', min_value = 0, value = 0, step = 50)
        ApplicantIncome = sel_col.number_input('Enter your income', min_value = 0, value = 0, step = 50)
        #TotalIncome = sel_col.number_input('Enter your partners income', min_value = 0, value = 0,step = 50)
        LoanAmount = sel_col.number_input('Enter your preferred loan amount', min_value = 0, value = 0, step = 50)
        LoanAmountTerm = sel_col.number_input('Enter your repayment duration', min_value = 12, value = 180, step = 12)

        data = {'gender': [gender],
                'married': [married],
                'kids': [kids],
                'employ':[employ],
                'property':[property],
                'Applicant Income': [ApplicantIncome],
                'Coapplicant Income': [CoapplicantIncome],
                'Total Income': [CoapplicantIncome + ApplicantIncome],
                'Credit history': [credit],
                'Loan Amount': [LoanAmount],
                'Loan Amount Term': [LoanAmountTerm]}

        features = pd.DataFrame(data)
        return features

    input_df = user_input_features()

    sel_col.subheader('User Input Features')
    load = pickle.load(open('testrfc.pkl', 'rb'))

    prediction = load.predict(features)
    sel_col.write([prediction])