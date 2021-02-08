
capitals = {
    'India': 'New Delhi',
    'US': "Washington, DC",
    'Canada': 'Ottawa',
    'UK': 'London',
}
print(capitals['India'])
print(len(capitals))
print(capitals.get('Spain'))
print(capitals.get('Canada'))

# sort dictionary by keys:
for country, capital in sorted(capitals.items()):
    print(country, capital)


