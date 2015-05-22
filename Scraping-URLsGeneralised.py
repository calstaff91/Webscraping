#A basic scrape to get URLs from a website containing multiple pages

#Import required modules
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
#-----------------------------------------------------------------------------

#Define base URL and blank set to append scraped URLs
base_url = "Insert URL Here (With %d replacing page numbers to be worked through)"
urls_to_do = set()
#-----------------------------------------------------------------------------

#Set counter for reference when scraping
counter = 1
#-----------------------------------------------------------------------------

#Define range of pages to be scraped: (Starting Page, Ending Page, Interval Between Pages)
for url in [base_url % i for i in range(0, 1530, 30)]: 
 
    print(counter)
    counter +=1
    
    #Request page content from URL
    r = requests.get(url)
    data = r.text
    soup=BeautifulSoup(data)
    soup_content = soup.find_all("Class Type Here", {"class": "Class Name Here"})
    
    #Concatenates main part of web address with the hrefs found within the content under that class
    resultslist = ["http://www.WebsiteHere.co.uk" + link["href"] for link in a]
    print resultslist
    
    #Appends the content from that page to an overall set
    urls_to_do = urls_to_do.union(set(resultslist))
    
    #Turns the set into a list
    urls_list=list(urls_to_do)

#Turns list into csv
pd.DataFrame(urls_list).to_csv(r"Location and Name of New csv Here.csv")