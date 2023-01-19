from urllib import request
import news.constants as const
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date
import xlwt
from fpdf import FPDF
import os



class News(webdriver.Chrome):
    def __init__(self):
        self.keyword =''
        
    
    def land_first_page(self,user_input):
        super(News,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        self.keyword=user_input
        self.get(const.BASE_URL)
        
    def search_your_text(self,text_search):
        search_feild = self.find_element(By.XPATH,"//input[@class='Ax4B8 ZAGvjd']").send_keys(text_search+"\n")
       
       
    def get_heading(self):
        headings = self.find_elements(By.XPATH,"//h3[@class='ipQwMb ekueJc RD0gLb']")
        headings_list=[]
        for heading in headings:
            headings_list.append(heading.text)
            print(heading.text)
            
        return headings_list
        
        
    def get_link(self):
        links = self.find_elements(By.XPATH,"//a[@class='VDXfz']")
        links_list=[]
        for link in links:
            links_list.append(link.get_attribute('href'))
        return links_list
    
    def get_pics(self):
        pics = self.find_elements(By.XPATH,"//img[@class='tvs3Id QwxBBf']")
        return pics
    
    def get_pic_url(self):
        picUrl=[]
        eachDiv =self.find_elements(By.XPATH,"//div[@class='NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc']")
        for index, individualDiv in enumerate(eachDiv):
           
            if(individualDiv.find_element(By.XPATH,"//img[@class='tvs3Id QwxBBf']").get_attribute('src')):
                picUrl.append(individualDiv.find_element(By.XPATH,"//img[@class='tvs3Id QwxBBf']").get_attribute('src'))
                print('present')
            else:
                picUrl.append(" no pic ")
                print('not')
        return picUrl
            
    def export_data(self):
        writeBook = xlwt.Workbook(encoding='utf-8')
        sheet = writeBook.add_sheet('Search_results', cell_overwrite_ok=True)
        style = xlwt.XFStyle()
        sheet.write(0,0,'News pic')
        sheet.write(0,1,'News Title')
        sheet.write(0,2,'News URL')
        titles= self.get_heading()
        urls = self.get_link()
        #pics = self.get_pic_url()
        for index, title in enumerate(titles):
            sheet.write(index+1,1,title)
            sheet.write(index+1,2,urls[index])
            #sheet.write(index+1,0,pics[index])
            
        writeBook.save(f"{self.keyword}_{date.today()}") 
    
    def export_pdf(self):
        #create pdf object
        #Layout ('P','L')
        #Unit('mm','cm','Letter')
        #format('A3','A4'(default),'A5','Letter','Legal',(100,150))
        pdf = FPDF('P','mm','A4')
        pdf.add_font('DejaVu Sans',fname='/Library/Fonts/DejaVuSansCondensed.ttf')
        pdf.set_font('DejaVuSans', size=14)
        pdf.set_text_color(0,0,0)
        titles= self.get_heading()
    
        urls = self.get_link()
        pics = self.get_pics()
        pdf.add_page()
        for index, title in enumerate(titles):
            pdf.cell(10,index*10,title)
            pdf.cell(30,index*10,urls[index])
            #if(index < len(pics)):
                #pdf.image(pics[index].get_attribute('src'),x=40,y= index * 10)
        pdf.output(f"{self.keyword}_{date.today()}.pdf","F")