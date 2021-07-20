import requests
import bs4

def get_corona_detail_of_india():
    url = "https://www.mohfw.gov.in/"
    html_data = requests.get(url)
    bs = bs4.BeautifulSoup(html_data.text,'html.parser')
    info_div1 = bs.find("section" ,class_ = "site-stats").find("li" , class_ = "bg-blue").find_all("span" , class_ = "mob-show")
    info_div2 = bs.find("section" ,class_ = "site-stats").find("li" , class_ = "bg-green").find_all("span" , class_ = "mob-show")
    info_div3 = bs.find("section" ,class_ = "site-stats").find("li" , class_ = "bg-red").find_all("span" , class_ = "mob-show")
    info_div4 = "\n\n" + bs.find("section" ,class_ = "site-stats").find("h6" , class_ = "covidupdae").get_text() + "\n"
    info_div5 = bs.find("section" ,class_ = "site-stats").find("div" , class_ = "fullbol").get_text()
    out1 = "\nActive : \n" + info_div1[2].get_text() + "↑\n"
    out2 = "\nDischarged : \n" +info_div2[2].get_text() + "↑\n"
    out3 = "\nDeaths : \n" +  info_div3[2].get_text() + "↑\n"
    out4 = info_div4
    out5 = info_div5
    lst = [out1 ,out2, out3 , out4 , out5]
    return lst
