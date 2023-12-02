
import os
import base64
import json
import math
import time
# Load dataset
existing_path = "/Users/xiaokairong/Desktop/mykeyan/downloaded_result"
existing_file = []
for (root, dirs, file) in os.walk(existing_path):
    for f in file:
        if '.json' in f:
            existing_file.append(f)
path = "/Users/xiaokairong/Desktop/mykeyan/new_pattern/"
output_path = "/Users/xiaokairong/Desktop/mykeyan/downloaded_result"
output_directory =  []
list_inputdirectory = []
m2m_api = []
m2m_noapi = []
data_dir_api = []
data_dir_noapi = []

# X = []
# y = []
# parent = []
# child = []
for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.json' in f:
            list_inputdirectory.append(root+"/"+f)
            output_directory.append(output_path+"/"+f)
for file_num, out_file in enumerate(output_directory):
    if "UNKNOWN to If" in out_file:
        key_name = "UNKNOWN to If"
    elif "UNKNOWN to Return" in out_file:
        key_name = "UNKNOWN to Return"
        f = open(out_file)
        data = json.load(f)[key_name]
        for i in range(len(data)):
            if "Complete After Code" and "Parent Commit" in data[i]:
                # X.append(data[i]["Parent Commit"])
                # y.append(data[i]["Complete After Code"])
                if data[i]["BodyUseAPI"] != []:
                    if len(data[i]["Complete After Code"]) < 1000 and len(data[i]["Parent Commit"]) < 1000:
                        data_dir_api.append(data[i])
                if data[i]["BodyUseAPI"] == []:
                    if len(data[i]["Complete After Code"]) < 1000 and len(data[i]["Parent Commit"]) < 1000:
                        data_dir_noapi.append(data[i])
    elif "UNKNOWN to Try" in out_file:
        key_name = "UNKNOWN to Try"
        f = open(out_file)
        data = json.load(f)[key_name]
        for i in range(len(data)):
            if "Complete After Code" and "Parent Commit" in data[i]:
                if data[i]["BodyUseAPI"] != []:
                    if len(data[i]["Complete After Code"]) < 1000 and len(data[i]["Parent Commit"]) < 1000:
                        data_dir_api.append(data[i])
                if data[i]["BodyUseAPI"] == []:
                    if len(data[i]["Complete After Code"]) < 1000 and len(data[i]["Parent Commit"]) < 1000:
                        data_dir_noapi.append(data[i])
                # X.append(data[i]["Source Code Diff"])
                # y.append(data[i]["BodyUseAPI"])
    elif "Constructor to Constructor" in out_file:
        key_name = "Constructor to Constructor"
    elif "Method to Method" in out_file:
        key_name = "Method=>Method"
        # f = open(out_file)
        # data = json.load(f)[key_name]
        # for i in range(len(data)):
            # if "Complete After Code" and "Parent Commit" in data[i]:
            #     if data[i]["BodyUseAPI"] != []:
            #         m2m_api.append(data[i])
            #     if data[i]["BodyUseAPI"] == []:
            #         m2m_noapi.append(data[i])
        # 雨下整夜，我的愛溢出就像雨水

print(len(data_dir_api))
print(len(data_dir_noapi))
# print(len(m2m_api))
# print(len(m2m_noapi))
test_yes = []
test_no = []

count_1 = 0
count_2 = 0
for i in range(15):
    
    test_yes.append(data_dir_api[count_1])
    test_no.append(data_dir_noapi[count_2])
    count_1 += 7
    count_2 += 20
out_path = "/Users/xiaokairong/Desktop/mykeyan/chat_gpt_prompt/"
for i in range(15):
    directory = "yes"
    try:
        os.mkdir(str(out_path + directory))
    except:
        pass
    with open(out_path + directory + "/textcase" + str(i) +".txt", 'w') as file:
        file.write("Fixed Version\n")
        file.write(test_yes[i]["Complete After Code"])
        file.write("Buggy Version\n")
        file.write(test_yes[i]["Parent Commit"][0])
    file.close
    temp = []
    count = 0
    with open(out_path + directory + "/textcase" + str(i) +".txt", 'r') as file:
        for x,j in enumerate(file):
            if j == "Fixed Version\n":
                count = 0
                temp.append("Fixed Version\n")
                continue
            if j == "Buggy Version\n":
                count = 0
                temp.append("Buggy Version\n")
                continue
            temp.append("Line "+str(count) + ":" + j)
            count +=1
    file.close
    with open(out_path + directory + "/textcase" + str(i) +".txt", 'w') as file:
        file.write("I need you to detect the API misuse in my dataset. I will send you fixed version and buggy version of the code, tell me if there is API misuse or not. Provide your answer as in following format:\n1. If there are API misuses, response YES, otherwise say NO\n2. If the previous question is YES, then give me the API Misuse line number. If the previous question is NO, then leave it blank\n")
        for x in temp:
            file.write(x)
    file.close

    directory = "no"
    try:
        os.mkdir(out_path + directory)
    except:
        pass
    with open(out_path + directory + "/textcase" + str(i) +".txt", 'w') as file:
        file.write("Fixed Version\n")
        file.write(test_no[i]["Complete After Code"])
        file.write("Buggy Version\n")
        file.write(test_no[i]["Parent Commit"][0])
    file.close
    temp = []
    count = 0

    with open(out_path + directory + "/textcase" + str(i) +".txt", 'r') as file:
        for x,j in enumerate(file):
            if j == "Fixed Version\n":
                temp.append("Fixed Version\n")
                count = 0
                continue
            if j == "Buggy Version\n":
                count = 0
                temp.append("Buggy Version\n")
                continue
            temp.append("Line "+str(count) + ":" + j)
            count +=1
    file.close
    with open(out_path + directory + "/textcase" + str(i) +".txt", 'w') as file:
        file.write("I need you to detect the API misuse in my dataset. I will send you fixed version and buggy version of the code, tell me if there is API misuse or not. Provide your answer as in following format:\n1. If there are API misuses, response YES, otherwise say NO\n2. If the previous question is YES, then give me the API Misuse line number. If the previous question is NO, then leave it blank")
        for x in temp:
            file.write(x)
    file.close
with open("/Users/xiaokairong/Desktop/mykeyan/chat_gpt_prompt/yes.txt", 'w') as f:
    for i in range(len(test_yes)):
        f.write("case"+str(i) + "   "+ test_yes[i]["Line"]+"\n" + test_yes[i]["Content"]+"\n")
with open("/Users/xiaokairong/Desktop/mykeyan/chat_gpt_prompt/no.txt", 'w') as f:
    for i in range(len(test_no)):
        f.write("case"+str(i) + "   "+ test_no[i]["Line"]+"\n" + test_no[i]["Content"]+"\n")






import os
from openai import AzureOpenAI
client = AzureOpenAI(
  api_key = os.getenv("TOKEN"),  
  api_version = "2023-05-15",
  azure_endpoint = os.getenv("https://tien.openai.azure.com/")
)
user_prompt = [
 {"role": "user", "content": "Tell me a joke"}]
response = client.chat.completions.create(
    model="gpt-35-turbo", # model = "deployment_name".
    messages=user_prompt
)

#print(response)


response = openai.ChatCompletion.create(engine = "gpt-35-turbo",messages = user_prompt)
print(response.model_dump_json(indent=2))
print(response.choices[0].message.content)
# def chat_gpt(prompt):
#     model = "gpt-35-turbo"  # You can change the model based on your preference
#     response = client.chat.completions.create(model=model,prompt=prompt)
#     return response.choices[0].message.content
# Example usage