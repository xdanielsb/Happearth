from google.cloud import bigquery
from django.core.cache import cache 
import os
import os.path

def existCredentialsFile():
    path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if path is None: 
      return False
    return os.path.exists(path)

def consumptionCommunity(dateFrom="2018-04-05", dateTo="2018-05-05"):
    def c(foo):
        if foo == None: return 0
        return abs(foo)
    key_cache_a = "ca-{}-{}".format(dateFrom, dateTo)
    key_cache_b = "cb-{}-{}".format(dateFrom, dateTo)
    res1 = cache.get(key_cache_a)
    res2 = cache.get(key_cache_b) 
    if res1 != None:
        return res2, res1
    asw = {"heating_cooling": 0 , "kitchen":0, "plug":0, "lighting": 0, "water_boiler":0}
    houses_consume = []
    
    if not existCredentialsFile():
        print("INFO: There is no credential file for database in BIGQUERY")
        return asw, houses_consume

    try:
        client = bigquery.Client()
        query = """SELECT serial,
                   SUM(ahu) as ahu, SUM(heatpump) as heatpump,
                   SUM(fridge) as fridge, SUM(dish) as dish, SUM(bath) as bath,
                   SUM(kitchen1) as kitchen1, SUM(kitchen2) as kitchen2,
                   SUM(hood) as hood, SUM(`range`) as `range`, SUM(light) as light,
                   SUM(room1) as room1, SUM(room2) as room2, SUM(smoke) as smoke,
                   SUM(waterheater) as waterheater
                   FROM `connected-community.prod.power_delta`
                   WHERE timestamp between DATETIME('{}') and DATETIME('{}')
                   GROUP BY serial 
                   
                   """.format(dateFrom, dateTo)
        CONV = 3600000
        query_job  = client.query(query)
        results = query_job.result()
        for row in results:
          if row.serial == 'synthetic': continue
          asw["heating_cooling"] +=  c(row.ahu) +c(row.heatpump)
          asw["kitchen"] +=  c(row.fridge) +c( row.dish) + c(row.kitchen1) +c(row.kitchen2) + c(row.hood) +c(row.range)
          asw["plug"] +=  c(row.bath) + c(row.room1) + c(row.room2) + c(row.smoke) 
          asw["lighting"] +=  c(row.light) 
          asw["water_boiler"] += c(row.waterheater) 
          subTotal = 0
          for con in row:
            if con == row.serial: 
              continue
            subTotal += c(con)
          houses_consume.append({'name':row.serial, 'y':subTotal // CONV})
        TOTAL = 0
        for key, value in asw.items():
            asw[key] = int(value / CONV)
            TOTAL += asw[key]
        asw["total"] = TOTAL
        cache.set(key_cache_a, houses_consume, 1*60*60*24 )
        cache.set(key_cache_b, asw, 1*60*60*24 )
        return asw, houses_consume
    except Exception as e:
        print( "----- ERROR -----" + str(e) )
        return asw, houses_consume

def consumptionHouse(serial, dateFrom="2018-04-05", dateTo="2018-05-05"):
    def c(foo):
        if foo == None: return 0
        return abs(foo)
    asw = {"heating_cooling": 0 , "kitchen":0, "plug":0, "lighting": 0, "water_boiler":0 }

    if not existCredentialsFile():
        print("INFO: There is no credential file for database in BIGQUERY")
        return asw

    try:
        client = bigquery.Client()
        query = """SELECT 
                   SUM(ahu) as ahu, SUM(heatpump) as heatpump,
                   SUM(fridge) as fridge, SUM(dish) as dish, SUM(bath) as bath,
                   SUM(kitchen1) as kitchen1, SUM(kitchen2) as kitchen2,
                   SUM(hood) as hood, SUM(`range`) as `range`, SUM(light) as light,
                   SUM(room1) as room1, SUM(room2) as room2, SUM(smoke) as smoke,
                   SUM(waterheater) as waterheater
                   FROM `connected-community.prod.power_delta`
                   WHERE serial='{}' and 
                   timestamp between DATETIME('{}') and DATETIME('{}')
                   """.format(serial, dateFrom, dateTo)
        query_job  = client.query(query)
        results = query_job.result()
        for row in results:
          asw["heating_cooling"] += c(row.ahu) +c( row.heatpump)
          asw["kitchen"] += c(row.fridge) +c( row.dish) + c(row.kitchen1) +c(row.kitchen2) + c(row.hood) +c(row.range)
          asw["plug"] += c(row.bath) + c(row.room1) + c(row.room2) + c(row.smoke)
          asw["lighting"] += c(row.light)
          asw["water_boiler"] += c(row.waterheater)
        CONV = 3600000
        TOTAL = 0
        for key, value in asw.items():
            asw[key] = int(value / CONV)
            TOTAL += asw[key]
        asw["total"] = TOTAL
        return asw
    except Exception as e:
      print( str(e) )
      return asw


if __name__ == "__main__":
    print(existCredentialsFile())
