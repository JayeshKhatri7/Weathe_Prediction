# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 10:23:19 2025

@author: jayes
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load model
w = pickle.load(open(r'C:\internship\sav\weather(logistic).sav', 'rb'))

def main():
    st.title("Weather Data Prediction App")

    # Numeric inputs
    temperature = st.text_input("Temperature (°C)")
    humidity = st.text_input("Humidity (%)")
    wind_speed = st.text_input("Wind Speed (km/h)")
    precipitation = st.text_input("Precipitation (%)")
    pressure = st.text_input("Atmospheric Pressure (hPa)")
    uv_index = st.text_input("UV Index")
    visibility = st.text_input("Visibility (km)")

    # Categorical inputs
    cloud_cover = st.selectbox("Cloud Cover", ['overcast', 'partly cloudy', 'clear', 'cloudy'])
    season = st.selectbox("Season", ['Winter', 'Spring', 'Autumn', 'Summer'])
    location = st.selectbox("Location", ['inland', 'mountain', 'coastal'])
    weather_type = st.selectbox("Weather Type", ['Rainy', 'Sunny', 'Cloudy', 'Snowy'])

    # Convert to numeric
    location_val = 0 if location == 'inland' else 1 if location == 'mountain' else 2
    weather_type_val = {'Rainy': 0, 'Sunny': 1, 'Cloudy': 2, 'Snowy': 3}[weather_type]
    cloud_cover_val = {'overcast': 0, 'partly cloudy': 1, 'clear': 2, 'cloudy': 3}[cloud_cover]
    season_val = {'Winter': 0, 'Spring': 1, 'Autumn': 2, 'Summer': 3}[season]

    diagnosis = ""
    if st.button("Get Weather Prediction"):
        try:
            input_list = [
                float(temperature), float(humidity), float(wind_speed), float(precipitation),
                float(pressure), float(uv_index), float(visibility),
                season_val, location_val, weather_type_val, cloud_cover_val
            ]
            prediction = w.predict([input_list])[0]
            diagnosis = f"✅ Weather prediction: {prediction}"
        except ValueError:
            diagnosis = "❌ Please enter valid numerical values in all fields."

        st.success(diagnosis)

if __name__ == "__main__":
    main()
