import re
from functions import *

import numpy as np
import time
def Brisbane(epoch):
    a = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(epoch))
    return(a)
def createCSVfile(inputlist , name):
    with open( name , 'w') as f:
        for i in inputlist:
            k = 0
            for item in i:
                f.write(str(item) + ',')
                k = k+1
            f.write('\n')
        return(f)
def inputCSVfile(csvfile):
    list1= []
    with open(csvfile, 'r') as f:
        for i in f:
            j = i.split(',')         
            le = len(j)
            j[le - 1] = (j[le- 1]).strip()
            list1.append(j)
        return(list1)
totalentries = 0
HFS = np.array(inputCSVfile('Routes.csv'))
#Working_DR  = 'Z:/GTFS/'
Working_DR  = 'Y:/Data/GTFS/'
fiction = ['-NA-','-NA-','-NA-','-NA-']
speed_file = inputCSVfile(Working_DR+ 'VE combined.csv')
speed_file = np.array(speed_file)
FO = []
trips = inputCSVfile('trips.csv')
trips = np.array(trips)
a_boolean1 = np.any(np.isin(speed_file,HFS),axis=1)
B = speed_file[a_boolean1,:]

createCSVfile( B, 'B2.csv')
def Processing(TripUpdate, Working_DR, fiction, stopid_matrix , speed_file, trips):
    for indexo, ki in enumerate(TripUpdate[10:]):
        print(indexo)
        #print(ki[0])
        A = inputCSVfile(Working_DR + 'Trip Update/' +str(ki[0]))
        B = ''.join(str(e) for e in A)
        FO = []
        for matchedtext in re.findall(r'(?<=trip {).*?(?<=timestamp: \d\d\d\d\d\d\d\d\d\d)', B):
            #print(matchedtext)
            #matchedtext = ''.join(str(e) for e in matchedtext)
            tripid = re.findall(r'(?<=trip_id: ").*?(?=")', matchedtext)
            Start_time = re.findall(r'(?<=start_time: ").*?(?=")', matchedtext)
            Start_date = re.findall(r'(?<=start_date: ").*?(?=")', matchedtext)
            schedule_relationship = re.findall(r"(?<=schedule_relationship:).*?(?=')", matchedtext)
            if len(schedule_relationship)!=0:
                sr = schedule_relationship[0]
            else:
                sr = '-NA-'
            #print(schedule_relationship, 'schedule_relationship.................')
            route_id = re.findall(r'(?<=route_id: ").*?(?=")', matchedtext)
            Vehid = re.findall(r"(?<='id: ).*?(?=')", matchedtext)
            timestamp = matchedtext[-10:]
            for stopseq in re.findall(r'(?<=stop_time_update {).*?(?<=\d")',matchedtext ):
                #print(stopseq)
                try:
                    Stop_Seq = re.findall(r"(?<=stop_sequence: ).*?(?=')", stopseq)
                    #print(Stop_Seq)
                    arrival = re.findall(r"(?<=arrival {').*?(?=})", stopseq)
                    arrival = ''.join(str(e) for e in arrival)
                    Arrival_time = re.findall(r"(?<='time: ).*?(?=')", arrival)
                    #print(Arrival_time, 'Arrival_time....................................')
                except:
                    Stop_Seq = ''
                try:
                    att = Arrival_time[0]
                    #print(att, 'attttttttttttt')
                    at = Brisbane(float(Arrival_time[0]))
                    #print(at)
                except:
                    att = ''
                    at = ''
                Arrival_Uncertainity = re.findall(r"(?<=uncertainty: ).*?(?=')", arrival)
                try:
                    au = Arrival_Uncertainity[0]
                except:
                    au = ''
                Arrival_Delay = re.findall(r"(?<=delay: ).*?(?=')", arrival)
                try:
                    ad = Arrival_Delay[0]
                except:
                    ad = ''
                departure = re.findall(r"(?<=departure {').*?(?=})", stopseq)
                departure = ''.join(str(e) for e in departure)
                departure_time = re.findall(r"(?<='time: ).*?(?=')", departure)
                try:
                    dtt = departure_time[0]
                    dt = Brisbane(float(departure_time[0]))
                except:
                    dtt = ''
                    dt = ''
                departure_Uncertainity = re.findall(r"(?<=uncertainty: ).*?(?=')", departure)
                try:
                    du =  departure_Uncertainity[0]
                except:
                    du = ''
                try:
                    sid = re.findall(r'(?<=stop_id: ").*?(?=")', stopseq)
                except:
                    sid = ''
                try:

                    if float(timestamp) > float(att)-900:
                        
                        data = [ tripid[0],Start_time[0],Start_date[0],route_id[0],Stop_Seq[0], ad , att, at, au , dtt, dt, du, sid[0],sr,Vehid[0],timestamp]
                        #print(data)
                        FO.append(data)
                    
                
                except:
                    if Stop_Seq[0] =='':
                        data = [ tripid[0],Start_time[0],Start_date[0],route_id[0],Stop_Seq[0], ad , att, at, au , dtt, dt, du, sid[0],sr,Vehid[0],timestamp]
                        FO.append(data)
                    continue
        Dt = pd.DataFrame(FO, columns=[ "Trip ID" , "Star t Time", "Start Date", "Route ID", "Stop Sequence","Arrival Delay", "Arrival Time (UNIX)","Arrival Time (UTC+10)", "Arrival Uncertainty", "Departure Time (UNIX)","Departure Time (UTC+10)", "Departure Uncertainty", "stop_id","schedule_relationship" ,"Vehicle ID", "timestamp" ])
        #print(Dt)
        df = Dt.merge(stopid_matrix, how='left').sort_values('Trip ID')
        df = df[["Trip ID", "Star t Time", "Start Date", "Route ID", "Stop Sequence", "Arrival Delay" , "Arrival Time (UNIX)","Arrival Time (UTC+10)",  "Arrival Uncertainty", "Departure Time (UNIX)", "Departure Time (UTC+10)", "Departure Uncertainty"  ,"stop_id", "stop_code", "stop_name", "stop_desc", "stop_lat", "stop_lon", "zone_id", "stop_url", "location_type", "parent_station", "platform_code", "schedule_relationship", "Vehicle ID", "timestamp"]]
        df = df.replace(np.nan, '-NA-')
        df.to_csv(Working_DR+ 'Trip_Update in Tabular form/'+ 'TU' + str(ki[0]), index = None, header=True)
        
