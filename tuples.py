import datetime as dt
person = "Bill", "Gates", "Microsoft", "1955-10-28"
print(type(person))

def divmod(a, b):
    return a // b, a % b

print(divmod(38, 7))

first_name, last_name, product, dob = person
print(first_name, last_name)

x, y = divmod(93, 8)
print(x)
print(y)

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

for person in people:
    print(person[0], person[1])
print("-" * 60)

for first_name, last_name, product, dob in people:
    #  first_name, last_name, product, dob = <next-element-of-people>
    print(first_name, last_name)
print("-" * 60)

time_data = [
    (5,2,10),
    (8,3,49, 9),
    (4,2,31, 14),
    (9,5,18),
    (5,1,7),
]
for hour, minute, *value in time_data:
    tm = dt.time(hour, minute)
    print(tm, value)
print()

colors = ['purple', 'green', 'orange', 'brown']
for i, color in enumerate(colors):
    print(i, color)
print()

airports = {
    'MAA': 'Chennai',
    'RDU': 'Raleigh-Durham',
    'PNY': 'Pondicherry',
    'PIT': 'Pittsburgh',
}

for code, name in airports.items():
    print(code, name)
print()