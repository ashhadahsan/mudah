from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from Google import Create_Service
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
CLIENT_SECRET_FILE='credentials.json'
API_NAME='sheets'
API_VERSION='v4'
SCOPES=['https://www.googleapis.com/auth/spreadsheets']
service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
import pandas as pd
sheet_body = {
    'properties': {
        'title': 'Mudah records',
        'locale': 'en_US', # optional
        }
    ,
    'sheets': [
        {
            'properties': {
                'title': 'Apartments'
            }
        }
        ]
    }



sheetfile=service.spreadsheets().create(body=sheet_body).execute() #create new sheet
sheet_id=sheetfile['spreadsheetId']
print(sheet_id)
worksheet_name = 'Apartments!'
cell_range_insert = 'A1'
values = [['Unique ID', 'Title', 'List ID', 'Date Posted','Price','Region','Subregion','Seller','Size','Bedrooms','Bathrooms','Seller Says','Contact No','Other Info','Facilities','Contact no 2','Type']]     
value_range_body = {
            'majorDimension': 'ROWS',
            'values': values
             }
service.spreadsheets().values().update(
                spreadsheetId=sheetfile['spreadsheetId'],
                valueInputOption='RAW',
                range=worksheet_name + cell_range_insert,
                body=value_range_body
            ).execute()
spreadsheets=service.spreadsheets()



request_body={'requests':[{
    'addSheet':{
        'properties':{
            'title':'Houses'
        }
    }
    
}]}
spreadsheets.batchUpdate(spreadsheetId=sheetfile['spreadsheetId'],body=request_body).execute()  

values = [['Unique ID', 'Title', 'List ID', 'Date Posted','Price','Region','Subregion','Seller','Size','Bedrooms','Bathrooms','Seller Says','Contact No','Other Info','Facilities','Contact no 2','Type']]     
value_range_body = {'majorDimension': 'ROWS','values': values}
service.spreadsheets().values().update(
                spreadsheetId=sheetfile['spreadsheetId'],
                valueInputOption='RAW',
                range='Houses!' + cell_range_insert,
                body=value_range_body
            ).execute()



request_body={'requests':[{
    'addSheet':{
        'properties':{
            'title':'Lands'
        }
    }
    
}]}
spreadsheets.batchUpdate(spreadsheetId=sheetfile['spreadsheetId'],body=request_body).execute()  

values = [['Unique ID', 'Title', 'List ID', 'Date Posted','Price','Region','Subregion','Seller','Size','Title Type','Property Type','Seller Says','Contact No','Other Info','Facilities','Contact no 2','Type']]     
value_range_body = {'majorDimension': 'ROWS','values': values}
service.spreadsheets().values().update(
                spreadsheetId=sheetfile['spreadsheetId'],
                valueInputOption='RAW',
                range='Lands!' + cell_range_insert,
                body=value_range_body
            ).execute()




request_body={'requests':[{
    'addSheet':{
        'properties':{
            'title':'Commercial'
        }
    }
    
}]}
spreadsheets.batchUpdate(spreadsheetId=sheetfile['spreadsheetId'],body=request_body).execute()  

values = [['Unique ID', 'Title', 'List ID', 'Date Posted','Price','Region','Subregion','Seller','Size','Title Type','Property Type','Seller Says','Contact No','Other Info','Facilities','Contact no 2','Type']]     
value_range_body = {'majorDimension': 'ROWS','values': values}
service.spreadsheets().values().update(
                spreadsheetId=sheetfile['spreadsheetId'],
                valueInputOption='RAW',
                range='Commercial!' + cell_range_insert,
                body=value_range_body
            ).execute()








import datetime
import os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options 

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os.path
from os import path
import sys
import requests
import shutil
from mydatabase import DATABASE
mydb=DATABASE()
#chrome_options=Options()
# chrome_options.headless=True
#chrome_options.add_argument('log-level=3')
# driver=webdriver.Chrome('./driver/chromedriver.exe',options=chrome_options)
firefox=Options()
firefox.headless=True
firefox.add_argument('log-level=3')




import numpy as np


# desired_capabilities = DesiredCapabilities.CHROME.copy()
# desired_capabilities['acceptInsecureCerts'] = True
import uuid
import xlsxwriter
from PIL import Image

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/bin/firefox')
driver=webdriver.Firefox(options=firefox,executable_path='./geckodriver',firefox_binary=binary)#FOR LINUX
import re

