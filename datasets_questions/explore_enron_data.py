#!/usr/bin/python

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print("Data set size: ", len(enron_data))
print("Data entry size: ", len(next(iter(enron_data.values()))))

pois = 0
for key, value in enron_data.items():
    if value["poi"] == 1:
        pois += 1

# for key, value in enron_data["SKILLING JEFFREY K"].items():
#     print(key, " = ", value)

print("POIs in data set:", pois)
print("James Prentice stock: ", enron_data["PRENTICE JAMES"]["total_stock_value"])
print("Wesley Colwell emails to POIs: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print("Jeffrey K Skilling stock: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
