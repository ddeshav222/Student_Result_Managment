from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3


class StudentClass:
    def __init__(self, root ):
        self.root= root
        self.root.title("STUDENT  RESULT  MANAGMENT  SYSTEM")
        self.root.geometry("1200x550+80+130")       
        self.root.config(bg="white")     
        self.root.focus_force()

        # title 
        title= Label(self.root, text="MANAGE STUDENT DETAILS",compound=LEFT,font=("Aerial Black",20,"bold"),bg="light green").place(x=0,y=0,relwidth=1,height=50)

        # variables
        self.val_rollno=StringVar()
        self.val_studentName=StringVar()
        self.val_email=StringVar()
        self.val_gender=StringVar()
        self.val_dob=StringVar()
        self.val_courseName=StringVar()
        self.val_contact=StringVar()
        self.val_state=StringVar()
        self.val_city=StringVar()
        self.val_pin=StringVar()
        self.val_admDate=StringVar()


        # update course list
        self.course_list=[]
        self.fetch_Courses()    


        # widgets  and entry fields
        lbl_rollNo=Label(self.root,text="Roll No",font=("goudy old style",15,"bold")).place(x=10, y=70)
        self.txt_rollno=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_rollno)
        self.txt_rollno.place(x=120, y=70)

        lbl_studentName=Label(self.root,text="Name",font=("goudy old style",15,"bold")).place(x=10, y=130)
        txt_studentName=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_studentName).place(x=120, y=130)
        
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15,"bold")).place(x=10, y=190)
        txt_email=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_email).place(x=120, y=190)

        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold")).place(x=10, y=250)
        self.txt_gender=ttk.Combobox(self.root,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER,textvariable=self.val_gender,values=("Male","Female","Others"))
        self.txt_gender.place(x=120, y=250,width=200)
        self.txt_gender.set("Select")







        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15,"bold")).place(x=360, y=70)
        self.txt_dob=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_dob)
        self.txt_dob.place(x=470, y=70)

        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold")).place(x=360, y=130)
        txt_contact=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_contact).place(x=470, y=130)
        
        lbl_admission=Label(self.root,text="Admission",font=("goudy old style",15,"bold")).place(x=360, y=190)
        txt_admission=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_admDate).place(x=470, y=190)

        lbl_courseName=Label(self.root,text="Course",font=("goudy old style",15,"bold")).place(x=360, y=250)
        self.txt_courseName=ttk.Combobox(self.root,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER,textvariable=self.val_courseName,values=self.course_list)
        self.txt_courseName.place(x=470, y=250,width=200)
        self.txt_courseName.set("Select")

        
        
        lbl_state=Label(self.root,text="State",font=("goudy old style",15,"bold")).place(x=10, y=300)
        txt_state=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_state).place(x=70, y=300,width=130)

        lbl_city=Label(self.root,text="City",font=("goudy old style",15,"bold")).place(x=220, y=300)
        txt_city=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_city).place(x=280, y=300,width=130)

        lbl_pin=Label(self.root,text="Pin",font=("goudy old style",15,"bold")).place(x=440, y=300)
        txt_pin=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_pin).place(x=490, y=300,width=130)



        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold")).place(x=10, y=350)
        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="light yellow")
        self.txt_address.place(x=120,y=350,width=400,height=80)


        # buttons
        self.btn_add=Button(self.root,text="SAVE",font=("",13,"bold"),bg="light green",cursor="hand2",command=self.add).place(x=100,y=460,width=90)
        self.btn_update=Button(self.root,text="UPDATE",font=("",13,"bold"),bg="light blue",cursor="hand2",command=self.update).place(x=230,y=460,width=90)
        self.btn_delete=Button(self.root,text="DELETE",font=("",13,"bold"),bg="red",cursor="hand2",command=self.delete).place(x=350,y=460,width=90)
        self.btn_clear=Button(self.root,text="CLEAR",font=("",13,"bold"),bg="yellow",cursor="hand2",command=self.clear).place(x=470,y=460,width=90)

        # search pannel
        self.var_searchRollno=StringVar()

        lbl_search_RollNo= Label(self.root,text="Search Roll No",font=("",15)).place(x=700,y=70)
        txt_searchRollNo=Entry(self.root,textvariable=self.var_searchRollno,font=("",15),bg="#FFFF9A").place(x=850,y=70)
        self.searc_btn=Button(self.root,text="SEARCH",font=("",10),bg="#7FFFD4",command=self.search).place(x=1090,y=70)

        # search list 

        self.C_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_frame.place(x=700,y=130,width=470,height=300)



        # course table

        scrollY=Scrollbar(self.C_frame,orient=VERTICAL)
        scrollX=Scrollbar(self.C_frame,orient=HORIZONTAL)

        self.StudentTable= ttk.Treeview(self.C_frame, columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)

        scrollX.config(command= self.StudentTable.xview)
        scrollY.config(command= self.StudentTable.yview) 


        self.StudentTable.heading("roll",text="Roll no")
        self.StudentTable.heading("name",text="Student Name")
        self.StudentTable.heading("email",text="Email")
        self.StudentTable.heading("gender",text="Gender")
        self.StudentTable.heading("dob",text="D.O.B")
        self.StudentTable.heading("contact",text="Contact")
        self.StudentTable.heading("admission",text="Admission")
        self.StudentTable.heading("course",text="Course")
        self.StudentTable.heading("state",text="State")
        self.StudentTable.heading("city",text="City")
        self.StudentTable.heading("pin",text="Pin")
        self.StudentTable.heading("address",text="Address")

        
        self.StudentTable["show"]='headings'

        self.StudentTable.column("roll",width=100)
        self.StudentTable.column("name",width=100)
        self.StudentTable.column("email",width=130)
        self.StudentTable.column("gender",width=100)
        self.StudentTable.column("dob",width=100)
        self.StudentTable.column("contact",width=100)
        self.StudentTable.column("admission",width=100)
        self.StudentTable.column("course",width=100)
        self.StudentTable.column("state",width=100)
        self.StudentTable.column("city",width=100)
        self.StudentTable.column("pin",width=100)
        self.StudentTable.column("address",width=150)

        self.StudentTable.pack(fill=BOTH,expand=1)
        self.StudentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        self.fetch_Courses()


    # ===================================================================================

    # fetch data from list and show it in text areas
    def get_data(self,ev):          
        
        self.txt_rollno.config(state="readonly")
        r=self.StudentTable.focus()
        content=self.StudentTable.item(r)
        row=content["values"]
        self.val_rollno.set(row[0])
        self.val_studentName.set(row[1])
        self.val_email.set(row[2])
        self.val_gender.set(row[3]),
        self.val_dob.set(row[4]),
        self.val_contact.set(row[5]),
        self.val_admDate.set(row[6]),
        self.val_courseName.set(row[7]),
        self.val_state.set(row[8]),
        self.val_city.set(row[9]),
        self.val_pin.set(row[10]),

        self.txt_address.delete("1.9",END)
        self.txt_address.insert(END,row[11])
        

    # add new course on the database
    def add(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            if self.val_rollno.get()=="":
                messagebox.showerror("Error","Roll No name should be required",parent=self.root) 
            else:
                curs.execute("select * from student where roll=?",(self.val_rollno.get(),))
                row=curs.fetchone()   
                if row !=None:
                    messagebox.showerror("Eror","Roll No already present",parent=self.root) 
                else:
                    curs.execute("insert into student (roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                                self.val_rollno.get(), 
                                self.val_studentName.get(), 
                                self.val_email.get(), 
                                self.val_gender.get(),
                                self.val_dob.get(),
                                self.val_contact.get(),
                                self.val_admDate.get(),
                                self.val_courseName.get(),
                                self.val_state.get(),
                                self.val_city.get(),
                                self.val_pin.get(),
                                self.txt_address.get("1.0",END) 
                                ) )
                    con.commit()
                    messagebox.showinfo("Success","Student added succesfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    


    # display courses on the table 
    def show(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            curs.execute("select * from student")
            rows=curs.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for ind in rows:
                self.StudentTable.insert('',END,values=ind)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")     


    # update the course details in the database 
    def update(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            if self.val_rollno.get()=="":
                messagebox.showerror("Error","Roll No should be required",parent=self.root) 
            else:
                curs.execute("select * from student where roll=?",(self.val_rollno.get(),))
                row=curs.fetchone()   
                if row ==None:
                    messagebox.showerror("Eror","Select Student from list",parent=self.root) 
                else:
                    curs.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(
                                self.val_studentName.get(), 
                                self.val_email.get(), 
                                self.val_gender.get(),
                                self.val_dob.get(),
                                self.val_contact.get(),
                                self.val_admDate.get(),
                                self.val_courseName.get(),
                                self.val_state.get(),
                                self.val_city.get(),
                                self.val_pin.get(),
                                self.txt_address.get("1.0",END), 
                                self.val_rollno.get()
                                
                                ) )
                    con.commit()
                    messagebox.showinfo("Success","Student detail updated succesfully",parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 

    def clear(self):
        self.show()
        self.val_rollno.set("")
        self.val_studentName.set("")
        self.val_email.set("")
        self.val_gender.set("Select")
        self.val_dob.set(""),
        self.val_contact.set(""),
        self.val_admDate.set(""),
        self.val_courseName.set("Select"),
        self.val_state.set(""),
        self.val_city.set(""),
        self.val_pin.set(""),
        self.txt_address.delete("1.0",END)
        self.var_searchRollno.set("")
        self.txt_rollno.config(state="normal")
                                 

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            if self.val_rollno.get()=="":
                messagebox.showerror("Error","Roll No should be required",parent=self.root) 
            else:
                curs.execute("select * from student where roll=?",(self.val_rollno.get(),))
                row=curs.fetchone()   
                if row ==None:
                    messagebox.showerror("Eror","please select Student from the list",parent=self.root) 
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        
                        curs.execute("delete from student where roll=?",(self.val_rollno.get(),))
                      
                        con.commit()
                        messagebox.showinfo("Delete","Deleted succesfully",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    



    def search(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            curs.execute(f"select * from student where roll=?",(self.var_searchRollno.get(),))
            rows=curs.fetchone()

            if rows!=None:
                self.StudentTable.delete(*self.StudentTable.get_children())
                self.StudentTable.insert('',END,values=rows)

            else:
                messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")     
         


    def fetch_Courses(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            curs.execute("select name from course")
            rows=curs.fetchall()
          
            if len(rows)>0:
                for i in rows:
                    self.course_list.append(i[0]) 

            # self.StudentTable.delete(*self.StudentTable.get_children())
            # for ind in rows:
            #     self.StudentTable.insert('',END,values=ind)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")     

if __name__=="__main__":
    root= Tk()
 
    obj= StudentClass(root)
    root.mainloop()   