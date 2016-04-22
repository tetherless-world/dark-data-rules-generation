#!/usr/bin/env python
import pandas as pd
import xlrd
import numpy as np

data = {}
with pd.ExcelFile('DarkData_Rules_Improved_AP.xlsx') as xls:
    data['Sheet1'] = pd.read_excel(xls, 'For_Rule_Gen', index_col=None, na_values=['NA'])
    data['Sheet2'] = pd.read_excel(xls, 'Formatted_For_Evaluation', index_col=None, na_values=['NA'],parse_cols=[0,1,2,3,4,5,6,7,8,9,10,12,22],convert_float=False)

def runrules(compatibility):
    if(str(data['Sheet1']['Event+Type'][i])=='nan'):
        if(np.isnan(data['Sheet1']['Processing+Level1'][i]) and np.isnan(data['Sheet1']['Processing+Level2'][i])):
            f.write(str("[Rule_no"+str(i)+":"+"\n"+"(?datafield1 dd:measurement ddmeasurement:"+data['Sheet1']['Measurement1'][i]+"),"+"\n"+
            "(?datafield2 dd:measurement ddmeasurement:"+data['Sheet1']['Measurement2'][i]+"),"+"\n"+
            "(?datafield1 dd:instrument ddinstrument:"+data['Sheet1']['Instrument1'][i]+"),"+"\n"+
            "(?datafield2 dd:instrument ddinstrument:"+data['Sheet1']['Instrument2'][i]+"),"+"\n"+
            "(?datafield1 dd:timeInterval ddtime:"+data['Sheet1']['Time_Interval1'][i]+"),"+"\n"+
            "(?datafield2 dd:timeInterval ddtime:"+data['Sheet1']['Time_Interval2'][i]+"),"+"\n"+
            "(?datafield1 dd:spatialResolution ddspatial:"+data['Sheet1']['Spatial_Resolution1'][i]+"),"+"\n"+
            "(?datafield2 dd:spatialResolution ddspatial:"+data['Sheet1']['Spatial_Resolution2'][i]+"),"+"\n"
            #+"(?datafield1 dd:processingLevel "+str(int(data['Sheet1']['Processing+Level1'][i]))+")"+"\n"+
            #"(?datafield1 dd:processingLevel "+str(int(data['Sheet1']['Processing+Level2'][i]))+")"+"\n"
            +"makeSkolem(?assertion, ?candidate, ?datafield1 , ?datafield2)"+"\n"
            +"->"+"\n"+
            "(?candidate dd:compatibilityAssertion ?assertion),"+"\n"+
            "(?assertion rdf:type dd:CompatibilityAssertion),"+"\n"+
            "(?assertion dd:compatibilityValue dd:"+compatibility+"\n"+
            " (?assertion dd:assertionConfidence \""+str(0.5)+"\"^^xsd:double)"+"\n"+
            "(?assertion dd:basisForAssertion <urn:rule/Rules.txt/<Rule_no"+str(i)+">)"+"\n"
            +"]"+"\n"
            ))
        elif(np.isnan(data['Sheet1']['Processing+Level1'][i])):
            f.write(str("[Rule_no"+str(i)+":"+"\n"+"(?datafield1 dd:measurement ddmeasurement:"+data['Sheet1']['Measurement1'][i]+"),"+"\n"+
            "(?datafield2 dd:measurement ddmeasurement:"+data['Sheet1']['Measurement2'][i]+"),"+"\n"+
            "(?datafield1 dd:instrument ddinstrument:"+data['Sheet1']['Instrument1'][i]+"),"+"\n"+
            "(?datafield2 dd:instrument ddinstrument:"+data['Sheet1']['Instrument2'][i]+"),"+"\n"+
            "(?datafield1 dd:timeInterval ddtime:"+data['Sheet1']['Time_Interval1'][i]+"),"+"\n"+
            "(?datafield2 dd:timeInterval ddtime:"+data['Sheet1']['Time_Interval2'][i]+"),"+"\n"+
            "(?datafield1 dd:spatialResolution ddspatial:"+data['Sheet1']['Spatial_Resolution1'][i]+"),"+"\n"+
            "(?datafield2 dd:spatialResolution ddspatial:"+data['Sheet1']['Spatial_Resolution2'][i]+"),"+"\n"
            #+"(?datafield1 dd:processingLevel "+str(int(data['Sheet1']['Processing+Level1'][i]))+")"+"\n"+
            +"(?datafield2 dd:processingLevel "+str(int(data['Sheet1']['Processing+Level2'][i]))+"),"+"\n"
            +"makeSkolem(?assertion, ?candidate, ?datafield1 , ?datafield2)"+"\n"
            +"->"+"\n"+
             "(?candidate dd:compatibilityAssertion ?assertion),"+"\n"+
            "(?assertion rdf:type dd:CompatibilityAssertion),"+"\n"+
            "(?assertion dd:compatibilityValue dd:"+compatibility+"\n"+
            " (?assertion dd:assertionConfidence \""+str(0.5)+"\"^^xsd:double)"+"\n"+
            "(?assertion dd:basisForAssertion <urn:rule/Rules.txt/<Rule_no"+str(i)+">)"+"\n"
            +"]"+"\n"
            ))
        elif(np.isnan(data['Sheet1']['Processing+Level2'][i])):
            f.write(str("[Rule_no"+str(i)+":"+"\n"+"(?datafield1 dd:measurement ddmeasurement:"+data['Sheet1']['Measurement1'][i]+"),"+"\n"+
            "(?datafield2 dd:measurement ddmeasurement:"+data['Sheet1']['Measurement2'][i]+"),"+"\n"+
            "(?datafield1 dd:instrument ddinstrument:"+data['Sheet1']['Instrument1'][i]+"),"+"\n"+
            "(?datafield2 dd:instrument ddinstrument:"+data['Sheet1']['Instrument2'][i]+"),"+"\n"+
            "(?datafield1 dd:timeInterval ddtime:"+data['Sheet1']['Time_Interval1'][i]+"),"+"\n"+
            "(?datafield2 dd:timeInterval ddtime:"+data['Sheet1']['Time_Interval2'][i]+"),"+"\n"+
            "(?datafield1 dd:spatialResolution ddspatial:"+data['Sheet1']['Spatial_Resolution1'][i]+"),"+"\n"+
            "(?datafield2 dd:spatialResolution ddspatial:"+data['Sheet1']['Spatial_Resolution2'][i]+"),"+"\n"
            +"(?datafield1 dd:processingLevel "+str(int(data['Sheet1']['Processing+Level1'][i]))+"),"+"\n"
            #"(?datafield1 dd:processingLevel "+str(int(data['Sheet1']['Processing+Level2'][i]))+")"+"\n"
            +"makeSkolem(?assertion, ?candidate, ?datafield1 , ?datafield2)"+"\n"
            +"->"+"\n"+
             "(?candidate dd:compatibilityAssertion ?assertion),"+"\n"+
            "(?assertion rdf:type dd:CompatibilityAssertion),"+"\n"+
            "(?assertion dd:compatibilityValue dd:"+compatibility+"\n"+
            " (?assertion dd:assertionConfidence \""+str(0.5)+"\"^^xsd:double)"+"\n"+
            "(?assertion dd:basisForAssertion <urn:rule/Rules.txt/<Rule_no"+str(i)+">)"+"\n"
            +"]"+"\n"
            ))
    else:
        if(np.isnan(data['Sheet1']['Processing+Level1'][i]) and np.isnan(data['Sheet1']['Processing+Level2'][i])):
            f.write(str("[Rule_no"+str(i)+":"+"\n"+"(?datafield1 dd:measurement ddmeasurement:"+data['Sheet1']['Measurement1'][i]+"),"+"\n"+
            "(?datafield2 dd:measurement ddmeasurement:"+data['Sheet1']['Measurement2'][i]+"),"+"\n"+
            "(?datafield1 dd:instrument ddinstrument:"+data['Sheet1']['Instrument1'][i]+"),"+"\n"+
            "(?datafield2 dd:instrument ddinstrument:"+data['Sheet1']['Instrument2'][i]+"),"+"\n"+
            "(?datafield1 dd:timeInterval ddtime:"+data['Sheet1']['Time_Interval1'][i]+"),"+"\n"+
            "(?datafield2 dd:timeInterval ddtime:"+data['Sheet1']['Time_Interval2'][i]+"),"+"\n"+
            "(?datafield1 dd:spatialResolution ddspatial:"+data['Sheet1']['Spatial_Resolution1'][i]+"),"+"\n"+
            "(?datafield2 dd:spatialResolution ddspatial:"+data['Sheet1']['Spatial_Resolution2'][i]+"),"+"\n"
            #+"(?datafield1 dd:processingLevel "+str(int(data['Sheet1']['Processing+Level1'][i]))+")"+"\n"+
            #"(?datafield1 dd:processingLevel "+str(int(data['Sheet1']['Processing+Level2'][i]))+")"+"\n"
            +"(?candidate dd:candidateEvent ?event),"+"\n"+
            "(?event rdf:type dd:"+data['Sheet1']['Event+Type'][i]+"),"+"\n"+
            "makeSkolem(?assertion, ?candidate, ?event, ?datafield1 , ?datafield2)"+"\n"
            +"->"+"\n"+
             "(?candidate dd:compatibilityAssertion ?assertion),"+"\n"+
            "(?assertion rdf:type dd:CompatibilityAssertion),"+"\n"+
            "(?assertion dd:compatibilityValue dd:"+compatibility+"\n"+
            " (?assertion dd:assertionConfidence \""+str(0.5)+"\"^^xsd:double)"+"\n"+
            "(?assertion dd:basisForAssertion <urn:rule/Rules.txt/<Rule_no"+str(i)+">)"+"\n"
            +"]"+"\n"
            ))
        elif(np.isnan(data['Sheet1']['Processing+Level1'][i])):
            f.write(str("[Rule_no"+str(i)+":"+"\n"+"(?datafield1 dd:measurement ddmeasurement:"+data['Sheet1']['Measurement1'][i]+"),"+"\n"+
            "(?datafield2 dd:measurement ddmeasurement:"+data['Sheet1']['Measurement2'][i]+"),"+"\n"+
            "(?datafield1 dd:instrument ddinstrument:"+data['Sheet1']['Instrument1'][i]+"),"+"\n"+
            "(?datafield2 dd:instrument ddinstrument:"+data['Sheet1']['Instrument2'][i]+"),"+"\n"+
            "(?datafield1 dd:timeInterval ddtime:"+data['Sheet1']['Time_Interval1'][i]+"),"+"\n"+
            "(?datafield2 dd:timeInterval ddtime:"+data['Sheet1']['Time_Interval2'][i]+"),"+"\n"+
            "(?datafield1 dd:spatialResolution ddspatial:"+data['Sheet1']['Spatial_Resolution1'][i]+"),"+"\n"+
            "(?datafield2 dd:spatialResolution ddspatial:"+data['Sheet1']['Spatial_Resolution2'][i]+"),"+"\n"
            #+"(?datafield1 dd:processingLevel "+str(int(data['Sheet1']['Processing+Level1'][i]))+")"+"\n"+
            +"(?datafield2 dd:processingLevel "+str(int(data['Sheet1']['Processing+Level2'][i]))+"),"+"\n"
            +"(?candidate dd:candidateEvent ?event),"+"\n"+
            "(?event rdf:type dd:"+data['Sheet1']['Event+Type'][i]+"),"+"\n"+
            "makeSkolem(?assertion, ?candidate, ?event, ?datafield1 , ?datafield2)"+"\n"
            +"->"+"\n"+
             "(?candidate dd:compatibilityAssertion ?assertion),"+"\n"+
            "(?assertion rdf:type dd:CompatibilityAssertion),"+"\n"+
            "(?assertion dd:compatibilityValue dd:"+compatibility+"\n"+
            " (?assertion dd:assertionConfidence \""+str(0.5)+"\"^^xsd:double)"+"\n"+
            "(?assertion dd:basisForAssertion <urn:rule/Rules.txt/<Rule_no"+str(i)+">)"+"\n"
            +"]"+"\n"
            ))
        elif(np.isnan(data['Sheet1']['Processing+Level2'][i])):
            f.write(str("[Rule_no"+str(i)+":"+"\n"+"(?datafield1 dd:measurement ddmeasurement:"+data['Sheet1']['Measurement1'][i]+"),"+"\n"+
            "(?datafield2 dd:measurement ddmeasurement:"+data['Sheet1']['Measurement2'][i]+"),"+"\n"+
            "(?datafield1 dd:instrument ddinstrument:"+data['Sheet1']['Instrument1'][i]+"),"+"\n"+
            "(?datafield2 dd:instrument ddinstrument:"+data['Sheet1']['Instrument2'][i]+"),"+"\n"+
            "(?datafield1 dd:timeInterval ddtime:"+data['Sheet1']['Time_Interval1'][i]+"),"+"\n"+
            "(?datafield2 dd:timeInterval ddtime:"+data['Sheet1']['Time_Interval2'][i]+"),"+"\n"+
            "(?datafield1 dd:spatialResolution ddspatial:"+data['Sheet1']['Spatial_Resolution1'][i]+"),"+"\n"+
            "(?datafield2 dd:spatialResolution ddspatial:"+data['Sheet1']['Spatial_Resolution2'][i]+"),"+"\n"
            +"(?datafield1 dd:processingLevel "+str(int(data['Sheet1']['Processing+Level1'][i]))+"),"+"\n"
            #"(?datafield1 dd:processingLevel "+str(int(data['Sheet1']['Processing+Level2'][i]))+")"+"\n"
            +"(?candidate dd:candidateEvent ?event),"+"\n"+
            "(?event rdf:type dd:"+data['Sheet1']['Event+Type'][i]+"),"+"\n"+
            "makeSkolem(?assertion, ?candidate, ?event, ?datafield1 , ?datafield2)"+"\n"
            +"->"+"\n"+
             "(?candidate dd:compatibilityAssertion ?assertion),"+"\n"+
            "(?assertion rdf:type dd:CompatibilityAssertion),"+"\n"+
            "(?assertion dd:compatibilityValue dd:"+compatibility+"\n"+
            " (?assertion dd:assertionConfidence \""+str(0.5)+"\"^^xsd:double)"+"\n"+
            "(?assertion dd:basisForAssertion <urn:rule/Rules.txt/<Rule_no"+str(i)+">)"+"\n"
            +"]"+"\n"
            ))

