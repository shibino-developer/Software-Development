from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        blank_space =" "
        self.root.title(150*blank_space+"Plamparambil Power Tools Billing and Management System |  Developed by Shibino")
        self.root.config(bg="#fafafa")

        # self.root.wm_iconbitmap('profile.ico')



        # images

        self.phone_image=ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=100,y=50)


        #Login frame

        self.employeeid=StringVar()
        self.password=StringVar()

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=750,y=90,width=350,height=460)

        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=40,relwidth=1)

        lbl_employeeid=Label(login_frame,text="User ID",font=("Andalus",15),bg="white",fg="#722F37").place(x=50,y=110)
       
        txt_uername=Entry(login_frame,textvariable=self.employeeid,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)


        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#722F37").place(x=50,y=190)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=220,width=250)

        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#722F37",activebackground="#722F37",fg="white",cursor="hand2").place(x=50,y=300,width=250,height=35)


       
      
        #animation images

        self.im1=ImageTk.PhotoImage(file="images/phonela.jpg")
        self.im2=ImageTk.PhotoImage(file="images/123.png")
    

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=220,y=100,width=250,height=428)

        self.animate()


    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im
    
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)


    def login(self):
        con=sqlite3.connect(database=r'tbs.db')
        cur=con.cursor()
        try:
            if self.employeeid.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employeeid.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid Username/password",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} ",parent=self.root)


root=Tk()
obj=Login_System(root)
root.mainloop()


