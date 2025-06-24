import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load trained model
w = pickle.load(open(r'WEATHER_APP/weather(logistic).sav', 'rb'))

def main():
    st.title("🌤️ Weather Data Prediction App")

    # Numeric inputs (text fields for all values including former dropdowns)
    temperature = st.text_input("Temperature (°C)").strip()
    humidity = st.text_input("Humidity (%)").strip()
    wind_speed = st.text_input("Wind Speed (km/h)").strip()
    precipitation = st.text_input("Precipitation (%)").strip()
    pressure = st.text_input("Atmospheric Pressure (hPa)").strip()
    uv_index = st.text_input("UV Index").strip()
    visibility = st.text_input("Visibility (km)").strip()

    # Previously dropdowns — now numeric fields
    cloud_cover_val = st.text_input("Cloud Cover (0=overcast, 1=partly cloudy, 2=clear, 3=cloudy)").strip()
    season_val = st.text_input("Season (0=Winter, 1=Spring, 2=Autumn, 3=Summer)").strip()
    location_val = st.text_input("Location (0=inland, 1=mountain, 2=coastal)").strip()
    weather_type_val = st.text_input("Weather Type (0=Rainy, 1=Sunny, 2=Cloudy, 3=Snowy)").strip()

    if st.button("Get Weather Prediction"):
        try:
            # Convert all to float (or int, but float is safer for ML models)
            input_list = [
                float(temperature), float(humidity), float(wind_speed), float(precipitation),
                float(pressure), float(uv_index), float(visibility),
                float(season_val), float(location_val), float(weather_type_val), float(cloud_cover_val)
            ]

            # Debug view
            st.write("🔍 Input to model:", input_list)

            # Prediction
            prediction = w.predict([input_list])[0]
            diagnosis = f"✅ Weather prediction result: {prediction}"

        except Exception as e:
            st.error(f"❌ Error: {e}")
        else:
            st.success(diagnosis)

if __name__ == "__main__":
    main()
