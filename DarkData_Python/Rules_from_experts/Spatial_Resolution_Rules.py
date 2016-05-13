import pandas as pd
import xlrd

Rules = {}

with pd.ExcelFile('X Applicability to Phenomena from experts.xlsx') as xls:
    Rules['Spatial_Resolution_Li'] = pd.read_excel(xls, 'Spatial Resolution', skiprows=[8,9,10], index_col=None, na_values=['NA'])
    Rules['Measurement_Li'] = pd.read_excel(xls, 'Measurement', skiprows=[8,9,10,11],index_col=0,na_values=['NA'])
    Rules['Spatial_Resolution_Shen'] = pd.read_excel(xls, 'Resolution_shen', skiprows=[8,9,10], index_col=None, na_values=['NA'])
    Rules['Measurement_Shen'] = pd.read_excel(xls, 'Measurement_shen', skiprows=[8,9,10,11],index_col=0,na_values=['NA'])


#print(Rules['Spatial_Resolution'])
#print(Rules['Measurement'])

spatialRes = ['2 x 2.5 deg.','1.0 x 1.25 deg.','1 x 1.25 deg.','0.5 x 0.625 deg.','0.125 deg.','1 deg.','0.1 deg.','0.667 x 1.25 deg.','0.5 deg.','5000 m','0.05 deg.','5600 m','0.25 deg.','0.5 x 0.667 deg.','1.25 deg.']
events = ['Hurricane','TropicalStorm','VolcanicEruption','Flood','Fire','DustStorm','Drought']

def fun(i,x,sheetname):

    y = (str(Rules[sheetname][spatialRes[x]][i]))
    yy = y.split(' ')

    if(yy[0].upper()=='GREAT'):
        f.write('(?assertion dd:compatibilityValue dd:strong_compatibility),'+"\n")
        f.write('(?assertion dd:assertionConfidence \"'+"0.5"+'\"^^xsd:double),'+"\n")
    elif(yy[0].upper()=='GOOD'):
        f.write('(?assertion dd:compatibilityValue dd:some_compatibility),'+"\n")
        f.write('(?assertion dd:assertionConfidence \"'+"0.5"+'\"^^xsd:double),'+"\n")
    elif(yy[0].upper()=='OK'):
        f.write('(?assertion dd:compatibilityValue dd:slight_compatibility),'+"\n")
        f.write('(?assertion dd:assertionConfidence \"'+"0.5"+'\"^^xsd:double),'+"\n")
    elif(yy[0].upper()=='BAD'):
        f.write('(?assertion dd:compatibilityValue dd:negative_compatibility),'+"\n")
        f.write('(?assertion dd:assertionConfidence \"'+"0.5"+'\"^^xsd:double),'+"\n")
    elif(yy[0].upper()=='GREAT?'):
        f.write('(?assertion dd:compatibilityValue dd:some_compatibility),'+"\n")
        f.write('(?assertion dd:assertionConfidence \"'+"0.25"+'\"^^xsd:double),'+"\n")
    elif(yy[0].upper()=='GOOD?'):
        f.write('(?assertion dd:compatibilityValue dd:some_compatibility),'+"\n")
        f.write('(?assertion dd:assertionConfidence \"'+"0.25"+'\"^^xsd:double),'+"\n")
    elif(yy[0].upper()=='OK?'):
        f.write('(?assertion dd:compatibilityValue dd:slight_compatibility),'+"\n")
        f.write('(?assertion dd:assertionConfidence \"'+"0.25"+'\"^^xsd:double),'+"\n")
    elif(yy[0].upper()=='BAD?'):
        f.write('(?assertion dd:compatibilityValue dd:negative_compatibility),'+"\n")
        f.write('(?assertion dd:assertionConfidence \"'+"0.25"+'\"^^xsd:double),'+"\n")
    else:
        f.write('(?assertion dd:compatibilityValue dd:indifferent_compatibility),'+"\n")
        f.write('(?assertion dd:assertionConfidence \"'+"0.5"+'\"^^xsd:double),'+"\n")

    #f.write('(?assertion dd:assertionConfidence \"'+yy[1]+'\"^^xsd:double),'+"\n")
    #f.write('(?assertion dd:assertionConfidence \"'+"0.5"+'\"^^xsd:double),'+"\n")
