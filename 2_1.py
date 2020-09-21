keys = list(map(int, input("Input keys : ").split()))
values = list(map(int, input("Input values :").split()))
d = {}
for n in range(len(keys)):
    if n < len(values):
        d[keys[n]] = values[n]
    else:
        d[keys[n]] = 'None'
print(d)
