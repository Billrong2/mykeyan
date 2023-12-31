import base64
import json
import os
import requests
import subprocess
import time
file = '/workspaces/mykeyan/new_pattern/Constructor to Constructor/Constructor to Constructor 0.json'
output_directory = "/workspaces/mykeyan/downloaded_result/Constructor to Constructor 0.json"
f = open(file)
data = json.load(f)['Constructor to Constructor']
for i in range(3):
    current_url = data[i]['Url']+"/commits/" + data[i]['Fixed commit']
    my_command = "curl --request GET \--url \"" + current_url + "\" \\--header \"Authorization: Bearer TOKEN\" \\--header \"X-GitHub-Api-Version: 2022-11-28\" "
    x = data[i]["FileName"].split('.')
    f_temp = x[-2]+'.'+x[-1]
    print(f_temp)
    response = subprocess.check_output(my_command, shell=True, text=True)
    commit_data = json.loads(response)
    print(commit_data)
    if "files" in commit_data:
        for j in range(len(commit_data["files"])):
            if f_temp in commit_data["files"][j]["filename"]:
                if("patch" in commit_data["files"][j]):
                    print("File Found" + f_temp)
                    data[i]["Source Code Diff"] = commit_data["files"][j]["patch"]
                    raw_url = commit_data["files"][j]["raw_url"]
                    print(data[i]["Source Code Diff"])
                else:
                    #print("cannot find patch \n")
                    continue
            else:
                #print("cannot find required files \n")
                pass
        response = requests.get(raw_url)
        response_data = response.text
        if response.status_code == 200:
            data[i]["Complete After Code"] = response_data
        else:
            data[i]["Complete After Code"] = "Missing Raw Link for After Code"
    else:
        #print("there is no file in commit data\n")
        pass
    print(str(i) +"traversal complete \n")
    time.sleep(0.2)
temp = 0
a = 0
with open(output_directory, 'w') as outfile:
    for i in range(len(data)):
        a += 1
        temp += 1
        if temp == 1:
            outfile.write(("{\"" + "UNKNOWN to Try" + "\":[" + json.dumps(data[i]) + ",\n" ))
        elif temp == len(data):
            outfile.write(json.dumps(data[i]) + "]}" + "\n")
        else:
            outfile.write(json.dumps(data[i]) + ",\n")

print(str(a)+"number of File is written \n")
