from splinter import Browser
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import pandas as pd
import datetime as dt

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def fuelly_scrapper():
    #define fuelly scrapper for fuelly log
    url='http://www.fuelly.com/activity?filter=4'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    data = soup.find_all('li', class_="activity-list-item fy-icon-fuel-ups")
        for data in data:
        user_list.append(data.a.get_text())
        vehicle_list.append(data.a.find_next().get_text())
        mpg_list.append(data.a.find_next().find_next().get_text())
        browser.quit()
        new_df = pd.DataFrame({
        "User": user_list,
        "Vehicle": vehicle_list,
        "MPG": mpg_list})
        new_df.drop_duplicates().to_csv('fuelly_data_export.csv')

def AAA_scrapper():
    list_name =[]
    regular_avg =[]
    mid_avg = []
    premium_avg = []
    diesel_avg = []
    e85_avg = []
    url='https://gasprices.aaa.com/'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    for data in data:
        list_name.append(data.tr.find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().get_text())
        regular_avg.append(data.tr.find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().get_text())
        mid_avg.append(data.tr.find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().get_text())
        premium_avg.append(data.tr.find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().get_text())
        diesel_avg.append(data.tr.find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().get_text())
        e85_avg.append(data.tr.find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().get_text())
       
        new_df = pd.DataFrame({
        "Gas Price": list_name,
        "Regular": regular_avg,
        "Mid-Grade": mid_avg,
        "Premium": premium_avg,
        "Diesel": diesel_avg,
        "E85": e85_avg})
        table = soup.find('table', attrs={'class':'table-mob'})
        table_rows = table.find_all('tr')
        gas_list_aaa = []
        
        for tr in table_rows:
            td = tr.find_all('td')
            row = [tr.text for tr in td]
            gas_list_aaa.append(row)
            gas_aaa_df = pd.DataFrame(gas_list_aaa, columns=["", "Regular", "Mid-Grade", "Premium","Diesel", "E85"]).drop([0])