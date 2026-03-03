# covid-vaccination-geo-dashboard

## COVID-19 Vaccination Geo Dashboard

An interactive geospatial dashboard visualizing global COVID-19 vaccination data using Python, Bokeh Server, and GeoJSON.

This project integrates vaccination statistics with geographic country boundaries to create a dynamic choropleth world map.

## 01 Features

01. Interactive world choropleth map

02. Date slider for temporal analysis

03. Country filter dropdown

04. Hover tooltips with detailed statistics

05. Color-coded vaccination rates

06. Real-time updates using Bokeh Server

## 02 Dataset

COVID-19 Vaccination Data (CSV)

* Contains:

* Country

* ISO Code

* Date

* Total Vaccinations

* People Vaccinated

* People Fully Vaccinated

* New Deaths

* Population

* Vaccination Ratio (%)

Countries GeoJSON File

* Used to render country boundaries and enable geo mapping.

## 03 Technologies Used

* Python 3.11

* Pandas

* GeoPandas

* Bokeh

* GeoJSON

## 04 Project Structure

covid-vaccination-geo-dashboard/
│
├── main.py
│
└── data/
    ├── covid-vaccination.csv
    └── countries.geojson
    
## 05 Installation & Setup
1️* Clone Repository

git clone https://github.com/Pawarasithumina/covid-vaccination-geo-dashboard.git
cd covid-vaccination-geo-dashboard


2️* Create Conda Environment
conda create -n visualization python=3.11
conda activate visualization


3️* Install Dependencies
pip install pandas geopandas bokeh



## 06 Run the Application

## From the parent directory:

bokeh serve --show covid-vaccination-geo-dashboard


## Open in browser:

http://localhost:5006/covid-vaccination-geo-dashboard



## 07 How It Works

* Loads vaccination CSV data

* Cleans and standardizes ISO country codes

* Merges vaccination data with GeoJSON

* Uses LinearColorMapper to map vaccination rates to colors

* Updates map dynamically based on user input (slider & dropdown)

## 08 Learning Outcomes

* Geo data integration

* Choropleth visualization design

* Bokeh Server deployment

* Interactive dashboard development

* Debugging JSON serialization issues

## 09 Future Improvements

* Metric selector (Vaccination vs Deaths)

* Country click → Time-series chart

* Cloud deployment (Render / Heroku)

* UI enhancements

