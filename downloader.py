import base64
import json
import os
import subprocess
import time
file = '/workspaces/mykeyan/parsing_target/0.json'
output_directory = "/workspaces/mykeyan/downloaded_result/0.json"
f = open(file)
data= json.load(f)['Single']
print(len(data))

for i in range(len(data)):
    current_url = data[i]['Url']+"/commits/" + data[i]['Fixed commit']
    my_command = "curl --request GET \--url \"" + current_url+ "\" \\--header \"Authorization: Bearer YOURTOKEN\" \\--header \"X-GitHub-Api-Version: 2022-11-28\" "
    x=data[i]["FileName"].split('.')
    f_temp = x[-2]+'.'+x[-1]
    response = subprocess.check_output(my_command, shell=True, text=True)
    commit_data = json.loads(response)
    print(commit_data)
    print("\n")
    #print('RUNNING', a)
    if "message" in commit_data:
        if "API rate limit exceeded" in commit_data['message']:
            data[i]["Complete Source Code"] = "ERROR API REQUEST REJECTED code 403"
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
    print(str(i) +"traversal complete")
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
