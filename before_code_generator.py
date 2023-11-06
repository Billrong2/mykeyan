import json
import numpy as np
import os
import requests
import subprocess
input_file_directory = "/workspaces/mykeyan/downloaded_result/UNKNOWN to Try 0.json"
diff_after = []
count = 0
with open(input_file_directory, 'r') as input:
    data = json.load(input)["UNKNOWN to Try"]
print(len(data))
for d_line in range(len(data)):
    if "Source Code Diff" not in data[d_line]:
        continue
    if "Complete After Code" not in data[d_line]:
        continue
    with open ("temp_diff.txt",'w') as output:
        output.write(data[d_line]["Source Code Diff"])
        output.close
    with open ("temp_diff_2.txt", 'w') as output:
        output.write(data[d_line]["Complete After Code"])
        output.close
    index = []
    with open("/workspaces/mykeyan/temp_diff.txt", 'r') as infile:
        change_num = 0
        for line_num, line in enumerate(infile):
            if line[0] == "@":
                change_num +=1
                index.append(line_num)
        res_restore, res_discard = [[] for x in range(change_num)], [[] for x in range(change_num)]
        for i in range(change_num):
            with open("/workspaces/mykeyan/temp_diff.txt", 'r') as mid_file:
                for line_num, line in enumerate(mid_file):
                    if i+1 == change_num and line_num >= index[i]:
                        if line[0] == '-':
                            line = line.replace("\n", "\\n")
                            res_restore[i].append(line[1:])
                        if line[0] == '+':
                            line = line.replace("\n", "\\n")
                            res_discard[i].append(line[1:])
                    elif(line_num >=index[i] and line_num<=index[i+1]):

                        if line[0] == '-':
                            line = line.replace("\n", "\\n")
                            res_restore[i].append(line[1:])
                        if line[0] == '+':
                            line = line.replace("\n", "\\n")
                            res_discard[i].append(line[1:])


    for i in range(change_num):
        temp_discard = ""
        temp_restore = ""
        for a in range(len(res_discard[i])):
            temp_discard += res_discard[i][a]
        for b in range(len(res_restore[i])):
            temp_restore += res_restore[i][b]
        # #print(temp_discard)
        # print(temp_restore)
        if temp_discard in data[d_line]["Complete After Code"]:
            print("Code frag found, restoring")
            if(temp_restore == ""):
                data[d_line]["Complete Before Code"] = data[d_line]["Complete After Code"].replace(temp_discard,"")
            else:
                data[d_line]["Complete Before Code"] = data[d_line]["Complete After Code"].replace(temp_discard,temp_restore)
            count +=1
            # print(str(count)+ "\n" + temp_restore)
        else:
            print("code frag not found \n")
temp = 0
with open("/workspaces/mykeyan/Before and After Code/UNKNOWN to Try 0.json", 'w') as outfile:
        for i in range(len(data)):
            temp +=1
            if temp == 1:
                outfile.write(("{\"" + "UNKNOWN to Try" + "\":[" + json.dumps(data[i]) + ",\n" ))
            elif temp == len(data):
                outfile.write(json.dumps(data[i]) + "]}" + "\n")
            else:
                outfile.write(json.dumps(data[i]) + ",\n")
print("Number of file restored is" + str(count))

