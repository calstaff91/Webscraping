#This is a basic html webscrape using BeautifulSoup, with a few examples of how class text can be stripped
#out to leave purely is required

#Import required modules
import os
import timeit
import pandas as pd
from bs4 import BeautifulSoup
import csv 
import urllib2
import re
import requests
#-----------------------------------------------------------------------------

#Setup timers and counters for reference when scrape is running
start = timeit.default_timer()
counter = 1
#-----------------------------------------------------------------------------

#Import list of URLs from csv to a list
variable_list=[]
os.chdir('Directory Name Here')

urls = csv.reader(open('File Here.csv'))
with open('File Here.csv', 'rb') as f:
    reader = csv.reader(f)
    URLs_List=list(reader)   
#-----------------------------------------------------------------------------


for URLs in URLs_List:
    
    #Displays number of URLs scraped
    print counter
    counter+=1
    
    #Makes call to website and returns html
    r = requests.get(url[0])
    soup = BeautifulSoup(r.text, "html5lib")
    class_appearances=soup.find_all("Type of Class Here",{"class":"Name of Class Here"})

    for class_appearance in class_appearances:
        
        #This first variable could be used where a number is required from a string, e.g. the number in a review
        try:
            variable1 = class_appearance.find("Type of Class Here",{"class":"Name of Class Here"})
            variable1 = variable1.find("Type of Class Here")["Part of Class Here"]
            variable1 = variable1.replace("Text to be Removed","Text to Replace With")
        #The 'except' is here for when there may not be a value for that URL, i.e. it hasn't been reviewed yet
        except (AttributeError):
            starrating = ""

        #This variable could be used where the text contains multiple blank lines, and only the first line is required
        try:
            variable2 = class_appearance.find("Type of Class Here",{"class":"Name of Class Here"})
            variable2 = variable2.text
            if "\n" in date:
                date = date.strip("\n") 

        except (AttributeError):
            date = ""
        
        #Create a dictionary containing the information scraped above and append to a list of all other entries
        variable_dict = {"URL":url,"Variable 1":variable1,"Variable 2":variable2}
        variable_list.append(variable_dict)
        
        #Pause the scrape so it doesn't bombard the website's servers too much
        from time import sleep
        sleep(0.05)
#-----------------------------------------------------------------------------

#Convert to a csv
pd.DataFrame(firstratings).to_csv(r"Location and Name of New csv Here.csv",encoding="utf-8")  
#-----------------------------------------------------------------------------

#Stop the timer and print the timer it has taken to complete the entire process
stop = timeit.default_timer()
print stop - start