import json
import json
import numpy as np
import os
import requests
import subprocess
input_file_directory = "/workspaces/mykeyan/Before and After Code/UNKNOWN to Try 0.json"
out_file_directory = "/workspaces/mykeyan/Results_Before_after/UNKNOWN to try 0.json"
diff_after = []
count = 0
a = 0
with open(input_file_directory, 'r') as input:
    data = json.load(input)["UNKNOWN to Try"]
data_out = []
for i in range(len(data)):
    if "Complete Before Code" in data[i]:
        data_out.append(data[i])
        count+=1
    else:
        a +=1
print("doc removed are " + str(a))
print("doc left are" + str(count))
temp = 0
with open(out_file_directory, 'w') as outfile:
    for i in range(len(data)):
        if temp == 1:
            outfile.write(("{\"" + "UNKNOWN to Try" + "\":[" + json.dumps(data[i]) + ",\n" ))
        elif temp == len(data):
            outfile.write(json.dumps(data[i]) + "]}" + "\n")
        else:
            outfile.write(json.dumps(data[i]) + ",\n")