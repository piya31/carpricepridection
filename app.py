import pandas as pd
import numpy as np
import pickle as pk 
import streamlit as st

Reg = pk.load(open('reg.pkl','rb'))

st.header("CAR PRICE PREDICTION SYSTEM")

cars_data = pd.read_csv(r"C:\Users\piyab\OneDrive\Desktop\ML Project\Car_details_updated.csv")

def get_brand_name(car_name):
  car_name = car_name.split(' ')[0]
  return car_name.strip()

cars_data['name'] = cars_data['name'].apply(get_brand_name)

name = st.selectbox('SELECT CAR BRAND', cars_data['name'].unique())

year = st.slider('SELECT MANUFACTURING YEAR', 1980,2024 )

km_driven = st.slider('SELECT KM DRIVEN', 0,3000000)

fuel = st.selectbox('SELECT FUEL TYPE', cars_data['fuel'].unique())

seller_type = st.selectbox("SELECT SELLER TYPE", cars_data['seller_type'].unique())

transmission = st.selectbox('SELECT TRANSMISSION TYPE', cars_data['transmission'].unique())

owner = st.selectbox('SELECT OWNER', cars_data['owner'].unique())

mileage = st.slider('SELECT CAR MILEAGE', 10,45)

engine = st.slider('SELECT ENGINE CAPACITY', 500,5000)

max_power = st.slider('SELECT MAX POWER', 0,500)

seats = st.slider('SELECT NUMBER OF SEATS', 5,10)

actual_price= st.slider('ACTUAL CAR PRICE', 500000, 30000000)

if st.button("PREDICT"):
  input_data= pd.DataFrame([[name, year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats, actual_price]], columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats','actual_price'])
  # st.write(input_data)

  input_data.fuel.replace({'Diesel':1, 'Petrol':2, 'CNG':3, 'LPG':4}, inplace= True)
  input_data.seller_type.replace({'Individual':1, 'Dealer':2, 'Trustmark Dealer':3,}, inplace= True)
  input_data.transmission.replace({'Manual':1, 'Automatic':2}, inplace= True)
  input_data['owner'] = cars_data['owner'].str.strip()  # Remove extra spaces/tabs
  input_data['owner'].replace({'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3, 'Fourth & Above Owner': 4, 'Test Drive Car': 5}, inplace=True)
  input_data.name.replace(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
       'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
       'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
       'Ambassador', 'Ashok', 'Isuzu', 'Opel'],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31], inplace = True)

  car_price = Reg.predict(input_data)     
  st.markdown(f"**THE PRICE OF CAR WILL BE:** {float(car_price[0][0]):.2f}")



