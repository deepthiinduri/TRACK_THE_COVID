from tkinter import *
import requests
import bs4
from bs4 import BeautifulSoup
import json
import time
import datetime
import datetime as dt
from PIL import ImageTk, Image ,ImageDraw, ImageFont, ImageFilter
import webbrowser
from Indiacases import get_corona_detail_of_india
from statewise import state_wise_info
from countrywise import country_wise_info
from healthinfo import covid_symptoms, covid_precautions, covid_treatments
from vaccination import covid_vaccination
from notifandhelpline import notif_and_helplines
from symptomanalyser import Syptom_analyser


def refresh():
    newdata = get_corona_detail_of_india()
    print("Refreshing...")
    text_1['text'] = newdata[0]
    text_4['text'] = newdata[1]
    text_5['text'] = newdata[2]
    text_6['text'] = newdata[3]
    text_7['text'] = newdata[4]

base = Tk()
base.title('TRACK THE COVID')
base.iconbitmap(r'C:\Users\DELL\Downloads\coronavirus_image_UXL_icon.ico')
base.geometry("1550x1000")
f = ("Times", "24", "bold italic")
img = ImageTk.PhotoImage(Image.open ("C:/Users/DELL/Downloads/Coronavirus image.jpg"). resize((300, 250), Image. ANTIALIAS))
canvas = Canvas(base, height = 1000 , width = 300 , bg = "black")
canvas.create_image(2, 0, image = img, anchor = NW)
canvas.create_text(150, 300, text = "TRACK THE COVID" , font = "Mistral 32 bold roman" , fill = 'red')
button1 = Button(canvas, text = " State-wise ", font = "Tahoma 14 bold italic",command = state_wise_info ,  bg = "#EC4D37" , fg = 'white', cursor = "hand2")
button1.config(width = 30)
canvas_button1 = canvas.create_window(150, 380, window = button1)
button2 = Button(canvas, text = " Country-wise ", font = "Tahoma 14 bold italic", command = country_wise_info , bg = "#EC4D37" , fg = 'white', cursor = "hand2")
button2.config(width = 30)
canvas_button2 = canvas.create_window(150, 450, window = button2)
popup = Menu(base, tearoff = 0, bg = "#EC4D37" , fg = 'white', font = "Tahoma 12 bold italic" )
popup.add_command(label = " Symptoms " , command = covid_symptoms)
popup.add_command(label = " Precautions ", command = covid_precautions)
popup.add_command(label = " Treatments " , command = covid_treatments)
popup.add_command(label = " Vaccination ", command = covid_vaccination)
button3 = Button(canvas, text = " Health-Info ", font = "Tahoma 14 bold italic" , bg = "#EC4D37" , fg = 'white', cursor = "hand2")
button3.config(width = 30)
def popupm(bt):
    try:
        x = bt.winfo_rootx() + 400
        y = bt.winfo_rooty()
        popup.tk_popup(x, y, 0)
    finally:
        popup.grab_release()
button3.configure(command = lambda: popupm(button3))
canvas_button3 = canvas.create_window(150, 520, window = button3)
button4 = Button(canvas, text = " Notification and Helplines ", font = "Tahoma 14 bold italic", command = notif_and_helplines , bg = "#EC4D37" , fg = 'white', cursor = "hand2")
button4.config(width = 30)
canvas_button4 = canvas.create_window(150, 590, window = button4)
button5 = Button(canvas, text = " Symptom Analyser ", font = "Tahoma 14 bold italic", command = Syptom_analyser , bg = "#EC4D37" , fg = 'white', cursor = "hand2")
button5.config(width = 30)
canvas_button5 = canvas.create_window(150, 660, window = button5)
def learn_more():
    webbrowser.open_new('https://www.who.int/')
button6 = Button(canvas, text = " Learn more on who.int ", font = "Tahoma 13 bold roman", command = learn_more , bg = "red" , fg = 'white', cursor = "hand2")
canvas_button6 = canvas.create_window(150, 765, window = button6)
text_2 = Label(base, text = "  COVID-19 CASES AND VACCINATION DETAILS IN INDIA  ",font = "Times 26 bold roman",fg = "#EC4D37", bg = "black" , pady = 15,  padx = 100)
canvas2 = Canvas(base, height = 100, width = 75)
canvas3 = Canvas(base, height = 100, width = 75)
textt = Label(base, text = "\n\n")
text_1 = Label(base, text = get_corona_detail_of_india()[0] , font = f , bg = "light blue")
text_4 = Label(base, text = get_corona_detail_of_india()[1] , font = f , bg = "tomato")
text_5 = Label(base, text = get_corona_detail_of_india()[2] , font = f , bg = "light green")
text_6 = Label(base, text = get_corona_detail_of_india()[3] , font = "Times 13 bold roman" , fg = "red")
text_7 = Label(base, text = get_corona_detail_of_india()[4] , font = f , bg = "gold2")
reBtn = Button(base, text = "REFRESH", font = "Century 24 bold roman" , command = refresh, fg = "green" , bg = "snow", cursor = "hand2")
button = Button(base, text = "EXIT",font = "Century 24 bold roman", command = base.quit , fg = "red", bg = "snow", cursor = "hand2")
canvas.pack(side = LEFT)
canvas2.pack(side = RIGHT, anchor = NE)
canvas3.pack(side = LEFT, anchor = NW)
text_3 = Label(base, text = "\n\nsource:" , font = "Times 10 bold roman")
def callback(event):
    webbrowser.open_new(event.widget.cget("text"))
lbl = Label(base, text = r"www.mohfw.gov.in", fg = "blue" , cursor = "hand2")
lbl.bind("<Button-1>", callback)
text_2.pack()
textt.pack()
text_1.pack(side = LEFT , anchor = NE)
text_4.pack(side = RIGHT , anchor = NE)
text_5.pack()
text_6.pack()
def update_time():
    labl['text'] = time.strftime('Current time: %H:%M:%S' + "\n")
    base.after(1000, update_time)
labl = Label(base, text = 'Current time: 00:00:00' + "\n", font = "Time 13 bold roman")
base.after(1000, update_time)
labl.pack()
text_7.pack()
text_3.pack()
lbl.pack()
reBtn.pack(side = LEFT)
button.pack(side = RIGHT)
base.mainloop()
