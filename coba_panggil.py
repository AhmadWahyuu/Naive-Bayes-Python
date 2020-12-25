import csv
V_1 = []
with open('V1.csv') as cf:
    buka = csv.reader(cf, delimiter=',')
    for raw in buka:
        V_1.append(raw)
    V_1[2][1]= 1
with open('V1.csv', mode='w', newline='') as cf:
    writer = csv.writer(cf, delimiter=',')
    for rew in V_1:
        writer.writerow(rew)
with open('V1.csv') as cf :
    buka = csv.reader(cf, delimiter=',')
    for dt in buka:
        print(dt)