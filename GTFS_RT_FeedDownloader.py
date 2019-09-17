from google.transit import gtfs_realtime_pb2
import urllib
import urllib.request
import time
import datetime
import os

def monthname(mydate):
    mydate = datetime.datetime.now()
    m = mydate.strftime("%B")
    return(m)

#Make adjustments to time depending on user location
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

def createCSVfileWCD(inputlist , name):
    with open( name , 'w') as f:
        for i in inputlist:
            f.write(str(i))
            f.write('\n')
        return(f)

#Change Working Directory to correspond with user location
Working_Directory = r"//rstore.qut.edu.au/projects/sef/hetrogenmodel/Data/GTFS/"
#Input Folder Names
TU = "TripUpdate entity"
VP = "VehiclePosition entity"
SA = "ServiceAlert entity"
FT = "File Tracker"

TU1directory= Working_Directory+ 'TripUpdate entity'
if not os.path.exists(TU1directory):
    os.makedirs(TU1directory)

VP1directory= Working_Directory+ 'VehiclePosition entity'
if not os.path.exists(VP1directory):
    os.makedirs(VP1directory)

SA1directory= Working_Directory+ 'ServiceAlert entity'
if not os.path.exists(SA1directory):
    os.makedirs(SA1directory)

FTdirectory= Working_Directory+ 'File Tracker'
if not os.path.exists(FTdirectory):
    os.makedirs(FTdirectory)
                                        

t = int(time.time())
tm1 = float(t)
tm2 = float(t)

datee = datetime.datetime.strptime(str(Brisbane(t)),"%d-%m-%Y %H:%M:%S" )
print(datee)
m = datee.month
y = datee.year
d = datee.day
m_name = monthname(Brisbane(t))

ttt = str(d)+"-"+str(m)+"-"+str(y)
ttt1 = str(m_name)+" ,"+str(y)
FTdirectory= FTdirectory+ "/"+ 'FT ' +str(ttt1) 
FTdirectory2= FTdirectory+ "/"+ 'FT - TripUpdate '+str(ttt1) + "/"
FTdirectory3= FTdirectory+ "/"+ 'FT - VehiclePositions '+str(ttt1) +"/"
FTdirectory4= FTdirectory+ "/"+ 'FT - Alert '+str(ttt1)+"/"
try:
    File_Tracker_TU1= inputCSVfile(FTdirectory2+'File_Tracker_TU '+str(d)+"-"+ str(m)+"-"+str(y)+ " " +'.csv')
except:
    File_Tracker_TU1 =[]
try:
    File_Tracker_VP1= inputCSVfile(FTdirectory3+'File_Tracker_VP '+str(d)+"-"+ str(m)+"-"+str(y)+ " " +'.csv')
except:
    File_Tracker_VP1 =[]
try:
    File_Tracker_SA1 = inputCSVfile(FTdirectory4+'File_Tracker_SA '+str(d)+"-"+ str(m)+"-"+str(y)+ " " +'.csv')
except:
    File_Tracker_SA1 =[]


ii = 0
A =[]
B =[]
C = []

t2 = 0

