#!/usr/bin/env python
from president import President

for term in 1, 26, 39, 45:
    p = President(term)  # George Washington

    print("{} {} was born at {}, {} on {}".format(
        p.first_name, p.last_name, p.birth_place, p.birth_state, p.birth_date
    ))
    print()

p = President(26)
print(p.last_name)

field_name = "party"
print(p.party)
print(getattr(p, field_name))

def convert(obj):
    for method in "to_csv", "csv", "csv_out":
        if hasattr(obj, method):
            m = getattr(obj, method)
            return m()
        else:
            pass
            # convert object manually or raise err

def get_full_name(self):
    return f"{self.first_name} {self.last_name}"

setattr(President, "full_name", get_full_name)

print(p.full_name())

setattr(President, "fullname", property(get_full_name))
print(p.fullname)
