
//图书馆的一个简单的软件系统，会将图书馆建模为图书和读者的一个集合。
//每本图书有一个等待借阅的读者的列表。每本图书有一个标题、一个作者、
//已经借阅了它的一名读者，以及等待这本图书还回后再继续借阅读者的列表。


# -*- coding: UTF-8 -*-
from prettytable import PrettyTable
import pymysql

class book():

    #初始化数据库
    def __init__(self):

        self.db = pymysql.connect("47.101.56.243","root","dingcji652@","mytest",charset="utf8")

        self.cursor = self.db.cursor()


    #调取图书列表
    def book_list(self):

        bk_list = PrettyTable(['图书编号','图书名称','图书作者','图书状态'])

        self.cursor.execute("SELECT * FROM book")

        for r in self.cursor:

            bk_list.add_row(r)

        print(bk_list)

        return bk_list

    #新增图书
    def add_book(self):
        falg = True
        while falg == True:
            x = input("请输入新增书的名称：")
            y = input("请输入新增书的作者：")
            sql_select = "INSERT INTO book(book_name, book_author, book_state) VALUES ('%s', '%s', '%d')" % (x, y, 0)
            self.cursor.execute(sql_select)
            self.db.commit()
            print("新增成功！")
            while falg == True:
                z = input("是否继续新增图书(Y/N)：")
                if z == "Y":
                    self.add_book()
                elif z == "N":
                    falg = False
                else:
                    print("输入错误，检查输入！")
        self.book_list()

    #借阅图书
    def Borrowing_book(self):
        print(self.book_list())
        x = int(input("请输入你要借阅的图书ID："))    
        sql_update ="update book set book_state = '%d' where book_id = %d"
        self.cursor.execute(sql_update % (1,x))
        self.db.commit()
        print("借阅成功！")

    #归还图书
    def return_book(self):
        x = int(input("请输入你要归还的图书ID："))    
        sql_update ="update book set book_state = '%d' where book_id = %d"
        self.cursor.execute(sql_update % (0,x))
        self.db.commit()
        print("归还成功！")

    #用户视图列表
    def view_admin(self):
        s_list = PrettyTable(["欢迎使用图书管理系统V0.1"])
        s_list.add_row(["1：查看列表"])
        s_list.add_row(["2：新增图书"])
        s_list.add_row(["3：借阅图书"])
        s_list.add_row(["4：归还图书"])
        print(s_list)

        i = int(input("请输入序列号进行操作："))
        if i == 1:
            self.book_list()
        elif i == 2:
            self.add_book()
        elif i == 3:
            self.Borrowing_book()
        elif i == 4:
            self.return_book()
        else:
            print("输入错误，检查输入！")


if __name__ == '__main__':
    r = book()
    print(r.view_admin())
