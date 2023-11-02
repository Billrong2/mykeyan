import json
import numpy as np
file_directory = '/workspaces/mykeyan/new_paper_result/V'
output_directory = "/workspaces/mykeyan/parsing_target/"
file = []
name = []
data_att1 = []
dist_single_known = []
dist_multi_known = []
dist_unknown = []
for i in range(177):
    file.append(file_directory + str(i+1)+'.json')
    name.append("V" + str(i+1))
out_temp = set()
out_data = []
line_traversaled = 0
for file_num in range(len(file)):
    if file_num == 139: # skip V140.json, file not found
        file_num+=1
    elif file_num == 169:# skip V170.json, file not found
        file_num+=1
    f = open(file[file_num])
    data_temp = []
    data_temp = json.load(f)
    #print("file # =" + str(b)+ "\n")
    for i in data_temp[name[file_num]]:
        out_data.append(i)
        line_traversaled += 1
print(line_traversaled, len(out_data))
file_written = 0
x = len(out_data) % 4500
x+=1
print(x)
count = 0
while count < x:
    temp = 0
    out_path = output_directory + str(count)+ ".json"
    outfile= open(out_path, 'w')
    for i in out_data:
        temp+=1
        file_written +=1

        if temp ==1:
            outfile.write(("{\""+ "Single" + "\":[" + json.dumps(i) + ",\n" ))
        elif temp ==4700:
            outfile.write(json.dumps(i) + "]}"+ "\n")
            temp = 0
            count +=1
            outfile.close
            out_path = output_directory + str(count)+ ".json"
            outfile = open(out_path, 'w')
            print(out_path)
        else:
            outfile.write(json.dumps(i) + ",\n")


# for i in range(count):
#     out_path = output_directory + str(i)+ ".json"
#     with open(out_path, 'w') as outfile:
#         temp = 0
#         for i in out_data[count]:
#             temp+=1
#             file_written +=1
#             if temp ==1:
#                 outfile.write(("{\""+ "Single" + "\":[" + json.dumps(i) + ",\n" ))
#             elif temp ==len(out_data[count]):
#                 outfile.write(json.dumps(i) + "]}"+ "\n")
#             else:
#                 outfile.write(json.dumps(i) + ",\n")
print(file_written)