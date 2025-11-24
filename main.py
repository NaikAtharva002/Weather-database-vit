import streamlit as st
import config
import weather_api
import ui

# Set page config
st.set_page_config(
    page_title=f"Weather Dashboard - {config.UNIVERSITY_NAME}",
    page_icon="⛅",
    layout="wide"
)

def main():
    ui.render_header()
    
    # Search Bar
    city = st.text_input("Enter City Name", "Bhopal")
    
    if city:
        with st.spinner(f"Fetching weather for {city}..."):
            # Fetch Data
            current_weather = weather_api.get_current_weather(city)
            forecast_data = weather_api.get_forecast(city)
            
            if current_weather and forecast_data:
                # Render UI
                ui.render_current_weather(current_weather)
                ui.render_forecast_charts(forecast_data)
                ui.render_7_day_forecast(forecast_data)
            else:
                st.error("City not found or API error. Please check the city name.")
    
    ui.render_footer()

if __name__ == "__main__":
    main()
