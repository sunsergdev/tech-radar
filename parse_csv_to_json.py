import csv
import json
ring_map = {
    "Adopt": 0,
    "Assess": 2,
    "Trial": 1,
    "Hold": 3
}

quadrant_map = {
    "Languages and Frameworks": 0,
    "Infrastructure": 1,
    "Datastores and Data Management": 2,
    "Techniques": 3
}

data_json = []

with open('assets/dot_tech_radar.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['label']:
            data_json.append({"label": row['label'], 
                              "link": row["link"], 
                              "active": True if row["active"] == "TRUE" else False, 
                              "moved": int(row["moved"]),
                              "quadrant": quadrant_map[row["quadrant"]],
                              "ring": ring_map[row["ring"]]
                              })
    
with open('entries.js', 'w') as file:
    file.write("var entries_tech_radar = {}".format(json.dumps(data_json)))