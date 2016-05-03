import pandas as pd

improvedRules = {}
def writeFromExcel(filename):
    with pd.ExcelFile(filename) as xls:
        improvedRules['Sheet1'] = pd.read_excel(xls, 'Sheet1', index_col=None, na_values=['NA'])




#print(improvedRules['Sheet1'])

var = [['Measurement1','dd:measurement','ddmeasurement:'],['Measurement2','dd:measurement','ddmeasurement:'],['Instrument1','dd:instrument','ddinstrument:'],['Instrument2','dd:instrument','ddinstrument:'],['Time_Interval1','dd:timeInterval','ddtime:'],['Time_Interval2','dd:timeInterval','ddtime:'],['Spatial_Resolution1','dd:spatialResolution','ddspatial:'],['Spatial_Resolution2','dd:spatialResolution','ddspatial:'],['Processing_Level1','dd:processingLevel',''],['Processing_Level2','dd:processingLevel','']]
events = [['VolcanicEruption','dd:candidateEvent','dd:'],['Hurricane','dd:candidateEvent','dd:'],['Flood','dd:candidateEvent','dd:'],['Fire','dd:candidateEvent','dd:']]

print(var[len(var)-1])

def runImprovedRules(compatibility,variable,eventType,i):
    fnew.write("[Rule_no"+str(i)+":"+"\n")
    for x in xrange(0,len(variable)-1,2):
        if(not(str(improvedRules['Sheet1'][variable[x][0]][i])=='nan')):
            fnew.write(str("(?datafield1 " + str(variable[x][1])+" " + str(variable[x][2])  +str(improvedRules['Sheet1'][variable[x][0]][i])+"),"+"\n"))
        if(not(str(improvedRules['Sheet1'][variable[x+1][0]][i])=='nan')):
            fnew.write(str("(?datafield2 " + str(variable[x][1])+" " + str(variable[x][2])  +str(improvedRules['Sheet1'][variable[x+1][0]][i])+"),"+"\n"))

    print(fnew.name)
    if(str(fnew.name) =='ImprovedTwoVarRules.txt'):
        fnew.write("(?candidate dd:candidateVariable ?datafield1),"+"\n"
            +"(?candidate dd:candidateVariable ?datafield2),"+"\n"
            +"notEqual(?datafield1, ?datafield2),"+"\n")

    for y in range(0,len(eventType)):
        if(not(str(improvedRules['Sheet1'][eventType[y][0]][i])=='nan') and (not(str(improvedRules['Sheet1'][eventType[y][0]][i])=='0.0'))):
            fnew.write("(?candidate "+str(eventType[y][1])+" ?event),"+"\n"+
                 "(?event rdf:type "+ str(eventType[y][2]) +str(eventType[y][0])+"),"+"\n")
    fnew.write("makeSkolem(?assertion, ?candidate, ?datafield1 , ?datafield2)"+"\n")
    fnew.write("->"+"\n")
    fnew.write("(?candidate dd:compatibilityAssertion ?assertion),"+"\n"+
            "(?assertion rdf:type dd:CompatibilityAssertion),"+"\n"+
            "(?assertion dd:compatibilityValue dd:"+compatibility+"),"+"\n"+
            "(?assertion dd:assertionConfidence \""+str(0.5)+"\"^^xsd:double)"+"\n"+
            "(?assertion dd:basisForAssertion <urn:rule/Rules.txt/<Rule_no"+str(i)+">)"+"\n"
            +"]"+"\n"
            )

#TODO How to state the different compatibilities?

writeFromExcel('TwoVarRules.xlsx')
#print(improvedRules['Sheet1'])

fnew = open('ImprovedTwoVarRules.txt','w')
fnew.write("@prefix dd: <http://www.purl.org/twc/ns/darkdata#>."+"\n"+
"@prefix ddmeasurement: <http://darkdata.tw.rpi.edu/data/measurement/>."+"\n"+
"@prefix ddtime: <http://darkdata.tw.rpi.edu/data/time-interval/>."+"\n"+
"@prefix ddspatial:<http://darkdata.tw.rpi.edu/data/spatial-resolution/>."+"\n"+
"@prefix ddinstrument:<http://darkdata.tw.rpi.edu/data/instrument/>."+"\n"+"\n")

for i in range(0,len(improvedRules['Sheet1'])):
    runImprovedRules('high',var,events,i)


fnew.close()

writeFromExcel('OneVarRules.xlsx')
#print(improvedRules['Sheet1'])

fnew = open('ImprovedOneVarRules.txt','w')
fnew.write("@prefix dd: <http://www.purl.org/twc/ns/darkdata#>."+"\n"+
"@prefix ddmeasurement: <http://darkdata.tw.rpi.edu/data/measurement/>."+"\n"+
"@prefix ddtime: <http://darkdata.tw.rpi.edu/data/time-interval/>."+"\n"+
"@prefix ddspatial:<http://darkdata.tw.rpi.edu/data/spatial-resolution/>."+"\n"+
"@prefix ddinstrument:<http://darkdata.tw.rpi.edu/data/instrument/>."+"\n"+"\n")

for i in range(0,len(improvedRules['Sheet1'])):
    runImprovedRules('high',var,events,i)
fnew.close()

writeFromExcel('OnlySecondVarRules.xlsx')
#print(improvedRules['Sheet1'])

fnew = open('ImprovedOnlySecondVarRules.txt','w')
fnew.write("@prefix dd: <http://www.purl.org/twc/ns/darkdata#>."+"\n"+
"@prefix ddmeasurement: <http://darkdata.tw.rpi.edu/data/measurement/>."+"\n"+
"@prefix ddtime: <http://darkdata.tw.rpi.edu/data/time-interval/>."+"\n"+
"@prefix ddspatial:<http://darkdata.tw.rpi.edu/data/spatial-resolution/>."+"\n"+
"@prefix ddinstrument:<http://darkdata.tw.rpi.edu/data/instrument/>."+"\n"+"\n")

for i in range(0,len(improvedRules['Sheet1'])):
    runImprovedRules('high',var,events,i)
fnew.close()
