import pandas as pd
import xlrd

Rules = {}

with pd.ExcelFile('X Applicability to Phenomena from experts.xlsx') as xls:
    Rules['Spatial_Resolution_Li'] = pd.read_excel(xls, 'Spatial Resolution', skiprows=[8,9,10], index_col=None, na_values=['NA'])
    Rules['Measurement_Li'] = pd.read_excel(xls, 'Measurement', skiprows=[8,9,10,11],index_col=0,na_values=['NA'])
    Rules['Spatial_Resolution_Shen'] = pd.read_excel(xls, 'Resolution_shen', skiprows=[8,9,10], index_col=None, na_values=['NA'])
    Rules['Measurement_Shen'] = pd.read_excel(xls, 'Measurement_shen', skiprows=[8,9,10,11],index_col=0,na_values=['NA'])

#print(Rules['Spatial_Resolution'])
#print(Rules['Measurement']['Sensible Heat Flux'])

measurements = ['Sensible Heat Flux','Wind Stress Direction','Latent Heat Flux','Wind','Albedo','Wind Velocity','Dust','NO2','CO2','Incident Radiation','Ground Heat','Statistics','Geopotential','Soil Temperature','Heat Flux','Soil Moisture']
events = ['Hurricane','TropicalStorm','VolcanicEruption','Flood','Fire','DustStorm','Drought']

def fun(i,x,sheetname):

    y = (str(Rules[sheetname][measurements[x]][i]))
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
f = open('measurement_Li.rules','w')
f.write('@prefix dd: <http://www.purl.org/twc/ns/darkdata#>.'+'\n'+
    '@prefix ddmeasurement: <http://darkdata.tw.rpi.edu/data/measurement/>.'+"\n")

sheetname1 = 'Measurement_Li'

for i in range(0,len(events)):
    f.write("\n"+"#"+events[i]+"\n")
    for j in range(0,len(measurements)):
        f.write("["+events[i]+"-"+str(Rules[sheetname1][measurements[j]].name).replace(' ','+')+":"+"\n")
        f.write("(?candidate dd:candidateEvent ?event),"+"\n"+
        "(?event rdf:type dd:"+events[i]+"),"+"\n"+
        "(?candidate dd:candidateVariable ?variable),"+"\n"+
        "(?variable dd:measurement ddmeasurement:"+str(Rules[sheetname1][measurements[j]].name).replace(' ','+')+"),"+"\n"+
        "makeSkolem(?assertion, ?candidate, ?event, dd:"+events[i]+" ,"+"ddmeasurement:"+str(Rules[sheetname1][measurements[j]].name).replace(' ','+')+", ?variable)" +"\n"+
        "->"+"\n"+
        "(?candidate dd:compatibilityAssertion ?assertion),"+"\n"+
        "(?assertion rdf:type dd:CompatibilityAssertion),"+"\n"
        )
        fun(i,j,sheetname1)
        f.write("(?assertion dd:basisForAssertion <urn:rule/measurement/"+events[i]+"-"+str(Rules[sheetname1][measurements[j]].name).replace(' ','+')+">"+")"+"\n"+"]"+"\n")

    f.write('\n')
f.close()


f = open('measurement_Shen.rules','w')
f.write('@prefix dd: <http://www.purl.org/twc/ns/darkdata#>.'+'\n'+
    '@prefix ddmeasurement: <http://darkdata.tw.rpi.edu/data/measurement/>.'+"\n")

sheetname2 = 'Measurement_Shen'
for i in range(0,len(events)):
    f.write("\n"+"#"+events[i]+"\n")
    for j in range(0,len(measurements)):
        f.write("["+events[i]+"-"+str(Rules[sheetname2][measurements[j]].name).replace(' ','+')+":"+"\n")
        f.write("(?candidate dd:candidateEvent ?event),"+"\n"+
        "(?event rdf:type dd:"+events[i]+"),"+"\n"+
        "(?candidate dd:candidateVariable ?variable),"+"\n"+
        "(?variable dd:measurement ddmeasurement:"+str(Rules[sheetname2][measurements[j]].name).replace(' ','+')+"),"+"\n"+
        "makeSkolem(?assertion, ?candidate, ?event, dd:"+events[i]+" ,"+"ddmeasurement:"+str(Rules[sheetname2][measurements[j]].name).replace(' ','+')+", ?variable)" +"\n"+
        "->"+"\n"+
        "(?candidate dd:compatibilityAssertion ?assertion),"+"\n"+
        "(?assertion rdf:type dd:CompatibilityAssertion),"+"\n"
        )
        fun(i,j,sheetname2)
        f.write("(?assertion dd:basisForAssertion <urn:rule/measurement/"+events[i]+"-"+str(Rules[sheetname2][measurements[j]].name).replace(' ','+')+">"+")"+"\n"+"]"+"\n")

    f.write('\n')
f.close()