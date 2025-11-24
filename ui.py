import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import config
import utils

def render_header():
    """
    Renders the VIT Bhopal branding and student details.
    """
    st.markdown(
        f"""
        <div style="background-color: {config.THEME_COLOR_ORANGE}; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
            <h1 style="color: white; text-align: center; margin: 0;">{config.UNIVERSITY_NAME}</h1>
            <h3 style="color: white; text-align: center; margin: 0;">Weather Dashboard</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.sidebar.markdown(f"### Student Details")
    st.sidebar.info(f"**Name:** {config.STUDENT_NAME}")
    st.sidebar.info(f"**Reg No:** {config.REG_NUMBER}")
    st.sidebar.markdown("---")

def render_current_weather(data):
    """
    Renders the current weather details in cards.
    """
    current = data['current']
    location = data['location']
    
    st.markdown(f"## 📍 {location['name']}, {location['region']}, {location['country']}")
    st.markdown(f"**Local Time:** {location['localtime']}")
    
    # Main Weather Card
    col1, col2 = st.columns([1, 2])
    
    with col1:
        icon_url = utils.get_weather_icon_url(current['condition']['icon'])
        st.image(icon_url, width=100)
        st.markdown(f"### {current['condition']['text']}")
    
    with col2:
        st.metric(label="Temperature", value=f"{current['temp_c']}°C", delta=f"Feels like {current['feelslike_c']}°C")
    
    # Details Grid
    st.markdown("### Details")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Humidity", f"{current['humidity']}%")
    c2.metric("Wind", f"{current['wind_kph']} km/h")
    c3.metric("Pressure", f"{current['pressure_mb']} mb")
    c4.metric("UV Index", f"{current['uv']}")

def render_forecast_charts(forecast_data):
    """
    Renders the hourly forecast chart using Plotly.
    """
    st.markdown("### 24-Hour Forecast")
    
    # Extract hourly data from the first forecast day
    hourly_data = forecast_data['forecast']['forecastday'][0]['hour']
    
    times = [utils.format_time(h['time_epoch']) for h in hourly_data]
    temps = [h['temp_c'] for h in hourly_data]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=times, 
        y=temps, 
        mode='lines+markers',
        name='Temperature',
        line=dict(color=config.THEME_COLOR_ORANGE, width=3)
    ))
    
    fig.update_layout(
        title="Hourly Temperature Trend",
        xaxis_title="Time",
        yaxis_title="Temperature (°C)",
        template="plotly_white",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

def render_7_day_forecast(forecast_data):
    """
    Renders the 7-day forecast in a table.
    """
    st.markdown("### 7-Day Forecast")
    
    days = forecast_data['forecast']['forecastday']
    data = []
    
    for day in days:
        data.append({
            "Date": utils.format_date(day['date']),
            "Condition": day['day']['condition']['text'],
            "Max Temp (°C)": day['day']['maxtemp_c'],
            "Min Temp (°C)": day['day']['mintemp_c'],
            "Chance of Rain (%)": day['day']['daily_chance_of_rain']
        })
        
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True, hide_index=True)

def render_footer():
    """
    Renders the footer.
    """
    st.markdown("---")
    st.markdown(
        f"""
        <div style="text-align: center; color: gray;">
            Submitted by <b>{config.STUDENT_NAME}</b>, {config.REG_NUMBER}, {config.UNIVERSITY_NAME}
        </div>
        """,
        unsafe_allow_html=True
    )
