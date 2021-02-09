import datetime as dt

colors = ['Purple', 'puce', 'pea green', 'green', 'orange', 'BROWN', 'Yellow', 'pink', 'blue']
c1 = sorted(colors)
print("c1:", c1, '\n')

def ignore_case(s):
    compare_value =  s.lower()
    # print("comparing {} as {}".format(s, compare_value))
    return compare_value

c2 = sorted(colors, key=ignore_case)
print("c2:", c2, '\n')

c3 = sorted(colors, key=len)
print("c3:", c3, '\n')

def special(c):
    return len(c), c.lower()

c4 = sorted(colors, key=special)
print("c4:", c4, '\n')

c5 = sorted(colors, key=str.lower)
print("c5:", c5, '\n')




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

for person in  sorted(people):
    print(person)
print('-' * 60)

def by_dob(p):
    return p[3]  # , k2, k3, ...

for person in  sorted(people, key=by_dob):
    print(person)
print('-' * 60)

def first_last(p):
    return p[1], p[0]

for person in  sorted(people, key=first_last):
    print(person)
print('-' * 60)


time_data = [
    (5,2,10),
    (8,3,49, 9),
    (5,18,36, 10),
    (4,2,31, 14),
    (9,5,18),
    (5,1,7),
]
def by_minute(t):
    return t[1], t[0], t[2]

for hour, minute, *value in sorted(time_data, key=by_minute):
    tm = dt.time(hour, minute)
    print(tm, value)
print()


airports = {
    'MAA': 'Chennai',
    'EWR': 'Newark',
    'MCO': 'Orlando',
    'RDU': 'Raleigh-Durham',
    'PNY': 'Pondicherry',
    'PIT': 'Pittsburgh',
}

for code, name in sorted(airports.items()):
    print(code, name)
print()
print(list(airports.items()))

def by_value(item):
    return item[1]

for code, name in sorted(airports.items(), key=by_value):
    print(code, name)
print()

for code, name in sorted(airports.items(), key=lambda e: e[1]):
    print(code, name)
print()