# from writetoexcel import writer
# w=writer()
countA=1
countB=1
countC=1
countD=1
areacode=""
mumber=""
true=0
null=0
false=1
def scrapethedata(typeofprop):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'div')))
    try:
        getnumber =str(driver.find_element_by_xpath('//*[@id="__NEXT_DATA__"]').get_attribute('innerHTML'))
        imagecontactnospan=re.search("phone",getnumber).span()
        startlimit=imagecontactnospan[1]+3
        imagecontactno=getnumber[startlimit:(startlimit+10)]
        findd=r'","price":'
        if  findd in imagecontactno:
           imagecontactno=""
    except:
        imagecontactno=""
    time.sleep(2)
       
    try:
        title=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[1]/div[1]/h1').text
        # print(title)
    except:
        title=""
    # print("title" +title)
    try:
        listid=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[1]/div[2]/span[1]').text.split(':')[1]
    # time.sleep(3)
    except:
        listid=""
    
    # print(listid)
    try:
        previosudate=(datetime.datetime.now() - datetime.timedelta(1)).strftime(r'%d-%m-%Y')
        dateposted=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[1]/div[2]/span[2]').text
        if "Yesterday" in dateposted:
            splitby=dateposted.split(" ")[-1]
            dateposted=previosudate+" "+splitby
            
    # print(dateposted)
    except:
        dateposted=""
    # time.sleep(2)
    try:
        price1=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[2]/div[1]/div[1]/div[2]/div').text
        price2=price1.replace(" ", "")
        price=int(price2.split("RM")[-1])
    # print(price)
    except:
        price=""
    # time.sleep(3)

    # print(price)
    try:
        
        location=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[2]/div[1]/div[2]/div[2]').text
        region=location.split("-")[0]
        subregions=location.split("-")[1]
    except:
        region=""
        subregions=""
    # time.sleep(3)
    # print(location)
  
    # print(region)
    # print(subregions)
    # time.sleep(3)
    try:
        seller=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[2]/div[1]/div[3]/div/div/div[2]/div/a').text
    except:
        seller=""
    # print(seller)
    # time.sleep(3)
    try:
        cateogory=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[3]/ul/li[1]/div[2]').text
    except:
        cateogory=""
    # time.sleep(3)

    # print(cateogory)
    try:
        size=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[3]/ul/li[2]/div[2]').text
    except:
        size=""
    # print(size)
    # time.sleep(3)

    if(cateogory =="Apartments" or cateogory=="Houses"):
        try:
            bedrooms=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[3]/ul/li[3]/div[2]').text
        # time.sleep(3)
        except:
            bedrooms=""

        # print(bedrooms)
        try:
            bathrooms=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[3]/ul/li[4]/div[2]').text
        # time.sleep(3)
        except:
            bathrooms=""
        # print(bathrooms)
    elif (cateogory == "Land" or cateogory=="Commercial Properties"):
        try:
            titletype=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[3]/ul/li[3]/div[2]').text
        # time.sleep(3)
        except:
            titletype=""

        # print(titletype)
        try:
            propertytype=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[3]/ul/li[4]/div[2]').text
        # time.sleep(3)
        except:
            propertytype=""
    
    try:
        sellersaysclick=driver.find_element_by_xpath("//button/span[contains(@class,'mw514')]").click()
        contact_no_2_CB=driver.find_element_by_xpath("//button/span[contains(@class,'mw512')]").click()
        # sellersays=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[4]/ul[2]/li/div/div[1]').text
    # print(sellersays)
        # sellersays=str(deEmojify(sellersays))
    except:
        pass
    try:
        sellersays=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[4]/ul[2]/li/div/div').text
        sellersays=str(deEmojify(sellersays))
    except:
        sellersays=""
    try:
        contact_no_2_one=re.search("01",sellersays).span()
        contact_no_2_one_two=contact_no_2_one[0]
        contact_no_2=sellersays[contact_no_2_one_two:(contact_no_2_one_two+11)]
    except:
        contact_no_2=""
    other_info=""
    facilities=""    
    
    try:
        driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[4]/ul[1]/li[2]').click()
        time.sleep(2)
        lengthpflist=driver.find_elements_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[4]/ul[2]/li/div/table/tbody/tr')
        for i in range(len(lengthpflist)):
            if 'Other Info' in lengthpflist[i].text:
                other_info=driver.find_element_by_xpath(f'//*[@id="__next"]/div[5]/div/div[1]/div[4]/ul[2]/li/div/table/tbody/tr[{i+1}]/td[2]/div').text
                # print(other_info)
            elif 'Facilities' in lengthpflist[i].text:
                # print(i)
                facilities=driver.find_element_by_xpath(f'//*[@id="__next"]/div[5]/div/div[1]/div[4]/ul[2]/li/div/table/tbody/tr[{i+1}]/td[2]/div').text
                # print(facilities)
    except:
        pass
    print(cateogory)
    if cateogory =="Apartments":
        
        # mydb.addapartments(title,listid,dateposted,price,region,subregions,seller,size,bedrooms,bathrooms,contact_no_1,sellersays,contact_no_2,other_info,facilities)
        uniqueid=getuniquekey()
        data=[[uniqueid,title,listid,dateposted,price,region,subregions,seller,size,bedrooms,bathrooms,sellersays,contact_no_2,other_info,facilities,imagecontactno,typeofprop]]
        value_range_body = {
        'majorDimension': 'ROWS',
        'values': data
                        }
        service.spreadsheets().values().append(
                spreadsheetId=sheetfile['spreadsheetId'],
                valueInputOption='RAW',
                range='Apartments!'+ cell_range_insert,
                body=value_range_body
        ).execute()
        print("added")
        
    elif cateogory =="Houses":
     
        uniqueid=getuniquekey()

        data=[[uniqueid,title,listid,dateposted,price,region,subregions,seller,size,bedrooms,bathrooms,sellersays,contact_no_2,other_info,facilities,imagecontactno,typeofprop]]
        value_range_body = {
        'majorDimension': 'ROWS',
        'values': data
                        }
        service.spreadsheets().values().append(
                spreadsheetId=sheetfile['spreadsheetId'],
                valueInputOption='RAW',
                range='Houses!'+ cell_range_insert,
                body=value_range_body
        ).execute()
        print("added")
    elif cateogory == "Land":
        
        uniqueid=getuniquekey()
        data=[[uniqueid,title,listid,dateposted,price,region,subregions,seller,size,titletype,propertytype,sellersays,contact_no_2,other_info,facilities,imagecontactno,typeofprop]]
        value_range_body = {
        'majorDimension': 'ROWS',
        'values': data}
        service.spreadsheets().values().append(
                spreadsheetId=sheetfile['spreadsheetId'],
                valueInputOption='RAW',
                range='Lands!'+ cell_range_insert,
                body=value_range_body
        ).execute()
        print("added")
        
    elif cateogory == "Commercial Properties":
       
        uniqueid=getuniquekey()
        data=[[uniqueid,title,listid,dateposted,price,region,subregions,seller,size,titletype,propertytype,sellersays,contact_no_2,other_info,facilities,imagecontactno,typeofprop]]
        value_range_body = {
        'majorDimension': 'ROWS',
        'values': data}
        service.spreadsheets().values().append(
                spreadsheetId=sheetfile['spreadsheetId'],
                valueInputOption='RAW',
                range='Commercial!'+ cell_range_insert,
                body=value_range_body
        ).execute()
        print("added")
    
