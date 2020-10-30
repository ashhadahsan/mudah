import xlsxwriter
import os
import datetime
class writer:
    def __init__(self):
        
        self.workbook=xlsxwriter.Workbook("Results.xlsx")
        self.bold = self.workbook.add_format({'bold': True})
        self.apartmentsheet=self.workbook.add_worksheet("Apartments")
        cell_format = self.workbook.add_format()
        cell_format.set_text_wrap()
        self.apartmentsheet.set_column('A:O',30)
        self.apartmentsheet.set_column('P:R',50)
        
        self.apartmentsheet.write('A1','ID',self.bold)
        self.apartmentsheet.write('B1','Title',self.bold)
        self.apartmentsheet.write('C1','List ID',self.bold)
        self.apartmentsheet.write('D1','Date Posted',self.bold)
        
        self.apartmentsheet.write('E1','Price',self.bold)
        self.apartmentsheet.write('F1','Region',self.bold)
        self.apartmentsheet.write('G1','Sub Region',self.bold)
        self.apartmentsheet.write('H1','Seller Name',self.bold)
        self.apartmentsheet.write('I1','Size',self.bold)
        self.apartmentsheet.write('J1','Bedrooms',self.bold)
        self.apartmentsheet.write('K1','Bathrooms',self.bold)
        self.apartmentsheet.write('L1','Seller Says',self.bold)
        self.apartmentsheet.write('M1','Other Contact',self.bold)
        self.apartmentsheet.write('N1','Other Info',self.bold)
        self.apartmentsheet.write('O1','Facilities',self.bold)
        self.apartmentsheet.write('P1','Contact No',self.bold)
        self.apartmentsheet.write('Q1','Type',self.bold)


        
        self.housesheet=self.workbook.add_worksheet('Houses')
        # cell_format = self.workbook.add_format()
        # cell_format.set_text_wrap()
        self.housesheet.set_column('A:O',30)
        self.housesheet.set_column('P:R',50)
        
        self.housesheet.write('A1','ID',self.bold)
        self.housesheet.write('B1','Title',self.bold)
        self.housesheet.write('C1','List ID',self.bold)
        self.housesheet.write('D1','Date Posted',self.bold)
        self.housesheet.write('E1','Price',self.bold)
        self.housesheet.write('F1','Region',self.bold)
        self.housesheet.write('G1','Sub Region',self.bold)
        self.housesheet.write('H1','Seller Name',self.bold)
        self.housesheet.write('I1','Size',self.bold)
        self.housesheet.write('J1','Bedrooms',self.bold)
        self.housesheet.write('K1','Bathrooms',self.bold)
        self.housesheet.write('L1','Seller Says',self.bold)
        self.housesheet.write('M1','Other Contact',self.bold)
        self.housesheet.write('N1','Other Info',self.bold)
        self.housesheet.write('O1','Facilities',self.bold)
        self.housesheet.write('P1','Contact No',self.bold)
        self.housesheet.write('Q1','Type',self.bold)
        
        self.landsheet=self.workbook.add_worksheet('Lands')
        # self.landsheet.set_column('A:R',30)
        self.landsheet.set_column('A:O',30)
        self.landsheet.set_column('P:R',50)
        self.landsheet.write('A1','ID',self.bold)
        self.landsheet.write('B1','Title',self.bold)
        self.landsheet.write('C1','List ID',self.bold)
        self.landsheet.write('D1','Date Posted',self.bold)
        self.landsheet.write('E1','Price',self.bold)
        self.landsheet.write('F1','Region',self.bold)
        self.landsheet.write('G1','Sub Region',self.bold)
        self.landsheet.write('H1','Seller Name',self.bold)
        self.landsheet.write('I1','Size',self.bold)
        self.landsheet.write('J1','Title Type',self.bold)
        self.landsheet.write('K1','Property Type',self.bold)
        self.landsheet.write('L1','Seller Says',self.bold)
        self.landsheet.write('M1','Other Contact',self.bold)
        self.landsheet.write('N1','Other Info',self.bold)
        self.landsheet.write('O1','Facilities',self.bold)
        self.landsheet.write('P1','Contact Number',self.bold)
        self.landsheet.write('Q1','Type',self.bold)



       
        self.compsheet=self.workbook.add_worksheet('Commercial Properties')
        # self.compsheet.set_column('A:R',30)
        self.compsheet.set_column('A:O',30)
        self.compsheet.set_column('P:R',50)
        self.compsheet.write('A1','ID',self.bold)
        self.compsheet.write('B1','Title',self.bold)
        self.compsheet.write('C1','List ID',self.bold)
        self.compsheet.write('D1','Date Posted',self.bold)
        self.compsheet.write('E1','Price',self.bold)
        self.compsheet.write('F1','Region',self.bold)
        self.compsheet.write('G1','Sub Region',self.bold)
        self.compsheet.write('H1','Seller Name',self.bold)
        self.compsheet.write('I1','Size',self.bold)
        self.compsheet.write('J1','Title Type',self.bold)
        self.compsheet.write('K1','Property Type',self.bold)
        self.compsheet.write('L1','Seller Says',self.bold)
        self.compsheet.write('M1','Other Contact',self.bold)
        self.compsheet.write('N1','Other Info',self.bold)
        self.compsheet.write('O1','Facilities',self.bold)
        self.compsheet.write('P1','Contact Number',self.bold)
        self.compsheet.write('Q1','Type',self.bold)

        
    def addtoapart(self,row,data):
        self.apartmentsheet.write_row(f'A{row}',data)
        # if (os.path.isfile(f'temp/img{one}.png')):
        #     self.apartmentsheet.insert_image(f'Q{row}',f'temp/img{one}.png',{'x_offset': 15, 'y_offset': 10})
        # else:
        #     self.apartmentsheet.write(f'Q{row}',' ')
        # if (os.path.isfile(f'temp/img{two}.png')):
        #     self.apartmentsheet.insert_image(f'R{row}',f'temp/img{two}.png',{'x_offset': 15, 'y_offset': 10})
        # else:
        #     self.apartmentsheet.write(f'R{row}',' ')
    def addtohouse(self,row,data):
        self.housesheet.write_row(f'A{row}',data)
        # if (os.path.isfile(f'temp/img{one}.png')):
        #     self.housesheet.insert_image(f'Q{row}',f'temp/img{one}.png',{'x_offset': 15, 'y_offset': 10})
        # else:
        #     self.housesheet.write(f'Q{row}',' ')
        # if (os.path.isfile(f'temp/img{two}.png')):
        #     self.housesheet.insert_image(f'R{row}',f'temp/img{two}.png',{'x_offset': 15, 'y_offset': 10})
        # else:
        #     self.housesheet.write(f'R{row}',' ')
        
    def addtoland(self,row,data):
        
        self.landsheet.write_row(f'A{row}',data)
        # if (os.path.isfile(f'temp/img{one}.png')):
        #     self.landsheet.insert_image(f'Q{row}',f'temp/img{one}.png',{'x_offset': 15, 'y_offset': 10})
        # else:
        #     self.landsheet.write(f'Q{row}',' ')
        # if (os.path.isfile(f'temp/img{two}.png')):
        #     self.landsheet.insert_image(f'R{row}',f'temp/img{two}.png',{'x_offset': 15, 'y_offset': 10})
        # else:
        #     self.landsheet.write(f'R{row}',' ')
    def addtocomm(self,row,data):
        self.compsheet.write_row(f'A{row}',data)
        # if (os.path.isfile(f'temp/img{one}.png')):
        #     self.compsheet.insert_image(f'Q{row}',f'temp/img{one}.png',{'x_offset': 15, 'y_offset': 10})
        # else:
        #     self.compsheet.write(f'Q{row}',' ')
        # if (os.path.isfile(f'temp/img{two}.png')):
        #     self.compsheet.insert_image(f'R{row}',f'temp/img{two}.png',{'x_offset': 15, 'y_offset': 10})
        # else:
        #     self.compsheet.write(f'R{row}',' ')
       
    def complete(self):
        self.workbook.close()
        
       

        

