# covid-vaccination-geo-dashboard

## COVID-19 Vaccination Geo Dashboard

An interactive geospatial dashboard visualizing global COVID-19 vaccination data using Python, Bokeh Server, and GeoJSON.

This project integrates vaccination statistics with geographic country boundaries to create a dynamic choropleth world map.

Features

01 Interactive world choropleth map

02 Date slider for temporal analysis

03 Country filter dropdown

04 Hover tooltips with detailed statistics

05 Color-coded vaccination rates

06 Real-time updates using Bokeh Server

Dataset
1️⃣ COVID-19 Vaccination Data (CSV)

Contains:

Country

ISO Code

Date

Total Vaccinations

People Vaccinated

People Fully Vaccinated

New Deaths

Population

Vaccination Ratio (%)

2️⃣ Countries GeoJSON File

Used to render country boundaries and enable geo mapping.

🛠️ Technologies Used

Python 3.11

Pandas

GeoPandas

Bokeh

GeoJSON

📁 Project Structure
covid-vaccination-geo-dashboard/
│
├── main.py
│
└── data/
    ├── covid-vaccination.csv
    └── countries.geojson
    
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/Pawarasithumina/covid-vaccination-geo-dashboard.git
cd covid-vaccination-geo-dashboard

2️⃣ Create Conda Environment
conda create -n visualization python=3.11
conda activate visualization

3️⃣ Install Dependencies
pip install pandas geopandas bokeh


▶️ Run the Application

From the parent directory:

bokeh serve --show covid-vaccination-geo-dashboard

Open in browser:

http://localhost:5006/covid-vaccination-geo-dashboard
📌 How It Works

Loads vaccination CSV data

Cleans and standardizes ISO country codes

Merges vaccination data with GeoJSON

Uses LinearColorMapper to map vaccination rates to colors

Updates map dynamically based on user input (slider & dropdown)

🎯 Learning Outcomes

Geo data integration

Choropleth visualization design

Bokeh Server deployment

Interactive dashboard development

Debugging JSON serialization issues

🔮 Future Improvements

Metric selector (Vaccination vs Deaths)

Country click → Time-series chart

Cloud deployment (Render / Heroku)

UI enhancements

👤 Author

Sanju
Undergraduate – Data Science

📜 License

This project is created for academic purposes.
