from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import tkinter.ttk as ttk
import sqlite3
class employeeClass:
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



        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()




        #search Frame
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12),bg="white",bd=3)
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #options
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",12))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="white",bd=3).place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=410,y=10,width=150,height=30)


        #title
        title=Label(self.root,text="Employee Details",font=("goudy old style",15,"bold"),bg="#722F37",fg="white",bd=3).place(x=50,y=100,width=1000)


        #content
        #row1
        lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",14),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",14),bg="white").place(x=370,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",14),bg="white").place(x=750,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("ARIEL",14),bg="white").place(x=150,y=150,width=180)
        # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("ARIEL",14),bg="white").place(x=450,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),state='readonly',justify=CENTER,font=("goudy old style",12))
        cmb_gender.place(x=450,y=150,width=180)
        cmb_gender.current(0)
        
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("ARIEL",14),bg="white").place(x=850,y=150,width=180)


        
        #row2
        lbl_name=Label(self.root,text="Name",font=("goudy old style",14),bg="white").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",14),bg="white").place(x=370,y=190)
        lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",14),bg="white").place(x=750,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("ARIEL",14),bg="white").place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("ARIEL",14),bg="white").place(x=450,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("ARIEL",14),bg="white").place(x=850,y=190,width=180)
        # # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("ARIEL",14),bg="white").place(x=450,y=150,width=180)
        # cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),state='readonly',justify=CENTER,font=("goudy old style",12))
        # cmb_gender.place(x=450,y=150,width=180)
        # cmb_gender.current(0)
        
        
        #row3
        lbl_email=Label(self.root,text="Email",font=("goudy old style",14),bg="white").place(x=50,y=230)
        lbl_pass=Label(self.root,text="Password",font=("goudy old style",14),bg="white").place(x=370,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",14),bg="white").place(x=750,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("ARIEL",14),bg="white").place(x=150,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("ARIEL",14),bg="white").place(x=450,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",12))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)

        #row4
        lbl_address=Label(self.root,text="Address",font=("goudy old style",14),bg="white").place(x=50,y=270)
        

        self.txt_address=Text(self.root,font=("ARIEL",14),bg="white")
        self.txt_address.place(x=150,y=280,width=300,height=60)
       
        #button
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=500,y=330,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=650,y=330,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=800,y=330,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#722F37",fg="white",bd=3,cursor="hand2").place(x=950,y=330,width=110,height=28)

        
        #Employee Details
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=380,relwidth=1,height=120)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
       

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview) #horizontal scrollbar
        scrolly.config(command=self.EmployeeTable.yview) #vertical scrollbar

        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")

        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=200)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#=======================================================================================

    def add(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID required",parent=self.root)
            else:
                cur.execute("Select * from employee id where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID already assigned, try a different ID",parent=self.root)
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address) values(?,?,?,?,?,?,?,?,?,?)",(
                                        self.var_emp_id.get(),
                                        self.var_name.get(),  
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                    
                                        self.var_dob.get(),
                                        self.var_doj.get(),

                                    
                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)   

    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        #print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])  
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])

    
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])

    
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END),  
        self.txt_address.insert(END,row[9])


    def update(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror(Error ,"Employee ID required",parent=self.root)
            else:
                cur.execute("Select * from employee id where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=? where eid=?",(
                                       
                                        self.var_name.get(),  
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                    
                                        self.var_dob.get(),
                                        self.var_doj.get(),

                                    
                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_emp_id.get(),                    
                                ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}" ,parent=self.root)

    
    def delete(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()

        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID required",parent=self.root)
            else:
                cur.execute("Select * from employee id where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete the selected record?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)
    
    def clear(self):                                 #clear
        self.var_emp_id.set("")
        self.var_name.set("")  
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("") 

    
        self.var_dob.set("")
        self.var_doj.set("")

    
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0',END),  
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
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)   

if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()