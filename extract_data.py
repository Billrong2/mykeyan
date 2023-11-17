import json
import numpy as np
file_directory = 'new_paper_result/V'
output_directory = "new_pattern/"
file = []
name = []
data_att1 = []
dist_single_known = []
dist_multi_known = []
dist_unknown = []
for i in range(177):
    file.append(file_directory + str(i+1)+'.json')
    name.append("V" + str(i+1))
out_path = output_directory + "result"+ ".json"
out_temp = set()
out_data = []
#out_path = 
#print(file[1])
b = 0
a = 0
with open(out_path, 'w') as outfile:
    for file_num in range(len(file)):
        if file_num == 139: # skip V140.json, file not found
            file_num+=1
        elif file_num == 169:# skip V170.json, file not found
            file_num+=1
        f = open(file[file_num])
        data_temp = []
        data_temp= json.load(f)

        b+=1
        #print("file # =" + str(b)+ "\n")
        for i in data_temp[name[file_num]]:
            a+=1
            # print("line_num:" +str(a) + "\n")
            if("UNKNOWN" not in i['Pattern']):
                if(i['BugDetectionTag'] in out_temp):
                    dist_single_known.append(i)
                elif(', ' in i['BugDetectionTag']):
                    #dist_multi_known.append[i['BugDetectionTag']]
                    dist_multi_known.append(i)
                elif('[]' in i['BugDetectionTag'] ):
                    pass
                else:
                    out_temp.add(i['BugDetectionTag'])
            else:
                dist_unknown.append(i)
print("file # =" + str(b))
print("Traversal lines =", a)

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



print(file_written)