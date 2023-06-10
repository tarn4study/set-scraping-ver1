from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

url = 'https://www.set.or.th/th/market/product/stock/quote/AAV/financial-statement/company-highlights'

driver.get(url)

data_list = pd.read_html(driver.page_source)
data_list[0].to_excel(r'D:\Project\web scraping\set\AAV.xlsx')