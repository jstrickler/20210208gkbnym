fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

# list comprehension = map() + filter()
# [EXPR for VAR in ITERABLE ... if CONDITION ...]
f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

all_food = ['spam', 'spam', 'toast', 'eggs', 'spam', 'ham', 'spam', 'spam', 'spam', 'spam',
            'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'ham', 'spam',
            'spam', 'eggs', 'spam', 'bacon', 'spam', 'spam', 'spam', 'spam', 'eggs']

good_food = [f for f in all_food if f not in ('spam', 'bacon', 'ham')]
print("good_food:", good_food, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print("last_names:", last_names, '\n')

last_names_gen = (p[1] for p in people)
print("last_names:", last_names_gen, '\n')
for last_name in last_names_gen:
    print(last_name)
print()



