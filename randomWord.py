ef check_code():
    import random
    checkcode = ""
    for i in range(4):
        current = random.randrange(0, 4)
        if current != i:
            temp = chr(random.randint(65, 90))
        else:
            temp = random.randint(0, 9)
        checkcode = str(temp)
    return checkcode
while True:
    code = check_code()
    code1 = code.lower()
    print(code1)
    ver_code = input("请输入上面验证码：")
    ver_code1 = ver_code.lower()
    if ver_code1 == code1:
        print("我喜欢你")
        break
