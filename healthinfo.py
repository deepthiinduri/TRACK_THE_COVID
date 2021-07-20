from tkinter import *
from PIL import ImageTk, Image ,ImageDraw, ImageFont, ImageFilter

def covid_symptoms():
    newWindow = Toplevel()
    newWindow.title("COVID SYMPTOMS")
    newWindow.state('zoomed')
    newWindow.iconbitmap(r'Images\coronavirus_image_UXL_icon.ico')
    labe1 = Label(newWindow, text = " SYMPTOMS " , font = "Times 25 bold roman" , pady = 5, padx = 1550 ,fg = "#EC4D37", bg = "black").pack()
    labe2 = Label(newWindow, text = "COVID-19 affects different people in different ways. Most infected people will develop mild to moderate illness and recover without hospitalization.",font = "Cambria 16 bold roman", pady = 25).pack()
    canvas = Canvas(newWindow, height = 20, width = 1550)
    canvas.create_line(150, 2, 1400, 2)
    canvas.pack()
    info_div1 = "Most common symptoms: " + "\n" + "• fever" + "\n" + "• dry cough" + "\n" + "• tiredness" + "\n\n" + "Less common symptoms:" "\n" + "• aches and pains" + "\n" + "• sore throat" + "\n" + "• diarrhoea" + "\n" + "• conjunctivitis" + "\n" + "• headache" + "\n" + "• loss of taste or smell" + "\n" + "• a rash on skin, or discolouration of fingers or toes" + "\n\n"
    info_div2 = "Serious symptoms:" + "\n" + "• difficulty breathing or shortness of breath" + "\n" + "• chest pain or pressure" + "\n" + "• loss of speech or movement" + "\n\n" + "Seek immediate medical attention if you have serious symptoms. Always call before visiting your doctor or health facility." + "\n\n" + "People with mild symptoms who are otherwise healthy should manage their symptoms at home." + "\n\n" + "On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days."
    info_div = info_div1 + info_div2
    render = ImageTk.PhotoImage(Image.open ("Images/symptoms.png").resize((440,440) , Image.ANTIALIAS))
    img = Label(newWindow, image = render)
    img.image = render
    img.pack(side = RIGHT, anchor = NE)
    labe3 = Label(newWindow, text = info_div , font = "Candara 14 normal roman", anchor = "e", justify = LEFT).pack()


def covid_precautions():
    newWindow = Toplevel()
    newWindow.title("COVID PRECAUTIONS")
    newWindow.state('zoomed')
    newWindow.iconbitmap(r'Images\coronavirus_image_UXL_icon.ico')
    labe1 = Label(newWindow, text = " PRECAUTIONS " , font = "Times 25 bold roman" , pady = 5, padx = 1550 ,fg = "#EC4D37", bg = "black").pack()
    render = ImageTk.PhotoImage(Image.open ("Images/covid prevention1.png").resize((470,740) , Image.ANTIALIAS))
    img = Label(newWindow, image = render)
    img.image = render
    img.pack(side = RIGHT, anchor = NE)
    render2 = ImageTk.PhotoImage(Image.open ("Images/globe3.png").resize((380,250) , Image.ANTIALIAS))
    img2 = Label(newWindow, image = render2)
    img2.image = render2
    img2.pack()
    canvas = Canvas(newWindow, height = 740 , width = 800)
    canvas.create_text(400, 100, text = "Wear a mask. Save lives." + "\n", font = "Stencil 46 normal roman" , fill = '#EC4D37')
    canvas.create_text(400,230 ,text = "\n\n" + "Wear a face cover" + "\n\n" + "Wash your hands" + "\n\n" + "Keep a safe distance." , font = "Elephant 30 normal roman")
    canvas.pack()

def covid_treatments():
    newWindow = Toplevel()
    newWindow.title("COVID TREATMENTS")
    newWindow.state('zoomed')
    newWindow.iconbitmap(r'Images\coronavirus_image_UXL_icon.ico')
    labe1 = Label(newWindow, text = " TREATMENTS " , font = "Times 25 bold roman" , pady = 5, padx = 1550 ,fg = "#EC4D37", bg = "black").pack()
    info_div1 = "Self-care: " + "\n\n" + "After exposure to someone who has COVID-19, do the following:" + "\n\n" + "• Call your health care provider or COVID-19 hotline to find out where and when to get a test." + "\n" + "• Cooperate with contact-tracing procedures to stop the spread of the virus." + "\n" 
    info_div2 = "• If testing is not available, stay home and away from others for 14 days." + "\n" + "• While you are in quarantine, do not go to work, to school or to public places. Ask someone to bring you supplies." + "\n" + "• Keep at least a 1-metre distance from others, even from your family members."+ "\n" + "• Wear a medical mask to protect others, including if/when you need to seek medical care." + "\n" + "• Clean your hands frequently." + "\n" + "• Stay in a separate room from other family members, and if not possible, wear a medical mask." + "\n" + "• Keep the room well-ventilated."+ "\n"
    info_div3 = "• If you share a room, place beds at least 1 metre apart." + "\n" + "• Monitor yourself for any symptoms for 14 days." + "\n" + "• Call your health care provider immediately if you have any of these danger signs: difficulty breathing, loss of speech or mobility, confusion or chest pain." + "\n" + "• Stay positive by keeping in touch with loved ones by phone or online, and by exercising at home." + "\n\n\n\n"
    info_div4 = "Medical treatments: " + "\n\n" + "Scientists around the world are working to find and develop treatments for COVID-19." + "\n\n" + "• Optimal supportive care includes oxygen for severely ill patients and those who are at risk for severe disease and more advanced respiratory support such as" + "\n" + "ventilation for patients who are critically ill." + "\n" + "• Dexamethasone is a corticosteroid that can help reduce the length of time on a ventilator and save lives of patients with severe and critical illness."
    info_div = info_div1 + info_div2 + info_div3 + info_div4
    labe2 = Label(newWindow, text = info_div, font = "Candara 16 normal roman", anchor = "e", justify = LEFT)
    labe2.pack(side = LEFT)
