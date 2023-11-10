import os
import base64
import json
import requests
import subprocess
import time
# This is my path
existing_path = "/workspaces/mykeyan/downloaded_result"
existing_file = []
for (root, dirs, file) in os.walk(existing_path):
    for f in file:
        if '.json' in f:
            existing_file.append(f)

path = "/workspaces/mykeyan/new_pattern/"
output_path = "/workspaces/mykeyan/downloaded_result"
output_directory =  []
# to store files in a list
list_inputdirectory = []
 
# dirs=directories
for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.json' in f:
            if f in existing_file:
                print("skipped file:" + f)
                continue
            list_inputdirectory.append(root+"/"+f)
            output_directory.append(output_path+"/"+f)
for file_num, out_file in enumerate(output_directory):
    if "UNKNOWN to If" in out_file:
        key_name = "UNKNOWN to If"
    elif "UNKNOWN to Return" in out_file:
        key_name = "UNKNOWN to Return"
    elif "UNKNOWN to Try" in out_file:
        key_name = "UNKNOWN to Try"
    elif "Constructor to Constructor" in out_file:
        key_name = "Constructor to Constructor"

    input_files = list_inputdirectory[file_num]
    f = open(input_files)
    data = json.load(f)[key_name]
    for i in range(len(data)):
        current_url = data[i]['Url']+"/commits/" + data[i]['Fixed commit']
        my_command = "curl --request GET \--url \"" + current_url + "\" \\--header \"Authorization: Bearer Token\" \\--header \"X-GitHub-Api-Version: 2022-11-28\" "
        x = data[i]["FileName"].split('.')
        f_temp = x[-2]+'.'+x[-1]
        response = subprocess.check_output(my_command, shell=True, text=True)
        commit_data = json.loads(response)
        if "files" in commit_data:
            for j in range(len(commit_data["files"])):
                if f_temp in commit_data["files"][j]["filename"]:
                    if("patch" in commit_data["files"][j]):
                        data[i]["Source Code Diff"] = commit_data["files"][j]["patch"]
                        raw_url = commit_data["files"][j]["raw_url"]
                    else:
                        continue
                else:
                    pass
            response = requests.get(raw_url)
            response_data = response.text
            if response.status_code == 200:
                data[i]["Complete After Code"] = response_data
            else:
                data[i]["Complete After Code"] = "Missing Raw Link for After Code"
        else:
            pass
        print(str(i) +"traversal complete \n")
        time.sleep(0.5)
    temp = 0
    a = 0
    with open(out_file, 'w') as outfile:
        for i in range(len(data)):
            a += 1
            temp += 1
            if temp == 1:
                outfile.write(("{\"" + key_name + "\":[" + json.dumps(data[i]) + ",\n" ))
            elif temp == len(data):
                outfile.write(json.dumps(data[i]) + "]}" + "\n")
            else:
                outfile.write(json.dumps(data[i]) + ",\n")
    print(str(a)+"number of File is written in"+ out_file+"\n")
