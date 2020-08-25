#选择排序
k = 0
for i in range(len(num)):
    temp = num[i]
    for j in range(i+1,len(num)):
        if num[j] < temp:
            temp = num[j]
            k = j
    if num[i] > num[k]:
        num[i],num[k] = num[k],num[i]
print(num)
