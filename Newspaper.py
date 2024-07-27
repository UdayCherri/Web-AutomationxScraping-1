from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import html5lib
from bs4 import BeautifulSoup 

def main():
    Menu()
    opt = input("Enter your Selecion option: ")
    print("\n")

    if opt=='1':
        #Headline Extraction
        Extract()
    elif opt=='2':
        #View Today's Newspaper
        View()
    else:
        print("Enter a vaild Input")

def Menu():
    print("What do you wanna do? \n      1.Get the Headlines of Today's newspaper\n      2.View today's newspaper\n")

def Extract():
        response = requests.get("https://www.nytimes.com/section/todayspaper/")
        soup = BeautifulSoup(response.content, 'html5lib')
        mainheadlines = soup.findAll("a", attrs = {"class": "css-1u3p7j1"})
        subheadlines = soup.findAll("h2", attrs = {"class": "css-1sd6y0f e1b0gigc0"})
        print("Today's main Topics are: \n")
        for i in mainheadlines:
            charact = i.text.strip()
            print("\t"+charact)
        print("\nToday's Sub-Topics are: \n")
        for i in subheadlines:
            charact = i.text.strip()
            print("\t"+charact)
        print("\n")

def View():
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.nytimes.com/section/todayspaper/")
        paper = driver.find_element(By.XPATH, '//*[@id="collection-todays-new-york-times"]/div[1]/section[1]/div[2]/section/div/div[2]/button/img')
        paper.click()
        view = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div/div/div/div/div[2]/a')
        view.click()
        time.sleep(1000)

