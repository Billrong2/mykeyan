
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
data_dir = []
X = []
y = []
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
                X.append(data[i]["Parent Commit"])
                y.append(data[i]["Complete After Code"])
    elif "UNKNOWN to Try" in out_file:
        key_name = "UNKNOWN to Try"
        f = open(out_file)
        data = json.load(f)[key_name]
        for i in range(len(data)):
            if "Complete After Code" and "Parent Commit" in data[i]:
                X.append(data[i]["Parent Commit"])
                y.append(data[i]["Complete After Code"])
    elif "Constructor to Constructor" in out_file:
        key_name = "Constructor to Constructor"
    elif "Method to Method" in out_file:
        key_name = "Method=>Method"
print(X, y)


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AdamW, get_scheduler
# Load pre-trained CodeT5 model and tokenizer
model_name = "eleutherai/codet5-small-0-finetuned-code-search-net"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Your list of input strings x
input_strings = X

# Tokenization
inputs = tokenizer(input_strings, return_tensors="pt", padding=True, truncation=True)

# Example: Prepare labels (replace this with your actual labels) y
label_strings = y
labels = tokenizer(label_strings, return_tensors="pt", padding=True, truncation=True)

# Fine-tuning setup
optimizer = AdamW(model.parameters(), lr=5e-5)
scheduler = get_scheduler(
    "linear",
    optimizer=optimizer,
    num_warmup_steps=0,
    num_training_steps=len(inputs["input_ids"]) * num_epochs,
)

# Fine-tuning loop
num_epochs = 1

for epoch in range(num_epochs):
    # Forward pass
    outputs = model(**inputs, labels=labels)
    loss = outputs.loss

    # Backward pass and optimization
    loss.backward()
    optimizer.step()
    scheduler.step()

    # Print or log the loss for monitoring
    print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item()}")

# Save fine-tuned model
model.save_pretrained("path/to/save/fine-tuned-model")

# Load fine-tuned model for inference
fine_tuned_model = AutoModelForSeq2SeqLM.from_pretrained("path/to/save/fine-tuned-model")