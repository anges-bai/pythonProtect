//编写一个程序，他以球体的半径（浮点数）作为输入，并输出球体的直径、圆周长、表面积、体积。


def ball():
    while True:
        try:
            p = 3.14
            r = float(input("请输入球体半径："))
            if r <= 0:
                print("输入的球体半径不能小于0！")
            else:
                print("球体的直径是:%.3f"%(r*2))
                print("球体的圆周长是:%.3f"%(2*p*r))
                print("球体的表面积是:%.3f"%(4*p*(r**2)))
                print("球体的体积是：%.3f"%((4/3)*p*pow(r,3)))
                break
        except ValueError:
            print("输入错误，请输入数字！")

if __name__ == "__main__":
    ball()
