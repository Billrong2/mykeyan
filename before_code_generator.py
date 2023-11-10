import os
import numpy as np
import json
path = "/workspaces/mykeyan/downloaded_result"
output_path = "//workspaces/mykeyan/Before and After Code"
output_directory =  []
# to store files in a list
list_inputdirectory = []
count = 0
waste = 0
# dirs=directories
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
    elif "UNKNOWN to Try" in out_file:
        key_name = "UNKNOWN to Try"
    elif "Constructor to Constructor" in out_file:
        key_name = "Constructor to Constructor"
    input_file_directory = list_inputdirectory[file_num]
    list = []
    wasted = 0
    with open(input_file_directory, 'r') as input:
        data = json.load(input)[key_name]
    for a in range(len(data)):
        if "Source Code Diff" not in data[a]:
            wasted +=1
            continue
        elif "Complete After Code" not in data[a]:
            wasted +=1
        else:
            pass
        with open ("temp_diff.txt",'w') as output:
            output.write(data[a]["Source Code Diff"])
            output.close
        with open ("temp_diff_2.txt", 'w') as output:
            output.write(data[a]["Complete After Code"])
            output.close
        index = []
        diff_msg =[]
        after_code = []
        with open("temp_diff_2.txt", 'r') as infile:
            for lines in infile:
                after_code.append(lines.strip())
        with open("temp_diff.txt", 'r') as infile:
            change_num = 0
            for line_num, line in enumerate(infile):
                diff_msg.append(line)
                if line[0] == "@":
                    change_num +=1
                    index.append(line_num)

        error_num = 0
        starting_line_restore = []
        starting_line_discard = []
        diff_line_restore_temp = []
        diff_line_discard_temp = []
        for i in diff_msg:
            if i[0] == "@":
                starting_line_restore.append([])
                starting_line_discard.append([])
                temp_restore = []
                temp_discard = []
                for j, c in enumerate(i):
                    if c.isdigit() and i[j-1]=='-':
                        for h in i[j:]:
                            if h.isdigit():
                                temp_restore.append(h)
                            else:

                                break
                    elif c.isdigit() and i[j-1]=='+':
                        for h in i[j:]:
                            if h.isdigit():
                                temp_discard.append(h)
                            else:

                                break
                starting_line_restore[error_num]= int("".join(temp_restore))
                starting_line_discard[error_num] = int("".join(temp_discard))
                error_num +=1
            if i[0] == '+':
                diff_line_discard_temp.append(i[1:])
            if i[0] == '-':
                diff_line_restore_temp.append(i[1:])    
            else:
                pass

        res_discard_line = []
        res_restore_line = []

        for i in range(change_num):
            res_discard_line.append([])
            res_restore_line.append([])
            with open("temp_diff.txt", 'r') as infile:
                for line_num, lines in enumerate(infile):
                    if line_num >= index[i] and i+1 == change_num:
                        if lines[0] == "+":
                            res_discard_line[i].append(line_num-index[i] + starting_line_discard[i]-2)
                        elif lines[0] == '-':
                            res_restore_line[i].append(line_num -index[i]+ starting_line_restore[i]-2)
                    elif (line_num >= index[i] and line_num <= index[i+1]):
                        if lines[0]== "+":
                            res_discard_line[i].append(line_num -index[i]+ starting_line_discard[i]-2)
                        elif lines[0] == '-':
                            res_restore_line[i].append(line_num -index[i]+ starting_line_restore[i]-2)
        final_diff = []
        for i in range(change_num):
            with open("temp_diff.txt", 'r') as infile:
                for line_num, lines in enumerate(infile):
                    if line_num >= index[i] and i+1 == change_num:
                        if lines[0] == "+":
                            final_diff.append([line_num-index[i] + starting_line_discard[i]-2, '+'])
                        elif lines[0] == '-':
                            final_diff.append([line_num-index[i] + starting_line_discard[i]-2, '-'])
                    elif (line_num >= index[i] and line_num <= index[i+1]):
                        if lines[0]== "+":
                            final_diff.append([line_num-index[i] + starting_line_discard[i]-2, '+'])
                        elif lines[0] == '-':
                            final_diff.append([line_num-index[i] + starting_line_discard[i]-2, '-'])
                                                
        counter_rec = 0
        counter_dis = 0

        for num, sign in final_diff:
            if sign == "+":
                try:
                    after_code.pop(num - counter_rec)
                    counter_rec +=1
                except:
                    print("too less arguement")
                    wasted+=1
                    after_code = []
                    continue
            if sign == "-":
                try:
                    after_code.insert(num - counter_rec, diff_line_restore_temp[counter_dis])
                    counter_dis+=1
                except:
                    print("cannot insert")
                    after_code = []
                    wasted +=1
                    continue
        if after_code !=None:        
            data[a]["Complete Before Code"] = after_code
            
    data_out = []
    for i in range(len(data)):
        count +=1
        if "Complete Before Code" in data[i]:
            data_out.append(data[i])
        else:
            waste +=1
    temp = 0
    with open(out_file, 'w') as outfile:
        for i in range(len(data_out)):
            temp += 1
            if temp == 1:
                outfile.write(("{\"" + key_name + "\":[" + json.dumps(data_out[i]) + ",\n" ))
            elif temp == len(data_out):
                outfile.write(json.dumps(data_out[i]) + "]}" + "\n")
            else:
                outfile.write(json.dumps(data_out[i]) + ",\n")
    print("Total testcases collected" + str(count - waste))
    print("Total invalid datapoint" + str(waste))