def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)
    
def getuniquekey():
    return str(uuid.uuid4())[0:16]



def start():
    
    print("Choose the options \n1. Get all ads (For Sale) \n2. Get all ads (For Rent) \n3. Update Ads (For Sale) \n4. Update Ads (For Rent)")
    choice = int(input(""))
    sales_list=['https://www.mudah.my/list?type=sell&category=2020&adsby=false',
                'https://www.mudah.my/list?type=sell&category=2040&adsby=false',
                'https://www.mudah.my/list?type=sell&category=2060&adsby=false',
                'https://www.mudah.my/list?type=sell&category=2080&adsby=false']
    rent_list=['https://www.mudah.my/list?type=let&category=2020&adsby=false',
                'https://www.mudah.my/list?type=let&category=2040&adsby=false',
                'https://www.mudah.my/list?type=let&category=2060&adsby=false',
                'https://www.mudah.my/list?type=let&category=2080&adsby=false']

    driver.maximize_window()
    # links_list=[]
    # links=driver.find_elements_by_xpath("//div[contains(@class,'sc')]/a").get_attribute("href")
    # time.sleep(3)
    # driver.get(links+'#show')
    Next=True
    print("Process is started it may take a while ...")
    print("Getting links ...")
    pcone=0
    pctwo=0
    pcthree=0
    pcfour=0
    if choice ==1:
        mydb.droplinkssale()
        mydb.createlinkssale()
        for sales in range(len(sales_list)):
            driver.get(sales_list[sales])
            time.sleep(3)
            while Next:
                try:
                    links=driver.find_elements_by_xpath("//div[contains(@class,'sc')]/a")
                    time.sleep(2)
                    mylink=[]
                    # print(links)
                    if sales ==0:
                       print("Page "+str(pcone+1))
                    elif sales ==1:
                        print("Page "+str(pctwo+1))
                    elif sales ==2 :
                        print("Page "+str(pcthree+1))
                    elif sales ==3 :
                        print("Page "+str(pcfour+1))
                    for l in range(len(links)):
                        mylink.append(links[l].get_attribute('href'))
                    for onelink in range(len(set(mylink))):
                        driver.get(mylink[onelink])
                        print("Scraping "+str(onelink+1)+ " of "+str(len(set(mylink)))+" ads")
                        scrapethedata("sales")
                        
                        
                    # print("len after scrape"+str(len(links)))
                    # print("len set scrape"+str(len(mylink)))
                    mydb.addsaleurls(list(set(mylink))) #data added to database
                    
                    if sales ==0:
                        pcone+=1
                        driver.get(f'https://www.mudah.my/list?adsby=false&category=2020&o={pcone}&type=sell')
                    elif sales ==1:
                        pctwo+=1
                        driver.get(f'https://www.mudah.my/list?adsby=false&category=2040&o={pctwo}&type=sell')
                    elif sales == 2:
                        pcthree+=1
                        driver.get(f'https://www.mudah.my/list?adsby=false&category=2060&o={pcthree}&type=sell')
                    elif sales == 3:
                        pcfour+=1
                        driver.get(f'https://www.mudah.my/list?adsby=false&category=2060&o={pcfour}&type=sell')
                        
                        
                    # driver.find_element_by_xpath('//*[@id="pagination"]/ul/li[10]/a/div').click()
                   
                    time.sleep(4)
                except (NoSuchElementException,StaleElementReferenceException):
                    # w.complete()
                    # driver.close()             
                    Next=False
            # stored=mydb.return_urls_sale() #previous records
            # storedlist=[]
            # # print("before append "+str(len(stored)))
            # for x in stored:
            #     storedlist.append(list(x))
            # # print("len in db "+str(len(stored)))
            # storedlist=np.array(storedlist)
            # storedlist=list(storedlist.flatten())
            # # print("len in db flatten "+str(len(storedlist)))
            # for t in range(len(storedlist)):
            #     driver.get(storedlist[t]+'show')
            #     print("Scraping "+str(t+1)+"of"+str(len(storedlist))+"ads")
            #     time.sleep(2)
            #     scrapethedata("Sale")
    if choice ==2:
        
        mydb.droplinksrent()
        mydb.createlinksrent()
        for rent in range(len(rent_list)):
            driver.get(rent_list[rent])
            time.sleep(3)
            while Next:
                try:
                    links=driver.find_elements_by_xpath("//div[contains(@class,'sc')]/a")
                    time.sleep(2)
                    mylink=[]
                    if rent ==0:
                        print("Page "+str(pcone+1))
                    elif rent ==1:
                        print("Page "+str(pctwo+1))
                    elif rent ==2 :
                        print("Page "+str(pcthree+1))
                    elif rent ==3 :
                        print("Page "+str(pcfour+1))
                    
                        
                    
                    for l in links:
                        mylink.append(l.get_attribute('href'))
                    for onelink in range(len(set(mylink))):
                        driver.get(mylink[onelink])
                        print("Scraping "+str(onelink+1)+ " of "+str(len(set(mylink)))+" ads")
                        scrapethedata("rent")
                    # print("len after scrape"+str(len(links)))
                    # print("len set scrape"+str(len(mylink)))
                    mydb.addrenturls(list(set(mylink))) #data added to database
                    # driver.find_element_by_xpath('//*[@id="pagination"]/ul/li[10]/a/div').click()
                    if rent ==0:
                        pcone+=1
                        driver.get(f'https://www.mudah.my/list?adsby=false&category=2020&o={pcone}&type=let')
                    elif rent ==1:
                        pctwo+=1
                        driver.get(f'https://www.mudah.my/list?adsby=false&category=2040&o={pctwo}&type=let')
                    elif rent == 2:
                        pcthree+=1
                        driver.get(f'https://www.mudah.my/list?adsby=false&category=2060&o={pcthree}&type=let')
                    elif rent == 3:
                        pcfour+=1
                        driver.get(f'https://www.mudah.my/list?adsby=false&category=2060&o={pcfour}&type=let')
                        
                    time.sleep(4)
                except (NoSuchElementException,StaleElementReferenceException):
                    # w.complete()
                    # driver.close()             
                    Next=False
            # stored=mydb.return_urls_rent() #previous records
            # storedlist=[]
            # # print("before append "+str(len(stored)))
        
            # for x in stored:
            #     storedlist.append(list(x))
            # # print("len in db "+str(len(stored)))
            # storedlist=np.array(storedlist)
            # storedlist=list(storedlist.flatten())
            # # print("len in db flatten "+str(len(storedlist)))
            # for t in range(len(storedlist)):
            #     driver.get(storedlist[t]+'show')
            #     print("Scraping "+str(t+1)+"of"+str(len(storedlist))+"ads")
            #     time.sleep(2)
            #     scrapethedata("Rent")

    if choice ==3:
        print("Checking for new ads")
        Next=True
        pc=0
        for sales in range(len(sales_list)):
            driver.get(sales_list[sales])
            if(sales == 0):
                ti=2020
            if sales == 1:
                ti=2040
            if sales == 2:
                ti=2060
            if sales ==3 :
                ti=2080
            
            while Next:
                try:
                    pc+=1
                    links=driver.find_elements_by_xpath("//div[contains(@class,'sc')]/a")
                    mylink=[]
                    print("Page "+str(pc))
                    time.sleep(4)
                    for l in links:
                        mylink.append(l.get_attribute('href'))
                    mylink=list(set(mylink))
                    
                    stored=mydb.return_urls_sale() #previous records
                    newlist=list(np.setdiff1d(mylink,stored)) #scrape only new
                    # print(len(newlist))
                    for x in range(len(newlist)):
                        driver.get(newlist[x]+'#show')
                        time.sleep(2)
                        print("Scraping "+str(x+1)+' of '+str(len(newlist))+" ads")
                        time.sleep(2)
                        scrapethedata("Sale")
                    mydb.addsaleurls(mylink) #data added to database
                    time.sleep(2)
                    driver.get(f'https://www.mudah.my/list?adsby=false&category={ti}&o={pc}&type=sell')
                    time.sleep(4)
                    driver.find_element_by_xpath('//*[@id="pagination"]/ul/li[10]/a/div').click()
                except NoSuchElementException:
                        # w.complete()
                        # driver.close()
                    Next=False
    if choice ==4:
        print("Checking for new ads")
        Next=True
        pc=0
        for sales in range(len(rent_list)):
            driver.get(rent_list[sales])
            if(sales == 0):
                ti=2020
            if sales == 1:
                ti=2040
            if sales == 2:
                ti=2060
            if sales ==3 :
                ti=2080
            
            while Next:
                try:
                    pc+=1
                    links=driver.find_elements_by_xpath("//div[contains(@class,'sc')]/a")
                    mylink=[]
                    print("Page "+str(pc))
                    time.sleep(4)
                    for l in links:
                        mylink.append(l.get_attribute('href'))
                    mylink=list(set(mylink))
                    stored=mydb.return_urls_rent() #previous records
                    newlist=list(np.setdiff1d(mylink,stored)) #scrape only new
                    # print(len(newlist))
                    for x in range(len(newlist)):
                        driver.get(newlist[x]+'#show')
                        time.sleep(2)
                        print("Scraping "+str(x+1)+' of '+str(len(newlist))+" ads")
                        time.sleep(2)
                        scrapethedata("Rent")
                    mydb.addrenturls(mylink) #data added to database
                    time.sleep(2)
                    driver.get(f'https://www.mudah.my/list?adsby=false&category={ti}&o={pc}&type=let')
                    time.sleep(4)
                    driver.find_element_by_xpath('//*[@id="pagination"]/ul/li[10]/a/div').click()
                except NoSuchElementException:
                        # w.complete()
                        # driver.close()
                    Next=False
        
    
   

        
        
                
                

                

                
            
        
    
    #     for i in range(len(stored)):
    #         driver.get(stored[i]+'#show')
    #         print("Scraping "+str(i+1)+' of '+str(len(stored))+" ads")
    #         time.sleep(2)
    #         scrapethedata()
    #     w.complete()
    #     driver.close()
    # else:
    #     newlist=list(np.setdiff1d(mylink,stored))
    #     for x in range(len(newlist)):
    #         driver.get(newlist[x]+'#show')
    #         time.sleep(2)
    #         print("Scraping "+str(x+1)+' of '+str(len(newlist))+" ads")
    #         time.sleep(2)
    #         scrapethedata()
    #     w.complete()
    #     mydb.addurls(mylink)
    #     driver.close()
            

       
            
start()

# while True:   
#     print(pc)
#     driver.get(f'https://www.mudah.my/list?adsby=false&category=2001&o={pc}&type=sell')
#     time.sleep(4)
#      driver.find_element_by_xpath('//*[@id="pagination"]/ul/li[10]/a/div').click()     
#     pc+=1    
#     print(pc)



# start()
# driver.maximize_window()
# driver.get('https://www.mudah.my/Bukit+Indah+3+Storey+High+End+Shoplot-85988589.htm#show')
# scrapethedata()
# w.complete()
