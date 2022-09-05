from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from stock import stockClass
from sales import salesClass
from billing import billClass
import sqlite3
from tkinter import messagebox
import os
import time
# from tkinter.filedialog import askopenfile
# from openpyxl import load_workbook
# import numpy
# import pandas as pd

class TBS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        blank_space =" "
        self.root.title(150*blank_space+"Plamparambil Power Tools Billing and Management System |  Developed by Shibino")
        self.root.config(bg="white")

        #title
        self.icon_title=PhotoImage(file="images/tool.png")
        title = Label(self.root,text="PLAMPARAMBIL POWER TOOLS",image=self.icon_title,compound=LEFT,font=("ARIEL",40,"bold"),bg="#722F37",fg="white", anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=120)

        #button logout
        btn_logout = Button(self.root,text="Logout",command=self.logout,font=("ARIEL",15,"bold"),bg="white",cursor="hand2").place(x=1200,y=30,height=50,width=100)

        #clock
        self.lbl_clock = Label(self.root,text="Welcome To Plamparambil Power Tools...!!\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("ARIEL",14),bg="white",fg="black",borderwidth=3, relief="solid")
        self.lbl_clock.place(x=0,y=120,relwidth=1,height=30)

        #Left Menu
        self.MenuLogo=PhotoImage(file="images/menu.png")
        

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=150,width=230,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu = Label(LeftMenu,text="MENU",font=("ARIEL",15,"bold"),bg="#722F37",fg="white")
        lbl_menu.pack(side=TOP,fill=X)


        btn_employee = Button(LeftMenu,text="Users",command=self.employee,image=self.icon_side,compound=LEFT,padx=20,anchor="w",font=("ARIEL",10,"bold"),bg="white",bd=3,cursor="hand2").place(x=30,y=260,height=40,width=150)
        btn_supplier = Button(LeftMenu,text="Suppliers",command=self.supplier,image=self.icon_side,compound=LEFT,padx=20,anchor="w",font=("ARIEL",10,"bold"),bg="white",bd=3,cursor="hand2").place(x=30,y=300,height=40,width=150)
        btn_stock = Button(LeftMenu,text="Stocks",command=self.stock,image=self.icon_side,compound=LEFT,padx=20,anchor="w",font=("ARIEL",10,"bold"),bg="white",bd=3,cursor="hand2").place(x=30,y=340,height=40,width=150)
        btn_sales = Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=20,anchor="w",font=("ARIEL",10,"bold"),bg="white",bd=3,cursor="hand2").place(x=30,y=380,height=40,width=150)
        btn_billing = Button(LeftMenu,text="Billing",command=self.billing,image=self.icon_side,compound=LEFT,padx=20,anchor="w",font=("ARIEL",10,"bold"),bg="white",bd=3,cursor="hand2").place(x=30,y=420,height=40,width=150)
        # btn_file = Button(LeftMenu,text="Upload File",command=self.openfile,image=self.icon_side,compound=LEFT,padx=20,anchor="w",font=("ARIEL",10,"bold"),bg="white",bd=3,cursor="hand2").place(x=30,y=460,height=40,width=150)


        #content
        self.lbl_employee = Label(self.root,text="Employees\n[ 0 ]",bd=5,relief=RIDGE,bg="#722F37",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=250,y=170,height=100,width=200)

        self.lbl_supplier = Label(self.root,text="Suppliers\n[ 0 ]",bd=5,relief=RIDGE,bg="#722F37",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=600,y=170,height=100,width=200)

        # self.lbl_category = Label(self.root,text="Categories\n[ 0 ]",bd=5,relief=RIDGE,bg="#722F37",fg="white",font=("goudy old style",20,"bold"))
        # self.lbl_category.place(x=900,y=170,height=100,width=200)

        self.lbl_stocks = Label(self.root,text="Stocks\n[ 0 ]",bd=5,relief=RIDGE,bg="#722F37",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_stocks.place(x=900,y=370,height=100,width=200)

        self.lbl_sale= Label(self.root,text="Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#722F37",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sale.place(x=350,y=370,height=100,width=200)

        

        #footer
        lbl_footer = Label(self.root,text="TBS-Plamparambil Power Tools Billing and Management System |  Developed by Shibino\nFor any technical issues Contact: +91-8111833958",font=("ARIEL",8),bg="#722F37",fg="white",borderwidth=1, relief="solid")
        lbl_footer.place(x=0,y=670,relwidth=1,height=50)

        self.update_content()

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    # def category(self):
    #     self.new_win=Toplevel(self.root)
    #     self.new_obj=categoryClass(self.new_win)

    def stock(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=stockClass(self.new_win)


    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=billClass(self.new_win)

    
    def update_content(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()
        try:
            cur.execute("select * from stock")
            product=cur.fetchall()
            self.lbl_stocks.config(text=f'Stocks\n[ {str(len(product))} ]')


            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Suppliers\n[ {str(len(supplier))} ]')


            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Employees\n[ {str(len(employee))} ]')

            bill=len(os.listdir('bill'))
            self.lbl_sale.config(text=f'Sales\n [{str(bill)}]')

            
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome To Plamparambil Power Tools...!!\t\t Date: {str(date_)}\t\t Time: {str(time_)}" )
            self.lbl_clock.after(200,self.update_content)
                


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)

    # def openfile(self):
    #     con=sqlite3.connect(database=r'tbs.db')
    #     file = askopenfile(mode ='r', filetypes =[('Excel Files', '*.xlsx *.xlsm *.sxc *.ods *.csv *.tsv')]) # To open the file that you want. 
    # # # ' mode='r' ' is to tell the filedialog to read the file
    # # # 'filetypes=[()]' is to filter the files shown as only Excel files

    #     wb = pd.read_excel('TBS\stock.xlsx',sheet_name = None)

    #     for sheet in wb:
    #         wb[sheet].to_sql(sheet,con,index=False)
    #     con.commit()
    #     con.close()

        # wb = load_workbook('First Excel.xlsx') # Load into openpyxl
        # wb2 = wb.active

        # col_a= wb2['A']
        # col_b= wb2['B']

        # print(col_a)


    def logout(self):
        self.root.destroy()
        os.system("python login.py")



if  __name__=="__main__":
    root=Tk()
    obj=TBS(root)
    root.mainloop()