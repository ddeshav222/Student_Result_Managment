from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
from register import RegisterClass
import os



class LoginClass:
    def __init__(self, root ):
        self.root= root
        self.root.title("Login  PAGE")
        self.root.geometry("1350x700+0+0")       
        self.root.config(bg="white")    
        self.root.resizable(False,False)


        frame1= Frame(self.root,bg="light blue")
        frame1.place(x=280,y=100,width=760,height=470)


    # ========== variables =================
        self.val_email=StringVar()
        self.val_pass=StringVar()


        title=Label(frame1,text="LOGIN HERE",font=("times new roman",20,"bold"),bg="light blue",fg="red").place(x=240,y=40)


        lbl_email=Label(frame1,text="Email Address",font=("",19,"bold"),bg="light green").place(x=140,y=120)
        txt_email=Entry(frame1,width=30,font=("",17,"bold"),textvariable=self.val_email).place(x=140,y=190,width=350,height=37)
        

        lbl_password=Label(frame1,text="Password",font=("",19,"bold"),bg="light green").place(x=140,y=280)
        txt_password=Entry(frame1,width=30,font=("",17,"bold"),textvariable=self.val_pass).place(x=140,y=350,width=350,height=37)

        login_btn=Button(frame1,text="LOGIN",bg="grey",font=("",12,"bold"),command=self.login).place(x=190,y=410,width=100)

        newAccount_btn=Button(frame1,text="SIGN UP",bg="light green",font=("",12,"bold"),command=self.register).place(x=370,y=410,width=100)
        
        back_btn=Button(frame1,text="BACK",bg="yellow",font=("",12,"bold"),command=self.back).place(x=520,y=410,width=100)
        

    def back(self):
        self.root.destroy()
        os.system("Python start.py")


    def register(self):
        self.new_win= Toplevel(self.root)
        self.new_obj=RegisterClass(self.new_win) 


    def login(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:

            if self.val_email.get()=="" or self.val_pass=="":
                messagebox.showerror("Error","Please fill all the entries",parent=self.root)      
  
            else:
                curs.execute("select * from employee where email=?",(self.val_email.get(),))
                row=curs.fetchone()

                if row == None:
                    messagebox.showerror("Error","No admin present with this email id",parent=self.root)      
                else:
                    if self.val_pass.get()!=str(row[7]):
                        messagebox.showerror("Error","Incoorect password",parent=self.root) 
                        con.commit() 
                    else:
                        messagebox.showinfo("Success","User authenticated",parent=self.root) 
                        con.commit()
                        self.root.destroy()
                        os.system("python dashboard.py")
                        

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    
        





if __name__=="__main__":
    root= Tk()
 
    obj= LoginClass(root)
    root.mainloop()   

