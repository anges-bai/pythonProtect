def quickSort(num,l,r):
    if l>=r:#如果只有一个数字时，结束递归
        return
    flag=l
    for i in range(l+1,r+1):#默认以第一个数字作为基准数，从第二个数开始比较，生成索引时要注意右部的值
        if num[flag]>num[i]:
            tmp=num[i]
            del num[i]
            num.insert(flag,tmp)
            flag+=1
    quickSort(num,l,flag-1)#将基准数前后部分分别递归排序
    quickSort(num,flag+1,r)
 
num=[1,-2,4,7,6,3,2,3]
quickSort(num,0,7)
print(num)
