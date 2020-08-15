s = ""
while True:
    name = input("请输入用户名:")[0:21]
    if name == "q" or name == "Q":
        break1
    ser = input("请输入密码:")[0:21]
    mal = input("请输入邮箱:")[0:21]
    info = "{0}\t{1}\t{2}\n"
    v = info.format(name, ser, mal)
    s = s + v
 
print(s.expandtabs(20))
