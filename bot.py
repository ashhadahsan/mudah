from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()


from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException,ElementNotInteractableException
import pandas as pd

import datetime
import os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
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
firefox=Options()
firefox.headless=False



contact_no=""
other_info=""
facilities=""
sellersays=""
import numpy as np


# desired_capabilities = DesiredCapabilities.CHROME.copy()
# desired_capabilities['acceptInsecureCerts'] = True
import uuid
import xlsxwriter
from PIL import Image
driver=webdriver.Firefox(options=firefox,executable_path='geckodriver')#FOR LINUX
import re

from writetoexcel import writer
w=writer()
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
    global contact_no_1
    global facilities
    global areacode
    global number
    global sellersays
    global true
    global null
    global false
    getnumber =str(driver.find_element_by_xpath('//*[@id="__NEXT_DATA__"]').get_attribute('innerHTML'))
    try:
        # time.sleep(3)
        # contactclick=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[2]/div[1]/div[4]/button[2]/span/span').click()
        # areacode=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[2]/div[1]/div[4]/button[2]/span/span').text
        # number=driver.find_element_by_id("phone-image").text
        # print(number)
        imagecontactnospan=re.search("phone",getnumber).span()
        startlimit=imagecontactnospan[1]+3
        imagecontactno=getnumber[startlimit:(startlimit+10)]
        findd=r'","price":'
        if  findd in imagecontactno:
           imagecontactno=""
        #    print("khali")
        # print(imagecontactno)
        
        
        
        
        # driver.execute_script("window.testSpread = new GcSpread.Sheets.Spread(arguments[0]);", numberelement)
        # driver.execute_script("window.testSpread.getActiveSheet().setValue(0,0,'1');")
        # number = driver.execute_script("return window.testSpread.getActiveSheet().getValue(0,0);")
        


        
    #     areacodelink=driver.find_element_by_xpath('//*[@id="number-space"]/div[1]/img').get_attribute('src')
    #     response = requests.get(areacodelink, stream=True)
    #     with open(f'temp/img{firstimage}.png', 'wb') as out_file:
    #         shutil.copyfileobj(response.raw, out_file)
    #     img = io.imread(f'temp/img{firstimage}.png')
    #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #     gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #     cv2.imwrite(f'temp/img{firstimage}.png', gray)
    #     firstimage+=2
    #     areacodelink=driver.find_element_by_xpath('//*[@id="number-space"]/div[2]/img').get_attribute('src')
    #     response = requests.get(areacodelink, stream=True)
    #     with open(f'temp/img{secondimage}.png', 'wb') as out_file:
    #         shutil.copyfileobj(response.raw, out_file)
    #     img = io.imread(f'temp/img{secondimage}.png')
    #     # print("image done")
    #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #     gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #     cv2.imwrite(f'temp/img{secondimage}.png', gray)
    #     secondimage+=2
    except NoSuchElementException:
        pass

    # time.sleep(3)
    try:
        title=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[1]/div[1]/h1').text
    except:
        title=""
    # print(title)
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
            splitby=h.split(" ")[-1]
            dateposted=previosudate+" "+a
            
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
        sellersaysclick=driver.find_element_by_xpath('(//*[@id="__next"]/div[5]/div/div[1]/div[4]/ul[2]/li/div/div/button[1]/span[1])[2]').click()
        contact_no_2_CB=driver.find_element_by_xpath('(//button/span[@class="mw218 mw216"])[1]').click()
        sellersays=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[4]/ul[2]/li/div/div[1]').text
    # print(sellersays)
        sellersays=str(deEmojify(sellersays))
    except:
        sellersays=driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div/div[1]/div[4]/ul[2]/li/div/div[1]').text
        sellersays=str(deEmojify(sellersays))
    try:
        contact_no_2_one=re.search("01",sellersays).span()
        contact_no_2_one_two=contact_no_2_one[0]
        contact_no_2=sellersays[contact_no_2_one_two:(contact_no_2_one_two+11)]
    except:
        contact_no_2=""
        
    # try:
    #     # time.sleep(3)
    #     contact_no_2=re.findall(r'\d{10}',sellersays)
    #     contact_no_2=contact_no_2[0]
    # except:
    #     pass
    # try:
    #     # time.sleep(3)
    #     contact_no_2=re.findall(r'\d{11}',sellersays)
    #     contact_no_2=contact_no_2[0]
    # except:
    #     pass

    # try:
    #     # time.sleep(3)
    #     contact_no_2=re.findall(r'\d{3}-\d{7}',sellersays)
    #     contact_no_2=contact_no_2[0]
    # except:
    #     pass
    # try:
    #     # time.sleep(3)

    #     contact_no_2=re.findall(r'\d{3}-\d{3}\s\d{4}',sellersays)
    #     contact_no_2=contact_no_2[0]
    # except:
    #     contact_no_2=""
    print(contact_no_2)
    # time.sleep(3)
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
    if cateogory =="Apartments":
        global countA
        countA+=1
        # mydb.addapartments(title,listid,dateposted,price,region,subregions,seller,size,bedrooms,bathrooms,contact_no_1,sellersays,contact_no_2,other_info,facilities)
        uniqueid=getuniquekey()
        data=(uniqueid,title,listid,dateposted,price,region,subregions,seller,size,bedrooms,bathrooms,sellersays,contact_no_2,other_info,facilities,imagecontactno,typeofprop)
        w.addtoapart(countA,data)
    elif cateogory =="Houses":
        global countB
        countB+=1
        
        # mydb.addhouses(title,listid,dateposted,price,region,subregions,seller,size,bedrooms,bathrooms,contact_no_1,sellersays,contact_no_2,other_info,facilities)
        uniqueid=getuniquekey()

        data=(uniqueid,title,listid,dateposted,price,region,subregions,seller,size,bedrooms,bathrooms,sellersays,contact_no_2,other_info,facilities,imagecontactno,typeofprop)
        w.addtohouse(countB,data)

    elif cateogory == "Land":
        global countC
        countC+=1
        # mydb.addlands(title,listid,dateposted,price,region,subregions,seller,size,titletype,propertytype,contact_no_1,sellersays,contact_no_2,other_info,facilities)
        uniqueid=getuniquekey()
        data=(uniqueid,title,listid,dateposted,price,region,subregions,seller,size,titletype,propertytype,sellersays,contact_no_2,other_info,facilities,imagecontactno,typeofprop)
        w.addtoland(countC,data)
    elif cateogory == "Commercial Properties":
        global countD
        countD+=1
        # mydb.addcommercial(title,listid,dateposted,price,region,subregions,seller,size,titletype,propertytype,contact_no_1,sellersays,contact_no_2,other_info,facilities)
        uniqueid=getuniquekey()
        data=(uniqueid,title,listid,dateposted,price,region,subregions,seller,size,titletype,propertytype,sellersays,contact_no_2,other_info,facilities,imagecontactno,typeofprop)
        w.addtocomm(countD,data)

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
    pc=0
    if choice ==1:
        mydb.droplinkssale()
        mydb.createlinkssale()
        for sales in sales_list:
            driver.get(sales)
            time.sleep(3)
            while Next:
                try:
                    links=driver.find_elements_by_xpath("//div[contains(@class,'sc')]/a")
                    time.sleep(2)
                    mylink=[]
                    print("Page "+str(pc+1))
                    for l in links:
                        mylink.append(l.get_attribute('href'))
                    # print("len after scrape"+str(len(links)))
                    # print("len set scrape"+str(len(mylink)))
                    mydb.addsaleurls(list(set(mylink))) #data added to database
                    driver.find_element_by_xpath('//*[@id="pagination"]/ul/li[10]/a/div').click()
                    pc+=1
                    time.sleep(4)
                except (NoSuchElementException,StaleElementReferenceException):
                    # w.complete()
                    # driver.close()             
                    Next=False
            stored=mydb.return_urls_sale() #previous records
            storedlist=[]
            # print("before append "+str(len(stored)))
        
            for x in stored:
                storedlist.append(list(x))
            # print("len in db "+str(len(stored)))
            storedlist=np.array(storedlist)
            storedlist=list(storedlist.flatten())
            # print("len in db flatten "+str(len(storedlist)))
            for t in range(len(storedlist)):
                driver.get(storedlist[t]+'show')
                print("Scraping "+str(t+1)+"of"+str(len(storedlist))+"ads")
                time.sleep(2)
                scrapethedata("Sale")
    if choice ==2:
        
        mydb.droplinksrent()
        mydb.createlinksrent()
        for rent in rent_list:
            driver.get(rent)
            time.sleep(3)
            while Next:
                try:
                    links=driver.find_elements_by_xpath("//div[contains(@class,'sc')]/a")
                    time.sleep(2)
                    mylink=[]
                    print("Page "+str(pc+1))
                    for l in links:
                        mylink.append(l.get_attribute('href'))
                    # print("len after scrape"+str(len(links)))
                    # print("len set scrape"+str(len(mylink)))
                    mydb.addrenturls(list(set(mylink))) #data added to database
                    driver.find_element_by_xpath('//*[@id="pagination"]/ul/li[10]/a/div').click()
                    pc+=1
                    time.sleep(4)
                except (NoSuchElementException,StaleElementReferenceException):
                    # w.complete()
                    # driver.close()             
                    Next=False
            stored=mydb.return_urls_rent() #previous records
            storedlist=[]
            # print("before append "+str(len(stored)))
        
            for x in stored:
                storedlist.append(list(x))
            # print("len in db "+str(len(stored)))
            storedlist=np.array(storedlist)
            storedlist=list(storedlist.flatten())
            # print("len in db flatten "+str(len(storedlist)))
            for t in range(len(storedlist)):
                driver.get(storedlist[t]+'show')
                print("Scraping "+str(t+1)+"of"+str(len(storedlist))+"ads")
                time.sleep(2)
                scrapethedata("Rent")

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
        
    
    w.complete()

        
        
                
                

                

                
            
        
    
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
