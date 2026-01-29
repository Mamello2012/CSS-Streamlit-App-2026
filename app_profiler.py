import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("What can i study with My Marks:RIGHT NOW")

# Collect basic information
name = "Mamello Malape"
institution = "University Of Free State"

# Display basic profile information
st.header("Resear")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
"data:image/jpeg;base64,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",
    caption="Nature (Pixabay)"
)

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add STEM Data Section
st.header("Explore STEM Data")

# Generate dummy data
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Tabbed view for STEM data
st.subheader("STEM Data Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["Physics Experiments", "Astronomy Observations", "Weather Data"]
)

if data_option == "Physics Experiments":
    st.write("### Physics Experiment Data")
    st.dataframe(physics_data)
    # Add widget to filter by Energy levels
    energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
    filtered_physics = physics_data[
        physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
    ]
    st.write(f"Filtered Results for Energy Range {energy_filter}:")
    st.dataframe(filtered_physics)

elif data_option == "Astronomy Observations":
    st.write("### Astronomy Observation Data")
    st.dataframe(astronomy_data)
    # Add widget to filter by Brightness
    brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
    filtered_astronomy = astronomy_data[
        astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
    ]
    st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
    st.dataframe(filtered_astronomy)

elif data_option == "Weather Data":
    st.write("### Weather Data")
    st.dataframe(weather_data)
    # Add widgets to filter by temperature and humidity
    temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
    filtered_weather = weather_data[
        weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
        weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
    ]
    st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
    st.dataframe(filtered_weather)

# Add a contact section
st.header("Contact Information")
email = "jane.doe@example.com"

st.write(f"You can reach {name} at {email}.")


