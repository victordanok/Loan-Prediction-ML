# Loan-Prediction-ML

## Overview
Before giving out a loan, companies would need to access the loan eligibility of their clients and their capabilities to pay back the loan. <br>
Develop an API to determine the Loan eligibility of clients based on socio-economic factors.

## Tools / Packages Used
<ul>
  <li> Python </li>
  <li> Numpy </li>
  <li> Pandas </li>
  <li> Matplotlib and seaborn for data visualizations </li>
  <li> Scikit-learn for Machine Learning </li>
</ul>

## Data
The data was gotten in two parts;
<ul>
<li> train.csv - the dataset for the model to be trained on consisting of past loans and their loan status </li>
<li> test.csv - the new customers for which we want to find their loan eligibility </li>
</ul>

The columns in the dataset are:
1. Gender                
2. Married                
3. Dependents            
4. Education              
5. Self_Employed         
6. ApplicantIncome        
7. CoapplicantIncome     
8. LoanAmount            
9. Loan_Amount_Term      
10. Credit_History        
11. Property_Area          
12. Loan_Status       

## Feature engineering
Taking the input of ApplicantIncome and CoApplicantIncome, the sum was used to calculate the Total Income of the household
Adding this feature to the data increases the accuracy and precision of the models.

## Model Performance
1. Logistic Regression has an accuracy of 0.84.
2. Naive Bayes has an overall accuracy of 0.82.
3. Random Forest has an overall accuracy of 0.78 using GridSearchCV
4. Decision Trees has an overall accuracy of 0.71

## API Development
A streamlit app is being built to collect inputs on gender, marital status, number of kids, total income, emloyment status, credit history, and property area.
After accepting these inputs, the model will be run using the best number of estimators and max depth to ensure the highest accuracy for prediction.








