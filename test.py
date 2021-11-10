import json
import Vaccine_Tracker

file = open("test.json", "rb")
data = json.load(file)


vts = []

for item in data:
    vt = Vaccine_Tracker.Vaccine_Tracker(
        IDNum = item["IDNum"],
        Name = item["Name"],
        address = item["address"],
        lot = item["lot"],
        expiration = item["expiration"],
        remaining = item["remaining"]
    )
    vts.append(vt)

vt_list = []

for vt in vts:
    vt_list.append(vt.__dict__)

with open('test.json', 'w') as outfile:
    json.dump(vt_list, outfile, indent=4, sort_keys=True)