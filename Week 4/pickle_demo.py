# Data Serialization

import pickle
import sys

cars = list()

cars.append({"make": "alfa", "colour": "red"})

cars.append({"make": "land rover", "colour": "green"})
cars.append({"make": "aston", "colour": "gold"})

cars[0]["ownercount"] = 2
cars[1]["ownercount"] = 1
cars[2]["ownercount"] = 3

cars[0]["owners"] = ["tom", "james"]
cars[1]["owners"] = ["alison"]
cars[2]["owners"] = ["tom", "james", "jake"]

cars[0]["history"] = [{"desc": "new clutch", "cost": "2314", "date": "4/3/2012" }]
cars[1]["history"] = [{"desc": "cambelt replacement",
                       "cost": "1688",
                       "date": "5/5/2014"}]

cars[2]["history"] = []
cars[2]["history"].append({"desc": "new engine",
                           "cost": "9599",
                           "date": "30/8/2010"})

cars[2]["history"].append({"desc": "wheel alignment",
                           "cost": "125",
                           "date": "4/9/2011"})

print(cars)

sampleList = [1, 2, 3]
sampleTuple = 1, 2, 3

with open('cars.pickle', 'bw') as pickle_file:
    pickle.dump(cars, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(sampleList, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(sampleTuple, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)


with open('cars.pickle', 'br') as pickle_file:
    new_car = pickle.load(pickle_file)
    new_sampleList = pickle.load(pickle_file)
    new_sampleTuple = pickle.load(pickle_file)

print(new_car)
print(new_sampleList)
print(new_sampleTuple)