f = open('spatial_res_Li.rules','w')
f.write('@prefix dd: <http://www.purl.org/twc/ns/darkdata#>.'+'\n'+
    '@prefix ddspatial:<http://darkdata.tw.rpi.edu/data/spatial-resolution/>.'+"\n")

sheetname1 = 'Spatial_Resolution_Li'

for i in range(0,len(events)):
    f.write("\n"+"#"+events[i]+"\n")
    for j in range(0,len(spatialRes)):
        f.write("["+events[i]+"-"+str(Rules[sheetname1][spatialRes[j]].name).replace(' ','+')+":"+"\n")
        f.write("(?candidate dd:candidateEvent ?event),"+"\n"+
        "(?event rdf:type dd:"+events[i]+"),"+"\n"+
        "(?candidate dd:candidateVariable ?variable),"+"\n"+
        "(?variable dd:spatialResolution <http://darkdata.tw.rpi.edu/data/spatial-resolution/"+str(Rules[sheetname1][spatialRes[j]].name).replace(' ','+')+">),"+"\n"+
        "makeSkolem(?assertion, ?candidate, ?event, dd:"+events[i]+", "+"<http://darkdata.tw.rpi.edu/data/spatial-resolution/"+str(Rules[sheetname1][spatialRes[j]].name).replace(' ','+')+"> ,?variable)" +"\n"+
        "->"+"\n"+
        "(?candidate dd:compatibilityAssertion ?assertion),"+"\n"+
        "(?assertion rdf:type dd:CompatibilityAssertion),"+"\n"
        )
        fun(i,j,sheetname1)
        f.write("(?assertion dd:basisForAssertion <urn:rule/spatial_res/"+events[i]+"-"+str(Rules[sheetname1][spatialRes[j]].name).replace(' ','+')+">)"+"\n"+"]"+"\n")

    f.write('\n')

f.close()

f = open('spatial_res_shen.rules','w')
f.write('@prefix dd: <http://www.purl.org/twc/ns/darkdata#>.'+'\n'+
    '@prefix ddspatial:<http://darkdata.tw.rpi.edu/data/spatial-resolution/>.'+"\n")
sheetname2 = 'Spatial_Resolution_Shen'
for i in range(0,len(events)):
    f.write("\n"+"#"+events[i]+"\n")
    for j in range(0,len(spatialRes)):
        f.write("["+events[i]+"-"+str(Rules[sheetname2][spatialRes[j]].name).replace(' ','+')+":"+"\n")
        f.write("(?candidate dd:candidateEvent ?event),"+"\n"+
        "(?event rdf:type dd:"+events[i]+"),"+"\n"+
        "(?candidate dd:candidateVariable ?variable),"+"\n"+
        "(?variable dd:spatialResolution <http://darkdata.tw.rpi.edu/data/spatial-resolution/"+str(Rules[sheetname2][spatialRes[j]].name).replace(' ','+')+">),"+"\n"+
        "makeSkolem(?assertion, ?candidate, ?event, dd:"+events[i]+", "+"<http://darkdata.tw.rpi.edu/data/spatial-resolution/"+str(Rules[sheetname2][spatialRes[j]].name).replace(' ','+')+"> ,?variable)" +"\n"+
        "->"+"\n"+
        "(?candidate dd:compatibilityAssertion ?assertion),"+"\n"+
        "(?assertion rdf:type dd:CompatibilityAssertion),"+"\n"
        )
        fun(i,j,sheetname2)
        f.write("(?assertion dd:basisForAssertion <urn:rule/spatial_res/"+events[i]+"-"+str(Rules[sheetname2][spatialRes[j]].name).replace(' ','+')+">)"+"\n"+"]"+"\n")

    f.write('\n')
