import sys
import argparse
import re
import json
#from objects.Hotel import Hotel
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


def readFromFile(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def parse_opts():
    parser = argparse.ArgumentParser(prog='main')
    parser.add_argument('-s','--scraprun', help="run the scrap portion", action='store_true')
    parser.add_argument('-l','--listrun', help="run the list processing portion", action='store_true')
    parser.add_argument('-i','--insertdb', help="run the list processing portion", action='store_true')

    args = parser.parse_args()
    opts = vars(args)
    return(opts)


def makeUrl(dateIn, dateOut, city):
    return 'https://www.booking.com/searchresults.html?ss={city}&lang=pt-br&sb=1&src_elem=sb&src=index&dest_type=city&checkin={dateIn}&checkout={dateOut}&group_adults=2&no_rooms=1&group_children=0'.format(
        dateIn = dateIn,
        dateOut = dateOut,
        city = city
    )


def getHTML(url):
    headers={
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        #"Accept-Encoding": "gzip, deflate, br",
    }
    response = requests.get(url,headers=headers)
    if response.status_code != 200:
        print("Error: ", response.status_code)
        return None
    elementSource = bs(response.content, 'html.parser')
    writeToFile('/Users/renan/Documents/Scripts/Concierge/Trip/Hotel/tmp/output.html', elementSource)
    return elementSource


def writeToFile(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        if content != None:
            file.write(str(content))



if __name__ == "__main__":
    sys.path.append('/Users/renan/Library/Python/3.9/lib/python/site-packages')
    optsHash = parse_opts()
    config = json.loads(readFromFile('Flight/config.json'))
    scenarios = pd.read_csv(config['run_file'])
    url = 'https://www.booking.com/searchresults.html?ss={city}&lang=pt-br&sb=1&src_elem=sb&src=index&dest_type=city&checkin={date_in}&checkout={date_out}&group_adults=2&no_rooms=1&group_children=0'
    getHTML(url)
