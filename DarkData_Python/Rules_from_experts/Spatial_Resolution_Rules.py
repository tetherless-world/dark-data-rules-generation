import pandas as pd
import xlrd

Rules = {}

with pd.ExcelFile('X Applicability to Phenomena.xlsx') as xls:
    Rules['Spatial_Resolution'] = pd.read_excel(xls, 'Spatial Resolution', skiprows=[8,9,10], index_col=None, na_values=['NA'])
    Rules['Spatial_Resolution'] = pd.read_excel(xls, 'Spatial Resolution', skiprows=[8,9,10], index_col=None, na_values=['NA'])
    Rules['Measurement'] = pd.read_excel(xls, 'Measurement', skiprows=[8,9,10,11],index_col=0,na_values=['NA'])


#print(Rules['Spatial_Resolution'])
#print(Rules['Measurement'])

spatialRes = ['2 x 2.5 deg.','1.0 x 1.25 deg.','1 x 1.25 deg.','0.5 x 0.625 deg.','0.125 deg.','1 deg.','0.1 deg.','0.667 x 1.25 deg.','0.5 deg.','5000 m','0.05 deg.','5600 m','0.25 deg.','0.5 x 0.667 deg.','1.25 deg.']
events = ['Hurricane','TropicalStorm','VolcanicEruption','Flood','Fire','DustStorm','Drought']

def fun(i,x):

    y = (str(Rules['Spatial_Resolution'][spatialRes[x]][i]))
    yy = y.split(' ')

    if(yy[0]=='GREAT'):
        f.write('(?assertion dd:compatibilityValue dd:strong_compatibility),'+"\n")
    elif(yy[0]=='GOOD'):
        f.write('(?assertion dd:compatibilityValue dd:some_compatibility),'+"\n")
    elif(yy[0]=='OK'):
        f.write('(?assertion dd:compatibilityValue dd:slight_compatibility),'+"\n")
    elif(yy[0]=='BAD'):
        f.write('(?assertion dd:compatibilityValue dd:negative_compatibility),'+"\n")
    else:
        f.write('(?assertion dd:compatibilityValue dd:indifferent_compatibility),'+"\n")

    f.write('(?assertion dd:assertionConfidence \"'+yy[1]+'\"^^xsd:double)'+"\n")

f = open('spatial_res.rules','w')
f.write('@prefix dd: <http://www.purl.org/twc/ns/darkdata#>.'+'\n'+
    '@prefix ddspatial:<http://darkdata.tw.rpi.edu/data/spatial-resolution/>.'+"\n")

for i in range(0,len(events)):
    f.write("\n"+"#"+events[i]+"\n")
    for j in range(0,len(spatialRes)):
        f.write("["+events[i]+"-"+str(Rules['Spatial_Resolution'][spatialRes[j]].name).replace(' ','+')+":"+"\n")
        f.write("(?candidate dd:candidateEvent ?event),"+"\n"+
        "(?event rdf:type dd:"+events[i]+"\n"+
        "(?candidate dd:candidateVariable ?variable),"+"\n"+
        "(?variable dd:spatialResolution ddspatial:"+str(Rules['Spatial_Resolution'][spatialRes[j]].name).replace(' ','+')+"\n"+
        "makeSkolem(?assertion, ?candidate, ?event, dd:"+events[i]+", ?variable)" +"\n"+
        "->"+"\n"+
        "(?candidate dd:compatibilityAssertion ?assertion),"+"\n"+
        "(?assertion rdf:type dd:CompatibilityAssertion),"+"\n"
        )
        fun(i,j)
        f.write("(?assertion dd:basisForAssertion <urn:rule/spatial_res/"+events[i]+"-"+str(Rules['Spatial_Resolution'][spatialRes[j]].name).replace(' ','+')+">"+"\n"+"]"+"\n")

    f.write('\n')

