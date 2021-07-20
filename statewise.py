from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
from covid import Covid
from covid_india import states
from PIL import ImageTk
import plotly.express as px
import plotly.graph_objects as go
from PIL import ImageTk, Image ,ImageDraw, ImageFont, ImageFilter
import imageio
import webbrowser


def state_wise_info():
    newWindow = Toplevel()
    newWindow.title("STATE WISE TRACKER")
    newWindow.state('zoomed')
    newWindow.iconbitmap(r'C:\Users\DELL\Downloads\coronavirus_image_UXL_icon.ico')
    canvas1 = Canvas(newWindow, height = 50 , width = 1600 , bg = "black")
    canvas1.create_text(800, 30, text = " COVID-19 STATE WISE DETAILS " , font = "Times 26 bold roman" , fill = '#EC4D37')
    canvas1.pack()
    url = 'https://api.covid19india.org/data.json'
    jsn = requests.get(url).json()
    statewise = jsn['statewise']
    df = pd.DataFrame(statewise)
    df = df.drop(df.index[0])

    def get_state_info():
        searchstate = txt.get()
        entry = states.getdata(searchstate)
        entry.pop('Total')
        covid_msg = ""
        for i in entry :
            covid_msg = covid_msg + i + " Cases : " + str(entry[i]) + "\n"
        output_text.set(covid_msg)

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
        
    canvas1 = Canvas(newWindow, height = 265 , width = 1150 ,borderwidth = 1, relief = "solid" )
    canvas1.pack()
    lbl = Label(canvas1, text =' Enter State ' , font = "Times 20 bold roman")
    canvas_1 = canvas1.create_window(350, 30, window = lbl)
    txt = Entry(canvas1, width = 30 , font = "Times 14 bold roman" , bd = 5 , fg = "dark blue")
    canvas_2 = canvas1.create_window(650, 30, window = txt)
    btn = Button(canvas1, text = ' Submit ', font = "Consolas 15 bold italic" , command = get_state_info, bg = "light grey", cursor = "hand2")
    canvas_3 = canvas1.create_window(300, 100, window = btn)
    btn2 = Button(canvas1, text = " State-wise Bar Graph ", font = "Consolas 15 bold italic", command = get_state_info_graph , bg = "light grey", cursor = "hand2")
    canvas_4 = canvas1.create_window(520, 100, window = btn2)
    btn3 = Button(canvas1, text = " District-wise Bar Graph ", font = "Consolas 15 bold italic", command = district_wise , bg = "light grey", cursor = "hand2")
    canvas_5 = canvas1.create_window(830, 100, window = btn3)
    output_text = StringVar()
    lbl_output = Label(canvas1, textvariable = output_text, font = "Times 20 bold italic" , fg = "red")
    canvas_6 = canvas1.create_window(550, 200, window = lbl_output)
    canvas2 = Canvas(newWindow, height = 500 , width = 1550)
    canvas2.pack(side = BOTTOM)
    render = ImageTk.PhotoImage(Image.open ("Images/indiamap2.jpg").resize((700,475) , Image.ANTIALIAS))
    img = Label(canvas2, image = render, padx = 100)
    img.image = render
    img.pack()

    def top10_confirmed_states():
        df2 = df
        df2['confirmed'] = df2['confirmed'].apply(lambda x : int(x))
        df2 = df2.sort_values(by = ['confirmed'], ascending = False).head(10)
        states = df2['state']
        fig = go.Figure(data = [go.Bar(name = 'confirmed', x = states, y = df2['confirmed'])])
        fig.update_traces(marker_color = 'rgb(158,202,225)', marker_line_color = 'rgb(8,48,107)',marker_line_width = 1.5, opacity = 0.6)
        fig.update_layout(barmode = 'group',title = "Top-10 Confirmed Cases States")
        fig.show()

    def top10_active_states():
        df3 = df
        df3['active'] = df3['active'].apply(lambda x : int(x))
        df3 = df3.sort_values(by = ['active'], ascending = False).head(10)
        states = df3['state']
        fig = go.Figure(data = [go.Bar(name = 'active', x = states, y = df3['active'])])
        fig.update_traces(marker_color = 'rgb(0, 255, 0)', marker_line_color = 'rgb(0,167, 0)',marker_line_width = 1.5, opacity = 0.6)
        fig.update_layout(barmode = 'group',title = "Top-10 Active Cases States")
        fig.show()

    def top10_deaths_states():
        df4 = df
        df4['deaths'] = df4['deaths'].apply(lambda x : int(x))
        df4 = df4.sort_values(by = ['deaths'], ascending = False).head(10)
        states = df4['state']
        fig = go.Figure(data = [go.Bar(name = 'deaths', x = states, y = df4['deaths'])])
        fig.update_traces(marker_color = 'rgb(255, 0, 0)', marker_line_color = 'rgb(167, 0, 0)',marker_line_width = 1.5, opacity = 0.6)
        fig.update_layout(barmode = 'group',title = "Top-10 Deaths Cases States")
        fig.show()

    def top10_recovered_states():
        df5 = df
        df5['recovered'] = df5['recovered'].apply(lambda x : int(x))
        df5 = df5.sort_values(by = ['recovered'], ascending = False).head(10)
        states = df5['state']
        fig = go.Figure(data = [go.Bar(name = 'recovered', x = states, y = df5['recovered'])])
        fig.update_traces(marker_color = 'rgb(0, 0, 255)', marker_line_color = 'rgb(0, 0, 167)',marker_line_width = 1.5, opacity = 0.6)
        fig.update_layout(barmode = 'group',title = "Top-10 Recovered Cases States")
        fig.show()

    canvas2_btn1 = Button(canvas2, text = 'Top 10 Confirmed Cases States' , font = "Consolas 12 bold italic " , command = top10_confirmed_states , cursor = "hand2", width = 35, fg = "blue", bg = "white")
    canvas_btn1 = canvas2.create_window(350, 120, window = canvas2_btn1)
    canvas2_btn2 = Button(canvas2, text = 'Top 10 Death Cases States' , font = "Consolas 12 bold italic " , command = top10_deaths_states ,  cursor = "hand2", width = 35, fg = "blue", bg = "white")
    canvas_btn2 = canvas2.create_window(350, 180, window = canvas2_btn2)
    canvas2_btn3 = Button(canvas2, text = 'Top 10 Recovered Cases States' , font = "Consolas 12 bold italic " , command = top10_recovered_states, cursor = "hand2", width = 35, fg = "blue", bg = "white")
    canvas_btn3 = canvas2.create_window(350, 240, window = canvas2_btn3)
    canvas2_btn4 = Button(canvas2, text = 'Top 10 Active Cases States' , font = "Consolas 12 bold italic " , command = top10_active_states, cursor = "hand2", width = 35, fg = "blue", bg = "white")
    canvas_btn4 = canvas2.create_window(350, 300, window = canvas2_btn4)
