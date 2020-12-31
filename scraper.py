# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:18:09 2020

@author: Justyn
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup as bs
import time
import re 


class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome(r'C:/Users/Justyn/Documents/Data science/chromedriver_win32/chromedriver.exe')
        self.url = 'https://carsandbids.com/past-auctions/'
        self.hrefs = []
        
    #returns hrefs 
    def get_hrefs(self):
        return self.hrefs
    
    def get_features(self, url):
        self.get_info(url)
        return self.features
    
    def load_url(self):
        self.driver.get(self.url)
        
    def scroll_down(self):
        self.driver.execute_script('window.scroll(0, document.body.scrollHeight)')
    
    #pulls all text once scrolled to the bottom of page
    #finds link for individual car webpage and puts in a list callled hrefs
    def read_data(self):
        main = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/ul')
        soup = bs(main.get_attribute('innerHTML'), 'html.parser')
        
        for elem in soup.findAll('a', {'class':'hero'}):
            href = str(elem['href'])
            self.hrefs.append(href)
    
    #takes individual car webpage urls and pulls features from each
    #adds list of features called features
    def get_info(self, url):
        self.features = []
        self.driver.get(url)
        
        #pulls car year and adds to feature list
        year_heading = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[1]')))
        yr_soup = bs(year_heading.get_attribute('innerHTML'), 'html.parser')
        yr_regex = re.compile('(\d+)')
        yr = yr_regex.findall(yr_soup.text)
        self.features.append(yr[0])
        
        #pulls car details and adds to feature list (make, model, mileage, powertrain, location, etc)
        quick_facts = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[1]/div[2]') 
        qf_soup = bs(quick_facts.get_attribute('innerHTML'), 'html.parser')
        for dd in qf_soup.findAll('dd'):
            self.features.append(dd.text)
            
        #gets selling price of vehicle. If reserve wasn't met then highest bid returned
        selling_price = self.driver.find_element_by_class_name('bid-value')
        sp_soup = bs(selling_price.get_attribute('innerHTML'), 'html.parser')
        self.features.append(sp_soup.text)
        

        #Determine if car listing had a reserve
        no_reserve_tag = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div[2]')
        ns_soup = bs(no_reserve_tag.get_attribute('innerHTML'), 'html.parser')
        if 'No Reserve' in ns_soup.text:
             self.features.append('No reserve')
        else:
             self.features.append('Has reserve')
             
        #Get horsepower and torque stats for single webpage
        power_text = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[1]/div[3]/div[2]/div')
        p_soup = bs(power_text.get_attribute('innerHTML'), 'html.parser')
        hp_regex = re.compile(('(\d+)\s*horsepower|(\d+)\s*hp'))
        hp_num = hp_regex.findall(p_soup.text)
        self.features.append(hp_num)
        torque = re.compile(('(\d+)\s*lb'))
        torque_num = torque.findall(p_soup.text)
        self.features.append(torque_num)
        
