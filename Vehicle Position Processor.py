import multiprocessing
import numpy as np
import math

def inputCSVfile(csvfile):
    list1= []
    with open(csvfile, 'r') as f:
        for i in f:
            j = i.split(',')
            
            le = len(j)
            j[le - 1] = (j[le- 1]).strip()
            list1.append(j)
        return(list1)
    
################################### Function 2 : Create a CSV file from a List  ############################################

def createCSVfile(inputlist , name):
    with open( name , 'w') as f:
        for i in inputlist:
            k = 0
            for item in i:
                f.write(str(item) + ',')
                k = k+1
            f.write('\n')
        return(f)
totalentries = 0
Working_DR  = 'Y:/Data/GTFS/'
C = inputCSVfile('STOP ID MATRIX.csv')
C = np.array(C)
fiction = ['-NA-','-NA-','-NA-','-NA-']
flag = 2

VehiclePosition = inputCSVfile(Working_DR +'File_Tracker_VP.csv')

def Processing(VehiclePosition):
  for ki in VehiclePosition:    
    Titlename =["trip_id" , "route_id" , "lattitude" , "longitude" , "current_status" ,  "time_stamp" , "S_id" , "Vehicle_Id" , "label" ] 
    FinalOutput = []
    FinalOutput.append(Titlename)
    AZ = inputCSVfile(Working_DR + 'Vehicle Position/'+ str(ki[0]))
    try:
      for index,i in enumerate(AZ):
        
        BZ = AZ

        try:
          for val in i:
              ii = str(val)
          if  ii[0:6] == 'trip {':
            flags = 'start'
          if flags == 'start':
            if index%2000 ==0:
              print(index)
              ooo = 0

            i = list(i)

            for val in i:
              ii = str(val)
            
            if ii[0:6] ==    'trip {':
              temp1 =[]
              temp2 =[]
              temp3 =[]
              tempdeparture =[]
              temparrival = []
              Vehicle_id =[]

            if ii[0:8] == "trip_id:":
              temp1 = []
              tid = str(ii[10:len(ii)-1])
              temp1.append(ii[10:len(ii)-1])

            if ii[0:10] == "route_id: ":
              if len(temp1) == 0:
                temp1.append('-NA-')
              tid1 = tid
              temp1.append(ii[11:len(ii)-1])

            if ii[0:3] == "id:":
              if len(temp1) == 6:
                temp1.append('-NA-')
              temp1.append(ii[5:len(ii)-1])
              
            if ii[0:8] == "stop_id:":
              if len(temp1) == 5:
                temp1.append('-NA-')
              temp1.append(ii[10:len(ii)-1])
              sid = str(ii[10:len(ii)-1])

            if ii[0:6] == "label:":
              if len(temp1) == 7:
                temp1.append('-NA-')
              temp1.append(ii[8:len(ii)-1])
              

            if ii[0:9] == "latitude:":
              if len(temp1) == 1:
                temp1.append('-NA-')
              temp1.append(ii[10:len(ii)-1])

            if ii[0:10] == "longitude:":
              if len(temp1) == 2:
                temp1.append('-NA-')
              temp1.append(ii[11:len(ii)-1])

            if ii[0:15] == "current_status:":
              if len(temp1) == 3:
                temp1.append('-NA-')
              temp1.append(ii[16:len(ii)-1])

            if ii[0:10] == "timestamp:":
              t = ii[11:]
              if len(temp1) == 4:
                temp1.append('Towards stop')
              temp1.append(ii[11:])

            if ii[0:6] == "label:" and len(temp1)==9:
              if len(temp1)==9:
                FinalOutput.append(temp1)
                temp1 = []
            if ii[0:6] == "label:" and len(temp1)!=9:
              temp1 = []

        except:
          print('error1')
          continue
      createCSVfile(FinalOutput, Working_DR + 'VP/'+ 'VP Entity' + str(ki[0]))
   
    except:
      print('ddddddddddddddddddddddddddd')
      continue
  
#Processing(VehiclePosition)
if __name__ == "__main__":
  VehiclePosition = inputCSVfile(Working_DR +'File_Tracker_VP.csv')
  p = 1
  length = int(len(VehiclePosition)/p)
  for n in range(0, length):
    VehiclePosition1 = VehiclePosition[n*p+0:n*p+p]
    p1 = multiprocessing.Process(target = Processing, args = (VehiclePosition1,))    
    p1.start()
    print('started')
