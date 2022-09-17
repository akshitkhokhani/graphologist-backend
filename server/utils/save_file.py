import datetime
import os
import shutil
import uuid

STATIC_FILE="images"


# Save File locally
def save_file(file):
    try:

        date = datetime.datetime.now()
        time_stamp = int(datetime.datetime.timestamp(date) * 1000)
        id = str(uuid.uuid4())

        # set filename
        extension = file.filename.split(".")[-1]
        file_name = str(id + "." + extension)

        # Open File and save as binary
        with open(f"{STATIC_FILE}/{file_name}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    except Exception as e:
        raise Exception("File Error Occured")

    return file_name