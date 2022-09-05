from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import tkinter.ttk as ttk
import sqlite3

class stockClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        blank_space =" "
        self.root.title(110*blank_space+"Plamparambil Power Tools Billing and Management System |  Developed by Shibino")
        self.root.config(bg="white")
        self.root.focus_force()


        #-----------------------------

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_pid=StringVar()
        self.var_hsncode=StringVar()
        self.var_discount=StringVar()
        self.sup_list=[]
        self.var_sup=StringVar()
        # self.var_cat=StringVar()
        
        # self.cat_list=[]
        self.fetch_sup()
       
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        stock_Frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        stock_Frame.place(x=10,y=10,width=450,height=480)

        title=Label(stock_Frame,text="Manage Stock Details",font=("goudy old style",18,"bold"),bg="#722F37",fg="white",bd=3)
        title.pack(side=TOP,fill=X)

        #col-1
        lbl_pid=Label(stock_Frame,text="P ID",font=("goudy old style",18,"bold"),bg="white",bd=3).place(x=30,y=60)
        lbl_supplier=Label(stock_Frame,text="Supplier",font=("goudy old style",18,"bold"),bg="white",bd=3).place(x=30,y=110)
        # lbl_category=Label(stock_Frame,text="Category",font=("goudy old style",18,"bold"),bg="white",bd=3).place(x=30,y=60)
        lbl_item_name=Label(stock_Frame,text="Item Name",font=("goudy old style",18,"bold"),bg="white",bd=3).place(x=30,y=160)
        lbl_hsn_code=Label(stock_Frame,text="HSN Code",font=("goudy old style",18,"bold"),bg="white",bd=3).place(x=30,y=210)
        lbl_price=Label(stock_Frame,text="Price",font=("goudy old style",18,"bold"),bg="white",bd=3).place(x=30,y=260)
        lbl_qty=Label(stock_Frame,text="Quantity",font=("goudy old style",18,"bold"),bg="white",bd=3).place(x=30,y=310)
        lbl_discount=Label(stock_Frame,text="Discount",font=("goudy old style",18,"bold"),bg="white",bd=3).place(x=30,y=360)
        # lbl_status=Label(stock_Frame,text="Status",font=("goudy old style",18,"bold"),bg="white",bd=3).place(x=30,y=310)


       
        #col-2

        
        cmb_sup=ttk.Combobox(stock_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",12))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)

        # cmb_cat=ttk.Combobox(stock_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",12))
        # cmb_cat.place(x=150,y=60,width=200)
        # cmb_cat.current(0)



        txt_pid=Entry(stock_Frame,textvariable=self.var_pid,font=("goudy old style",12),bg="white").place(x=150,y=60,width=200)
        txt_name=Entry(stock_Frame,textvariable=self.var_name,font=("goudy old style",12),bg="white").place(x=150,y=160,width=200)
        txt_hsn_code=Entry(stock_Frame,textvariable=self.var_hsncode,font=("goudy old style",12),bg="white").place(x=150,y=210,width=200)
        txt_price=Entry(stock_Frame,textvariable=self.var_price,font=("goudy old style",12),bg="white").place(x=150,y=260,width=200)
        txt_qty=Entry(stock_Frame,textvariable=self.var_qty,font=("goudy old style",12),bg="white").place(x=150,y=320,width=200)
        txt_discount=Entry(stock_Frame,textvariable=self.var_discount,font=("goudy old style",12),bg="white").place(x=150,y=370,width=200)
       

        # cmb_status=ttk.Combobox(stock_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",12))
        # cmb_status.place(x=150,y=310,width=200)
        # cmb_status.current(0)


        #buttons

        btn_add=Button(stock_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=10,y=420,width=100,height=40)
        btn_update=Button(stock_Frame,text="Update",command=self.update,font=("goudy old style",15),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=120,y=420,width=100,height=40)
        btn_delete=Button(stock_Frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=230,y=420,width=100,height=40)
        btn_clear=Button(stock_Frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=340,y=420,width=100,height=40)
    

        #search Frame
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12),bg="white",bd=3)
        SearchFrame.place(x=480,y=10,width=600,height=80)

        #options
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Supplier","Itemname"),state='readonly',justify=CENTER,font=("goudy old style",12))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="white",bd=3).place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=410,y=10,width=150,height=30)

        #Stock Details
        s_Frame=Frame(self.root,bd=3,relief=RIDGE)
        s_Frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(s_Frame,orient=VERTICAL)
        scrollx=Scrollbar(s_Frame,orient=HORIZONTAL)
       

        self.StockTable=ttk.Treeview(s_Frame,columns=("pid","Supplier","itemname","hsncode","price","qty","discount"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.StockTable.xview) #horizontal scrollbar
        scrolly.config(command=self.StockTable.yview) #vertical scrollbar

        self.StockTable.heading("pid",text="P Id")
        self.StockTable.heading("Supplier",text="Supplier")
        self.StockTable.heading("itemname",text="Itemname")
        self.StockTable.heading("hsncode",text="HSN Code")
        self.StockTable.heading("price",text="Price")
        self.StockTable.heading("qty",text="Quantity")
        self.StockTable.heading("discount",text="Discount")

        self.StockTable["show"]="headings"

        self.StockTable.column("pid",width=90)
        self.StockTable.column("Supplier",width=100)
        self.StockTable.column("itemname",width=100)
        self.StockTable.column("hsncode",width=100)
        self.StockTable.column("price",width=100)
        self.StockTable.column("qty",width=100)
        self.StockTable.column("discount",width=100)
        self.StockTable.pack(fill=BOTH,expand=1)
        self.StockTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        self.fetch_sup()


    def fetch_sup(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            self.sup_list.append("Empty")
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)   


    def add(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()
        try:
            if self.var_sup.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields required",parent=self.root)
            else:
                cur.execute("Select * from stock where itemname=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product Already Present, try different",parent=self.root)
                else:
                    cur.execute("Insert into stock (supplier,itemname,hsncode,price,qty,discount) values(?,?,?,?,?,?)",(
                                        self.var_sup.get(),  
                                        self.var_name.get(),
                                        self.var_hsncode.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_discount.get()
                                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Item Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from stock")
            rows=cur.fetchall()
            # print(rows)
            self.StockTable.delete(*self.StockTable.get_children())
            for row in rows:
               self.StockTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)   

    def get_data(self,ev):
        f=self.StockTable.focus()
        content=(self.StockTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_sup.set(row[1])  
        self.var_name.set(row[2])
        self.var_hsncode.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_discount.set(row[6])




    def update(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please select item from list",parent=self.root)
            else:
                cur.execute("Select * from stock where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Item",parent=self.root)
                else:
                    cur.execute("Update stock set supplier=?,itemname=?,hsncode=?,price=?,qty=?,discount=? where pid=?",(
                                        self.var_sup.get(),  
                                        self.var_name.get(),
                                        self.var_hsncode.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_discount.get(),
                                        self.var_pid.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Item Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}" ,parent=self.root)


    def delete(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()

        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Select Item from the List",parent=self.root)
            else:
                cur.execute("Select * from stock where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete the selected record?",parent=self.root)
                    if op==True:
                        cur.execute("delete from stock where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Item Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)

    def clear(self):                                 #clear
        self.var_sup.set("Select"),  
        self.var_name.set(""),
        self.var_hsncode.set("")
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_pid.set("") ,
        self.var_discount.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()


    def search(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search Input should be required",parent=self.root)
            else:
                cur.execute("select * from stock where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.StockTable.delete(*self.StockTable.get_children())
                    for row in rows:
                        self.StockTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)   




if __name__=="__main__":
    root=Tk()
    obj=stockClass(root)
    root.mainloop()
