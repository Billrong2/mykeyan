import json
import sys
file_directory = "/workspaces/mykeyan/PaperResults_P1/V"
output_directory = "/workspaces/mykeyan/new_paper_result/V"
file = []
name = []
data_att1 = []
for i in range(85):
    file.append(file_directory + str(i+1)+".json")
    name.append("V" + str(i+1))
# Re_organize data
for file_num in range(len(file)):
    if file_num == 139: # skip V140.json, file not found
        file_num+=1
    elif file_num == 169:# skip V170.json, file not found
        file_num+=1
    f = open(file[file_num], 'r')
    data_temp = f.readlines()
    temp = 0
    out_path = output_directory + name[file_num] + ".json"
    # make appropriate json file
    with open(out_path, 'w') as outfile:
        for i in data_temp:
            temp += 1
            if temp == 1:
                outfile.write("{\""+ name[file_num] + "\":[" + i.strip() + ",\n" )
            elif temp == len(data_temp):
                outfile.write(i.strip() + "]}"+ "\n")
            else:
                outfile.write(i.strip() + "," + "\n")
# create multi-hunk, single-hunk
# 