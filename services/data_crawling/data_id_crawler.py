import os
from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from bs4 import BeautifulSoup
from typing import List, Dict

from geopy.geocoders import Nominatim

class DataIdCrawler(): # id값들을 반환할 것! + nominatim util 로 전환

    data_ids: List[Dict] | None = None

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('lang=ko_KR')
    chromedriver_path = "chromedriver"
    driver = webdriver.Chrome(os.path.join(os.getcwd(), chromedriver_path), options=options)  

    