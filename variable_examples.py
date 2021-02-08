x = 5    # create int obj with value 5, assign label "x"
# NOT int x = 5;
m = 10

result = x + m
print(result)
y = x    # assign label "y" to same object as "x"

x = 25   # create int obj, assign 25, assign 'x'
print(x, y)

x = "Hello"
x = [1, 2, 3]
x = None
x = {}

print(type(None))

import re
sample = "this is a mango"
m = re.search("s.*m", sample)
if m:
    print(m.group())  # print match
else:
    print("no match")

customer_id = None

#  a-z A-Z 0-9 _

#  snake_case

#  words_separated_by_underscores

#  classes only:   StudlyCaps

# NO: camelCase

# instead of
c_name = "BNYM"
# use
customer_name = "BNYM"

# bool int float complex  NUMERIC
# str bytes list tuple  SEQUENCE
# dict set frozenset   INDEXED






