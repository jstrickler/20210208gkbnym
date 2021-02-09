import os

start_dir = "."
#  start_dir = os.path.abspath(start_dir)
SKIP = ".git"
for folder, folders, files in os.walk(start_dir):
    if SKIP in folders:
        folders.remove(SKIP)
    print(folder)
    for file_name in files:
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder, file_name)
            file_size = os.path.getsize(file_path)
            print("  {:8d} {}".format(file_size, file_name))
