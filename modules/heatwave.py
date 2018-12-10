def heatwave(befyestdata,yestdata,todata):
    if befyestdata<yestdata:
        if yestdata<todata:
            return ("Lyon, We have a heatwave");
        else:
            return ("No worries, we are not in a heatwave");
    else:
        return ("No worries, we are not in a heatwave");

def heatwaveEHF(befyestdata,yestdata,todata):
    if befyestdata>0:
        if yestdata>0:
            if todata>0:
                return ("Lyon, We have a heatwave");
            else:
                return ("No worries, we are not in a heatwave");  
        else:
            return ("No worries, we are not in a heatwave");
    else:
        return ("No worries, we are not in a heatwave");

def excessheatfactor(a,b):
    import numpy as np
    T=[]
    for i in range (33):
        x=str(32-i)
        T.append(a['temperature'][x])

    Theat = np.sum(T[:3])
    Tav=np.sum(T[3:])
    Theat/=3
    Tav/=30
    T90 = b

    EHIsig = Theat-T90
    EHIacc = Theat -Tav
    if EHIacc >= 1:
        y = EHIacc
    else:
        y = 1
    EHF = EHIsig*y 
    date =  a['date']['32']  
    q=1
    return ([({'date':date, 'EHIsig':EHIsig, 'EHIaccreal':EHIacc, 'EHIacc':y, 
               'EHF':EHF,'q':q})])




