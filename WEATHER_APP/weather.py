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
    location_val = 0 if location == 'inland' else 1 if location == 'mountain' else 2
    weather_type_val = {'Rainy': 0, 'Sunny': 1, 'Cloudy': 2, 'Snowy': 3}[weather_type]
    cloud_cover_val = {'overcast': 0, 'partly cloudy': 1, 'clear': 2, 'cloudy': 3}[cloud_cover]
    season_val = {'Winter': 0, 'Spring': 1, 'Autumn': 2, 'Summer': 3}[season]

    # Prediction button logic
    if st.button("Get Weather Prediction"):
        try:
            # Convert input fields to float
            float_inputs = [
                float(temperature),
                float(humidity),
                float(wind_speed),
                float(precipitation),
                float(pressure),
                float(uv_index),
                float(visibility)
            ]

            # Create final input list for prediction
            input_list = float_inputs + [
                int(season_val),
                int(location_val),
                int(weather_type_val),
                int(cloud_cover_val)
            ]

            # Debug: show model input
            st.write("🔍 Input to model:", input_list)

            # Predict using model
            prediction = w.predict([input_list])[0]
            diagnosis = f"✅ Weather prediction result: {prediction}"

        except Exception as e:
            diagnosis = f"❌ Error: {e}"

        st.success(diagnosis)

# Run the app
if __name__ == "__main__":
    main()
