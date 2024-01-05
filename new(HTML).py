from bs4 import BeautifulSoup
import time
from selenium import webdriver
import pyautogui

url = "https://humanbenchmark.com/tests/aim"
browser = webdriver.Chrome()

browser.get(url)
time.sleep(5)
browser.implicitly_wait(10)
#BeautifulSoup to extract information from the website

while True:
    source = browser.page_source
    soup = BeautifulSoup(source, 'html.parser')
    spans = soup.find('div', class_='css-1k4dpwl e6yfngs0')
    spans = str(spans).split('d(')[1]
    spans = str(spans).split(');')[0]
    spans = str(spans).split(', ')
    print(spans)
    pyautogui.click(float(spans[12])+100, float(spans[13])+100)

    #WORK IN PROGRESS