from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib.dates import DateFormatter, WeekdayLocator
from datetime import timedelta
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pycountry
from prettytable import PrettyTable
from IPython.core.display import display, HTML
from threading import Thread
from pandas.core.frame import DataFrame
import json
import html5lib
import plyer
import urllib.request
import folium
from folium.plugins import HeatMap
from pandas.io.json import json_normalize
import plotly.graph_objects as go
from PIL import ImageTk, Image ,ImageDraw, ImageFont, ImageFilter
import imageio
import webbrowser
import http.client
import time
import datetime
import datetime as dt
import plotly.express as px

def country_wise_info():
    newWindow = Toplevel()
    newWindow.title("COUNTRY WISE TRACKER")
    newWindow.state('zoomed')
    newWindow.iconbitmap(r'C:\Users\DELL\Downloads\coronavirus_image_UXL_icon.ico')
    
    def get_country_info():
        url = 'https://api.covid19api.com/summary'
        response = requests.request("GET" , url)
        data = json.loads(response.text)
        searchcountry = txt.get()
        def get_country_index(country):
            for index,item in enumerate(data['Countries']):
                if item['Country'] == country:
                    return index
        countryid = get_country_index(searchcountry)
        newconfirmed = data['Countries'][countryid]['NewConfirmed']
        totalconfirmed = data['Countries'][countryid]['TotalConfirmed']
        covid_msg = f'Last number of new confirmed cases in {searchcountry}: {newconfirmed}.\nThe total cases are: {totalconfirmed}'
        output_text.set(covid_msg)

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

    def map_world_2():
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
        m1 = folium.Map(tiles = 'StamenToner', min_zoom = 2)
        deaths = covid_final['TotalDeaths'].astype(float)
        lat = covid_final['latitude'].astype(float)
        lon = covid_final['longitude'].astype(float)
        m1.add_child(HeatMap(zip(lat,lon,deaths),radius=0))

        def plotDot2(point):
            folium.CircleMarker(location = [point.latitude, point.longitude],radius=5,weight=2,popup = [point.Country,point.TotalDeaths],fill_color = '#000000').add_to(m1)
        covid_final.apply(plotDot2, axis = 1)
        m1.fit_bounds(m1.get_bounds())
        m1.save("covid_map_2.html")
        webbrowser.open("covid_map_2.html")

    canvas = Canvas(newWindow, height = 50 , width = 1600 , bg = "black")
    canvas.create_text(800, 30, text = " COVID-19 COUNTRY WISE DETAILS " , font = "Times 26 bold roman" , fill = '#EC4D37')
    canvas.pack(side = TOP)
    canvas1 = Canvas(newWindow, height = 260 , width = 1150 ,borderwidth = 1, relief = "solid" )
    canvas1.pack(side = TOP)
    lbl = Label(canvas1, text =' Enter Country ' , font = "Times 20 bold roman")
    canvas_1 = canvas1.create_window(350, 30, window = lbl)
    txt = Entry(canvas1, width = 30 , font = "TimeS 14 bold roman" , bd = 5 , fg = "dark blue")
    canvas_2 = canvas1.create_window(650, 30, window = txt)
    btn = Button(canvas1, text = '  Submit  ', command = get_country_info, font = "Consolas 15 bold italic" , bg = "light grey", cursor = "hand2")
    canvas_3 = canvas1.create_window(570, 90, window = btn)
    output_text = StringVar()
    lbl_output = Label(canvas1, textvariable = output_text, font = "Times 20 bold italic" , fg = "red")
    canvas_4 = canvas1.create_window(550, 220, window = lbl_output)
    btn3 = Button(canvas1, text = ' World Total Cases (Map) ' , font = "Consolas 15 bold italic " , command = map_world , bg = "light grey", cursor = "hand2")
    canvas_6 = canvas1.create_window(410, 155, window = btn3)
    btn4 = Button(canvas1, text = ' World Active Cases (Map) ' , font = "Consolas 15 bold italic " , command = map_world_2 , bg = "light grey", cursor = "hand2")
    canvas_6 = canvas1.create_window(730, 155, window = btn4)
    def callback(event):
        webbrowser.open_new(event.widget.cget("text"))
    lbl1 = Label(canvas1, text = r"https://covidvisualizer.com/", fg = "blue" , cursor = "hand2", font = "Times 14 bold roman")
    lbl1.bind("<Button-1>", callback)
    canvas1.create_window(1000,100, window = lbl1 )
    lbl2 = Label(newWindow, text = "GLOBAL COVID VISUALISER :",font = "Times 16 normal roman")
    canvas1.create_window(1000,70, window = lbl2 )
    url_request = requests.get("https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=json")
    url_json = url_request.json()
    df = pd.DataFrame(url_json['features'])
    data_list = df['attributes'].tolist()
    data = pd.DataFrame(data_list)
    data.set_index('OBJECTID')
    data = data[['Province_State','Country_Region','Last_Update','Lat','Long_','Confirmed','Recovered','Deaths','Active']]
    data.columns = ('State','Country','Last Update','Lat','Long','Confirmed','Recovered','Deaths','Active')
    data['State'].fillna(value = '', inplace = True)

    def convert_time(t):
        t = int(t)
        return dt.datetime.fromtimestamp(t)
    data = data.dropna(subset = ['Last Update'])
    data['Last Update'] = data['Last Update']/1000
    data['Last Update'] = data['Last Update'].apply(convert_time)

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

    canvas2 = Canvas(newWindow, height = 500 , width = 1550)
    canvas2.pack(side = BOTTOM)
    render1 = ImageTk.PhotoImage(Image.open ("C:/Users/DELL/Downloads/worldmap.png").resize((1550,480) , Image.ANTIALIAS))
    img1 = Label(canvas2, image = render1)
    img1.image = render1
    img1.pack(side = BOTTOM)
    canvas2_btn1 = Button(canvas2, text = 'Top 10 Confirmed Cases Countries' , font = "Consolas 12 bold italic " , command = confirmed_cases_countries , cursor = "hand2", width = 35, fg = "blue", bg = "white")
    canvas_btn1 = canvas2.create_window(785, 100, window = canvas2_btn1)
    canvas2_btn2 = Button(canvas2, text = 'Top 10 Death Cases Countries' , font = "Consolas 12 bold italic " , command = confirmed_deaths_countries ,  cursor = "hand2", width = 35, fg = "blue", bg = "white")
    canvas_btn2 = canvas2.create_window(785, 170, window = canvas2_btn2)
    canvas2_btn3 = Button(canvas2, text = 'Top 10 Recovered Cases Countries' , font = "Consolas 12 bold italic " , command = confirmed_recovered_countries , cursor = "hand2", width = 35, fg = "blue", bg = "white")
    canvas_btn3 = canvas2.create_window(785, 240, window = canvas2_btn3)
    canvas2_btn4 = Button(canvas2, text = 'Top 10 Active Cases Countries' , font = "Consolas 12 bold italic " , command = confirmed_active_countries , cursor = "hand2", width = 35, fg = "blue", bg = "white")
    canvas_btn4 = canvas2.create_window(785, 310, window = canvas2_btn4)
