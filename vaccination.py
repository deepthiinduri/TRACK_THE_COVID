from tkinter import *
from PIL import ImageTk, Image ,ImageDraw, ImageFont, ImageFilter
import time
import datetime
import datetime as dt
import numpy as np
import pandas as pd
import seaborn as sns
from tabulate import tabulate
import matplotlib
import matplotlib.pyplot as plt
import ctypes
import requests
import bs4
from bs4 import BeautifulSoup
import json
import html5lib
import plyer
import urllib.request
import imageio
import webbrowser
from scipy.interpolate import interp1d
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from urllib.request import urlopen
import matplotlib.patches as mpatches


def covid_vaccination():
    newWindow = Toplevel()
    newWindow.title("COVID VACCINATION")
    newWindow.state('zoomed')
    newWindow.iconbitmap(r'Images\coronavirus_image_UXL_icon.ico')
    labe1 = Label(newWindow, text = " VACCINATION " , font = "Times 25 bold roman" , pady = 5, padx = 1550 ,fg = "#EC4D37", bg = "black").pack()
    path = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv'
    df = pd.read_csv(path)
    df.dropna()
    df.rename(columns = {'location': "Country"}, inplace=True)
    df = df.drop_duplicates('Country', keep = 'last')

    def vaccine_availability():
        newWindow2 = Toplevel(newWindow)
        newWindow2.title("VACCINATION AVAILABILITY")
        newWindow2.state('zoomed')
        newWindow2.iconbitmap(r'Images\coronavirus_image_UXL_icon.ico')
        labe1 = Label(newWindow2, text = " VACCINATION AVAILABILITY CHECK IN INDIA " , font = "Times 25 bold roman" , pady = 5, padx = 1550 ,fg = "#EC4D37", bg = "black").pack()
        labe2 = Label(newWindow2, text = " ",font = "Times 7 normal roman").pack()
        labe3 = Label(newWindow2, text = " Search with pincode, vaccination center details. ",font = "Times 15 bold roman", padx = 1550 , bg = "gold").pack()
        labe4 = Label(newWindow2, text = " ",font = "Times 11 normal roman").pack()

        def vaccine_availability_search():
            MessageBox = ctypes.windll.user32.MessageBoxW
            if(txt3.get()=='' or txt1.get()=='' or txt2.get()==''):
                MessageBox(None, ' Please enter all the fields. ', ' Alert! ', 0)
                return
            elif(int(txt3.get())>10):
                MessageBox(None, ' Please enter data for a period of up to ten days. ', ' Alert! ', 0)
                return
            numdays = int(txt3.get())
            POST_CODE = int(txt1.get())
            age = int(txt2.get())
            base = datetime.datetime.today()
            date_list = [base + datetime.timedelta(days = x) for x in range(numdays)]
            date_str = [x.strftime("%d-%m-%Y") for x in date_list]
            print_flag = 'Y'
            vaccout = ""
            for INP_DATE in date_str:
                url_vaccine = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(POST_CODE, INP_DATE)
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                result = requests.get(url_vaccine, headers = headers)
                response = result.content.decode()
                resp_json = json.loads(response)
                flag = False
                if resp_json["centers"]:
                    vaccout = vaccout + "Slots on " + str(INP_DATE) + " : " + "\n"
                    if(print_flag=='y' or print_flag=='Y'):
                        for center in resp_json["centers"]:
                            for session in center["sessions"]:
                                if session["min_age_limit"] <= age:
                                    vaccout = vaccout + "\t center_id: " +  str(center["center_id"]) + "\n"
                                    vaccout = vaccout + "\t Name: " +  center["name"] + "\n"
                                    vaccout = vaccout + "\t Address: " +  center["address"] + "\n"
                                    vaccout = vaccout + "\t block_name: " +  center["block_name"] + "\n"
                                    vaccout = vaccout + "\t from: " +  center["from"] + "\n"
                                    vaccout = vaccout + "\t to: " +  center["to"] + "\n"
                                    vaccout = vaccout + "\t Price: " +  center["fee_type"] + "\n"
                                    vaccout = vaccout + "\t Available Capacity: " +  str(session["available_capacity"]) + "\n"
                                    if(session["vaccine"] != ''):
                                        vaccout = vaccout + "\t Date: " + str(session["date"]) + "\n"
                                        vaccout = vaccout + "\t Vaccine: " + str(session["vaccine"]) + "\n"
                                        vaccout = vaccout + "\t Slots: " + str(session["slots"]) + "\n"
                                    vaccout = vaccout + "\n\n"
                                else:
                                    vaccout = vaccout + "\t No Vaccination slots Available below " + str(session["min_age_limit"]) + "\n\n"
                                    break
                else:
                    vaccout = vaccout + "\t No available slots on " + str(INP_DATE) + "\n\n"

            vaccine_availability_search.text_canvas2 = canvas2.create_text(10,10,text = vaccout,anchor = NW, font = "Times 12 bold roman")
            def copy_button():
                    clip = Tk()
                    clip.withdraw()
                    clip.clipboard_clear()
                    clip.clipboard_append(vaccout)
                    clip.update()
                    clip.destroy()
                    
            canvas2.create_window(1350, 30 , window = Button(canvas2, text = "copy" , command = copy_button) )
            canvas2.update()

        def reset_canvas2():
            txt1.delete(0, 'end')
            txt2.delete(0, 'end')
            txt3.delete(0, 'end')
            canvas2.delete('all')
            
        canvas1 = Canvas(newWindow2, width = 1550, height = 1000, bg = 'red')
        canvas1.pack(expand = Y,fill = BOTH)
        frame = Frame(newWindow2,width = 1430,height = 550)
        canvas1.create_window(770, 370, window = frame)
        canvas2 = Canvas(frame,width = 1430, height = 550,scrollregion = (0,0,1500,20000))
        vbar = Scrollbar(frame,orient = VERTICAL)
        vbar.pack(side = RIGHT,fill = Y)
        vbar.config(command = canvas2.yview)
        canvas2.config(xscrollcommand = hbar.set, yscrollcommand = vbar.set)
        canvas2.pack(side = LEFT,expand = True,fill = BOTH)

        label1 = Label(canvas1, text = 'Search by' , font = "Times 30 bold roman", bg = "red", fg = "#00239C")
        canvas1.create_window(120, 48, window = label1)
        lbl1 = Label(canvas1, text = 'PINCODE :' , font = "Times 20 bold roman", bg = "red")
        canvas1.create_window(330, 50, window = lbl1)
        txt1 = Entry(canvas1, width = 15 , font = "Times 14 bold roman" ,bd = 5,  fg = "dark blue")
        canvas1.create_window(500, 50, window = txt1)
        lbl2 = Label(canvas1, text = 'AGE :' , font = "Times 20 bold roman", bg = "red")
        canvas1.create_window(680, 50, window = lbl2)
        txt2 = Entry(canvas1, width = 10, font = "Times 14 bold roman" ,bd = 5,  fg = "dark blue")
        canvas1.create_window(790, 50, window = txt2)
        lbl3 = Label(canvas1, text = 'NUMBER OF DAYS :' , font = "Times 20 bold roman", bg = "red")
        canvas1.create_window(1040, 50, window = lbl3)
        txt3 = Entry(canvas1, width = 10, font = "Times 14 bold roman" ,bd = 5,  fg = "dark blue")
        canvas1.create_window(1245, 50, window = txt3)
        button1 = Button(canvas1, text = "SEARCH", font = "Times 13 bold italic", bg = "#EC4D37",command = vaccine_availability_search , fg = 'white', cursor = "hand2",width = 13)
        canvas1.create_window(1435, 23, window = button1)
        button2 = Button(canvas1, text = "RESET", font = "Times 13 bold italic", bg = "#EC4D37",command = reset_canvas2 , fg = 'white', cursor = "hand2",width = 13)
        canvas1.create_window(1435, 70, window = button2)
    
    def vaccine_graph_world():
        world = df.groupby("Country")['people_fully_vaccinated_per_hundred'].sum().reset_index()
        world = world.where(world['Country'] != 'World')
        world = world.where(world['Country'] != 'Asia')
        world = world.where(world['Country'] != 'Europe')
        world = world.where(world['Country'] != 'Africa')
        world = world.where(world['Country'] != 'North America')
        world = world.where(world['Country'] != 'South America')
        world = world.where(world['Country'] != 'Upper middle income')
        world = world.where(world['Country'] != 'Lower middle income')
        world = world.where(world['Country'] != 'High income')
        world = world.where(world['Country'] != 'European Union')
        top_20 = world.sort_values(by = ['people_fully_vaccinated_per_hundred'], ascending = False).head(20)
        fig1 = px.bar(top_20, x = 'people_fully_vaccinated_per_hundred', y = top_20['Country'], height = 600, color = 'people_fully_vaccinated_per_hundred', orientation = 'h',
            color_continuous_scale = ['orange','red'], title = 'Country Vs. People fully Vaccinated per hundred')
        fig1.show()
        
    def vaccine_map_world():
        figure = px.choropleth(df,locations = 'Country', locationmode ='country names', color = 'total_vaccinations', hover_name = 'Country', color_continuous_scale = 'tealgrn', range_color = [1,100000000],title = 'Countries with people vaccinated')
        figure.show()
 
    def vaccine_graph_world_perday():
        world = df.groupby("Country")['daily_vaccinations'].sum().reset_index()
        world = world.where(world['Country'] != 'World')
        world = world.where(world['Country'] != 'Asia')
        world = world.where(world['Country'] != 'Europe')
        world = world.where(world['Country'] != 'Africa')
        world = world.where(world['Country'] != 'North America')
        world = world.where(world['Country'] != 'South America')
        world = world.where(world['Country'] != 'Upper middle income')
        world = world.where(world['Country'] != 'Lower middle income')
        world = world.where(world['Country'] != 'High income')
        world = world.where(world['Country'] != 'Low income')
        world = world.where(world['Country'] != 'European Union')
        top_20 = world.sort_values(by = ['daily_vaccinations'], ascending = False).head(20)
        fig2 = px.bar(top_20, x = 'daily_vaccinations', y = top_20['Country'], height = 600, color = 'daily_vaccinations', orientation = 'h',
            color_continuous_scale = ['#ADEFD1','#00203F'], title = 'Country Vs. Daily Vaccinations')
        fig2.show()

    def vaccines_covid_types():
        path_vaccine = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv'
        df_vac = pd.read_csv(path_vaccine)
        df_vac.dropna()
        df_vac.drop(['last_observation_date','source_name','source_website'], axis = 1, inplace = True)
        df_vac.rename(columns = {'location': "Country"}, inplace = True)
        fig = px.choropleth(df_vac, locations = "iso_code",color = "vaccines",hover_name = "Country",color_continuous_scale = px.colors.sequential.Plasma,title = "Vaccines used by different countries")
        fig.update_layout(showlegend = False)
        fig.show()

    def state_wise_vaccine_data():
        url = "https://www.mohfw.gov.in/"
        html_data = requests.get(url)
        bs = bs4.BeautifulSoup(html_data.text,'html.parser')
        data = bs.find("div" , class_ = "main-body-content").find("div" , id = "main-content").find("div" , class_ = "col-sm-2 btns").find("li" , claumuss = "icon-dashboard sizeicon")
        webbrowser.open_new(data.find("a").get('href'))

    def vaccine_graph_taken():
        path_vaccine = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv'
        df_vac = pd.read_csv(path_vaccine)
        df_vac.dropna()
        df_vac.drop(['last_observation_date','source_name','source_website'], axis = 1, inplace = True)
        df_vac.rename(columns = {'location': "Country"}, inplace = True)
        merge_data = pd.merge(df,df_vac, on = 'iso_code', how = 'left')
        grp = ['Country_x', 'total_vaccinations', 'iso_code', 'vaccines']
        vacc_no = merge_data[grp].groupby('vaccines').max().sort_values('total_vaccinations', ascending=False).dropna(subset = ['total_vaccinations'])
        fig2 = px.bar(vacc_no, x = 'total_vaccinations', y = vacc_no.index, color = 'total_vaccinations', orientation = 'h',
            color_continuous_scale = ['blue','orange'], title = 'Various categories of COVID-19 vaccines offered')
        fig2.show()

    canvas = Canvas(newWindow, width = 1550, height = 100)
    button1 = Button(canvas, text = "Vaccine Types", font = "Tahoma 14 bold italic", bg = "#EC4D37" ,command = vaccines_covid_types, fg = 'white', cursor = "hand2",width = 18)
    canvas.create_window(160, 50, window = button1)
    button2 = Button(canvas, text = "Vaccine Center Check", font = "Tahoma 14 bold italic",command = vaccine_availability, bg = "#EC4D37" , fg = 'white', cursor = "hand2",width = 18)
    canvas.create_window(460, 50, window = button2)
    button3 = Button(canvas, text = "Graphs", font = "Tahoma 14 bold italic", bg = "#EC4D37" , fg = 'white', cursor = "hand2",width = 18)
    popup = Menu(newWindow, tearoff = 0, bg = "#EC4D37" , fg = 'white', font = "Tahoma 12 bold italic" )
    popup.add_command(label = " Top-20 Fully Vaccinated Countries " ,command = vaccine_graph_world)
    popup.add_command(label = " Top-20 Vaccinated Countries in a day  ",command = vaccine_graph_world_perday)
    popup.add_command(label = " Top-20 Types of Vaccines offered ",command = vaccine_graph_taken)
    def popupm(bt):
        try:
            x = bt.winfo_rootx() + 173
            y = bt.winfo_rooty() + 55
            popup.tk_popup(x, y, 0)
        finally:
            popup.grab_release()
    button3.configure(command = lambda: popupm(button3))
    canvas.create_window(760, 50, window = button3)
    button4 = Button(canvas, text = "Total Vaccinations", font = "Tahoma 14 bold italic",command = vaccine_map_world, bg = "#EC4D37" , fg = 'white', cursor = "hand2",width = 18)
    canvas.create_window(1060, 50, window = button4)
    button5 = Button(canvas, text = "India state-wise", font = "Tahoma 14 bold italic", bg = "#EC4D37" , fg = 'white', command = state_wise_vaccine_data, cursor = "hand2",width = 18)
    canvas.create_window(1360, 50, window = button5)
    canvas.pack()
    
    frame = Frame(newWindow,width = 1550,height = 1000)
    frame.pack(expand = True, fill = BOTH)
    canvas1 = Canvas(frame,width = 1550, height = 1000,scrollregion = (0,0,1000,800))
    hbar = Scrollbar(frame, orient = HORIZONTAL)
    hbar.pack(side = BOTTOM,fill = X)
    hbar.config(command = canvas1.xview)
    vbar = Scrollbar(frame,orient = VERTICAL)
    vbar.pack(side = RIGHT,fill = Y)
    vbar.config(command = canvas1.yview)
    canvas1.config(width = 1550,height = 1000)
    canvas1.config(xscrollcommand = hbar.set, yscrollcommand = vbar.set)
    canvas1.pack(side = LEFT,expand = True,fill = BOTH)
    render1 = ImageTk.PhotoImage(Image.open ("Images/Corona-vaccine3.png").resize((400,400) , Image.ANTIALIAS))
    img1 = Label(canvas1, image = render1, padx = 100)
    img1.image = render1
    canvas1.create_window(58,58, window = img1)
    labe1 = Label(canvas1, text = " COVID-19 vaccines " , font = "Times 26 bold roman" , pady = 5 ,fg = "white", bg = "#008DC9")
    canvas1.create_window(460,30, window = labe1)
    render2 = ImageTk.PhotoImage(Image.open ("Images/vaccine.jpg").resize((700,650) , Image.ANTIALIAS))
    img2 = Label(canvas1, image = render2, padx = 100)
    img2.image = render2
    canvas1.create_window(1150,300, window = img2)
    url = 'https://covid19.trackvaccines.org/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(url, headers = headers)
    bs = bs4.BeautifulSoup(result.text,'html.parser')
    f1 = ("Courier New", "60", "bold roman")
    f2 = ("Bahnschrift SemiBold", "27", "normal roman")
    info_data = bs.find("div" , id = "content").find("div" , class_ = "post-content entry-content section-inner thin").find_all("div" , class_ = "data-graphic__item")
    canvas1.create_window(450, 140, window = Label(canvas1, text = (info_data[0].find("div", class_ = "data-graphic__value").get_text()).strip() , font = f1, fg = "blue"))
    canvas1.create_window(450, 200, window = Label(canvas1, text = "APPROVED CANDIDATES", font = f2))
    canvas1.create_window(450, 310, window = Label(canvas1, text = (info_data[1].find("div", class_ = "data-graphic__value").get_text()).strip() , font = f1, fg = "blue"))
    canvas1.create_window(450, 370, window = Label(canvas1, text = "TRIALS" , font = f2))
    canvas1.create_window(450, 480, window = Label(canvas1, text = (info_data[2].find("div", class_ = "data-graphic__value").get_text()).strip() , font = f1, fg = "blue"))
    canvas1.create_window(450, 530, window = Label(canvas1, text = "APPROVED VACCINES" , font = f2))
    canvas1.create_window(500, 700, window = Label(canvas1, text = " Register or SignIn for Vaccination: " , font = "Times 25 bold roman", bg = "#008DC9", width = 35, height = 1))
    def open():
        url_1 = "https://selfregistration.cowin.gov.in/"
        webbrowser.open_new(url_1)
    labelv1 = Label(canvas1, text = "https://selfregistration.cowin.gov.in/", font = "Times 25 bold roman", cursor = "hand2", fg = "snow",bg = "#008DC9", width = 30, height = 1)
    labelv1.bind("<Button-1>", lambda e: open())
    canvas1.create_window(1050, 700 , window = labelv1)
