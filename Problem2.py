l = [3,2,1]
new = []
for i, v in enumerate(l):
    temp = list([x for x in l if x != l[i]])
    res = 1
    for k in temp:
        res *= k
    new.append(res)
    print(temp)
print(new)