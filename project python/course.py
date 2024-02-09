from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3


class CourseClass:
    def __init__(self, root ):
        self.root= root
        self.root.title("STUDENT  RESULT  MANAGMENT  SYSTEM")
        self.root.geometry("1200x480+80+170")       
        self.root.config(bg="white")     
        self.root.focus_force()

        # title 
        title= Label(self.root, text="MANAGE COURSE DETAILS",compound=LEFT,font=("Aerial Black",20,"bold"),bg="light green").place(x=0,y=0,relwidth=1,height=50)

        # variables
        self.val_course=StringVar()
        self.val_duration=StringVar()
        self.val_charges=StringVar()

        # widgets  and entry fields
        lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold")).place(x=10, y=70)
        self.txt_courseName=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_course)
        self.txt_courseName.place(x=180, y=70)

        lbl_courseDuration=Label(self.root,text="Course Duration",font=("goudy old style",15,"bold")).place(x=10, y=130)
        txt_courseDuration=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_duration).place(x=180, y=130)
        
        lbl_courseCharges=Label(self.root,text="Course Charges",font=("goudy old style",15,"bold")).place(x=10, y=190)
        txt_courseCharges=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_charges).place(x=180, y=190)

        lbl_courseDescription=Label(self.root,text="Description",font=("goudy old style",15,"bold")).place(x=10, y=250)
        self.txt_Discription=Text(self.root,font=("goudy old style",15,"bold"),bg="light yellow")
        self.txt_Discription.place(x=180,y=250,width=400,height=100)


        # buttons
        self.btn_add=Button(self.root,text="SAVE",font=("",13,"bold"),bg="light green",cursor="hand2",command=self.add).place(x=100,y=400,width=90)
        self.btn_update=Button(self.root,text="UPDATE",font=("",13,"bold"),bg="light blue",cursor="hand2",command=self.update).place(x=230,y=400,width=90)
        self.btn_delete=Button(self.root,text="DELETE",font=("",13,"bold"),bg="red",cursor="hand2",command=self.delete).place(x=350,y=400,width=90)
        self.btn_clear=Button(self.root,text="CLEAR",font=("",13,"bold"),bg="yellow",cursor="hand2",command=self.clear).place(x=470,y=400,width=90)

        # search pannel
        self.var_search=StringVar()

        lbl_search_courseName= Label(self.root,text="Search Course",font=("",15)).place(x=700,y=70)
        txt_searchCourse=Entry(self.root,textvariable=self.var_search,font=("",15),bg="#FFFF9A").place(x=850,y=70)
        self.searc_btn=Button(self.root,text="SEARCH",font=("",10),bg="#7FFFD4",command=self.search).place(x=1090,y=70)

        # search list 

        self.C_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_frame.place(x=700,y=130,width=470,height=300)



        # course table

        scrollY=Scrollbar(self.C_frame,orient=VERTICAL)
        scrollX=Scrollbar(self.C_frame,orient=HORIZONTAL)

        self.CourseTable= ttk.Treeview(self.C_frame, columns=("cid","name","duration","charges","description"),xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)

        scrollX.config(command= self.CourseTable.xview)
        scrollY.config(command= self.CourseTable.yview) 


        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Course Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]='headings'

        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=150)

        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


    # ===================================================================================

    # fetch data from list and show it in text areas
    def get_data(self,ev):          
        
        self.txt_courseName.config(state="readonly")
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.val_course.set(row[1])
        self.val_duration.set(row[2])
        self.val_charges.set(row[3])
        self.txt_Discription.delete("1.9",END)
        self.txt_Discription.insert(END,row[4])
        

    # add new course on the database
    def add(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            if self.val_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root) 
            else:
                curs.execute("select * from course where name=?",(self.val_course.get(),))
                row=curs.fetchone()   
                if row !=None:
                    messagebox.showerror("Eror","course name already present",parent=self.root) 
                else:
                    curs.execute("insert into course (name,duration,charges,description) values(?,?,?,?)",(
                                self.val_course.get(), 
                                self.val_duration.get(), 
                                self.val_charges.get(), 
                                self.txt_Discription.get("1.0",END) 
                                ) )
                    con.commit()
                    messagebox.showinfo("Success","Course added succesfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    


    # display courses on the table 
    def show(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            curs.execute("select * from course")
            rows=curs.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for ind in rows:
                self.CourseTable.insert('',END,values=ind)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")     


    # update the course details in the database 
    def update(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            if self.val_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root) 
            else:
                curs.execute("select * from course where name=?",(self.val_course.get(),))
                row=curs.fetchone()   
                if row ==None:
                    messagebox.showerror("Eror","Select course from list",parent=self.root) 
                else:
                    curs.execute("update course set duration=?,charges=?,description=? where name=?",(
                                self.val_duration.get(), 
                                self.val_charges.get(), 
                                self.txt_Discription.get("1.0",END),
                                self.val_course.get() 
                                ) )
                    con.commit()
                    messagebox.showinfo("Success","Course update succesfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 

    def clear(self):
        self.show()
        self.val_course.set("")
        self.val_duration.set("")
        self.val_charges.set("")
        self.txt_Discription.delete("1.0",END)
        self.var_search.set("")
        self.txt_courseName.config(state="normal")
                                 

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            if self.val_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root) 
            else:
                curs.execute("select * from course where name=?",(self.val_course.get(),))
                row=curs.fetchone()   
                if row ==None:
                    messagebox.showerror("Eror","please select course from the list",parent=self.root) 
                else:
                    op=messagebox.askyesno("Confirm","Do tou really want to delete",parent=self.root)
                    if op==True:
                        
                        curs.execute("delete from course where name=?",(self.val_course.get(),))
                      
                        con.commit()
                        messagebox.showinfo("Delete","Deleted succesfully",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    



    def search(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            curs.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=curs.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for ind in rows:
                self.CourseTable.insert('',END,values=ind)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")     
         




if __name__=="__main__":
    root= Tk()
 
    obj= CourseClass(root)
    root.mainloop()   