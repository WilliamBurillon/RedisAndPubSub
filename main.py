# -*- coding: utf-8 -*-
import redis
import pandas as pd
r=redis.Redis(db=2,charset='utf-8')


#read CSV File with Pandas
cityFile = pd.read_csv('villes.csv',sep=',',encoding='utf-8')
jobsFile=pd.read_csv('jobs.csv',sep=',',encoding='utf-8')

#Useful Variables

cityList = cityFile["Ville"].to_numpy()


def insertGeoDataToDB(df,redis):
    """
    Function which inserts geoData from city to Redis
    :param df: cityCsvFile
    :param redis: Redis Client connected to the DB 2
    :return: None
    """
    with redis.pipeline() as pipe:
        for index,row in df.iterrows():
            pipe.geoadd("ville",row["Longitude"],row["Latitude"],row["Ville"])
        pipe.execute()
    r.bgsave()



def insertJobToDb(df,redis):
    """
    Function which inserts job data to redis in list (key list is the city where localized the job)
    :param df: jobCsvFile
    :param redis: Redis Client connected to the DB 2
    :return: None
    """
    with redis.pipeline() as pipe:
        for index, row in df.iterrows():
            pipe.lpush(row["Ville"].encode('utf-8'),row["Offre"])
        pipe.execute()

def getCityNearACenteCity(centerCity,cityList,distanceMax,redis):
    """
    Function which get city near a city center with a chosen distance
    :param centerCity: the City which represents the center of the search
    :param cityList: The list of potential matching cities
    :param distanceMax: The chosen distnace
    :param redis: Redis Client connected to the DB 2
    :return: Return Matching cities which the distance condition
    """
    res = []
    for city in cityList :
        if city != centerCity:
            dist = redis.geodist("ville",centerCity,city,"km")
            if dist<=distanceMax :
                res.append(city)

    return  res




if __name__ == "__main__":

   # insertJobToDb(jobsFile,r)
   #  insertGeoDataToDB(cityFile,r)
   #  print(getCityNearACenteCity("Amiens",cityList,35,r))
    print("teest")
