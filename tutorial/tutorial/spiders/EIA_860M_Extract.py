import pandas as pd
import os
import psycopg2
import uuid
from multiprocessing import Process
import time

class EIA_860M_Extract(object):

    def __init__(self, file_path):
    
        self.file_path = file_path
        
        self.data = []

    def Get_EIA_860M_Data(self):
    
        excel_workbook = pd.ExcelFile(self.file_path)
        
        '''excel_sheet = excel_workbook.parse(sheet_name=1)'''
        
        sheet_titles = excel_workbook.sheet_names
        
        sheet_count = len(sheet_titles)
        
        for i in range(sheet_count):
        
            if (sheet_titles[i] == 'Planned'):
            
                excel_sheet = excel_workbook.parse(sheet_name=i)
        
                '''data.append(excel_sheet['Unnamed: 2'][2])'''
                
                '''print(data[2])'''
                
                print(excel_sheet.columns)
                
                '''record_number = len(excel_sheet.axes[0])'''
                
                record_number = len(excel_sheet.index)
                
                for i in range(record_number - 2):
                
                    self.data.append([str(excel_sheet.iloc[i + 1]['Unnamed: 2']), str(excel_sheet.iloc[i + 1]['Unnamed: 3']), str(excel_sheet.iloc[i + 1]['Unnamed: 8']), str(excel_sheet.iloc[i + 1]['Unnamed: 16']), str(excel_sheet.iloc[i + 1]['Unnamed: 18']), str(excel_sheet.iloc[i + 1]['Unnamed: 19']), str(excel_sheet.iloc[i + 1]['Unnamed: 17']), str(excel_sheet.iloc[i + 1]['Unnamed: 5']), str(excel_sheet.iloc[i + 1]['Unnamed: 14']), str(excel_sheet.iloc[i + 1]['Unnamed: 15']), str(excel_sheet.iloc[i + 1]['Unnamed: 6']), str(excel_sheet.iloc[i + 1]['Unnamed: 11'])])
                    
                '''print (data)'''
                
                sql_string = """DECLARE PLANTIDNUM INTEGER; MWCAPACITYNUM INTEGER; LATITUDENUM INTEGER; LONGITUDENUM INTEGER; MONTHNUM INTEGER; YEARNUM INTEGER; BEGIN PLANTIDNUM := CAST({} AS INTEGER); MWCAPACITYNUM := CAST({} AS REAL); LATITUDENUM := CAST({} AS DOUBLE PRECISION); LONGITUDENUM := CAST({} AS DOUBLE PRECISION); MONTHNUM := CAST({} AS INTEGER); YEARNUM := CAST({} AS INTEGER); INSERT INTO public.eiaplantdata values({}, PLANTIDNUM, {}, {}, MWCAPACITYNUM, LATITUDENUM, LONGITUDENUM, {}, {}, MONTHNUM, YEARNUM, {}, {}); END; LANGUAGE plpgsql;"""
                
                sql_string = sql_string.format(self.data[0][0], self.data[0][2], self.data[0][4], self.data[0][5], self.data[0][8], self.data[0][9], uuid.uuid4().hex, self.data[0][1], self.data[0][3], self.data[0][6], self.data[0][7], self.data[0][10], self.data[0][11])
                
                print ("sql_string:\n", sql_string)
                
                conn = None
                
                conn = psycopg2.connect(database="renewabletracking")
                
                cur = conn.cursor()
                
                for i in range(record_number - 2):
                
                    cur.callproc("eiaparameters", [str(self.data[i][0]), str(self.data[i][2]), str(self.data[i][4]), str(self.data[i][5]), str(self.data[i][8]), str(self.data[i][9]), str(uuid.uuid4().hex), str(self.data[i][1]), str(self.data[i][3]), str(self.data[i][6]), str(self.data[i][7]), str(self.data[i][10]), str(self.data[i][11]),])
                    
                conn.commit()
                
                cur.close()
                
                if conn is not None:
                
                    conn.close()
        
        '''print("Plant ID: " + str(excel_sheet.iloc[8]['Unnamed: 2']) + "\nPlant Name: " + str(excel_sheet.iloc[8]['Unnamed: 3']) + "\nMW Capacity: " + str(excel_sheet.iloc[8]['Unnamed: 8']) + "\nStatus: " + str(excel_sheet.iloc[8]['Unnamed: 16']) + "\nLatitude: " + str(excel_sheet.iloc[8]['Unnamed: 18']) + "\nLongitude: " + str(excel_sheet.iloc[8]['Unnamed: 19']))'''
        
'''I added this part of the code to stop the program if it gets too long.'''
        
def do_actions():

    Obj = EIA_860M_Extract("/Users/andrewjackson/Personal Projects/VirtualEnvelope/scrapy_env_3.6/tutorial/EIA-860M_february_generator2020.xlsx")
            
    Obj.Get_EIA_860M_Data()
    
action_process = Process(target=do_actions)

action_process.start()

action_process.join(timeout=120)

action_process.terminate()

