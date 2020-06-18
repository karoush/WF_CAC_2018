# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 12:02:53 2018

@author: kroush7
"""

import csv
from itertools import islice
import difflib
from statistics import median
import time

activity=1
number=2
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

#with open('ML_data.csv','w') as csvfile:
#    csvfile.write('Household heating => 70F,'
#    'Household heating < 70F,'
#    'Use of heat pump,'
#    'Use of air conditioner,'
#    'shower - short,'
#    'shower - long (> 3 min),'
#    'bath,'
#    'wash-up,'
#    'use of dishwasher,'
#    'use of clothes washer,'
#    'use of clothes dryer,'
#    'use of cooking range,'
#    'use of  oven,'
#    'use of self-clean feature of electric oven,'
#    'Small kitchen appliance in the home,'
#    'TV/computer use,'
#    'air travel - large plane,'
#    'air travel - small  plane (<50 seats),'
#    'car trips- self only,'
#    'car trips - driver and self,'
#    'car trips - 2+ people with multiple end points,'
#    'trips using public ground transportation,'
#    'bags of garbage disposed,'
#    'bags of recycling deposited (negative CF),'
#    'bags of compost deposited (negative CF),'
#    'hazardous or electric items disposed,'
#    'large items disposed')


#a=difflib.ndiff('Small kitchen applicance in the home', 'Small kitchen appliance in the home')
#print(a)
#activity=1
#number=3
#junk=[]
#while activity<=27:
#    with open('raw_data.csv') as f:
#        fifthlines = islice(f, activity, None, 27)
#        for line in fifthlines:
#            line=line.split(',')
#            junk.append(line[number])
#            junk=list(filter(lambda x: x != '', junk))
#            junk=[float(x) for x in junk]
#        medianVal=median(junk)
    #activity+=1
    #print(activity)
    #time.sleep(0.1)
#with open('raw_data.csv') as f:
#    fifthlines = islice(f, activity, None, 27)
#    for line in fifthlines:
#        line=line.split(',')
#        junk.append(int(line[number]))
#    medianVal=median(junk)

#def activity2num(activity):
#    return {
#        'Household heating => 70F': 1,
#        'Household heating < 70F': 2,
#        'Use of heat pump':3,
#        'Use of air conditioner':4,
#        'shower - short':5,
#        'shower - long (> 3 min)':6,
#        'bath':7,
#        'wash-up':8,
#        'use of dishwasher':9,
#        'use of clothes washer':10,
#        'use of clothes dryer':11,
#        'use of cooking range':12,
#        'use of  oven':13,
#        'use of self-clean feature of electric oven':14,
#        'Small kitchen applicance in the home':15,
#        'TV/computer use':16,
#        'air travel - large plane':17,
#        'air travel - small  plane (<50 seats)':18,
#        'car trips- self only':19,
#        'car trips - driver and self':20,
#        'car trips - 2+ people with multiple end points':21,
#        'trips using public ground transportation':22,
#        'bags of garbage disposed':23,
#        'bags of recycling deposited (negative CF)':24,
#        'bags of compost deposited (negative CF)':25,
#        'hazardous or electric items disposed':26,
#        'large items disposed':27,
#    }[activity]
#activity=1
#number=2
#junk=[]
#test=[]
#with open('raw_data.csv') as f:
#    fifthlines = islice(f, activity, None, 27)
#    for line in fifthlines:
#        test.append(line)
#        line=line.split(',')
#        junk.append(line[number])

#for item in a[0]:
#    print(item)
#import csv
#
#    with open('output.csv','w') as csvfile:
#        csvfile.write('Individual, Initial CFP, Inital CFP (Importance Adjusted)')
#
##totalCFP=[]
##activityCP=[]
#activityNum=0
#while activityNum<=26:
#    totalCFP.append(activityCFP(activityNum,file,actSource,duration))
#    activityNum+=1
#totalCFP=sum(totalCFP)

#cps=[]
#activityNum=0
#for item in actSource[activityNum]:
#    cps.append(float(file[activityNum][item]))
#CFP=min(cps)*float(duration[activityNum])
#return CFP
#file=[]
#with open('weights.csv') as csvfile:
#    readCSV = csv.reader(csvfile, delimiter=',')
#    for row in readCSV:
#        file.append(row)
#activityCP=[]
#activityNum=0
#x=0
#while x<len(actSource[activityNum-1]):
#    fp=file[activityNum+1][actSource[activityNum][x]]
#    activityCP.append(fp)
#    x+=1
#activityCP=float(min(activityCP))*float(duration[activityNum])

#    with open('carbonfootprints.csv','a') as ot:
#        ot.write(min(activityCP))

#activityCP=[]
#activityNum=0
#while activityNum<=2:
#    activityCFP(activityNum,file,actSource,duration)
#    activityNum+=1
##return activityCP