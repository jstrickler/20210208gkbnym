data = [5, 8, 9, 1, 4]

for d in data:
    print(d * 1000)

# for VAR in ITERABLE:
#    ...use VAR...

actor = "Chris Hemsworth"
for char in actor:
    print(char, end=' ')
print('\n')

for i in range(5):
    print("Python is awesome!!")
print()

while True:
    file_name = input("file name (or q to quit):")
    if file_name == 'q':
        break
    if file_name == '':
        continue
    try:
        with open(file_name) as file_in:
            for line in file_in:
                print(line.rstrip())
    except FileNotFoundError as err:
        print(err)