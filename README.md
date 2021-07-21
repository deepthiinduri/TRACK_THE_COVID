<img width="30"  src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/Images/coronavirus_image_UXL_icon.ico">  **_TRACK THE COVID_**
======

> **This Tracker Application helps in tracking and breaking chains of transmission of COVID-19. It uses maps and graphs to analyze the global distribution of covid-19.**
> 
> **This tracker is designed to inform people regarding risks, best practices and relevant advisories related to coronavirus.**
> 
> **It also helps to check the availability of vaccination centers in your area (India).**

### Prerequisites ###

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

___

### About our project ###

#### 🏡 Home Page ####

In the Home Page the Tracker shows the number of Active, Deaths, Discharged cases from novel coronavirus and Vaccinations in India with Refresh and Exit buttons.

##### Importing Modules

```python
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
```

<img src="https://github.com/deepthiinduri/TRACK_THE_COVID/blob/main/TRACK_THE_COVID/Home%20Page.png">





