import sys
from PyQt5 import QtWidgets, QtSql
from PyQt5.Qt import Qt
from getpass import getpass
from mysql.connector import connect, Error
from PyQt5.QtWidgets import QDialog, QApplication
import menu, order, orderlist, orderproductlist, employeelist, customerlist, productlist, salelist
from datetime import datetime

class Main(QtWidgets.QMainWindow, menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def init(self):
        #назначаем действия по кнопкам
        self.pushButton.clicked.connect(self.employeelist)
        self.pushButton_2.clicked.connect(self.customerlist)
        self.pushButton_3.clicked.connect(self.productlist)
        self.pushButton_4.clicked.connect(self.order)
        self.pushButton_5.clicked.connect(self.salelist)
        
    def order(self):
        self.order = Order()
        self.order.show()
        self.hide()
    
    def employeelist(self):
        self.employeelist = EmployeeList()
        self.employeelist.show()
        self.hide()

    def customerlist(self):
        self.customerlist = CustomerList()
        self.customerlist.show()
        self.hide()

    def productlist(self):
        self.productlist = ProductList()
        self.productlist.show()
        self.hide()

    def salelist(self):
        self.salelist = SaleList()
        self.salelist.show()
        self.hide()

class Order(QtWidgets.QMainWindow, order.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def init(self):
        self.pushButton.clicked.connect(self.orderlist)
        self.pushButton_2.clicked.connect(self.orderproductlist)
        self.pushButton_4.clicked.connect(self.back)

    def back(self):
        self.main = Main()
        self.main.show()
        self.hide()

    def orderlist(self):
        self.orderlist = Orderlist()
        self.orderlist.show()
        self.hide()

    def orderproductlist(self):
        self.orderproductlist = OrderProductList()
        self.orderproductlist.show()
        self.hide()

class Orderlist(QtWidgets.QMainWindow, orderlist.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from orders"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_3.clicked.connect(self.framed)
        self.pushButton_5.clicked.connect(self.delivered)

    def back(self):
        self.driver = Order()
        self.driver.show()
        self.hide()

    def framed(self):
        id = self.lineEdit_3.text()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
        ) as connection:
            select_query = "call set_status_framed(%s)"
            select_tuple = [(id, )]
            with connection.cursor() as cursor:
                cursor.execute(select_query, select_tuple[0])
                connection.commit()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from orders"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)
                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def delivered(self):
        id = self.lineEdit_3.text()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
        ) as connection:
            select_query = "call set_status_delivered(%s)"
            select_tuple = [(id, )]
            with connection.cursor() as cursor:
                cursor.execute(select_query, select_tuple[0])
                connection.commit()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from orders"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)
                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
        ) as connection:
            delete_query = "DELETE from orders where Order_ID = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from orders"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)
                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

                    self.lineEdit_2.setText("")

    def add(self):
        Order_Employee_ID = self.lineEdit.text()
        Status = "Создан"
        OrderDate = datetime.now()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                insert_query = "INSERT INTO orders(Order_Employee_ID, Status, OrderDate) VALUES (%s, %s, %s)"
                insert_tuple = [(Order_Employee_ID, Status, OrderDate)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from orders"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)
                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

                    self.lineEdit.setText("")

class OrderProductList(QtWidgets.QMainWindow, orderproductlist.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from orderproducts"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1
                   


    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)

    def back(self):
        self.driver = Order()
        self.driver.show()
        self.hide()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
        ) as connection:
            delete_query = "DELETE from orderproducts where OrderProduct_ID = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from orderproducts"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)
                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

                    self.lineEdit_2.setText("")

    def add(self):
        Order_ID = self.lineEdit.text()
        Product_ID = self.lineEdit_3.text()
        Order_Product_Quantity = self.lineEdit_4.text()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                insert_query = "INSERT INTO orderproducts(Order_ID, Product_ID, Order_Product_Quantity) VALUES (%s, %s, %s)"
                insert_tuple = [(Order_ID, Product_ID, Order_Product_Quantity)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from orderproducts"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)
                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1
                            
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")

class EmployeeList(QtWidgets.QMainWindow, employeelist.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from employees"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1
                   


    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)

    def back(self):
        self.driver = Main()
        self.driver.show()
        self.hide()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
        ) as connection:
            delete_query = "DELETE from employees where Employee_ID = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from employees"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)
                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

                    self.lineEdit_2.setText("")

    def add(self):
        FirstName = self.lineEdit.text()
        LastName = self.lineEdit_3.text()
        Position = self.lineEdit_4.text()
        Salary = self.lineEdit_5.text()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                insert_query = "INSERT INTO employees(FirstName, LastName, Position, Salary) VALUES (%s, %s, %s, %s)"
                insert_tuple = [(FirstName, LastName, Position, Salary)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from employees"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)
                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1
                            
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.lineEdit_5.setText("")

class CustomerList(QtWidgets.QMainWindow, customerlist.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from customers"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1
                   


    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)

    def back(self):
        self.driver = Main()
        self.driver.show()
        self.hide()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
        ) as connection:
            delete_query = "DELETE from customers where Customer_ID = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from customers"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)
                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

                    self.lineEdit_2.setText("")

    def add(self):
        FirstName = self.lineEdit.text()
        LastName = self.lineEdit_3.text()
        Adress = self.lineEdit_4.text()
        PhoneNumber = self.lineEdit_5.text()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                insert_query = "INSERT INTO customers(FirstName, LastName, Adress, PhoneNumber) VALUES (%s, %s, %s, %s)"
                insert_tuple = [(FirstName, LastName, Adress, PhoneNumber)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from customers"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)
                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1
                            
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.lineEdit_5.setText("")

class ProductList(QtWidgets.QMainWindow, productlist.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from products"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 6):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1
                   


    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)

    def back(self):
        self.driver = Main()
        self.driver.show()
        self.hide()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
        ) as connection:
            delete_query = "DELETE from products where Product_ID = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from products"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)
                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 6):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

                    self.lineEdit_2.setText("")

    def add(self):
        Name = self.lineEdit.text()
        Description = self.lineEdit_3.text()
        Price = self.lineEdit_4.text()
        Quantity = self.lineEdit_5.text()
        Manufacturer = self.lineEdit_6.text()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                insert_query = "INSERT INTO products(Name, Description, Price, Quantity, Manufacturer) VALUES (%s, %s, %s, %s, %s)"
                insert_tuple = [(Name, Description, Price, Quantity, Manufacturer)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from products"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)
                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 6):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1
                            
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.lineEdit_5.setText("")
                    self.lineEdit_6.setText("")

class SaleList(QtWidgets.QMainWindow, salelist.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from sales"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 7):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1
                   
    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)

    def back(self):
        self.driver = Main()
        self.driver.show()
        self.hide()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
        ) as connection:
            delete_query = "DELETE from sales where Sale_ID = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from sales"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)
                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 7):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

                    self.lineEdit_2.setText("")

    def add(self):
        Customer_ID = self.lineEdit.text()
        Employee_ID = self.lineEdit_3.text()
        Product_ID = self.lineEdit_4.text()
        Quantity = self.lineEdit_5.text()
        SaleDate = datetime.now()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                insert_query = "INSERT INTO sales(Customer_ID, Employee_ID, Product_ID, Quantity, SaleDate) VALUES (%s, %s, %s, %s, %s)"
                insert_tuple = [(Customer_ID, Employee_ID, Product_ID, Quantity, SaleDate)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        with connect(
                host="localhost",
                user="root",
                password="89181024524Ni@",
                database="pharmacy2",
            ) as connection:
                select_query = "select * from sales"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)
                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 7):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1
                            
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.lineEdit_5.setText("")

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec_()

if __name__ == '__main__':
    main()
