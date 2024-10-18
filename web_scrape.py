from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

chrome_driver_path = "C:\\WebDriver\\chromedriver.exe"

chrome_options = Options()
chrome_options.binary_location = "C:\\Users\\Phili\\Downloads\\chrome-win\\chrome-win\\chrome.exe"
chrome_options.add_argument('--no-sandbox')  

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.flipkart.com/search?sid=b5g&otracker=CLP_Filters&p%5B%5D=facets.processor%255B%255D%3DRyzen%2B7%2BQuad%2BCore")

products = []
prices = []
ratings = []

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

for a in soup.findAll('div', attrs={'class':'_1YokD2 _3Mn1Gg'}):
    name = a.find('div', attrs={'class':'_4rR01T'})
    price = a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating = a.find('div', attrs={'class':'_3LWZlK'})
    
    if name and price and rating:
        products.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text)

df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
df.to_csv('flipkart_products.csv', index=False, encoding='utf-8')

driver.quit()
print("Web scraping completed. Data saved to 'flipkart_products.csv'.")