while True:
    try:
        while True:
            try:
                t = int(time.time())
                datee = datetime.datetime.strptime(str(Brisbane(t)),"%d-%m-%Y %H:%M:%S" )
                m = datee.month
                y = datee.year
                d = datee.day
                m_name = monthname(Brisbane(t))
                if t2!=0:
                    if d!=d1:
                        File_Tracker_TU =[]
                        File_Tracker_VP =[]
                        File_Tracker_SA =[]

                ii= ii+1
                ttt = str(d)+"-"+str(m)+"-"+str(y)
                ttt1 = str(m_name)+" ,"+str(y)
                Trip_Update = []
                Vehicle_Positions = []
                Service_Alert = []
                feed = gtfs_realtime_pb2.FeedMessage()
                ii= ii+1
                TUdirectory = Working_Directory + TU +"/" + 'TU '+str(ttt1)
                VPdirectory = Working_Directory + VP +"/" + 'VP '+str(ttt1)
                SAdirectory = Working_Directory + SA +"/" + 'SA '+str(ttt1)
                if not os.path.exists(TUdirectory):
                    os.makedirs(TUdirectory)
                TUdirectory2= TUdirectory+ "/"+ 'TU '+str(ttt)
                if not os.path.exists(TUdirectory2):
                    os.makedirs(TUdirectory2)          
                VPdirectory = Working_Directory + VP +"/" + 'VP '+str(ttt1)

                if not os.path.exists(VPdirectory):
                    os.makedirs(VPdirectory)
                VPdirectory2= VPdirectory+ "/"+ 'VP '+str(ttt)
                if not os.path.exists(VPdirectory2):
                    os.makedirs(VPdirectory2)

                SAdirectory = Working_Directory + SA +"/" + 'SA '+str(ttt1)
                if not os.path.exists(SAdirectory):
                    os.makedirs(SAdirectory)
                SAdirectory2= SAdirectory+ "/"+ 'SA '+str(ttt)
                if not os.path.exists(SAdirectory2):
                    os.makedirs(SAdirectory2)

                FTdirectory = Working_Directory + FT +"/" + 'FT '+str(ttt1)
                if not os.path.exists(FTdirectory):
                    os.makedirs(FTdirectory)
                FTdirectory2= FTdirectory+ "/"+ 'FT - TripUpdate '+str(ttt1) + "/"
                FTdirectory3= FTdirectory+ "/"+ 'FT - VehiclePositions '+str(ttt1) +"/"
                FTdirectory4= FTdirectory+ "/"+ 'FT - Alert '+str(ttt1)+"/"
                if not os.path.exists(FTdirectory2):
                    os.makedirs(FTdirectory2)
                if not os.path.exists(FTdirectory3):
                    os.makedirs(FTdirectory3)
                if not os.path.exists(FTdirectory3):
                    os.makedirs(FTdirectory3)
                

                Trip_Update = []
                Vehicle_Positions = []
                Service_Alert =[]
                
                try:
                    response = urllib.request.urlopen('https://gtfsrt.api.translink.com.au/Feed/SEQ')
                    feed.ParseFromString(response.read())
                except:
                    break
                for entity in feed.entity:
                    if entity.HasField('trip_update'):
                        Trip_Update.append(str(entity.trip_update))
                for entity in feed.entity:
                    if entity.HasField('vehicle'):
                        Vehicle_Positions.append(str(entity.vehicle))
                for entity in feed.entity:
                    if entity.HasField('alert'):
                        Service_Alert.append(str(entity.alerts))
                print('Feed recieved')
                if Trip_Update != A:
                    try:
                        createCSVfileWCD(Trip_Update, TUdirectory2 + "/"  'Trip_Update'+str(t)+'.csv')
                        print(float(time.time())-tm1)
                        tm1 = float(time.time())
                        temp = []
                        temp.append('Trip_Update'+str(t)+'.csv')
                        temp.append(Brisbane(t))
                        File_Tracker_TU1.append(temp)
                        try:
                            createCSVfile(File_Tracker_TU1,FTdirectory2 + 'File_Tracker_TU '+str(d)+"-"+ str(m)+"-"+str(y)+ " " +'.csv')
                        except:
                            continue
                        A = Trip_Update
                    except:
                        continue
                if Vehicle_Positions != B:
                    try:
                        print(float(time.time())- tm2)
                        tm2 = float(time.time())
                        createCSVfileWCD(Vehicle_Positions, VPdirectory2 +"/" 'Vehicle_Positions'+str(t)+'.csv')
                        temp = []
                        temp.append('Vehicle_Positions'+str(t)+'.csv')
                        temp.append(Brisbane(t))
                        File_Tracker_VP1.append(temp)
                        try:
                            createCSVfile(File_Tracker_VP1, FTdirectory3 + 'File_Tracker_VP '+str(d)+"-"+ str(m)+"-"+str(y)+ " " +'.csv')
                        except:
                            continue
                        B = Vehicle_Positions
                    except:
                        continue
                if Service_Alert != C:
                    createCSVfileWCD(Service_Alert,SAdirectory2 +"/"  'Service_Alert'+str(t)+'.csv')
                    temp = []
                    temp.append('Service_Alert'+str(t)+'.csv')
                    temp.append(Brisbane(t))
                    File_Tracker_SA1.append(temp)
                    try:
                        createCSVfile(File_Tracker_SA1,FTdirectory4 + 'File_Tracker_SA1 '+str(d)+"-"+ str(m)+"-"+str(y)+ " " +'.csv')
                    except:
                        continue
                    C = Service_Alert
                d1 = d
                t2 = 1
            except:
                continue
            break
            
    except:
        continue