#print(str(int(data['Sheet1']['Processing+Level2'][176])))
#print(len(data['Sheet1']))
print(type(data['Sheet1']['Correctness Average'][2]))
i = 0
f = open('Rules.txt','w+')
f.write("@prefix dd: <http://www.purl.org/twc/ns/darkdata#>."+"\n"+
"@prefix ddmeasurement: <http://darkdata.tw.rpi.edu/data/measurement/>."+"\n"+
"@prefix ddtime: <http://darkdata.tw.rpi.edu/data/time-interval/>."+"\n"+
"@prefix ddspatial:<http://darkdata.tw.rpi.edu/data/spatial-resolution/>."+"\n"+
"@prefix ddinstrument:<http://darkdata.tw.rpi.edu/data/instrument/>."+"\n"+"\n")
for i in range(0,len(data['Sheet1'])):
    print i
    if(data['Sheet1']['Correctness Average'][i]>4.0 and data['Sheet1']['Correctness Average'][i]<=5.0):
        runrules('strong_compatibility')
    elif(data['Sheet1']['Correctness Average'][i]>3.0 and data['Sheet1']['Correctness Average'][i]<=4.0):
        runrules("some_compatibility")
    elif(data['Sheet1']['Correctness Average'][i]>2.0 and data['Sheet1']['Correctness Average'][i]<=3.0):
        runrules("slight_compatibility")
    elif(data['Sheet1']['Correctness Average'][i]>1.0 and data['Sheet1']['Correctness Average'][i]<=2.0):
        runrules("indifferent_compatibility")
    else:
        runrules("negative_compatibility")
