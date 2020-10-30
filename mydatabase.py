import sqlite3
class DATABASE:
    def __init__(self):
        self.mydb=sqlite3.connect("mudah.db")
        
    
        
        self.mycursor = self.mydb.cursor()
        # self.mycursor.execute("CREATE DATABASE IF NOT EXISTS mudahproperty")
        # self.mycursor.execute("USE mudahproperty")
        # self.mycursor.execute("CREATE TABLE IF NOT EXISTS apartments (id INT AUTO_INCREMENT PRIMARY KEY,title varchar(255), list_id VARCHAR(255),dateposted VARCHAR(255),price VARCHAR(255),region varchar(225),subregion varchar(225),seller_name varchar(225),size varchar(225),bedrooms varchar(225),bathrooms varchar(225),contact_no_1 varchar(225),seller_says varchar(225),contact_no_2 varchar(225),other_info varchar(225),facilities varchar(225))")
        # self.mycursor.execute("CREATE TABLE IF NOT EXISTS houses (id INT AUTO_INCREMENT PRIMARY KEY,title varchar(255), list_id VARCHAR(255),dateposted VARCHAR(255),price VARCHAR(255),region varchar(225),subregion varchar(225),seller_name varchar(225),size varchar(225),bedrooms varchar(225),bathrooms varchar(225),contact_no_1 varchar(225),seller_says varchar(225),contact_no_2 varchar(225),other_info varchar(225),facilities varchar(225))")
        # self.mycursor.execute("CREATE TABLE IF NOT EXISTS lands (id INT AUTO_INCREMENT PRIMARY KEY,title varchar(255), list_id VARCHAR(255),dateposted VARCHAR(255),price VARCHAR(255),region varchar(225),subregion varchar(225),seller_name varchar(225),size varchar(225),title_type varchar(225),property_type varchar(225),contact_no_1 varchar(225),seller_says varchar(225),contact_no_2 varchar(225),other_info varchar(225),facilities varchar(225))")
        # self.mycursor.execute("CREATE TABLE IF NOT EXISTS Commercial_properties (id INT AUTO_INCREMENT PRIMARY KEY,title varchar(255), list_id VARCHAR(255),dateposted VARCHAR(255),price VARCHAR(255),region varchar(225),subregion varchar(225),seller_name varchar(225),size varchar(225),title_type varchar(225),property_type varchar(225),contact_no_1 varchar(225),seller_says varchar(225),contact_no_2 varchar(225),other_info varchar(225),facilities varchar(225))")
        self.mycursor.execute("create table if not exists rentlinks(url TEXT,dummy TEXT")
        self.mycursor.execute("create table if not exists propertylinks(url TEXT,dummy TEXT")


    def addhouses(self,first,second,third,fourth,fith,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen):
      
        sql = "INSERT INTO apartments (title,list_id,dateposted,price,region,subregion,seller_name,size,bedrooms,bathrooms,contact_no_1,seller_says,contact_no_2,other_info,facilities) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (first,second,third,fourth,fith,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
    def addhouse2s(self,first,second,third,fourth,fith,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen):
      
        sql = "INSERT INTO houses (title,list_id,dateposted,price,region,subregion,seller_name,size,bedrooms,bathrooms,contact_no_1,seller_says,contact_no_2,other_info,facilities) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (first,second,third,fourth,fith,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
    def addlands(self,first,second,third,fourth,fith,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen):
      
        sql = "INSERT INTO lands (title,list_id,dateposted,price,region,subregion,seller_name,size,title_type,property_type,contact_no_1,seller_says,contact_no_2,other_info,facilities) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (first,second,third,fourth,fith,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
    def addcommercial(self,first,second,third,fourth,fith,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen):
        sql = "INSERT INTO Commercial_properties (title,list_id,dateposted,price,region,subregion,seller_name,size,title_type,property_type,contact_no_1,seller_says,contact_no_2,other_info,facilities) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (first,second,third,fourth,fith,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
    def addrenturls(self,url_list):
        # print("Len when rec in db"+str(len(url_list)))
        data=[]
        for i in range(len(url_list)):
            datad=(url_list[i],'1')
            data.append(datad)
        # print("Len when rec after db"+str(len(data)))
        sql="INSERT INTO rentlinks (url,dummy) VALUES(?,?)"
        self.mycursor.executemany(sql,data)
        self.mydb.commit()
    def return_urls_sale(self):
        self.mycursor.execute("SELECT url FROM salelinks")
        myresult = self.mycursor.fetchall()
        return myresult
    def return_urls_rent(self):
        self.mycursor.execute("SELECT url FROM rentlinks")
        myresult = self.mycursor.fetchall()
        return myresult
    def droplinksrent(self):
        self.mycursor.execute("DROP TABLE IF EXISTS salelinks")
    def droplinkssale(self):
        
        self.mycursor.execute("DROP TABLE IF EXISTS rentlinks")
        
    def createlinksrent(self):
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS rentlinks (url TEXT,dummy TEXT)")
    def createlinkssale(self):
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS salelinks (url TEXT,dummy TEXT)")
    def addsaleurls(self,url_list):
        data=[]
        for i in range(len(url_list)):
            datad=(url_list[i],'1')
            data.append(datad)
        # print("Len when rec after db"+str(len(data)))
        sql="INSERT INTO salelinks (url,dummy) VALUES(?,?)"
        self.mycursor.executemany(sql,data)
        self.mydb.commit()
        

    
       


        
        









