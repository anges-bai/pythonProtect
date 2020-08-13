count = 0
for i in range(10000, 100000):
    a = str(i)
    if a[0] == a[-1] and a[1] == a[-2]:
        count +=1
        print(i)
print(count)
