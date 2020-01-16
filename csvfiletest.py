import csv

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Username", "Password"])
    writer.writerow(["1", "ICYLGR01", "Cocoban123"])
    writer.writerow(["2", "skalman", "fruktsallad"])