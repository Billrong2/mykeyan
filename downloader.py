import base64
import json
import os

import requests
import numpy as np
file = '/workspaces/mykeyan/parsing_target/0.json'
output_directory = "/workspaces/mykeyan/downloaded_result/0.json"
f = open(file)
data= json.load(f)['Single']
print(len(data))
#headers = "Authorization: Bearer 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"
for i in range(5000):
    current_url = data[i]['Url']+"/commits/" + data[i]['Fixed commit']
    x=data[i]["FileName"].split('.')
    f_temp = x[-2]+'.'+x[-1]
    response = requests.get(current_url)
    commit_data = response.json()
    print(commit_data)
    print("\n")
    #print('RUNNING', a)
    if response.status_code != 200:
        data[i]["Complete Source Code"] = "ERROR API REQUEST REJECTED code 403"
        print("missed")
    elif response.status_code == 403:
        print("rate_limit exceeded")
        break
    else:
        if "files" in commit_data:
            for j in range(len(commit_data["files"])):
                if f_temp in commit_data["files"][j]["filename"]:
                    data[i]["Complete Source Code"] = commit_data["files"][j]["patch"]
                else:
                    pass
        else: pass
temp = 0
with open(output_directory, 'w') as outfile:
    for i in range(len(data)):
        temp+=1

        if temp ==1:
            outfile.write(("{\""+ "Single" + "\":[" + json.dumps(data[i]) + ",\n" ))
        elif temp ==len(data):
            outfile.write(json.dumps(data[i]) + "]}"+ "\n")
        else:
            outfile.write(json.dumps(data[i]) + ",\n")
