# -*- coding: utf-8 -*-
"""
Karl Roush
Wells Fargo Campus Analytics Challenge 2018
"""
import csv
from itertools import islice
from statistics import median
from random import randint, uniform
import time
import os

def clean():
    os.remove('output.csv')
    os.remove('ML_raw_data.csv')
    os.remove('ML_output.csv')
    
def create_index(activity,number): #number: duration=2,importance=3
    activity=activity2num(activity)
    junk=[]
    with open('raw_data.csv') as f:
        fifthlines = islice(f, activity, None, 27)
        for line in fifthlines:
            line=line.split(',')
            if line[number]!='':
                junk.append(line[number])
        junk=[float(x) for x in junk]
        if len(junk)!=0:
            medianVal=median(junk)
        else:
            medianVal=0
    return medianVal

def gimmetheValues():
    with open('insights-duration.csv','w') as csvfile:
        csvfile.write('Activity, Median Duration\n')
        activity=1
        while activity <=27:
            insights(activity,2)
            activity+=1
            
def gimmetheValues2():
    with open('insights-Importance.csv','w') as csvfile:
        csvfile.write('Activity, Median Importance \n')
        activity=1
        while activity <=27:
            insights2(activity,3)
            activity+=1            
        
def insights(activity,number): #number: duration=2,importance=3
    junk=[]
    with open('insights-duration.csv','a') as f:
        fifthlines = islice(f, activity, None, 27)
        for line in fifthlines:
            line=line.split(',')
            if line[number]!='':
                junk.append(line[number])
        junk=[float(x) for x in junk]
        if len(junk)!=0:
            medianVal=median(junk)
        else:
            medianVal=0
    return medianVal        

def insights2(activity,number): #number: duration=2,importance=3
    junk=[]
    with open('insights-Importance.csv','a') as f:
        fifthlines = islice(f, activity, None, 27)
        for line in fifthlines:
            line=line.split(',')
            if line[number]!='':
                junk.append(line[number])
        junk=[float(x) for x in junk]
        if len(junk)!=0:
            medianVal=median(junk)
        else:
            medianVal=0
    return medianVal   

def insights_real(): #look at medians
    activity=1
    number=3
    while activity<=27: #number: duration=2,importance=3
        junk=[]
        with open('raw_data.csv') as f:
            fifthlines = islice(f, activity, None, 27)
            for line in fifthlines:
                line=line.split(',')
                if line[number]!='':
                    junk.append(line[number])
            junk=[float(x) for x in junk]
            if len(junk)!=0:
                medianVal=median(junk)
            else:
                medianVal=0
            #print('Activity: %d,  Median Importance: %f' %(activity,medianVal))
            print(medianVal)
        activity+=1   
        
def activity2num(activity):
    return {
        'Household heating => 70F': 1,
        'Household heating < 70F': 2,
        'Use of heat pump':3,
        'Use of air conditioner':4,
        'shower - short':5,
        'shower - long (> 3 min)':6,
        'bath':7,
        'wash-up':8,
        'use of dishwasher':9,
        'use of clothes washer':10,
        'use of clothes dryer':11,
        'use of cooking range':12,
        'use of  oven':13,
        'use of self-clean feature of electric oven':14,
        'Small kitchen appliance in the home':15,
        'TV/computer use':16,
        'air travel - large plane':17,
        'air travel - small  plane (<50 seats)':18,
        'car trips- self only':19,
        'car trips - driver and self':20,
        'car trips - 2+ people with multiple end points':21,
        'trips using public ground transportation':22,
        'bags of garbage disposed':23,
        'bags of recycling deposited (negative CF)':24,
        'bags of compost deposited (negative CF)':25,
        'hazardous or electric items disposed':26,
        'large items disposed':27,
    }[activity]

def setupOutput():
    with open('output.csv','w') as csvfile:
        csvfile.write('Individual, Initial CFP,Minimized (Lifestyle Adjusted), Percent Reduction\n')
        
def outputAdd(indiv,totalCFP_out,totalCFP_impt_out,reducedCFP):
    with open('output.csv','a') as csvfile:
        data_row=str(indiv)+','+str(totalCFP_impt_out)+','+str(totalCFP_out)+','+str(reducedCFP)+'\n'
        csvfile.write(data_row)

def outputAdd_ML(indiv,totalCFP_impt_out):
    with open('ML_output.csv','a') as csvfile:
        #totalCFP_impt_out=totalCFP_impt_out/10
        totalCFP_impt_out=totalCFP_impt_out*(uniform(1.0, 1.2))
        data_row=str(indiv)+','+str(totalCFP_impt_out)+'\n'
        csvfile.write(data_row)
        
def totalCFP(): #does not account for importance
    totalCFP=[]
    activityNum=0
    while activityNum<=25:
        a=activityCFP(activityNum,file,actSource,duration)
        totalCFP.append(a)
        activityNum+=1
    return totalCFP

def totalCFP_green(): 
    totalCFP_green=[]
    activityNum=0
    while activityNum<=25:
        a=activityCFP(activityNum,file,actSource,adj_duration)
        totalCFP_green.append(a)
        activityNum+=1
    totalCFP_green=sum(totalCFP_green)
    return totalCFP_green

def activityCFP(activityNum,file,actSource,duration): #calculates CFP for each activity
    cps=[]
    for item in actSource[activityNum]:
        if item==0:
            cps.append(0) #a zero here means that they did not do a certain activity
        else:
            cps.append(float(file[activityNum][item]))
    CFP=min(cps)*float(duration[activityNum])
    return CFP

