import csv
import pymongo
import random

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["energyPlantsDB"]
mycol = mydb["energy_plants"]

with open('dataset/energy_plants.csv', 'r') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i > 0:
            obj = {row[1], row[2]}
            print(obj)
            data = {}
            data['Region'] = row[1]
            data['Country'] = row[2]
            data['Plant'] = row[3]
            data['NumReactor'] = row[4]
            data['Latitude'] = row[5]
            data['Longitude'] = row[6]
            data['Radiation'] = random.randint(1,200)
            print(data)
            mycol.insert_one(data)