from timeit import Timer
setup = """
import re
"""

snippet1 = """
with open('DATA/alice.txt') as alice_in:
    with open('karen.txt', 'w') as karen_out:
        for line in alice_in:
            new_line = re.sub('Alice', 'Karen', line, 0, re.IGNORECASE)
            karen_out.write(new_line)
"""

snippet2 = """
with open('DATA/alice.txt') as alice_in:
    with open('karen.txt', 'w') as karen_out:
        contents = alice_in.read()
        new_contents = re.sub('Alice', 'Karen', contents, 0, re.I)
        karen_out.write(new_contents)
"""

t1 = Timer(snippet1, setup)
t2 = Timer(snippet2, setup)

print(t1.timeit(1000))
print(t2.timeit(1000))
