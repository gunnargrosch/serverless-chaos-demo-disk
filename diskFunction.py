import os
import json
import time
import glob
import boto3

from chaos_lib import *

@corrupt_diskspace
def function(event, context):

    path = "/tmp/"
    filename = path + "diskFunction-"+str(time.time())+".txt"

    # create text file in tmp
    with open(filename, "w") as file:
        diskfree = float(os.statvfs(path).f_bsize * os.statvfs(path).f_bavail) / 1024 / 1024
        file.write("Free disk space " + str(diskfree) + " MB")

    # read text file in tmp
    with open(filename, "r") as file:
        filecontents = file.read()

    # list files in tmp
    files = [f for f in glob.glob(path + "*.*", recursive=True)] 
    
    # assemble the result
    result = {'Filename': filename, 'FileContents': filecontents, 'FolderContents': files}

    # create a response
    response = {
        "statusCode": 200,
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
            },
        "body": json.dumps(result)
    }

    return response
