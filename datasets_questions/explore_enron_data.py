#!/usr/bin/python

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print("Data set size: ", len(enron_data))
print("Data entry size: ", len(next(iter(enron_data.values()))))

pois = 0
salaries = 0
emails = 0
payments_missing = 0
poi_payments_missing = 0
for key, value in enron_data.items():
    if value["poi"] == 1:
        pois += 1
    if value["salary"] != 'NaN':
        salaries += 1
    if value["email_address"] != 'NaN':
        emails += 1
    if value["total_payments"] == 'NaN':
        payments_missing += 1
    if value["total_payments"] == 'NaN' and value["poi"] == 1:
        poi_payments_missing += 1

# for key, value in enron_data["SKILLING JEFFREY K"].items():
#     print(key, " = ", value)

print("POIs in data set:", pois)
print("James Prentice stock: ", enron_data["PRENTICE JAMES"]["total_stock_value"])
print("Wesley Colwell emails to POIs: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print("Jeffrey K Skilling stock: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

print("Jeffrey K Skilling total_payments: ", enron_data["SKILLING JEFFREY K"]["total_payments"])
print("Andrew Fastow total_payments: ", enron_data["FASTOW ANDREW S"]["total_payments"])
print("Kenneth Lay total_payments: ", enron_data["LAY KENNETH L"]["total_payments"])

print("Total with salaries: ", salaries)
print("Total with emails: ", emails)
print("Total without payments: ", payments_missing, " or ", payments_missing / len(enron_data) * 100, "%")
print("Total POI without payments: ", poi_payments_missing, " or ", poi_payments_missing / len(enron_data) * 100, "%")
