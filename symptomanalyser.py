from tkinter import *
from PIL import ImageTk, Image ,ImageDraw, ImageFont, ImageFilter
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
import webbrowser
import ctypes


def Syptom_analyser():
    newWindow = Toplevel()
    newWindow.title("SYMPTOM ANALYSER")
    newWindow.state('zoomed')
    newWindow.iconbitmap(r'C:\Users\DELL\Downloads\coronavirus_image_UXL_icon.ico')
    labe1 = Label(newWindow, text = " SYMPTOM ANALYSER " , font = "Times 25 bold roman" , pady = 5, padx = 1550 ,fg = "#EC4D37", bg = "black").pack()
    render = ImageTk.PhotoImage(Image.open ("Images/symptoms covid.png").resize((1550,180) , Image.ANTIALIAS))
    img = Label(newWindow, image = render, padx = 100)
    img.image = render
    img.pack()
    canvas = Canvas(newWindow, height = 800, width = 1550)
    canvas.pack()
    label1 = Label(canvas, text = " Age :" ,font = "Times 16 bold roman")
    label1_canvas = canvas.create_window(100, 50, window = label1)

    def show():
        op1 = n1.get()
        op2 = n2.get()
        op3 = v.get()
        op4 = CheckVar1.get()
        op5 = CheckVar2.get()
        op6 = CheckVar3.get()
        op7 = CheckVar4.get()
        op8 = CheckVar5.get()
        op9 = CheckVar6.get()
        op10 = CheckVar7.get()
        op11 = CheckVar8.get()
        op12 = CheckVar9.get()
        total = op5 + op6 + op7 + op8+ op9 + op10 + op11 + op12
        MessageBox = ctypes.windll.user32.MessageBoxW
        if(op1 and op2 and op3 and (op4 or op5 or op6 or op7 or op8 or op9 or op10 or op11 or op12)):
            if(op4==1) and (op5==1 or op6==1 or op7==1 or op8==1 or op9==1 or op10==1 or op11==1 or op12==1):
                MessageBox(None, ' Enter only None if there are no symptoms. ', ' Error! ', 0)
            elif(op1.isspace() or op2.isspace()):
                MessageBox(None, ' Please enter all the fields. ', ' Alert! ', 0)
            elif(op3=='2'):
                if(op4==1):
                    label_result.config(text = "No Risk", fg = "SpringGreen2")
                elif(total==8):
                    if(op1 == " Below 5 years " or op1 == " 5 - 17 years "):
                        label_result.config(text = '72/100' + "\n" + "High Risk", fg = "red2")
                    elif(op1 == " 18 - 30 years "):
                        label_result.config(text = '74/100' + "\n" + "High Risk", fg = "red2")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '77/100' + "\n" + "High Risk", fg = "red3")
                        else:
                            label_result.config(text = '76/100' + "\n" + "High Risk", fg = "red3")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '80/100' + "\n" + "High Risk", fg = "red3")
                        else:
                            label_result.config(text = '79/100' + "\n" + "High Risk", fg = "red3")
                elif(total==7):
                    if(op1 == " Below 5 years " or op1 == " 5 - 17 years "):
                        label_result.config(text = '62/100' + "\n" + "Medium Risk", fg = "red2")
                    elif(op1 == " 18 - 30 years "):
                        label_result.config(text = '64/100' + "\n" + "Medium Risk", fg = "red2")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '66/100' + "\n" + "High Risk", fg = "red2")
                        else:
                            label_result.config(text = '65/100' + "\n" + "High Risk", fg = "red2")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '70/100' + "\n" + "High Risk", fg = "red2")
                        else:
                            label_result.config(text = '69/100' + "\n" + "High Risk", fg = "red2")
                elif(total==6):
                    if(op1 == " Below 5 years " or op1 == " 5 - 17 years "):
                        label_result.config(text = '52/100' + "\n" + "Medium Risk", fg = "red")
                    elif(op1 == " 18 - 30 years "):
                        label_result.config(text = '54/100' + "\n" + "Medium Risk", fg = "red")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '57/100' + "\n" + "Medium Risk", fg = "red")
                        else:
                            label_result.config(text = '56/100' + "\n" + "Medium Risk", fg = "red")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '60/100' + "\n" + "Medium Risk", fg = "red2")
                        else:
                            label_result.config(text = '59/100' + "\n" + "Medium Risk", fg = "red")
                elif(total==5):
                    if(op1 == " Below 5 years " or op1 == " 5 - 17 years "):
                        label_result.config(text = '43/100' + "\n" + "Medium Risk", fg = "green2")
                    elif(op1 == " 18 - 30 years "):
                        label_result.config(text = '45/100' + "\n" + "Medium Risk", fg = "red2")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '48/100' + "\n" + "Medium Risk", fg = "red2")
                        else:
                            label_result.config(text = '47/100' + "\n" + "Medium Risk", fg = "red2")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '50/100' + "\n" + "Medium Risk", fg = "red2")
                        else:
                            label_result.config(text = '49/100' + "\n" + "Medium Risk", fg = "red2")
                elif(total==4):
                    if(op1 == " Below 5 years " or op1 == " 5 - 17 years "):
                        label_result.config(text = '35/100' + "\n" + "Low Risk", fg = "green2")
                    elif(op1 == " 18 - 30 years "):
                        label_result.config(text = '36/100' + "\n" + "Low Risk", fg = "green2")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '38/100' + "\n" + "Low Risk", fg = "green2")
                        else:
                            label_result.config(text = '39/100' + "\n" + "Low Risk", fg = "green2")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '41/100' + "\n" + "Medium Risk", fg = "green2")
                        else:
                            label_result.config(text = '40/100' + "\n" + "Medium Risk", fg = "green2")
                elif(total==3):
                    if(op1 == " Below 5 years " or op1 == " 5 - 17 years "):
                        label_result.config(text = '25/100' + "\n" + "Low Risk", fg = "green3")
                    elif(op1 == " 18 - 30 years "):
                        label_result.config(text = '28/100' + "\n" + "Low Risk", fg = "green3")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '31/100' + "\n" + "Low Risk", fg = "green2")
                        else:
                            label_result.config(text = '30/100' + "\n" + "Low Risk", fg = "green2")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '33/100' + "\n" + "Low Risk", fg = "green2")
                        else:
                            label_result.config(text = '32/100' + "\n" + "Low Risk", fg = "green2")
                elif(total==2):
                    if(op1 == " Below 5 years " or op1 == " 5 - 17 years "):
                        label_result.config(text = '16/100' + "\n" + "Low Risk", fg = "green3")
                    elif(op1 == " 18 - 30 years "):
                        label_result.config(text = '18/100' + "\n" + "Low Risk", fg = "green3")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '21/100' + "\n" + "Medium Risk", fg = "green3")
                        else:
                            label_result.config(text = '20/100' + "\n" + "Low Risk", fg = "green3")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '23/100' + "\n" + "Low Risk", fg = "green3")
                        else:
                            label_result.config(text = '22/100' + "\n" + "Low Risk", fg = "green3")
                elif(total==1):
                    if(op1 == " Below 5 years " or op1 == " 5 - 17 years "):
                        label_result.config(text = '12/100' + "\n" + "Very Low Risk", fg = "green4")
                    elif(op1 == " 18 - 30 years "):
                        label_result.config(text = '15/100' + "\n" + "Low Risk", fg = "green3")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '18/100' + "\n" + "Medium Risk", fg = "green3")
                        else:
                            label_result.config(text = '17/100' + "\n" + "Low Risk", fg = "green3")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '21/100' + "\n" + "Medium Risk", fg = "green3")
                        else:
                            label_result.config(text = '20/100' + "\n" + "Low Risk", fg = "green3")

            elif(op3=='1'):
                if(op4==1):
                    label_result.config(text = '20/100' + "\n" + "Low Risk", fg = "green3")
                elif(total==8):
                    if(op1 == " Below 5 years "):
                        label_result.config(text = '95/100' + "\n" + "Extreme Risk", fg = "red4")
                    elif(op1 == " 5 - 17 years "):
                        label_result.config(text = '96/100' + "\n" + "Extreme Risk", fg = "red4")
                    elif(op1 == " 18 - 30 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '97/100' + "\n" + "Extreme Risk", fg = "red4")
                        else:
                            label_result.config(text = '96.5/100' + "\n" + "Extreme Risk", fg = "red4")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '98/100' + "\n" + "Extreme Risk", fg = "red4")
                        else:
                            label_result.config(text = '97.5/100' + "\n" + "Extreme Risk", fg = "red4")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '99/100' + "\n" + "Extreme Risk", fg = "red4")
                        else:
                            label_result.config(text = '98.5/100' + "\n" + "Extreme Risk", fg = "red4")
                elif(total==7):
                    if(op1 == " Below 5 years "):
                        label_result.config(text = '88/100' + "\n" + "High Risk", fg = "red3")
                    elif(op1 == " 5 - 17 years "):
                        label_result.config(text = '89/100' + "\n" + "High Risk", fg = "red3")
                    elif(op1 == " 18 - 30 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '91/100' + "\n" + "Extreme Risk", fg = "red4")
                        else:
                            label_result.config(text = '90.5/100' + "\n" + "Extreme Risk", fg = "red4")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '92.5/100' + "\n" + "Extreme Risk", fg = "red4")
                        else:
                            label_result.config(text = '92/100' + "\n" + "Extreme Risk", fg = "red4")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '94/100' + "\n" + "Extreme Risk", fg = "red4")
                        else:
                            label_result.config(text = '93.5/100' + "\n" + "Extreme Risk", fg = "red4")
                elif(total==6):
                    if(op1 == " Below 5 years "):
                        label_result.config(text = '81/100' + "\n" + "High Risk", fg = "red3")
                    elif(op1 == " 5 - 17 years "):
                        label_result.config(text = '81.5/100' + "\n" + "High Risk", fg = "red3")
                    elif(op1 == " 18 - 30 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '83.5/100' + "\n" + "High Risk", fg = "red3")
                        else:
                            label_result.config(text = '83/100' + "\n" + "High Risk", fg = "red3")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '85/100' + "\n" + "High Risk", fg = "red3")
                        else:
                            label_result.config(text = '84.5/100' + "\n" + "High Risk", fg = "red3")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '87/100' + "\n" + "High Risk", fg = "red3")
                        else:
                            label_result.config(text = '86/100' + "\n" + "High Risk", fg = "red3")
                elif(total==5):
                    if(op1 == " Below 5 years "):
                        label_result.config(text = '72/100' + "\n" + "High Risk", fg = "red2")
                    elif(op1 == " 5 - 17 years "):
                        label_result.config(text = '73/100' + "\n" + "High Risk", fg = "red2")
                    elif(op1 == " 18 - 30 years "):
                        label_result.config(text = '75/100' + "\n" + "High Risk", fg = "red2")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '77/100' + "\n" + "High Risk", fg = "red2")
                        else:
                            label_result.config(text = '76.5/100' + "\n" + "High Risk", fg = "red2")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '80/100' + "\n" + "High Risk", fg = "red3")
                        else:
                            label_result.config(text = '79/100' + "\n" + "High Risk", fg = "red3")
                elif(total==4):
                    if(op1 == " Below 5 years " or op1 == " 5 - 17 years "):
                        label_result.config(text = '65/100' + "\n" + "High Risk", fg = "red2")
                    elif(op1 == " 18 - 30 years "):
                        label_result.config(text = '66/100' + "\n" + "High Risk", fg = "red2")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '69/100' + "\n" + "High Risk", fg = "red2")
                        else:
                            label_result.config(text = '68/100' + "\n" + "High Risk", fg = "red2")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '70.5/100' + "\n" + "High Risk", fg = "red2")
                        else:
                            label_result.config(text = '70/100' + "\n" + "High Risk", fg = "red2")
                elif(total==3):
                    if(op1 == " Below 5 years " or op1 == " 5 - 17 years "):
                        label_result.config(text = '59/100' + "\n" + "Medium Risk", fg = "red")
                    elif(op1 == " 18 - 30 years "):
                        label_result.config(text = '60/100' + "\n" + "Medium Risk", fg = "red2")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '61.5/100' + "\n" + "Medium Risk", fg = "red2")
                        else:
                            label_result.config(text = '61/100' + "\n" + "Medium Risk", fg = "red2")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '63/100' + "\n" + "Medium Risk", fg = "red2")
                        else:
                            label_result.config(text = '62/100' + "\n" + "Medium Risk", fg = "red2")
                elif(total==2):
                    if(op1 == " Below 5 years " or op1 == " 5 - 17 years "):
                        label_result.config(text = '50/100' + "\n" + "Medium Risk", fg = "red")
                    elif(op1 == " 18 - 30 years "):
                        label_result.config(text = '52/100' + "\n" + "Medium Risk", fg = "red")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '55/100' + "\n" + "Medium Risk", fg = "red")
                        else:
                            label_result.config(text = '54/100' + "\n" + "Medium Risk", fg = "red")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '58/100' + "\n" + "Medium Risk", fg = "red")
                        else:
                            label_result.config(text = '57/100' + "\n" + "Medium Risk", fg = "red")
                elif(total==1):
                    if(op1 == " Below 5 years "):
                        label_result.config(text = '39/100' + "\n" + "Low Risk", fg = "green2")
                    elif(op1 == " 5 - 17 years "):
                        label_result.config(text = '40/100' + "\n" + "Medium Risk", fg = "green2")
                    elif(op1 == " 18 - 30 years "):
                        label_result.config(text = '42/100' + "\n" + "Medium Risk", fg = "green2")
                    elif(op1 == " 31 - 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '45/100' + "\n" + "Medium Risk", fg = "red")
                        else:
                            label_result.config(text = '44/100' + "\n" + "Medium Risk", fg = "green2")
                    elif(op1 == " Above 60 years "):
                        if(op2 == " Female "):
                            label_result.config(text = '48/100' + "\n" + "Medium Risk", fg = "red")
                        else:
                            label_result.config(text = '47/100' + "\n" + "Medium Risk", fg = "red")
        else:
            MessageBox(None, ' Please enter all the fields. ', ' Alert! ', 0)

    n1 = StringVar(canvas)
    monthchoosen1 = ttk.Combobox(canvas, width = 25, textvariable = n1,font = "Times 13 bold roman")
    monthchoosen1['values'] = (" Below 5 years "," 5 - 17 years "," 18 - 30 years "," 31 - 60 years "," Above 60 years ")
    mothchoosen1_canvas = canvas.create_window(320, 50, window = monthchoosen1)
    monthchoosen1.current()
    label2 = Label(canvas, text = " Gender :" ,font = "Times 16 bold roman")
    label2_canvas = canvas.create_window(100, 120, window = label2)
    n2 = StringVar(canvas)
    monthchoosen2 = ttk.Combobox(canvas, width = 25, textvariable = n2,font = "Times 13 bold roman")
    monthchoosen2['values'] = (" Male "," Female "," Others ")
    mothchoosen2_canvas = canvas.create_window(320, 120, window = monthchoosen2)
    monthchoosen2.current()
    label3 = Label(canvas, text = " Recent contact with Covid patient in last 14 days? " ,font = "Times 16 bold roman")
    label3_canvas = canvas.create_window(260, 200, window = label3)
    v = StringVar(canvas)
    R1 = Radiobutton(canvas, text = " Yes ", variable = v, value = 1,font = "Times 17 bold roman")
    canvas.create_window(150, 250, window = R1)
    R2 = Radiobutton(canvas, text = " No ", variable = v, value = 2,font = "Times 17 bold roman")
    canvas.create_window(150, 300, window = R2)
    label4 = Label(canvas, text = " Are you having one or more of the following symptoms? " ,font = "Times 16 bold roman")
    label4_canvas = canvas.create_window(1000, 60, window = label4)

    CheckVar1 = IntVar()
    C1 = Checkbutton(canvas, text = " None ", variable = CheckVar1,onvalue = 1, offvalue = 0,font = "Times 17 bold roman")
    canvas.create_window(902, 100, window = C1)
    CheckVar2 = IntVar()
    C2 = Checkbutton(canvas, text = " Fever ", variable = CheckVar2,onvalue = 1, offvalue = 0,font = "Times 17 bold roman")
    canvas.create_window(905, 150, window = C2)
    CheckVar3 = IntVar()
    C3 = Checkbutton(canvas, text = " Dry Cough ", variable = CheckVar3,onvalue = 1, offvalue = 0,font = "Times 17 bold roman")
    canvas.create_window(931, 200, window = C3)
    CheckVar4 = IntVar()
    C4 = Checkbutton(canvas, text = " Feeling shortness of breath ", variable = CheckVar4,onvalue = 1, offvalue = 0,font = "Times 17 bold roman")
    canvas.create_window(1010, 250, window = C4)
    CheckVar5 = IntVar()
    C5 = Checkbutton(canvas, text = " Sore throat ", variable = CheckVar5,onvalue = 1, offvalue = 0,font = "Times 17 bold roman")
    canvas.create_window(931, 300, window = C5)
    CheckVar6 = IntVar()
    C6 = Checkbutton(canvas, text = " Hoarseness in voice ", variable = CheckVar6,onvalue = 1, offvalue = 0,font = "Times 17 bold roman")
    canvas.create_window(970, 350, window = C6)
    CheckVar7 = IntVar()
    C7 = Checkbutton(canvas, text = " Headache ", variable = CheckVar7,onvalue = 1, offvalue = 0,font = "Times 17 bold roman")
    canvas.create_window(924, 400, window = C7)
    CheckVar8 = IntVar()
    C8 = Checkbutton(canvas, text = " Running nose ", variable = CheckVar8,onvalue = 1, offvalue = 0,font = "Times 17 bold roman")
    canvas.create_window(941, 450, window = C8)
    CheckVar9 = IntVar()
    C9 = Checkbutton(canvas, text = " Loss of Smell and taste ", variable = CheckVar9,onvalue = 1, offvalue = 0,font = "Times 17 bold roman")
    canvas.create_window(988, 500, window = C9)
    btn = Button(canvas, text = ' Submit ', font = "Times 20 bold italic" , cursor = "hand2", command = show)
    canvas.create_window(500,360, window = btn)
    label5 = Label(canvas, text = " Result : " ,font = "Times 18 bold roman")
    label5_canvas = canvas.create_window(200, 440, window = label5)
    label_result = Label(canvas, font = "Times 19 bold roman")
    canvas.create_window(350, 440, window = label_result)
    def callback():
        url_open = "https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/index.html"
        webbrowser.open_new(url_open)
    label6 = Label(canvas,text = " For More Information ",font = "Times 12 normal roman" ,fg = "blue", cursor = "hand2")
    label6.bind("<Button-1>", lambda e: callback())
    canvas.create_window(1400, 540, window = label6)
