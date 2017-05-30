import json
import datetime
import pandas as pd
import numpy as np
from pymongo import MongoClient, GEO2D
from pymongo.errors import BulkWriteError
import requests
from yaml import load, dump
from bson import json_util
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def get_netatmo_token(client_id=None, client_secret=None, username=None, password=None):

    assert client_id and client_secret and username and password != None, "No args in get_netatmo_token !\n"

    data = dict(grant_type='password', client_id=client_id, client_secret=client_secret, 
                username=username, password=password, scope='read_station')
    resp = requests.post('https://api.netatmo.com/oauth2/token', data=data)

    if resp.status_code == 200:
        token = resp.json()
        return token['access_token']
    return None

def get_data(api, username=None, password=None): #better: request_data
    return requests.get(api, auth=(username, password))

def clean_lyon_data(lyon_request, furtherInfo=True):
    
    assert lyon_request.status_code == 200, "No data in clean_lyon_data !\n"
    
    lyon_data = lyon_request.json()
    lyon_data = lyon_data['features']
    
    res = []
    for data in lyon_data:
        dic = data['properties']
        if data['geometry']['type'] == "LineString":
            location = data['geometry']['coordinates']
        elif data['geometry']['type'] == "MultiLineString":
            location = data['geometry']['coordinates'][0]
        else:
            raise ValueError(" Unknown data['geometry']['type']:" + data['geometry']['type'] + 'in Lyon Traffic Data')
        #[location[0][0], location[0][1]] #[<longitude>, <latitude>]
        dic['loc']   =  { "type" : "Point",
                          "coordinates" : [ location[0][0], location[0][1]]}

        dic['name']  = dic['twgid']
        _ = dic.pop('twgid', None)
        dic['last_update'] = datetime.datetime.strptime(dic['last_update'], '%Y-%m-%d %H:%M:%S')
        dic['last_update_fme'] = datetime.datetime.strptime(dic['last_update_fme'], '%Y-%m-%d %H:%M:%S')
        if furtherInfo:
            dic['layer'] = 'traffic'
            dic['icon']  = "car"
            dic['iconColor'] = "red"
        res.append(dic)
    
    return res

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def clean_lyon_data2(lyon_data, furtherInfo=True):
    
    res = []
    for data in lyon_data:
        dic = dict(data['properties'])    #, default=myconverter)
        if data['geometry']['type'] == "LineString":
            location = data['geometry']['coordinates']
        elif data['geometry']['type'] == "MultiLineString":
            location = data['geometry']['coordinates'][0]
        else:
            raise ValueError(" Unknown data['geometry']['type']:" + data['geometry']['type'] + 'in Lyon Traffic Data')
        dic['loc']   = { "type" : "Point",
                          "coordinates" : [ location[0][0], location[0][1]]}
        dic['name']  = dic['twgid']
        _ = dic.pop('twgid', None)
        dic['last_update']     = datetime.datetime.strptime(dic['last_update'], '%Y-%m-%d %H:%M:%S')
        dic['last_update_fme'] = datetime.datetime.strptime(dic['last_update_fme'], '%Y-%m-%d %H:%M:%S')
        
        if furtherInfo:
            dic['layer'] = 'traffic'
            dic['icon']  = "car"
            dic['iconColor'] = "red"
        if any(id(dic) == id(x) for x in res):
            continue
        else:
            res.append(dic)
    
    return res

def clean_netatmo_data(netatmo_api, furtherInfo=True, overwriteDate=None):
    
    netatmo_request = requests.get(netatmo_api)
    assert netatmo_request.status_code == 200, "No data in clean_lyon_data !\n"
    
    netatmo_data = netatmo_request.json()
    if overwriteDate:
        last_update_fme = overwriteDate
    else:
        ts = netatmo_data['time_server']
        last_update_fme = datetime.datetime.fromtimestamp(ts)#.strftime('%Y-%m-%d %H:%M:%S')
    netatmo_data = netatmo_data['body']
    
    res = []
    for data in netatmo_data:
        dic = {}
        id_ = data['_id']
        location = data['place']['location']
        for measure in data['measures']:
            if 'res' in data['measures'][measure] and 'temperature' in data['measures'][measure]['type']:
                aux = data['measures'][measure]['res']
                for code in aux:
                    dic['temp']  = aux[code][0]
                    dic['pres']  = aux[code][1]
                break
        #  [location[0], location[1]] #[<longitude>, <latitude>]
        dic['loc']   = { "type" : "Point",
                         "coordinates" : [ location[0], location[1] ] }
        dic['name']  = id_
        dic['last_update_fme'] = last_update_fme
       
        if furtherInfo:
            dic['layer'] = "netatmo";
            dic['icon']  = "globe";
            dic['iconColor'] = "orange";
        res.append(dic)
    
    return res


