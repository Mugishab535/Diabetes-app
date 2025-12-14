import stramlit as st
import pickle
import numpy as np 
with open('GROUP_05.pkl','rb') as file:
    model=pickle.load(file)
    
st.title("DIABETES PREDICTION")
st.write("enter the following data")
PG=st.number_input("Pregnancies",value=0.0)
GS=st.number_input("Glucose",value=0.0)
BP=st.number_input("BloodPressure",value=0.0)
ST=st.number_input("SkinThickness",value=0.0)
IS=st.number_input("Insulin",value=0.0)
BM=st.number_input("BMI",value=0.0)
DP=st.number_input("DiabetesPedigreeFunction",value=0.0)
AG=st.number_input("Age",value=0.0)
if st.button("predict patient diabetes"):
    Input=np.array([[PG,GS,BP,ST,IS,BM,DP,AG]])
    prediction=model.predict(Input)
    st.success(pediction[0])

