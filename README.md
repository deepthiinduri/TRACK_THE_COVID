<img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/TRACK%20THE%20COVID%20LOGO.png">

> **TRACK THE COVID Application helps in tracking and breaking chains of transmission of COVID-19. It uses maps and graphs to analyze the global distribution of covid-19.**
> 
> **This tracker is designed to inform people regarding risks, best practices and relevant advisories related to coronavirus.**
> 
> **It helps to check the availability of vaccination centers in your area (India) and also shows Helplines, Regional Contacts and fetch covid-19 related news.**
> 
> **It also has a feature of a Symptom Analyser in which it calculates the probability of an individual getting infected by covid-19.**


## Table of Contents

- [Prerequisites](#prerequisites)
- [Important Links](#important-links)
- [About the project](#about-the-project)
  - [Home Page](#-home-page)
    - [Importing Modules](#importing-modules)
    - [Calling functions](#calling-functions-defined-in-other-python-files-to-mainpy)
    - [Main.py](#main-code---mainpy)
    - [Requesting Web Page and Pulling data](#make-a-request-to-a-web-page-and-pulling-data-out-of-file-using-requests-and-beautifulsoup-modules)
    - [Indiacases.py](#code---indiacasespy)
  - [State Wise](#-state-wise-india)
    - [Importing Covid and Coivd_India Modules](#importing-covid-and-covid_india-modules)
    - [State Wise Visualization - Graph](#state-wise-visualization---graph)
    - [District Wise Visualization - Graph](#district-wise-visualization---graph)
    - [Top 10 States Visualization](#top-10-cases-states)
    - [StateWise.py](#statewise-code---statewisepy)
  - [Country Wise](#-country-wise)
    - [Importing Modules](#importing-pycountry-and-folium-modules)
    - [World Cases Visualization Using Folium Maps](#world-cases-maps)
    - [Top 10 Countries Visualization](#top-10-cases-countries)
    - [CountryWise.py](#countrywise-code---countrywisepy)
  - [Health Info](#-health-info)
    - [Symptoms](#)
    - [Precautions](#)
    - [Treatments](#)
    - [Vaccination](#)

## Prerequisites

Inorder to get this project working on system. We need to install the following:
1. Python 3 - 64 Bit
2. Visual Studio - June 2021 (version 1.58) (or) any other editions
3. Web Browser - Mozilla Firefox (or) Google Chrome (or) Microsoft Edge (or) Internet Explorer
4. Internet - Ethernet connection / a wireless adapter (Wi-Fi)
5. Modules:
* tkinter, tkinter.ttk
* bs4, requests, webbrowser
* numpy, seaborn, pandas, folium, matplotlib, tabulate
* PIL, threading, urllib, plyer, prettytable
* covid, covid_india, pycountry

### Important Links

Data is collected from different sources-
1.  https://www.mohfw.gov.in/
2.	https://api.covid19india.org/data.json
3.	https://api.covid19india.org/state_district_wise.json
4.	https://api.covid19api.com/summary
5.	https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json
6.	https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=json
7.  https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv
8.	https://covid19.trackvaccines.org/
9.	https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}
10.	https://www.who.int/



## About the project

### 🏡 Home Page

In the Home Page the Tracker shows the number of Active, Deaths, Discharged cases from novel coronavirus and Vaccinations in India with Refresh and Exit buttons.

#### Importing Modules

```python

from tkinter import *
import requests
import bs4
from bs4 import BeautifulSoup
import json
import time
import datetime
import webbrowser
import datetime as dt
from PIL import ImageTk, Image ,ImageDraw, ImageFont, ImageFilter

```

#### Calling functions defined in other Python files to Main.py

```python

from Indiacases import get_corona_detail_of_india
from statewise import state_wise_info
from countrywise import country_wise_info
from healthinfo import covid_symptoms, covid_precautions, covid_treatments
from vaccination import covid_vaccination
from notifandhelpline import notif_and_helplines
from symptomanalyser import Syptom_analyser

```

##### Main code - [Main.py](https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/Main.py)

#### Make a request to a web page, and pulling data out of file using requests and Beautifulsoup modules:

```python

url = "https://www.mohfw.gov.in/"
html_data = requests.get(url)
bs = bs4.BeautifulSoup(html_data.text,'html.parser')

```

##### Code - [Indiacases.py](https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/Indiacases.py)

<img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Home%20Page.png">


### 👩‍👧 State Wise (India)
#### Importing covid and covid_india Modules

```python

from covid import Covid
from covid_india import states

```
#### covid and covid_india modules:
> ***covid*** - Python package to get information regarding the novel corona virus provided by Johns Hopkins university and worldometers.info
> 
> ***covid_india*** - Python package for providing data for the COVID-19 cases in India. This can provide data both online as well as offline.

The requests Python module retrieves JSON data and decode it, due to it's builtin JSON decoder and Convert the dictionary data into DataFrame using pandas.

```python

url = 'https://api.covid19india.org/data.json'
jsn = requests.get(url).json()
statewise = jsn['statewise']
df = pd.DataFrame(statewise)
    
```

<img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/State%20Wise.png">

#### State Wise Visualization - Graph

All the plotly graphs are displayed in the default web browser.

```python

def get_state_info_graph():
    df1 = df
    df1['active'] = df1['active'].apply(lambda x : int(x))
    df1['deaths'] = df1['deaths'].apply(lambda x : int(x))
    df1['confirmed'] = df1['confirmed'].apply(lambda x : int(x))
    df1['recovered'] = df1['recovered'].apply(lambda x : int(x))
    states = df1['state']
    fig = go.Figure(data = [go.Bar(name = 'confirmed', x = states, y = df1['confirmed']),go.Bar(name = 'active', x = states, y = df1['active']),go.Bar(name = 'recovered', x = states, y = df1['recovered'])])
    fig.update_layout(barmode = 'group')
    fig.show()

```
#### District Wise Visualization - Graph

```python

def district_wise():
    url = 'https://api.covid19india.org/state_district_wise.json'
    jsn = requests.get(url).json()
    searchstate = txt.get()
    district = jsn[searchstate]
    df = pd.DataFrame(district)
    for key in district['districtData']:
        district['districtData'][key].pop('notes', None)
        district['districtData'][key].pop('migratedother', None)
        district['districtData'][key].pop('delta', None)
    keys = district['districtData'].keys()
    df = pd.DataFrame.from_dict(district['districtData'], orient = 'index').reset_index(drop=True)
    df['Names'] = keys
    df = df.drop(df.index[0])
    df['active'] = df['active'].apply(lambda x : int(x))
    df['deceased'] = df['deceased'].apply(lambda x : int(x))
    df['confirmed'] = df['confirmed'].apply(lambda x : int(x))
    df['recovered'] = df['recovered'].apply(lambda x : int(x))
    states = df['Names']
    fig = go.Figure(data = [go.Bar(name = 'confirmed', x = states, y = df['confirmed']),go.Bar(name = 'active', x = states, y = df['active']),go.Bar(name = 'recovered', x = states, y = df['recovered']),go.Bar(name = 'deceased', x = states, y = df['deceased'])])
    fig.update_layout(barmode = 'group')
    fig.show()

```

<p align="center">
  <img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/State%20Wise%20Graph.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/District%20Wise%20Graph.png" width="45%">
</p>

#### Top 10 Cases States

Code for Top 10 Confirmed States

```python

def top10_confirmed_states():
    df2 = df
    df2['confirmed'] = df2['confirmed'].apply(lambda x : int(x))
    df2 = df2.sort_values(by = ['confirmed'], ascending = False).head(10)
    states = df2['state']
    fig = go.Figure(data = [go.Bar(name = 'confirmed', x = states, y = df2['confirmed'])])
    fig.update_traces(marker_color = 'rgb(158,202,225)', marker_line_color = 'rgb(8,48,107)',marker_line_width = 1.5, opacity = 0.6)
    fig.update_layout(barmode = 'group',title = "Top-10 Confirmed Cases States")
    fig.show()

```

<p align="center">
  <img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Top%2010%20Confirmed%20Cases%20States.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Top%2010%20Deaths%20Cases%20States.png" width="45%">
</p>
<p align="center">
  <img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Top%2010%20%20Recovered%20Cases%20States.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Top%2010%20Active%20Cases%20States.png" width="45%">
</p>

##### Statewise Code - [StateWise.py](https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/statewise.py)


### 👩‍👩‍👧‍👧 Country Wise

#### Importing pycountry and folium modules

```python

import pycountry
import html5lib
import plyer
import urllib.request
import folium
from folium.plugins import HeatMap

```

<img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Country%20Wise.png">

#### World Cases (Maps)

Code to create folium maps

```python

def map_world():
    conn = http.client.HTTPSConnection("api.covid19api.com")
    payload = ''
    headers = {}
    conn.request("GET", "/summary", payload, headers)
    res = conn.getresponse()
    data = res.read().decode('UTF-8')
    covid1= json.loads(data)
    pd.json_normalize(covid1['Countries'],sep=",")
    df = pd.DataFrame(covid1['Countries'])
    covid2 = df.drop(columns =['CountryCode','Slug','Date','Premium'],axis=1)
    m = folium.Map(tiles="Stamen Terrain", min_zoom=1.5)
    url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
    country_shapes = f'{url}/world-countries.json'
    folium.Choropleth(geo_data=country_shapes, min_zoom=2, name='COVID-19', data=covid2, columns=['Country', 'TotalConfirmed'], key_on='feature.properties.name', fill_color='OrRd',    nan_fill_color='black',  legend_name='Total Confirmed Covid Cases',).add_to(m)

    covid2.update(covid2['TotalConfirmed'].map('Total Confirmed:{}'.format))
    covid2.update(covid2['TotalRecovered'].map('Total Recovered:{}'.format))
    coordinates = pd.read_csv('C:/Users/DELL/Documents/Folder1/countries-csv.csv')
    covid_final= pd.merge(covid2,coordinates,on='Country')

    def plotDot(point):
        folium.CircleMarker(location=[point.latitude, point.longitude],radius=5,weight=2,popup = [point.Country,point.TotalConfirmed,point.TotalRecovered],fill_color='#000000').add_to(m)
    covid_final.apply(plotDot, axis = 1)
    m.fit_bounds(m.get_bounds())
    m.save("covid_map_1.html")
    webbrowser.open("covid_map_1.html")

```

<p align="center">
  <img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/COVID%20MAP%201.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/COVID%20MAP%202.png" width="45%">
</p>


> **To create the maps folium module is used.**
> 
> **Folium makes easy to visualize data in Python on an interactive map. It enables both the binding of data to a map for choropleth visualizations as well as passing HTML visualizations as markers on the map.**
> 
> **Here to create the map we used two url's. One is to get the latitudes and longitudes to place all the countries and the other is to get the covid-19 data.**
> 
> **Using folium.CircleMarker method when we give the lat , long , radius ,colour ; circle is created at that specific place.**
> 
> **The created Folium map is saved as HTML file. This HTML file is opened using webbrowser.open() method.**

#### Top 10 Cases Countries

Code for Top 10 Countries(Confirmed, Deaths, Recovered, Active)

```python

def confirmed_cases_countries():
    top10_confirmed = pd.DataFrame(data.groupby('Country')['Confirmed'].sum().nlargest(10).sort_values(ascending = False))
    fig1 = px.scatter(top10_confirmed, x = top10_confirmed.index, y = 'Confirmed', size = 'Confirmed', size_max = 120,
            color = top10_confirmed.index, title = 'Top 10 Confirmed Cases Countries')
    fig1.show()
    
def confirmed_deaths_countries():
    top10_deaths = pd.DataFrame(data.groupby('Country')['Deaths'].sum().nlargest(10).sort_values(ascending = True))
    fig2 = px.bar(top10_deaths, x = 'Deaths', y = top10_deaths.index, height = 600, color = 'Deaths', orientation = 'h',
        color_continuous_scale = ['deepskyblue','red'], title = 'Top 10 Death Cases Countries')
    fig2.show()
    
def confirmed_recovered_countries():
    top10_recovered = pd.DataFrame(data.groupby('Country')['Recovered'].sum().nlargest(10).sort_values(ascending = False))
    fig3 = px.bar(top10_recovered, x = top10_recovered.index, y = 'Recovered', height = 600, color = 'Recovered',
         title = 'Top 10 Recovered Cases Countries', color_continuous_scale = px.colors.sequential.Viridis)
    fig3.show()
    
def confirmed_active_countries():
    top10_active = pd.DataFrame(data.groupby('Country')['Active'].sum().nlargest(10).sort_values(ascending = True))
    fig4 = px.bar(top10_active, x = 'Active', y = top10_active.index, height = 600, color = 'Active', orientation = 'h',
         color_continuous_scale = ['paleturquoise','blue'], title = 'Top 10 Active Cases Countries')
    fig4.show()

```

<p align="center">
  <img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Top%2010%20Confirmed%20Cases%20Countries.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Top%2010%20Death%20Cases%20Countries.png" width="45%">
</p>
<p align="center">
  <img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Top%2010%20Recovered%20Cases%20Countries.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Top%2010%20Active%20Cases%20Countries.png" width="45%">
</p>

##### Countrywise Code - [CountryWise.py](https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/countrywise.py)


### 🤒 Health Info

<img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Health%20Info.png" align="left" width="300px"/>
HealthInfo contains Symptoms, Treatments, Precautions of Covid-19 and Vaccinations all around the world and available vaccination centers in India for the next 10 days.
<img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Symptoms%20page.png" width="45%" align="right">
<p align="center">
  <img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Treatments%20page.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Precautions%20page.png" width="45%">
</p>
