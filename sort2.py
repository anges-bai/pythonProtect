#插入排序
for i in range(1,len(num)):
    temp = num[i]
    for j in range(i,-1,-1):
        if num[j-1] > temp:
            num[j] = num[j-1]
        else:
            break
    if i !=j:
        num[j] = temp
print(num)
