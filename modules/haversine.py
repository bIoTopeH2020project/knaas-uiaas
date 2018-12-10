import math
def haversine (lat1, lon1, lat2, lon2):
    r = 6371
    x1 = math.radians(lat1-25.289266)
    y1 = math.radians(lon1-51.564183)
    h1 = math.asin(math.sqrt(math.pow(math.sin(x1/2),2)+math.cos(lat1)*math.cos(25.289266)*math.pow(math.sin(y1/2),2)))
    distance1 = 2*r*h1
    x2 = math.radians(lat2-25.289266)
    y2 = math.radians(lon2-51.564183)
    h2 = math.asin(math.sqrt(math.pow(math.sin(x2/2),2)+math.cos(lat2)*math.cos(25.289266)*math.pow(math.sin(y2/2),2)))
    distance2 = 2*r*h2    
    if distance1 < distance2:
        result = 0
    else:
        result = 1
    return(result)

def rightgate (lat1, lon1):
    r = 6371
    
    gate1 = [25.288238,51.563434]
    gate2 = [25.290555,51.564410]
    gate3 = [25.288780,51.565461]
    x1 = math.radians(lat1-gate1[0])
    y1 = math.radians(lon1-gate1[1])
    h1 = math.asin(math.sqrt(math.pow(math.sin(x1/2),2)+math.cos(lat1)*math.cos(gate1[0])*math.pow(math.sin(y1/2),2)))
    distance1 = 2*r*h1
    x2 = math.radians(lat1-gate2[0])
    y2 = math.radians(lon1-gate2[1])
    h2 = math.asin(math.sqrt(math.pow(math.sin(x2/2),2)+math.cos(lat1)*math.cos(gate2[0])*math.pow(math.sin(y2/2),2)))
    distance2 = 2*r*h2  
    x3 = math.radians(lat1-gate3[0])
    y3 = math.radians(lon1-gate3[1])
    h3 = math.asin(math.sqrt(math.pow(math.sin(x3/2),2)+math.cos(lat1)*math.cos(gate3[0])*math.pow(math.sin(y3/2),2)))
    distance3 = 2*r*h3 
    
    if (distance1 < distance2 and distance1 < distance3):
        result = 'Gate 1, with lat= ' + str(gate1[0]) + ', lon= ' + str(gate1[1]) + ', is your best option'
    elif (distance2 < distance1 and distance2 < distance3):
        result = 'Gate 2, with lat= ' + str(gate2[0]) +', lon= ' + str(gate2[1]) + ', is your best option'
    else:
        result = 'Gate 3, with lat= ' + str(gate3[0]) + ', lon= ' + str(gate3[1]) + ', is your best option'
    return(result)

