import os   # includes os.path
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "alice.txt"

file_path = os.path.join(FOLDER, FILE_NAME)
print("file path:", file_path)

file_size = os.path.getsize(file_path)
print("file size:", file_size)




raw_modtime = os.path.getmtime(file_path)
print("raw mod time:", raw_modtime)
mod_time = datetime.fromtimestamp(raw_modtime)
print("mod time:", mod_time)

print("is it a file?", os.path.isfile(file_path))

print("path only:", os.path.dirname(file_path))
print("file only:", os.path.basename(file_path))
print("absolute path:", os.path.abspath(file_path))

for path in file_path, "gadzooks!",  "wankel_rotary_engine.txt":
    print(path, os.path.exists(path))
