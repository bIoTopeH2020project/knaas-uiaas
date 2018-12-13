def working (number):
    if number =='200':
        return ('Extract Response O-MI Node: Success in reading O-MI Node Contents');
    else:
        return ('Extract Response O-MI Node: Failure in reading O-MI Node Contents');

def code (things):
    import time
    nodeName = 'Lyon'
    lstForGeo = []
    parsedGeoAndCorrespondingTemp = []
    lstForPOI = []
    tempList = []
    for items in things['Object']:
        tempid = items['id'][0]
        if tempid == 'OrganizationalUnit:DINSI':
            templist = items['Object']
            for objs in templist:
                tempid2 = objs['id'][0]
                if tempid2 == 'Deployment:Sensing-Labs-IP68-Outdoor-Temperature-Sensor:I':
                    lstForPOI = objs['Object']


    for geoloc in lstForPOI:
        infoItem = geoloc['InfoItem']
        ids = geoloc['id'][0]
        date = time.strftime('%Y/%m/%d')
        dayPart = time.strftime('%X')
        if dayPart[:2] == '20':
            dayPart = 'night'
        elif dayPart[:2] == '07':
            dayPart = 'morning'
        
        if ids[:6] == 'Sensor': 
            objectItem = geoloc['Object']
            longitude = 0
            latitude = 0
            resultTemp = 0
    
            for item in infoItem:
                if item['$']['name'] == 'geo:long':
                    longitude = item['value'][0]['_']
                elif item['$']['name'] =='geo:lat':
                    latitude = item['value'][0]['_']

        
            for items in objectItem:
                if items['$']['type'] == 'sosa:Observation':
                    resultTemp = items['InfoItem'][0]['value'][0]['_']
                    lstForGeo.append({'geo':[longitude, latitude],'temp':resultTemp, 'date':date, 'time':dayPart})
                    parsedGeoAndCorrespondingTemp.append({'lon':float(longitude), 'lat':float(latitude),'date':date,
                                                          'time':dayPart, 'temperature':float(resultTemp), 'name':ids, 'layer':'heatWave'})
    return parsedGeoAndCorrespondingTemp;










