import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open('model/model.pkl','rb') as file:
            model = pickle.load(file)
            
with open('model/pipe.pkl','rb') as file:
            preprocessor = pickle.load(file)


def main():
    st.title('🩺 Cancer Surivival Prediction 📊')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.number_input("Age")
        Protein1 = st.number_input('Protein1')
        Tumour_Stage = st.selectbox('Tumor_stage',['II', 'I', 'III'])
        ER_status = st.selectbox('ER_status',['Positive','Negative'])
    with col2:
        Gender =  st.selectbox('Gender',['Male', 'Female'])
        Protein2 = st.number_input('Protein2')
        Histology = st.selectbox('Histology',['Infiltrating Ductal Carcinoma', 'Infiltrating Lobular Carcinoma','Mucinous Carcinoma'])
        PR_status = st.selectbox('PR_status',['Positive','Negative'])
    with col3:
        Protein3 = st.number_input('Protein3')
        Protein4 = st.number_input('Protein4')
        HER2_status = st.selectbox('HER2_status',['Negative', 'Positive'])
        Surgery_type = st.selectbox('Surgery_type',['Other', 'Lumpectomy', 'Modified Radical Mastectomy','Simple Mastectomy'])
    
    st.markdown(
    """ 
    #### Problem Statement 
     The objective here is to predict the Breast Cancer Survival Rate for a given order based on features like Age, Gender, protein levels and treatment history.
     """
    )
    survival_labels = {0: 'negative', 1: 'positive'}

    if st.button("Predict"):
        data = pd.DataFrame({
            'Age':[Age],
            'Gender':[Gender],
            'Protein1':[Protein1],
            'Protein2':[Protein2],
            'Protein3':[Protein3],
            'Protein4':[Protein4],
            'Tumour_Stage':[Tumour_Stage],
            'Histology':[Histology],
            'HER2 status':[HER2_status],
            'Surgery_type':[Surgery_type],
            'ER status':[ER_status],
            'PR status':[PR_status]
        })
        
        processed_data = preprocessor.transform(data)
        
        prediction = model.predict(processed_data)[0][0]
        
        if prediction == 1:
            st.markdown(f"<h1 style='text-align: center; font-size: 36px; font-weight: bold; color: green;'>The survival rate of patient is {survival_labels[prediction]} </h1>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h1 style='text-align: center; font-size: 36px; font-weight: bold; color: red;'>The survival rate of patient is {survival_labels[prediction]} </h1>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
