from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import tkinter.ttk as ttk
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        blank_space =" "
        self.root.title(110*blank_space+"Plamparambil Power Tools Billing and Management System |  Developed by Shibino")
        self.root.config(bg="white")
        self.root.focus_force()

        #All Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_sup_invoice=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_supdate=StringVar()
       



      

        # #options
        lbl_search=Label(self.root,text="Invoice No.",bg="white",font=("goudy old style",12))
        lbl_search.place(x=700,y=80)
       

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="white",bd=3).place(x=800,y=80,width=160)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=980,y=79,width=100,height=28)


        #title
        title=Label(self.root,text="Supplier Details",font=("goudy old style",15,"bold"),bg="#722F37",fg="white",bd=3).place(x=50,y=10,width=1000,height=40)


        #content
        #row1
        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",14),bg="white").place(x=50,y=80)
       
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("ARIEL",14),bg="white").place(x=180,y=80,width=180)
        # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("ARIEL",14),bg="white").place(x=450,y=150,width=180)
      
        


        
        #row2
        lbl_name=Label(self.root,text="Name",font=("goudy old style",14),bg="white").place(x=50,y=120)
       

        txt_name=Entry(self.root,textvariable=self.var_name,font=("ARIEL",14),bg="white").place(x=180,y=120,width=180)
       
        # # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("ARIEL",14),bg="white").place(x=450,y=150,width=180)
        # cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),state='readonly',justify=CENTER,font=("goudy old style",12))
        # cmb_gender.place(x=450,y=150,width=180)
        # cmb_gender.current(0)
        
        
        #row3
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",14),bg="white").place(x=50,y=160)
       

        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("ARIEL",14),bg="white").place(x=180,y=160,width=180)
       

        #row4
        lbl_supdate=Label(self.root,text="Date",font=("goudy old style",14),bg="white").place(x=50,y=200)
        var_supdate=Entry(self.root,textvariable=self.var_supdate,font=("ARIEL",14),bg="white").place(x=180,y=200,width=180)

       
        #button
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=180,y=370,width=100,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=300,y=370,width=100,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=420,y=370,width=100,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=540,y=370,width=100,height=35)

        
        #Employee Details
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,width=380,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
       

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","supdate"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview) #horizontal scrollbar
        scrolly.config(command=self.supplierTable.yview) #vertical scrollbar

        self.supplierTable.heading("invoice",text="Invoice No.")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("supdate",text="Sup.Date")
        

        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("supdate",width=100)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#=======================================================================================

    def add(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error" ,"Invoice required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Invoice No. already assigned, try a different ID",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,supdate) values(?,?,?,?)",(
                                                self.var_sup_invoice.get(),
                                                self.var_name.get(),  
                                                self.var_contact.get(),
                                                self.var_supdate.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)   

    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        #print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])  
        self.var_contact.set(row[2])
        self.var_supdate.set(row[3])


    def update(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,supdate=? where invoice=?",(
                                        self.var_name.get(),  
                                        self.var_contact.get(),
                                        self.var_supdate.get(),
                                        self.var_sup_invoice.get(),                    
                                ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}" ,parent=self.root)

    
    def delete(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()

        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete the selected record?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)
    
    def clear(self): 
        self.var_sup_invoice.set("")                                #clear
        self.var_name.set("")  
        self.var_contact.set("") 

    
        self.var_supdate.set(""),  
        self.var_searchtxt.set("")
        self.show()

    
    def search(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)   

if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()