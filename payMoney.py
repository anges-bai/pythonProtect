
//编写一个程序，让用户输入文件名并且向终端输出报表，展示在给定的周期应该向每一位雇员支付的工资。
//这个报表应该是表格的格式，并且具有相应的表头。每一行应该包含雇员的名称、工作的小时数，以及该周期所支付的工资。


from prettytable import PrettyTable

class zhou_money():

    def __init__(self):
        self.name_form = PrettyTable(["雇员名称","工作小时","周工资"])
        self.break_flag = True

    def __str__(self):
        print(self.name_form)
        
    #获取用户输入
    def add_salary(self):
        while self.break_flag == True:
            try:
                self.add_name = input("请输入雇员名称：")
                self.add_time = int(input("请输入工作小时："))
                if self.add_time < 0:
                    print("工作小时不能少于0小时！")
                    continue
                self.add_Hoursmoney = float(input("请输入时薪："))
                if self.add_Hoursmoney <= 0:
                    print("工作时薪必须大于0元每小时")
                    continue
                self.add_day_money = self.add_time*self.add_Hoursmoney
                self.Wage_scale()
                self.confirm()
                break
            except ValueError:
                print("输入错误，请从新输入！")
            self.break_flag == False

    #列表中添加保存用户输入记录
    def Wage_scale(self):
        self.name_form.add_row([self.add_name,self.add_time,self.add_day_money])
        
    #添加结束判断
    def confirm(self):
        while self.break_flag == True:
            try:
                self.add_confrim = input("添加完毕，是否继续添加(Y/N)：")
                if self.add_confrim.isalpha() == False:
                    print("请输入字母进行操作！")
                elif self.add_confrim == "Y":
                    self.add_salary()
                    break
                elif self.add_confrim == "N":
                    break
            except ValueError:
                print("输入错误，请从新输入！")
            print(1)
            self.break_flag == False
        

test = zhou_money()
test.add_salary()
test.__str__()

