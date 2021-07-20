from tkinter import *
from PIL import ImageTk, Image ,ImageDraw, ImageFont, ImageFilter
import json
import html5lib
import plyer
import urllib.request
import imageio
import webbrowser
import requests
import bs4



def notif_and_helplines():
    url = "https://www.mohfw.gov.in/"
    html_data = requests.get(url)
    bs = bs4.BeautifulSoup(html_data.text,'html.parser')
    newWindow = Toplevel()
    newWindow.title("NOTIFICATIONS, HELPLINES AND ADVISORIES")
    newWindow.state('zoomed')
    newWindow.iconbitmap(r'C:\Users\DELL\Downloads\coronavirus_image_UXL_icon.ico')

    def shift():
        x1,y1,x2,y2 = canvas.bbox("marquee")
        if(x2<0 or y1<0):
            x1 = canvas.winfo_width()
            y1 = canvas.winfo_height()//2
            canvas.coords("marquee",x1,y1)
        else:
            canvas.move("marquee", -2, 0)
        canvas.after(1000//fps,shift)
    labe1 = Label(newWindow, text = " LATEST NOTIFICATIONS " , font = "Times 28 bold roman" , pady = 10, padx = 20 ,fg = "#EC4D37", bg = "black").pack()
    labe2 = Label(newWindow, text = " " , font = "Times 15 bold roman").pack()
    canvas = Canvas(newWindow,bg = '#EC4D37')
    canvas.pack(fill = BOTH, expand = 1)
    text_var = bs.find("span" ,class_ = "tested").get_text()
    text = canvas.create_text(0,-2000, text = text_var, font = ('Times New Roman',20,'bold'),fill = 'black',tags = ("marquee",),anchor = 'w')
    x1,y1,x2,y2 = canvas.bbox("marquee")
    width = x2-x1
    height = y2-y1
    canvas['width'] = width
    canvas['height'] = height
    fps = 45
    shift()

    def labe3_open():
        webbrowser.open_new('https://cdn.s3waas.gov.in/s30777d5c17d4066b82ab86dff8a46af6f/uploads/2020/05/2020050898.pdf')

    labe3 = Label(newWindow, text = " For any technical enquiry with respect to COVID-19, you may kindly email on technicalquery.covid19@gov.in                   Aarogya Setu IVRS ✆ 1921 ",
                font = "Times 15 normal roman" , pady = 3, padx = 170 ,fg = "red", bg = "gray13", cursor = "hand2")
    labe3.bind("<Button-1>", lambda e: labe3_open())
    labe3.pack()
    labe4 = Label(newWindow,text = " Helpline Number : +91-11-23978046                Toll Free : 1075                Helpline Email ID : ncov2019@gov.in ", font = "Times 13 normal roman" ,fg = "black", bg = "yellow",padx = 420 ).pack()
    def labe5_open():
        url2 = "https://www.mohfw.gov.in/pdf/StatewiseCovidHospitalslink19062020.pdf"
        webbrowser.open_new(url2)
    labe5 = Label(newWindow,text = " COVID-19 Facilities in States & Union Territories ",font = "Times 12 bold roman" ,fg = "blue", 
                bg = "yellow", cursor = "hand2", padx = 620 )
    labe5.bind("<Button-1>", lambda e: labe5_open())
    labe5.pack()

    frame = Frame(newWindow,width = 900,height = 900)
    frame.pack(expand = True, fill = BOTH)
    canvas1 = Canvas(frame,width = 900, height = 900,scrollregion = (0,0,1000,1000))
    hbar = Scrollbar(frame, orient = HORIZONTAL)
    hbar.pack(side = BOTTOM,fill = X)
    hbar.config(command = canvas1.xview)
    vbar = Scrollbar(frame,orient = VERTICAL)
    vbar.pack(side = LEFT,fill = Y)
    vbar.config(command = canvas1.yview)
    canvas1.config(width = 900,height = 900)
    canvas1.config(xscrollcommand = hbar.set, yscrollcommand = vbar.set)
    canvas1.pack(side=LEFT,expand = True,fill = BOTH)
    info_div1 = bs.find("div" , class_ = "main-body-content").find("section" ,class_ = "site-update").find("div" , class_ = "container").find("div" , class_ = "row").find_all("div" , class_ = "update-box")
    info_div2 = bs.find("div" , class_ = "main-body-content").find_all("section" ,class_ = "site-update")[4].find("div" , class_ = "container").find("div" , class_ = "row").find("div" , class_ = "site-faq").find("div" , class_ = "faq-content")

    def Button_1_open():
        webbrowser.open_new(info_div1[0].find("a").get('href'))
    def Button_2_open():
        webbrowser.open_new(info_div1[1].find("a").get('href'))
    def Button_3_open():
        webbrowser.open_new(info_div1[2].find("a").get('href'))
    def Button_4_open():
        webbrowser.open_new(info_div1[3].find("a").get('href'))
    def Button_5_open():
        webbrowser.open_new(info_div1[4].find("a").get('href'))
    def Button_6_open():
        webbrowser.open_new(info_div1[5].find("a").get('href'))
    def Button_7_open():
        webbrowser.open_new(info_div2.find("a").get('href'))
    render = ImageTk.PhotoImage(Image.open ("C:/Users/DELL/Downloads/coronavirus3.png").resize((300,40) , Image.ANTIALIAS))
    covid_img = Label(canvas1)
    covid_img.image = render
    canvas1.create_image(180, 45,image = render)
    f1 = ('Bookman Old Style', "25", "bold roman")
    text_1 = Label(canvas1, text = " Updates ",fg = "gray20" , font = f1)
    canvas_text1 = canvas1.create_window(415, 45, window = text_1)
    '''text = info_div1[0].find("a").get_text().strip()'''
    button_1 = Button(canvas1, text = " COVID-19 Vaccination of Pregnant Women PosterEnglish " ,wraplength = 300,command = Button_1_open , cursor = "hand2", fg = "blue" , font = "serif 10 normal roman" , padx = 4, pady = 4,height = 5,width = 57)
    canvas_button1 = canvas1.create_window(250, 150, window = button_1)
    button_2 = Button(canvas1, text = " Counseling booklet for Frontline workers and Vaccinators " ,wraplength = 300,command = Button_2_open, cursor = "hand2", fg = "blue" , font = "serif 10 normal roman", padx = 4, pady = 4,height = 5,width = 57)
    canvas_button2 = canvas1.create_window(250, 250, window = button_2)
    button_3 = Button(canvas1, text = info_div1[2].find("a").get_text().strip() ,wraplength = 300,command = Button_3_open, cursor = "hand2", fg = "blue" , font = "serif 10 normal roman", padx = 4, pady = 4,height = 5,width = 57)
    canvas_button3 = canvas1.create_window(250, 350, window = button_3)
    button_4 = Button(canvas1, text = " Toolkit for Youth Campaign on COVID Appropriate Behaviour, Vaccination drive and Psychosocial well-being " ,wraplength = 300,command = Button_4_open, cursor = "hand2", fg = "blue" , font = "serif 10 normal roman", padx = 4, pady = 4,height = 5,width = 57)
    canvas_button4 = canvas1.create_window(250, 450, window = button_4)
    button_5 = Button(canvas1, text = info_div1[4].find("a").get_text().strip() ,wraplength = 300,command = Button_5_open, cursor = "hand2", fg = "blue" , font = "serif 10 normal roman", padx = 4, pady = 4,height = 5,width = 57) 
    canvas_button5 = canvas1.create_window(250, 550, window = button_5)
    button_6 = Button(canvas1, text = info_div1[5].find("a").get_text().strip() ,wraplength = 300,command = Button_6_open, cursor = "hand2", fg = "blue" , font = "serif 10 normal roman" , padx = 4, pady = 4,height = 5,width = 57)
    canvas_button6 = canvas1.create_window(250, 650, window = button_6)
    text_2 = Label(canvas1, text = " FAQ's ", fg = "gray20" , font = "Times 25 bold roman")
    canvas_text2 = canvas1.create_window(80, 755, window = text_2)
    button_7 = Button(canvas1, text = info_div2.get_text() ,wraplength = 500,command = Button_7_open, cursor = "hand2", fg = "blue" , font = "serif 10 normal roman" , padx = 4, pady = 4,height = 5,width = 57)
    canvas_button7 = canvas1.create_window(250, 855, window = button_7)
    text_3 = Label(canvas1, text = " source: " , font = "Times 15 bold roman")
    canvas_text2 = canvas1.create_window(160, 970, window = text_3)

    def call_back(event):
        webbrowser.open_new(event.widget.cget("text"))
    lbl = Label(canvas1, text = r"www.mohfw.gov.in", fg = "blue" , cursor = "hand2",font = "Times 13 bold roman")
    canvas_lbl = canvas1.create_window(280, 970, window = lbl)
    lbl.bind("<Button-1>", call_back)
    render2 = ImageTk.PhotoImage(Image.open ("C:/Users/DELL/Downloads/vaccination.png").resize((570,550) , Image.ANTIALIAS))
    img2 = Label(frame, image = render2)
    img2.image = render2
    img2.pack(side = RIGHT)

    url2 = "https://www.worldometers.info/coronavirus/"
    html_data2 = requests.get(url2)
    bs2 = bs4.BeautifulSoup(html_data2.text,'html.parser')
    info_data = bs2.find("div" , class_ = "content-inner").find_all("div" , id = "maincounter-wrap")
    f = ("Times", "20", "bold italic")
    text1 = Label(canvas1, text = " Worldwide " , font = "Times 25 bold roman" , width = 17)
    canvas1.create_window(750, 45, window = text1)
    text2 = Label(canvas1, text = info_data[0].get_text() , font = f , bg = "light blue", height = 4, width = 17,borderwidth = 1, relief = "solid")
    canvas1.create_window(750, 150, window = text2)
    text3 = Label(canvas1, text = info_data[1].get_text() , font = f , bg = "tomato", height = 4, width = 17,borderwidth = 1, relief = "solid")
    canvas1.create_window(750, 300, window = text3)
    text4 = Label(canvas1, text = info_data[2].get_text() , font = f , bg = "light green", height = 4, width = 17,borderwidth = 1, relief = "solid")
    canvas1.create_window(750, 450, window = text4)
    info_data2 = bs2.find("div" , class_ = "content-inner").find_all("div" , class_ = "col-md-6")
    text5 = Label(canvas1, text = " Active Cases " + "\n" + "────────────────────" + "\n\n" + info_data2[0].find("div" , class_ = "number-table-main").get_text() + "\n" +  "currently infected patients" + "\n" , font = "Times 19 bold italic" , bg = "gray85", height = 6, width = 24,borderwidth = 1, relief = "solid")
    canvas1.create_window(750, 650, window = text5)
    text6 = Label(canvas1, text = " Closed Cases " + "\n" + "────────────────────" + "\n\n" + info_data2[1].find("div" , class_ = "number-table-main").get_text() + "\n" +  "cases which had an outcome" + "\n" , font = "Times 19 bold italic" , bg = "gray85", height = 6, width = 24,borderwidth = 1, relief = "solid")
    canvas1.create_window(750, 880, window = text6)
