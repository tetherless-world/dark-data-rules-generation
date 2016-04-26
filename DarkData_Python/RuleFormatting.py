#!/usr/bin/env python

import csv
import numpy as np
import string
import json
import xlsxwriter

f = open('DarkData_Rules_Improved_AP.txt', 'r')
reader = csv.DictReader(f, delimiter='\t')


temprules = open('Temprules.txt','w')

for row in reader:
    #print row
    temprules.write(row['rules'].replace("{","").replace(" => ",",").replace("}","").replace("=",",")+"\n")

temprules.close()

temprules = open('Temprules.txt','r')

ruleread = csv.reader(temprules,delimiter = ',')

l = []

for row1 in ruleread:
    l.append(row1)


ll = []

for i in range(0,len(l)):
    ll.append(dict(zip(l[i][::2],l[i][1::2])))

# for i in range(0,len(ll)):
print(ll[i])

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('TrialRules.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': 1})

var = ['Processing_Level1','Processing_Level2','Measurement1','Measurement2','Instrument1','Instrument2','Time_Interval1','Time_Interval2','Spatial_Resolution1','Spatial_Resolution2','Hurricane','Volcano','Fire','Flood','Service']
cols = ['A1','B1','C1','D1','E1','F1','G1','H1','I1','J1','K1','L1','M1','N1','O1']
# Write some data headers.
for i in range(0,len(var)):
    worksheet.write(cols[i],var[i] , bold)


#print ll[i]['Service']
print(len(ll))
rows = 1
col = 0

for rows in range(1,len(ll)):
    col = 0
    for i in range(0,len(var)):
        try:
            print(ll[rows-1][var[i]])
            worksheet.write_string(rows,col,ll[rows-1][var[i]])
        except KeyError:
            print "Sorry"
            worksheet.write_string(rows,col,'NA')

        col = col+1
    print "\n"


workbook.close()