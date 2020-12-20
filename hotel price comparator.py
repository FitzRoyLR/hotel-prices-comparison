# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 22:15:33 2020

@author: Louis Régis
"""


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


#data points
hotel_com_price= 'https://ch.hotels.com/'
booking_com_price = 'https://www.booking.com/index.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaCyIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4Aszh-f4FwAIB0gIkY2ZmZTI0YTYtMmE1Ny00NWRhLTg4ZGMtZDY0ZDlhZTFjYWFh2AIF4AIB;sid=401b18c75022eaf722888afffc747937;keep_landing=1&sb_price_type=total&'
priceline_price = 'https://www.priceline.com/?vrid=7974d12dea2cb2a72a8d6abd35fd98f6'
tripadvisor_price = 'https://www.tripadvisor.com/Hotels-g154979-Ontario-Hotels.html'

# Select custom Chrome options
# Select custom Chrome options
options = webdriver.ChromeOptions()
#options.add_argument('--headless') 
#options.add_argument('start-maximized') 
#options.add_argument('disable-infobars')
#options.add_argument('--disable-extensions')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(hotel_com_price)

#hotel subject
search_item = "Royal Monceau"

#hotel_com_price
search_bar = driver.find_element_by_id('qf-0q-destination')
search_bar.send_keys(search_item)
driver.find_element_by_xpath('.//button[contains(@class, "cta cta-strong")]').click()