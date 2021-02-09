value = 56

a = 100

if value > 25:
    a = 44

for i in range(1000000):
    pass

def spam():
    b = 1234  # local
    print("in spam(): a is", a)

spam()
print("in main(): a is", a)
print("i is", i)


#  local -> nonlocal -> global -> builtin