def clean_netatmo_data2(netatmo_data, furtherInfo=True, overwriteDate=None):
    
    #netatmo_request = requests.get(netatmo_api)
    #assert netatmo_request.status_code == 200, "No data in clean_lyon_data !\n"
    
    #netatmo_data = netatmo_request.json()
    if overwriteDate:
        last_update_fme = overwriteDate
    else:
        ts = netatmo_data['time_server']
        last_update_fme = datetime.datetime.fromtimestamp(ts)#.strftime('%Y-%m-%d %H:%M:%S')
    netatmo_data = netatmo_data['body']
    
    res = []
    for data in netatmo_data:
        dic = {}
        id_ = data['_id']
        location = data['place']['location']
        for measure in data['measures']:
            if 'res' in data['measures'][measure] and 'temperature' in data['measures'][measure]['type']:
                aux = data['measures'][measure]['res']
                for code in aux:
                    dic['temp']  = aux[code][0]
                    dic['pres']  = aux[code][1]
                break
        dic['loc']   = { "type" : "Point",
                         "coordinates" : [ location[0], location[1] ] }
        dic['name']  = id_
        dic['last_update_fme'] = last_update_fme
       
        if furtherInfo:
            dic['layer'] = "netatmo";
            dic['icon']  = "globe";
            dic['iconColor'] = "orange";
        res.append(dic)
    
    return res


def read_data(configFile='config.yml', sameDate=True):

    stream = file(configFile, 'r')
    data = load(stream, Loader=Loader)

    # Netatmo Get Data Through Rest API:
    token = get_netatmo_token(data['netatmo_client_id'], data['netatmo_client_secret'], 
                              data['netatmo_username'], data['netatmo_password'])
    netatmo_api = data['netatmo_rest_api'][0] + token + data['netatmo_rest_api'][1]

    netatmo_request = get_data(data['netatmo_rest_api'][0]+token)

    # Lyon Get Data Through Rest API:
    lyon_request = get_data(data['lyon_rest_api'], data['lyon_username'], data['lyon_password'])

    # Clean both data streams:
    data_lyon = clean_lyon_data(lyon_request)
    if sameDate:
        overwriteDate = data_lyon[0]['last_update_fme']
    else:
        overwriteDate = None
    data_netatmo = clean_netatmo_data(netatmo_api, overwriteDate=overwriteDate)

    return {'lyon': data_lyon, 'netatmo': data_netatmo, 'datetime': overwriteDate}


def _connect_mongo(host, port, username, password, db):
    """ A util for making a connection to mongo """

    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    return conn[db]

def insert_mongo(db, collection, data, host='mongodb', port=27017, username=None, password=None):
    """ Insert a bunch of data into Mongo """
    
    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)
    
    try:
        res = db[collection].insert_many(data)
    except BulkWriteError as bwe:
        print bwe.details
        raise

    return res

#http://api.mongodb.com/python/current/examples/geo.html
#http://stackoverflow.com/questions/16249736/how-to-import-data-from-mongodb-to-pandas
def read_mongo(db, collection, query={}, host='mongodb', port=27017, username=None, password=None, limit_num = None, no_id=True):
    """ Read from Mongo and Store into DataFrame """

    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    if limit_num:
        assert type(limit_num) is int, "@read_mongo: id is not an integer: %r" % id
        cursor = db[collection].find(query).limit(limit_num)
    else:
        cursor = db[collection].find(query)

    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))

    # Delete the _id
    if no_id:
        del df['_id']

    return df

#http://alexgaudio.com/2012/07/07/monarymongopandas.html
#http://stats.stackexchange.com/questions/1174/how-can-i-test-if-given-samples-are-taken-from-a-poisson-distribution
#http://stackoverflow.com/questions/37941881/how-to-implement-poisson-regression
#https://pymc-devs.github.io/pymc3/notebooks/GLM-poisson-regression.html

