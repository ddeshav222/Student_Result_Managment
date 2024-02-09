from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3


class RegisterClass:
    def __init__(self, root ):
        self.root= root
        self.root.title("REGISTER  PAGE")
        self.root.geometry("1350x700+0+0")       
        self.root.config(bg="white")     

    # ====== background image=============
    


    # ========= Variable ============

        self.val_answer=StringVar()
        self.val_fname=StringVar()
        self.val_lname=StringVar()
        self.val_email=StringVar()
        self.val_contact=StringVar()
        self.val_answer=StringVar()
        self.val_pass=StringVar()
        self.val_confirmPass=StringVar()
        self.val_adminCode=StringVar()
        self.val_question=StringVar()


    # ============= Register Frame =============
       

        frame1= Frame(self.root,bg="light green")
        frame1.place(x=480,y=100,width=760,height=570)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=240,y=40)


        lbl_fName=Label(frame1,text="First Name",font=("",12,"bold"),bg="light green").place(x=20,y=120)
        txt_fName=Entry(frame1,width=30,font=("",12,"bold"),textvariable=self.val_fname).place(x=140,y=120,width=160,height=27)
        
        lbl_lName=Label(frame1,text="Last Name",font=("",12,"bold"),bg="light green").place(x=370,y=120)
        txt_lName=Entry(frame1,width=30,font=("",12,"bold"),textvariable=self.val_lname).place(x=480,y=120,width=160,height=27)

    
        lbl_email=Label(frame1,text="Email",font=("",12,"bold"),bg="light green").place(x=370,y=200)
        txt_email=Entry(frame1,width=30,font=("",12,"bold"),textvariable=self.val_email).place(x=480,y=200,width=160,height=27)

        lbl_contact=Label(frame1,text="Contact No.",font=("",12,"bold"),bg="light green").place(x=20,y=200)
        txt_contact=Entry(frame1,width=30,font=("",12,"bold"),textvariable=self.val_contact).place(x=140,y=200,width=160,height=27)

        lbl_question=Label(frame1,text="Question",font=("",12,"bold"),bg="light green").place(x=20,y=270)
       
        self.txt_question=ttk.Combobox(frame1,font=("",12,"bold"),state='readonly',justify=CENTER,textvariable=self.val_question)
        self.txt_question.place(x=150, y=270,width=360,height=30)
        self.txt_question['values']=("Your first pet name","Your favouriate place","Your favouriate number")
        self.txt_question.set("Select secret question")

        lbl_answer=Label(frame1,text="Answer",font=("",12,"bold"),bg="light green").place(x=20,y=330)
        txt_answer=Entry(frame1,width=30,font=("",12,"bold"),textvariable=self.val_answer).place(x=150,y=330,width=360,height=27)

        lbl_password=Label(frame1,text="Password",font=("",12,"bold"),bg="light green").place(x=20,y=400)
        txt_password=Entry(frame1,width=30,font=("",12,"bold"),textvariable=self.val_pass).place(x=140,y=400,width=160,height=27)
        
        lbl_confirm_password=Label(frame1,text="Confirm Password",font=("",12,"bold"),bg="light green").place(x=370,y=400)
        txt_confirm_password=Entry(frame1,width=30,font=("",12,"bold"),textvariable=self.val_confirmPass).place(x=530,y=400,width=160,height=27)

        
        lbl_admin_code=Label(frame1,text="Admin Code",font=("",12,"bold"),bg="light green").place(x=20,y=460)
        txt_admin_code=Entry(frame1,width=30,font=("",12,"bold"),textvariable=self.val_adminCode).place(x=140,y=460,width=160,height=27)


        register_btn=Button(frame1,text="REGISTER",bg="grey",font=("",12,"bold"),command=self.register_data).place(x=290,y=510)




    def register_data(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:

            if (self.val_fname.get()=="") or (self.val_email.get()=="") or (self.val_contact.get()=="") or (self.val_answer.get()=="") or (self.val_pass.get()=="") or (self.val_confirmPass.get()=="") or (self.val_adminCode.get()=="") :
                messagebox.showerror("Error","Please enter all give fields",parent=self.root)
            elif  self.val_question.get()=="Select secret question":
                messagebox.showerror("Error","Please choose one secret question",parent=self.root)
            elif  self.val_pass.get()!=self.val_confirmPass.get():
                messagebox.showerror("Error","Passwords do not match",parent=self.root)
            elif  self.val_adminCode.get()!="101":
                messagebox.showerror("Error","Admin code is incorrect",parent=self.root)
            else:
                curs.execute("select * from employee where email=?",(self.val_email.get(),))
                row=curs.fetchone()

                if row != None:
                    messagebox.showerror("Error","Admin with this email id is already present",parent=self.root)      
                else:
                    curs.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",(
                            self.val_fname.get(),
                            self.val_lname.get(),
                            self.val_contact.get(),
                            self.val_email.get(),
                            self.val_question.get(),
                            self.val_answer.get(),
                            self.val_pass.get()
                            ) )

                    con.commit()
                    messagebox.showinfo("Success","Amin registered succesfully",parent=self.root)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    
        

           



        


        






if __name__=="__main__":
    root= Tk()
 
    obj= RegisterClass(root)
    root.mainloop()   