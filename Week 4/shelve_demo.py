import shelve

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

sampleList = [1, 2, 3]
sampleTuple = 1, 2, 3
names = ['Mehdi', 'Ahmad', 'Ali']

# shelves are persisted dictionaries
with shelve.open('demo.shelve') as shelve_file:
    shelve_file['cars'] = cars
    shelve_file['sampleList'] = sampleList
    shelve_file['sampleTuple'] = sampleTuple
    print(shelve_file['sampleList'])
    print(shelve_file)
    print(type(shelve_file))
    shelve_file['names'] = names
    # del shelve_file['name']

    print('----------')
    for item in shelve_file:
        print(item, '\t', shelve_file[item])


# There is no literal for shelve
with shelve.open('test.shelve') as s_file:
    s_file = {'cars': cars,
              'sampleList': sampleList,
              'sampleTuple': sampleTuple}
    print(type(s_file))










