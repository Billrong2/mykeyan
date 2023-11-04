import json
import os

import numpy as np
file_directory = 'new_paper_result/V'
output_directory = "new_pattern"
file = []
name = []
dist_mtm = []
dist_else = []
dist_unknowntif =[]
dist_unknownttry = []
dist_unknowntreturn = []
dist_ctc = []
for i in range(177):
    file.append(file_directory + str(i+1)+'.json')
    name.append("V" + str(i+1))

out_data = []

b = 0
a = 0

for file_num in range(len(file)):
    if file_num == 139: # skip V140.json, file not found
        file_num+=1
    elif file_num == 169:# skip V170.json, file not found
        file_num+=1
    f = open(file[file_num])
    data_temp = []
    data_temp= json.load(f)
    b+=1
    for i in data_temp[name[file_num]]:
        a+=1
        if(i['Pattern'] == "Method=>Method"):
            dist_mtm.append(i)
        elif(i['Pattern'] == "UNKNOWN=>Try" ):
            dist_unknownttry.append(i)
        elif(i['Pattern'] == "UNKNOWN=>If" ):
            dist_unknowntif.append(i)
        elif(i['Pattern'] == "UNKNOWN=>Return"):
            dist_unknowntreturn.append(i)
        elif(i['Pattern']== "Constructor=>Constructor"):
            dist_ctc.append(i)
        else:
            dist_else.append(i)

print("file # =" + str(b))
print("Traversed lines =", a)

file_written = 0

count = 0
out_path = output_directory + "/Method to Method/Method to Method "+ str(count)+ ".json"
outfile= open(out_path, 'w')
temp = 0
for i in range(len(dist_mtm)):
    temp+=1
    file_written +=1
    if temp ==1:
        outfile.write(("{\""+ "Method=>Method" + "\":[" + json.dumps(dist_mtm[i]) + ",\n" ))
    elif temp ==3000:
        outfile.write(json.dumps(dist_mtm[i]) + "]}"+ "\n")
        temp = 0
        count +=1
        outfile.close
        out_path = output_directory +"/Method to Method/Method to Method "+  str(count)+ ".json"
        outfile = open(out_path, 'w')
        print(out_path)
    elif i == len(dist_mtm)-1:
        outfile.write(json.dumps(dist_mtm[i]) + "]}"+ "\n")    
    else:
        outfile.write(json.dumps(dist_mtm[i]) + ",\n")

count = 0
out_path = output_directory + "/UNKNOWN to If/UNKNOWN to If "+ str(count)+ ".json"
outfile= open(out_path, 'w')
temp = 0

for i in range(len(dist_unknowntif)):
    temp+=1
    file_written +=1
    if temp ==1:
        outfile.write(("{\""+ "UNKNOWN to If" + "\":[" + json.dumps(dist_unknowntif[i]) + ",\n" ))
    elif temp ==3000:
        outfile.write(json.dumps(dist_unknowntif[i]) + "]}"+ "\n")
        temp = 0
        count +=1
        outfile.close
        out_path = output_directory +"/UNKNOWN to If/UNKNOWN to If "+  str(count)+ ".json"
        outfile = open(out_path, 'w')
        print(out_path)
    elif i == len(dist_unknowntif)-1:
        outfile.write(json.dumps(dist_unknowntif[i]) + "]}"+ "\n")
    else:
        outfile.write(json.dumps(dist_unknowntif[i]) + ",\n")

count = 0
out_path = output_directory + "/UNKNOWN to Try/UNKNOWN to Try "+ str(count)+ ".json"
outfile= open(out_path, 'w')
temp = 0

for i in range(len(dist_unknownttry)):
    temp+=1
    file_written +=1
    if temp ==1:
        outfile.write(("{\""+ "UNKNOWN to Try" + "\":[" + json.dumps(dist_unknownttry[i]) + ",\n" ))
    elif temp ==3000:
        outfile.write(json.dumps(dist_unknownttry[i]) + "]}"+ "\n")
        temp = 0
        count +=1
        outfile.close
        out_path = output_directory +"/UNKNOWN to Try/UNKNOWN to Try "+  str(count)+ ".json"
        outfile = open(out_path, 'w')
        print(out_path)
    elif i == len(dist_unknownttry)-1:
        outfile.write(json.dumps(dist_unknownttry[i]) + "]}"+ "\n")
    else:
        outfile.write(json.dumps(dist_unknownttry[i]) + ",\n")

count = 0
out_path = output_directory + "/UNKNOWN to Return/UNKNOWN to Return "+ str(count)+ ".json"
outfile= open(out_path, 'w')
temp = 0

for i in range(len(dist_unknowntreturn)):
    temp+=1
    file_written +=1
    if temp ==1:
        outfile.write(("{\""+ "UNKNOWN to Return" + "\":[" + json.dumps(dist_unknowntreturn[i]) + ",\n" ))
    elif temp ==3000:
        outfile.write(json.dumps(dist_unknowntreturn[i]) + "]}"+ "\n")
        temp = 0
        count +=1
        outfile.close
        out_path = output_directory +"/UNKNOWN to Return/UNKNOWN to Return "+  str(count)+ ".json"
        outfile = open(out_path, 'w')
        print(out_path)
    elif i == len(dist_unknowntreturn)-1:
        outfile.write(json.dumps(dist_unknowntreturn[i]) + "]}"+ "\n")
    else:
        outfile.write(json.dumps(dist_unknowntreturn[i]) + ",\n")

count = 0
out_path = output_directory + "/Constructor to Constructor/Constructor to Constructor "+ str(count)+ ".json"
outfile= open(out_path, 'w')
temp = 0

for i in range(len(dist_ctc)):
    temp+=1
    file_written +=1
    if temp ==1:
        outfile.write(("{\""+ "Constructor to Constructor" + "\":[" + json.dumps(dist_ctc[i]) + ",\n" ))
    elif temp ==3000:
        outfile.write(json.dumps(dist_ctc[i]) + "]}"+ "\n")
        temp = 0
        count +=1
        outfile.close
        out_path = output_directory +"/Constructor to Constructor/Constructor to Constructor "+  str(count)+ ".json"
        outfile = open(out_path, 'w')
        print(out_path)
    elif i == len(dist_ctc)-1:
        outfile.write(json.dumps(dist_ctc[i]) + "]}"+ "\n")
    else:
        outfile.write(json.dumps(dist_ctc[i]) + ",\n")

count = 0
out_path = output_directory + "/Else/Else "+ str(count)+ ".json"
outfile= open(out_path, 'w')
temp = 0

for i in range(len(dist_else)):
    temp+=1
    file_written +=1
    if temp ==1:
        outfile.write(("{\""+ "Else" + "\":[" + json.dumps(dist_else[i]) + ",\n" ))
    elif temp ==3000:
        outfile.write(json.dumps(dist_else[i]) + "]}"+ "\n")
        temp = 0
        count +=1
        outfile.close
        out_path = output_directory +"/Else/Else "+  str(count)+ ".json"
        outfile = open(out_path, 'w')
        print(out_path)
    elif i == len(dist_else)-1:
        outfile.write(json.dumps(dist_else[i]) + "]}"+ "\n")
    else:
        outfile.write(json.dumps(dist_else[i]) + ",\n")

print(file_written)

print("Traversed lines =", a)