def actCFP_importance(activityNum,file,actSource,duration): #calculates CFP for each activity, accounts for importance
    cps=[]
    activityNum=0
    for item in actSource[activityNum]:
        if item==0:
            cps.append(0) #a zero here means that they did not do a certain activity
        else:
            cps.append(float(file[activityNum][item]))
    CFP_importance=min(cps)*float(duration[activityNum])*importance[activityNum]
    return CFP_importance
   
def totalCFP_importance(): #accounts for importance
    totalCFP_importance=[]
    activityNum=0
    while activityNum<=26:
        a=actCFP_importance(activityNum,file,actSource,duration)
        totalCFP_importance.append(a)
        activityNum+=1
    return totalCFP_importance

def savedCFP(totalCFP_out,totalCFP_impt_out):
    #reducedCFP=[a-b for a,b in zip(totalCFP_out,totalCFP_impt_out)]
    reducedCFP=(totalCFP_impt_out-totalCFP_out)*100
    reducedCFP=round(reducedCFP,12)
    if reducedCFP<0:
        reducedCFP*=-1
    return reducedCFP    

def getWeights():
    file=[]
    with open('weights.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            file.append(row)
        file=file[1:] #remove headers
    return file

def adjustDuration(duration,importance):
    duration=[float(x) for x in duration]
    importance=[float(x) for x in importance]
    
    adj_duration=[a*b for a,b in zip(duration,importance)]
    return adj_duration

def getIndivData(indiv): #gets the data for each individual
    with open('raw_data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        activities=[]
        duration=[]
        importance=[]
        actSource=[]
        for row in islice(readCSV,26*(indiv-1)+indiv,26*indiv+indiv):
            act = row[1] #2rd column= activity
            if row[2]=='': #3rd column= duration
                consum=create_index(row[1],2) #replaces empty with median
                #consum=0 #if no duration is specified, default to zero
            else:
                consum=row[2]
            if row[3]=='':
                impor=create_index(row[1],3) #replaces empty with median
                #impor=0 #if no importance is specified, default to zero
            else:
                impor=int(row[3])/100 #convert percentage to decimal
            typeof= [i for i,x in enumerate(row) if x=='1'] #finds the indices of type of footprint
            typeof[:]= [a-3 for a in typeof] #need to -3 to sync with weights
            typeof=typeof[1:] #says which columns are used in weights (specific CFP)
            if len(typeof)==0:
                typeof=[0]
            
            actSource.append(typeof)
            activities.append(act)
            duration.append(consum)
            importance.append(impor)
    return activities, duration, importance, actSource

def setupML_data():
    with open('ML__raw_data.csv','w') as csvfile:
        csvfile.write('Household heating => 70F,'
        'Household heating < 70F,'
        'Use of heat pump,'
        'Use of air conditioner,'
        'shower - short,'
        'shower - long (> 3 min),'
        'bath,'
        'wash-up,'
        'use of dishwasher,'
        'use of clothes washer,'
        'use of clothes dryer,'
        'use of cooking range,'
        'use of  oven,'
        'use of self-clean feature of electric oven,'
        'Small kitchen appliance in the home,'
        'TV/computer use,'
        'air travel - large plane,'
        'air travel - small  plane (<50 seats),'
        'car trips- self only,'
        'car trips - driver and self,'
        'car trips - 2+ people with multiple end points,'
        'trips using public ground transportation,'
        'bags of garbage disposed,'
        'bags of recycling deposited (negative CF),'
        'bags of compost deposited (negative CF),'
        'hazardous or electric items disposed,'
        'Total CFP \n')
        
def ML_data(totalCFP_raw,totalCFP_impt_out):
    with open('ML_raw_data.csv','a') as csvfile:
        totalCFP_raw.append(str(totalCFP_impt_out))
        data_row = ','.join(str(e) for e in totalCFP_raw)
        data_row=data_row+'\n'
        csvfile.write(data_row)
        #for item in totalCFP_raw:
            #csvfile.write(str(item))
            #csvfile.write('%f,' % item)
            #line.append(item)
#    data_row=[str(x) for x in totalCFP_raw]
#    data_row = ','.join(map(str, data_row))
        #data_row=str(totalCFP_raw)+'\n'
        #csvfile.write(data_row)
start_time = time.time()        
clean() #to prevent append errors

setupOutput()
#setupML_data()
file=getWeights()
#gimmetheValues() #insights
#gimmetheValues2()
indiv=1
while indiv<=1002: #iterate through all the individuals
    [activities, duration, importance, actSource]=getIndivData(indiv) #return file, activities, duration, importance, actSource
    totalCFP_out=sum(totalCFP())
    totalCFP_impt_out=sum(totalCFP_importance())
    
    totalCFP_out=round(totalCFP_out,12)
    totalCFP_impt_out=round(totalCFP_impt_out,12)
    reducedCFP=savedCFP(totalCFP_out,totalCFP_impt_out)
#   adj_duration=adjustDuration(duration,importance)
#   goGreen=round(totalCFP_out,12)
    totalCFP_raw=totalCFP() #raw CFP per activity
    
    ML_data(totalCFP_raw,totalCFP_impt_out)
    outputAdd_ML(indiv,totalCFP_out)
    outputAdd(indiv,totalCFP_out,totalCFP_impt_out,reducedCFP)
    
    indiv+=1
#print("--- %s seconds ---" % (time.time() - start_time)) #test how long program takes