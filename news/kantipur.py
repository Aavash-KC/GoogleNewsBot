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
        self.get("https://ekantipur.com/")
        self.implicitly_wait(30)
       