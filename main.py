import streamlit as st
import plotly.express as px
from backend import get_data

# add title, text input, slider, selectbox, and sub header
st.title("Weather Forecast for the next days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get the temperature of sky
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict1["main"]["temp"]/10 for dict1 in filtered_data]
            dates = [dict1["dt_txt"] for dict1 in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict1["weather"][0]["main"] for dict1 in filtered_data]
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.info("The place wasn't found, try again")