from zipfile import ZipFile 
with ZipFile("/workspaces/mykeyan/single-line data.zip", 'r') as zObject: 
    zObject.extractall( path="/workspaces/mykeyan") 