import sys
import os
import json
import csv

with open("ind-out.dat","w") as f:
    f.write("%% position, #steps, ture/false\n")

with open("dataset.dat","w") as f:
    f.write("%% joints X1 Y1 X2 Y2\n")

def bone2sig(json_file, start):
    f = open(json_file)
    Lines = f.readlines();
    f.close()
    #print(len(Lines))
    xary = []
    x = []
    for line in Lines:
        data = json.loads(line)
        d1 = data["predictions"]
        for ind in range(len(d1)):
            bbox = d1[ind]['bbox']
            if bbox[0] < 320:
                continue
            if (json_file.find("fall-13") == 0 or json_file.find("fall-14") == 0) and bbox[0] < 370: # labeling mutiple persons
                continue
            keys = d1[ind]['keypoints']
            x = []
            for i in range(17):
                xi = keys[i*3]
                if xi == 0.0:
                    x.append(0.0) # xi
                    x.append(0.0) # yi
                else:
                    x.append(xi-320) # xi
                    x.append(239-keys[i*3+1]) # yi
        if len(x) == 0:
            for i in range(34):
                x.append(0.0)
        xary.append(x)
    print("size=", len(xary))
    start = start + len(xary)
    
    with open("ind-out.dat","a") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        xx = [];
        xx.append(start)
        if json_file.find("fall") == -1:
            xx.append(0)
        else:
            xx.append(1)
        xx.append(len(xary))
#        xx.append(json_file)
        csvWriter.writerow(xx)

    with open("dataset.dat","a") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(xary)
    return start

if len(sys.argv) < 2:
    print('*E* -- Please provide a file.') 

entries = os.listdir(sys.argv[1])
start = 0
for entry in entries:
    print(entry)
    start = bone2sig(entry,start)
    
