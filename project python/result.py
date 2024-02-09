from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3


class ResultClass:
    def __init__(self, root ):
        self.root= root
        self.root.title("STUDENT  RESULT  MANAGMENT  SYSTEM")
        self.root.geometry("1200x480+80+170")       
        self.root.config(bg="white")     
        self.root.focus_force()

        # title 
        title= Label(self.root, text="ADD STUDENTS RESULT",compound=LEFT,font=("Aerial Black",20,"bold"),bg="orange").place(x=0,y=0,relwidth=1,height=50)


# ============== widgets ==============

    # ========== variables================
        self.val_name=StringVar()
        self.val_rollno=StringVar()
        self.val_course=StringVar()
        self.val_marksObtained=StringVar()
        self.val_totalMarks=StringVar()
        self.roll_list=[]
        self.fetch_RollNo()

        lbl_select=Label(self.root,text="Select  Roll No",font=("goudy old style",17,"bold"),bg="white").place(x=50,y=100)
        self.txt_student_roll=ttk.Combobox(self.root,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER,textvariable=self.val_rollno,values=self.roll_list)
        self.txt_student_roll.place(x=220, y=100,width=200)
        self.txt_student_roll.set("Select")  

        self.btn_search=Button(self.root,text="Search",font=("",13,"bold"),bg="light blue",cursor="hand2",command=self.search).place(x=440,y=100,width=90,height=30)



        lbl_name=Label(self.root,text="Name",font=("goudy old style",17,"bold"),bg="white").place(x=50,y=160)
        txt_student_name=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_name,state='readonly').place(x=220, y=160)

        lbl_course=Label(self.root,text="Course",font=("goudy old style",17,"bold"),bg="white").place(x=50,y=220)
        txt_course=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_course,state='readonly').place(x=220, y=220)

        lbl_marks_obtained=Label(self.root,text="Marks Obtained",font=("goudy old style",17,"bold"),bg="white").place(x=50,y=280)
        txt_marks_obtained=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_marksObtained).place(x=220, y=280)

        lbl_total_marks=Label(self.root,text="Toatal Marks",font=("goudy old style",17,"bold"),bg="white").place(x=50,y=340)
        txt_total_marks=Entry(self.root,font=("goudy old style",15,"bold"),bg="light yellow",textvariable=self.val_totalMarks).place(x=220, y=340)


    # ============= buttons =============
        self.btn_add=Button(self.root,text="SUBMIT",font=("",13,"bold"),bg="light green",cursor="hand2",command=self.submit).place(x=200,y=400,width=90)
        self.btn_clear=Button(self.root,text="CLEAR",font=("",13,"bold"),bg="yellow",cursor="hand2",command=self.clear).place(x=350,y=400,width=90)



# ========================= functions ================================


    def fetch_RollNo(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            curs.execute("select roll from student")
            rows=curs.fetchall()
          
            if len(rows)>0:
                for i in rows:
                    self.roll_list.append(i[0]) 

            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")   


    def search(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            curs.execute(f"select name,course from student where roll=?",(self.val_rollno.get(),))
            rows=curs.fetchone()

            if rows!=None:
                self.val_name.set(rows[0])
                self.val_course.set(rows[1])

            else:
                messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  

    def submit(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            if self.val_name.get()=="":
                messagebox.showerror("Error","Please search student first",parent=self.root)
            else:
                curs.execute("Select * from result where roll=? and course=?",(self.val_rollno.get(),self.val_course.get()))    
                row=curs.fetchone()

                if row!=None:
                    messagebox.showerror("Error","Result already present",parent=self.root)
                    self.clear()
                else:
                    per=(int(self.val_marksObtained.get())*100)/(int(self.val_totalMarks.get()))

                    curs.execute("insert into result (roll,name,course,marks_ob,marks_tot,per) values(?,?,?,?,?,?)",(
                            self.val_rollno.get(),
                            self.val_name.get(),
                            self.val_course.get(),
                            self.val_marksObtained.get(),
                            self.val_totalMarks.get(),
                            str(per)

                    ) )    
                    con.commit()
                    self.clear()
                    messagebox.showinfo("Success","Result added succesfully",parent=self.root)
                    

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 
                 
    def clear(self):
        self.val_rollno.set("Select")
        self.val_name.set(""),
        self.val_course.set(""),
        self.val_marksObtained.set(""),
        self.val_totalMarks.set(""),

if __name__=="__main__":
    root= Tk()
 
    obj= ResultClass(root)
    root.mainloop()   