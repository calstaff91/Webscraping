#Scraping a range of items from a webpage using CSS selectors. I have found CSS selectors are more reliable 
#when scraping more complicated websites, as they provide a simpler path to the target of the scrape

#Import required modules
import os
import timeit
import pandas as pd
from bs4 import BeautifulSoup
import csv 
import urllib2
import re
import lxml.html
from lxml.cssselect import CSSSelector
import requests
#-----------------------------------------------------------------------------

#Setup timers and counters for reference when scrape is running
start = timeit.default_timer()
counter = 1
#-----------------------------------------------------------------------------

#Defines a function to only proceed with the scrape for that page if it is possible, otherwise to skip, to prevent
#an error being caused and the process being interrupted
def request_is_valid(request):
            """
            This is a function that
            returns True if the request
            is valid otherwise fail
            """
            if r.text == "":
                        return False
            else:
                        return True
#-----------------------------------------------------------------------------

#Import list of URLs from csv to a list
os.chdir('Directory Name Here')
vistorratings_to_do = set()
urls = csv.reader(open('File Here.csv'))
with open('File Here.csv', 'rb') as f:
    reader = csv.reader(f)
    URLs_list=list(reader)
#-----------------------------------------------------------------------------

#Create blank list for appending scraped entities to
results_list=[]
#-----------------------------------------------------------------------------

#Works through each URL, scraping features
for URL in URLs_List:
    
    print counter
    counter+=1
 
    #Searches for content to be scraped. Skips if no content to be scraped
    r = requests.get(url[0])
    if not request_is_valid(r):
        continue
    
    #This is an example scrape for text-based classes
    try:
        tree = lxml.html.fromstring(r.text)
        potential_paths = CSSSelector('CSS Path Here')
        results1 = potential_paths(tree)
        match1 = results1[0]
        soup1=BeautifulSoup(lxml.html.tostring(match1))
        text_var1 = soup1.text
        
        #This if statement can be used if text needs to be removed from the string
        if "Text to be Removed Here" in ins1i:
            text_var1=text_var1.replace("Text to be Removed Here","Text to be Inserted Here")
        
        #This statement can be used to strip multiple blank lines from the string
        text_var1 = text_var1.strip('\n')
     
    #The 'try, except' function is included so that if one feature is not found, any error messages
    #will not interrupt the process, and instead a blank entry will be generated
    except (IndexError, TypeError):
        
        title = ""
        results1 = ""
        match1 = ""
        soup1 = ""
        text_var1 = ""
    
    #This is an example of a scrape for the meta data associated with an image
    try:
        tree = lxml.html.fromstring(r.text)
        tascore = CSSSelector('CSS Path Here')
        results2 = tascore(tree)
        match2 = results2[0]
        soup2 = BeautifulSoup(lxml.html.tostring(match2))
        img_var2 = soup2.find("img")["alt"]
        
    except (IndexError, TypeError):

        tascore = ""
        results2 = ""
        match2 = ""
        soup2 = ""
        img_var2 = ""
    
    #Creates entry for dictionary with all features for that URL and appends to a list
    scrape_dict={"Text":text_var1,
                 "Image Meta Data":img_var2,}
    
    results_list.append(scrape_dict)
    
    #Sleeps scrape momentarily to prevent the website's servers being bombarded
    from time import sleep
    sleep(0.01) 

#Creates csv
df = pd.DataFrame(results_list)
df.to_csv(r"Location and Name of New csv Here.csv",encoding="utf-8")
#-----------------------------------------------------------------------------

#Prints overall time for process
stop = timeit.default_timer()
print stop - start