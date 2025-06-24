# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 10:23:19 2025

@author: jayes
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load trained model
w = pickle.load(open(r'WEATHER_APP/weather(logistic).sav', 'rb'))

def main():
    st.title("🌤️ Weather Data Prediction App")

    # Numeric inputs
    temperature = st.text_input("Temperature (°C)").strip()
    humidity = st.text_input("Humidity (%)").strip()
    wind_speed = st.text_input("Wind Speed (km/h)").strip()
    precipitation = st.text_input("Precipitation (%)").strip()
    pressure = st.text_input("Atmospheric Pressure (hPa)").strip()
    uv_index = st.text_input("UV Index").strip()
    visibility = st.text_input("Visibility (km)").strip()

    # Categorical dropdowns
    cloud_cover = st.selectbox("Cloud Cover", ['overcast', 'partly cloudy', 'clear', 'cloudy'])
    season = st.selectbox("Season", ['Winter', 'Spring', 'Autumn', 'Summer'])
    location = st.selectbox("Location", ['inland', 'mountain', 'coastal'])
    weather_type = st.selectbox("Weather Type", ['Rainy', 'Sunny', 'Cloudy', 'Snowy'])

    # Convert to integer values
    if location == 'inland':
        location_val = 0
    elif location == 'mountain':
        location_val = 1
    else:
        location_val = 2

    if weather_type == 'Rainy':
        weather_type_val = 0
    elif weather_type == 'Sunny':
        weather_type_val = 1
    elif weather_type == 'Cloudy':
        weather_type_val = 2
    else:
        weather_type_val = 3

    if cloud_cover == 'overcast':
        cloud_cover_val = 0
    elif cloud_cover == 'partly cloudy':
        cloud_cover_val = 1
    elif cloud_cover == 'clear':
        cloud_cover_val = 2
    else:
        cloud_cover_val = 3

    if season == 'Winter':
        season_val = 0
    elif season == 'Spring':
        season_val = 1
    elif season == 'Autumn':
        season_val = 2
    else:
        season_val = 3

    # Cast categorical to int explicitly
    location_val = int(location_val)
    weather_type_val = int(weather_type_val)
    cloud_cover_val = int(cloud_cover_val)
    season_val = int(season_val)

    diagnosis = ""

    if st.button("Get Weather Prediction"):
        try:
            # Check for empty fields
            if "" in [temperature, humidity, wind_speed, precipitation, pressure, uv_index, visibility]:
                raise ValueError("Missing input values")

            # Convert inputs to float
            input_list = [
                float(temperature),
                float(humidity),
                float(wind_speed),
                float(precipitation),
                float(pressure),
                float(uv_index),
                float(visibility),
                season_val,
                location_val,
                weather_type_val,
                cloud_cover_val
            ]

            # Predict using model
            prediction = w.predict([input_list])[0]
            diagnosis = f"✅ Weather prediction result: {prediction}"

        except ValueError:
            diagnosis = "❌ Please enter valid numerical values in all fields."

        st.success(diagnosis)

if __name__ == "__main__":
    main()
