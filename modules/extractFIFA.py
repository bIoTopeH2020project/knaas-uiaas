def working (number):
    if number =='200':
        return ('Extract Response O-MI Node: Success in reading O-MI Node Contents');
    else:
        return ('Extract Response O-MI Node: Failure in reading O-MI Node Contents');

def code (things, topic):
    import time
    nodeName = 'Doha'
    lstForGeo = []
    parsedGeoAndCorrespondingTemp = []
    lstForPOI = []
    tempList = []
    if topic == 'Health':
        for items in things['Object']:
            tempid = items['id'][0]
            if tempid == 'Health Unit':
                templist = items['Object']
                for objs in templist:
                    tempid2 = objs['id'][0]
                    if tempid2[:7] == 'Vehicle':
                        lstForPOI = objs['Object']
                        infoItem = objs['InfoItem']
                        for item in infoItem:
                            if item['$']['name'] == 'geo:long':
                                longitude = item['value'][0]
                            elif item['$']['name'] =='geo:lat':
                                latitude = item['value'][0]

                        for geoloc in lstForPOI:
                            ids = geoloc['id'][0]
                            date = time.strftime('%Y/%m/%d')
                            dayPart = time.strftime('%X')
                            
                            if ids[:7] == 'vehicle': 
                                for items in geoloc['InfoItem']:
                                    if items['$']['name'] == 'plate':
                                        plate = items ['value'][0]
                                    if items['$']['name'] == 'Model':
                                        model = items ['value'][0] 
                    
                            if ids[:6] == 'person': 
                                for items in geoloc['InfoItem']:
                                    if items['$']['name'] == 'DNI':
                                        DNI = items ['value'][0]
                                    if items['$']['name'] == 'Name':
                                        Name = items ['value'][0] 

                        lstForGeo.append({'geo':[longitude, latitude], 'Plate Number':plate,'Vehicle Model':model, 'Responsible ID':DNI,'Responsible Name':Name, 'date':date, 'time':dayPart})
                        parsedGeoAndCorrespondingTemp.append({'lon':float(longitude), 'lat':float(latitude), 'Plate Number':plate,'Vehicle Model':model, 'date':date, 'Responsible ID':DNI,
                                                              'Responsible Name':Name, 'name':ids, 'layer':'Fifa World Cup'})
    
    if topic == 'Fire':
        for items in things['Object']:
            tempid = items['id'][0]
            if tempid == 'Fire Unit':
                templist = items['Object']
                for objs in templist:
                    tempid2 = objs['id'][0]
                    if tempid2[:7] == 'Vehicle':
                        lstForPOI = objs['Object']
                        infoItem = objs['InfoItem']
                        for item in infoItem:
                            if item['$']['name'] == 'geo:long':
                                longitude = item['value'][0]
                            elif item['$']['name'] =='geo:lat':
                                latitude = item['value'][0]

                        for geoloc in lstForPOI:
                            ids = geoloc['id'][0]
                            date = time.strftime('%Y/%m/%d')
                            dayPart = time.strftime('%X')
                            
                            if ids[:7] == 'vehicle': 
                                for items in geoloc['InfoItem']:
                                    if items['$']['name'] == 'plate':
                                        plate = items ['value'][0]
                                    if items['$']['name'] == 'Model':
                                        model = items ['value'][0] 
                    
                            if ids[:6] == 'person': 
                                for items in geoloc['InfoItem']:
                                    if items['$']['name'] == 'DNI':
                                        DNI = items ['value'][0]
                                    if items['$']['name'] == 'Name':
                                        Name = items ['value'][0] 

                        lstForGeo.append({'geo':[longitude, latitude], 'Plate Number':plate,'Vehicle Model':model, 'Responsible ID':DNI,'Responsible Name':Name, 'date':date, 'time':dayPart})
                        parsedGeoAndCorrespondingTemp.append({'lon':float(longitude), 'lat':float(latitude), 'Plate Number':plate,'Vehicle Model':model, 'date':date, 'Responsible ID':DNI,
                                                              'Responsible Name':Name, 'name':ids, 'layer':'Fifa World Cup'})
    
    if topic == 'Safety':
        for items in things['Object']:
            tempid = items['id'][0]
            if tempid == 'Police Station':
                templist = items['Object']
                for objs in templist:
                    tempid2 = objs['id'][0]
                    if tempid2[:7] == 'Vehicle':
                        lstForPOI = objs['Object']
                        infoItem = objs['InfoItem']
                        for item in infoItem:
                            if item['$']['name'] == 'geo:long':
                                longitude = item['value'][0]
                            elif item['$']['name'] =='geo:lat':
                                latitude = item['value'][0]

                        for geoloc in lstForPOI:
                            ids = geoloc['id'][0]
                            date = time.strftime('%Y/%m/%d')
                            dayPart = time.strftime('%X')
                            
                            if ids[:7] == 'vehicle': 
                                for items in geoloc['InfoItem']:
                                    if items['$']['name'] == 'plate':
                                        plate = items ['value'][0]
                                    if items['$']['name'] == 'Model':
                                        model = items ['value'][0] 
                    
                            if ids[:6] == 'person': 
                                for items in geoloc['InfoItem']:
                                    if items['$']['name'] == 'DNI':
                                        DNI = items ['value'][0]
                                    if items['$']['name'] == 'Name':
                                        Name = items ['value'][0] 

                        lstForGeo.append({'geo':[longitude, latitude], 'Plate Number':plate,'Vehicle Model':model, 'Responsible ID':DNI,'Responsible Name':Name, 'date':date, 'time':dayPart})
                        parsedGeoAndCorrespondingTemp.append({'lon':float(longitude), 'lat':float(latitude), 'Plate Number':plate,'Vehicle Model':model, 'date':date, 'Responsible ID':DNI,
                                                              'Responsible Name':Name, 'name':ids, 'layer':'Fifa World Cup'})
    return parsedGeoAndCorrespondingTemp;




