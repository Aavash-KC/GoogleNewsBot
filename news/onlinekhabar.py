from urllib import request
import news.constants as const
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date
import xlwt
from xlwt import Workbook, Formula
from fpdf import FPDF
import os
import time


class OnlineKhabar(webdriver.Chrome):
    
        
    def land_first_page(self):
        super(OnlineKhabar,self).__init__()
        self.maximize_window()
        self.get("https://www.onlinekhabar.com/")
        self.implicitly_wait(30)
        latest = self.find_element(By.XPATH,"//a[@class='ok-btn-quick update-24']")
        time.sleep(10)
        latest.click()
    
    def get_heading(self):
        self.implicitly_wait(10)
        divs = self.find_elements(By.XPATH,"//div[@class='span-4']")
        headings_list=[]
        for div in divs:
            heading=div.find_element(By.TAG_NAME, "h2").text
            headings_list.append(heading)
            print(heading)
        print(len(headings_list))
            
            
        return headings_list
        
        
    def get_link(self):
        divs = self.find_elements(By.XPATH,"//div[@class='span-4']")
        links_list=[]
        for div in divs:
            link=div.find_element(By.TAG_NAME, "a").get_attribute('href')
            links_list.append(link)
        print(len(links_list))
        return links_list
    
    def export_data(self):
        writeBook = xlwt.Workbook(encoding='utf-8')
        sheet = writeBook.add_sheet('Search_results', cell_overwrite_ok=True)
        style = xlwt.XFStyle()
        sheet.write(0,1,'News Title')
        sheet.write(0,2,'News URL')
        titles= self.get_heading()
        urls = self.get_link()
        for index, title in enumerate(titles):
            sheet.write(index+1,1,title)
            sheet.write(index+1,2,xlwt.Formula(f'HYPERLINK("{urls[index]}")'))
            
        writeBook.save("online") 
    
        