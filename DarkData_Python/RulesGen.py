#!/usr/bin/env python
import pandas as pd
import xlrd
import numpy as np

data = {}
with pd.ExcelFile('DarkData_Rules_Improved_AP.xlsx') as xls:
    data['Sheet1'] = pd.read_excel(xls, 'For_Rule_Gen', index_col=None, na_values=['NA'])
    data['Sheet2'] = pd.read_excel(xls, 'Formatted_For_Evaluation', index_col=None, na_values=['NA'],parse_cols=[0,1,2,3,4,5,6,7,8,9,10,12,22],convert_float=False)

#print(data['Sheet1'])

f = open('Rules.txt','w+')
f.write("@prefix dd: <http://www.purl.org/twc/ns/darkdata#>."+"\n"+
"@prefix ddmeasurement: <http://darkdata.tw.rpi.edu/data/measurement/>."+"\n"+
"@prefix ddtime: <http://darkdata.tw.rpi.edu/data/time-interval/>."+"\n"+
"@prefix ddspatial:<http://darkdata.tw.rpi.edu/data/spatial-resolution/>."+"\n"+
"@prefix ddinstrument:<http://darkdata.tw.rpi.edu/data/instrument/>."+"\n"+"\n")

var = [['Measurement1','dd:measurement','ddmeasurement:'],['Measurement2','dd:measurement','ddmeasurement:'],['Instrument1','dd:instrument','ddinstrument:'],['Instrument2','dd:instrument','ddinstrument:'],['Time_Interval1','dd:timeInterval','ddtime:'],['Time_Interval2','dd:timeInterval','ddtime:'],['Spatial_Resolution1','dd:spatialResolution','ddspatial:'],['Spatial_Resolution2','dd:spatialResolution','ddspatial:'],['Processing+Level1','dd:processingLevel',''],['Processing+Level2','dd:processingLevel',''],['Event+Type','dd:candidateEvent','dd:']]


def runR(compatibility,variable,i):
    f.write("[Rule_no"+str(i)+":"+"\n")
    for x in xrange(0,len(variable)-2,2):
        if(not(str(data['Sheet1'][variable[x][0]][i])=='nan')):
            f.write(str("(?datafield1 " + str(variable[x][1])+" " + str(variable[x][2])  +str(data['Sheet1'][variable[x][0]][i])+"),"+"\n"))
        if(not(str(data['Sheet1'][variable[x+1][0]][i])=='nan')):
            f.write(str("(?datafield2 " + str(variable[x][1])+" " + str(variable[x][2])  +str(data['Sheet1'][variable[x+1][0]][i])+"),"+"\n"))

    if(not(str(data['Sheet1'][variable[len(variable)-1][0]][i])=='nan')):
        f.write("(?candidate "+str(variable[len(variable)-1][1])+" ?event),"+"\n"+
             "(?event rdf:type "+ str(variable[len(variable)-1][2]) +str(data['Sheet1'][variable[len(variable)-1][0]][i])+"),"+"\n")
    f.write("makeSkolem(?assertion, ?candidate, ?datafield1 , ?datafield2)"+"\n")
    f.write("->"+"\n")
    f.write("(?candidate dd:compatibilityAssertion ?assertion),"+"\n"+
            "(?assertion rdf:type dd:CompatibilityAssertion),"+"\n"+
            "(?assertion dd:compatibilityValue dd:"+compatibility+"),"+"\n"+
            "(?assertion dd:assertionConfidence \""+str(0.5)+"\"^^xsd:double)"+"\n"+
            "(?assertion dd:basisForAssertion <urn:rule/Rules.txt/<Rule_no"+str(i)+">)"+"\n"
            +"]"+"\n"
            )
for i in range(0,len(data['Sheet1'])):
    print i
    if(data['Sheet1']['Correctness Average'][i]>4.0 and data['Sheet1']['Correctness Average'][i]<=5.0):
        runR('strong_compatibility',var,i)
    elif(data['Sheet1']['Correctness Average'][i]>3.0 and data['Sheet1']['Correctness Average'][i]<=4.0):
        runR("some_compatibility",var,i)
    elif(data['Sheet1']['Correctness Average'][i]>2.0 and data['Sheet1']['Correctness Average'][i]<=3.0):
        runR("slight_compatibility",var,i)
    elif(data['Sheet1']['Correctness Average'][i]>1.0 and data['Sheet1']['Correctness Average'][i]<=2.0):
        runR("indifferent_compatibility",var,i)
    else:
        runR("negative_compatibility",var,i)


f.close()