def find_road(db, collection, street_name, date=None, host='mongodb', port=27017, username=None, password=None):
    
    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)
    
    if date:
        query = { "$and": [ { "layer": 'traffic' }, \
		            {"last_update_fme": {"$eq": date}}, \
		            {"libelle": street_name} ] }
    else:
        query = { "$and": [ { "layer": 'traffic' }, \
		            {"libelle": street_name} ] }
                        
    cursor = list(db[collection].find(query))

    if cursor:
        return cursor[0]
    else:
        return None


def find_near_sensors(db, collection, geo, date=None, host='mongodb', port=27017, username=None, password=None, limit_num = None):
    
    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

    if date:
        query = { "$and": [ { "layer": 'netatmo' }, 
                            {"last_update_fme": {"$eq": date}}, \
                            #{"loc": {"$near": [geo[0], geo[1]]}} ] }
                            {"loc": {"$nearSphere": { "$geometry" : { "type" : "Point" ,
                                               	"coordinates" : [geo[0], geo[1]] }
          					}
                                    }
                            } ] }

#{
            
    else:
        query = { "$and": [ { "layer": 'netatmo' }, 
                            {"loc": {"$nearSphere": { "$geometry" : { "type" : "Point" ,
                                               	"coordinates" : [geo[0], geo[1]] }
          					}
                                    }
                            } ] }
                        
    if limit_num:
        assert type(limit_num) is int, "@find_near_sensors: id is not an integer: %r" % id
        cursor = db[collection].find(query).limit(limit_num)
    else:
        cursor = db[collection].find(query)
                        
    return list(cursor)


def floatize(frame):
    for index, row in frame.iterrows():
        #print 'The speed is:' + row['vitesse']
        frame.set_value(index,'longueur',int(row['longueur']))
        #frame.set_value(index,'temp'    ,float(row['temp']))
        #frame.set_value(index,'pres'    ,float(row['pres']))
	frame.set_value(index,'vitesse' ,float(row['vitesse'].replace(' km/h','')) if row['vitesse'] else None)
    frame.longueur = frame.longueur.astype(np.float32)
    frame.vitesse = frame.vitesse.astype(np.float32)
    return


def create_frame(db, collection, street_name, dates=[], limit_num = None):
     #from pandas import to_numeric

    results=[]

    lyon_exclude = ['_id', 'code', 'fournisseur', 'gid', 'icon', 'iconColor', 'last_update', 'last_update_fme',
                    'id_fournisseur', 'ids_ptm', 'layer', 'libelle']

    for date in dates:
        res = find_road(db=db, collection=collection, street_name=street_name, date=date)
        for exclusion in lyon_exclude:
            _ = res.pop(exclusion, None)
   
        #print res['loc']   

        sensors = find_near_sensors(db=db, collection=collection, geo=res['loc']["coordinates"], date=date, limit_num=limit_num)
        #print(sensors, 'geiaaa')
        _ = res.pop('loc', None)

        
        #{ "type" : "Point",
        #   "coordinates" : [ location[0], location[1] ] 
        #}
        temp_mean = 0.0
        pres_mean = 0.0

        for sensor in sensors:
            #print(sensor['temp'], sensor['pres'])
            temp_mean += sensor['temp']
            pres_mean += sensor['pres']

        temp_mean = (1.0*temp_mean)/limit_num
        pres_mean = (1.0*pres_mean)/limit_num

        res['temp'] = temp_mean
        res['pres'] = pres_mean

        results.append(res)
    #else:
    #    results = find_road(db=db, collection=collection, street_name=street_name, date=None)

    print results

    results = pd.DataFrame(results)
    #print results
    floatize(results)
    results = pd.DataFrame(results)
    #results[['longueur','vitesse']] = results[['longueur','vitesse']].apply(pd.to_numeric)


    return results
    #u'_id': ObjectId('58c16da60bba280c3042759b'),
    #u'code': u'LYO01623',
    #u'etat': u'*',
    #u'fournisseur': u'CRITER',
    #u'gid': u'2677',
    #u'icon': u'car',
    #u'iconColor': u'red',
    #u'id_fournisseur': u'',
    #u'ids_ptm': u'',
    #u'last_update': datetime.datetime(2017, 3, 9, 15, 57, 50),
    #u'last_update_fme': datetime.datetime(2017, 3, 9, 15, 58, 3),
    #u'layer': u'traffic',
    #u'libelle': u'R DU DAUPHINE',
    #u'loc': [4.920427697160733, 45.71192648948453],
    #u'longueur': u'1087',
    #u'name': u'1623',
    #u'sens': u'1',
    #u'vitesse': u'',
    #u'zoom': u'3'
    
