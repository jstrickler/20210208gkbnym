import os

total_lines = 0

for folder, folders, filenames in os.walk('.'):
    for file_name in filenames:
        if file_name.endswith('.py'):
            file_path = os.path.join(folder, file_name)
            with open(file_path) as file_in:
                for i, _ in enumerate(file_in):
                    pass
                total_lines += (i + 1)
print("Total: {} lines".format(total_lines))