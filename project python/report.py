from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3


class ReportClass:
    def __init__(self, root ):
        self.root= root
        self.root.title("STUDENT  RESULT  MANAGMENT  SYSTEM")
        self.root.geometry("1200x480+80+170")       
        self.root.config(bg="white")     
        self.root.focus_force()
        self.root.resizable(False,False)

        # title 
        title= Label(self.root, text="VIEW STUDENT RESULT",compound=LEFT,font=("Aerial Black",20,"bold"),bg="orange").place(x=0,y=0,relwidth=1,height=50)

        # ===========variables=======
        self.val_searchRoll= StringVar()    


        lbl_search_rollNo=Label(self.root,text="Search by Roll no",font=("goudy old style",17,"bold"),bg="white").place(x=250,y=100)
        txt_search_Rollno=Entry(self.root,textvariable=self.val_searchRoll,font=("goudy old style",17,"bold"),bg="light yellow").place(x=450,y=100)

        self.btn_search=Button(self.root,text="Search",font=("",13,"bold"),bg="light blue",cursor="hand2",command=self.search).place(x=710,y=100,width=90,height=30)
        self.btn_clear=Button(self.root,text="Clear",font=("",13,"bold"),bg="light green",cursor="hand2",command=self.clear).place(x=840,y=100,width=90,height=30)


        lbl_rollNo=Label(self.root,text="Roll no",font=("goudy old style",17,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=200,width=150)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",17,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=200,width=150)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",17,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=200,width=150)
        lbl_marks_obt=Label(self.root,text="Marks Obtained",font=("goudy old style",17,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=200,width=190)
        lbl_marks_tot=Label(self.root,text="Total Marks",font=("goudy old style",17,"bold"),bg="white",bd=2,relief=GROOVE).place(x=790,y=200,width=150)
        lbl_percent=Label(self.root,text="Percentage",font=("goudy old style",17,"bold"),bg="white",bd=2,relief=GROOVE).place(x=940,y=200,width=150)
        
        self.rollNo_val=Label(self.root,text="",font=("goudy old style",17,"bold"),bg="white",bd=2,relief=GROOVE)
        self.rollNo_val.place(x=150,y=233,width=150,height=50)
        self.name_val=Label(self.root,text="",font=("goudy old style",17,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name_val.place(x=300,y=233,width=150,height=50)
        self.course_val=Label(self.root,text="",font=("goudy old style",17,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course_val.place(x=450,y=233,width=150,height=50)
        self.marks_obt_val=Label(self.root,text="",font=("goudy old style",17,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marks_obt_val.place(x=600,y=233,width=190,height=50)
        self.marks_tot_val=Label(self.root,text="",font=("goudy old style",17,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marks_tot_val.place(x=790,y=233,width=150,height=50)
        self.percent_val=Label(self.root,text="",font=("goudy old style",17,"bold"),bg="white",bd=2,relief=GROOVE)
        self.percent_val.place(x=940,y=233,width=150,height=50)
        
        self.btn_delete=Button(self.root,text="Delete",font=("",13,"bold"),bg="red",cursor="hand2",command=self.delete).place(x=500,y=350,width=90,height=30)


    # =============== function ===================

    def search(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            
            if self.val_searchRoll.get()=="":
                messagebox.showerror("Error","Please Enter Student Roll No",parent=self.root)

            else:
                
                curs.execute(f"select * from result where roll=?",(self.val_searchRoll.get(),))
                rows=curs.fetchone()

                if rows!=None:
                    self.rollNo_val.config(text=rows[1])
                    self.name_val.config(text=rows[2])
                    self.course_val.config(text=rows[3])
                    self.marks_obt_val.config(text=rows[4])
                    self.marks_tot_val.config(text=rows[5])
                    per=float(rows[6])
                    per=round(per,3)
                    num=str(per)
                    self.percent_val.config(text=num)


                else:
                    messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  

    def clear(self):
        
            self.val_searchRoll.set("")
            self.rollNo_val.config(text="")
            self.name_val.config(text="")
            self.course_val.config(text="")
            self.marks_obt_val.config(text="")
            self.marks_tot_val.config(text="")
            self.percent_val.config(text="")
        

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            if self.rollNo_val.cget("text")=="":
                messagebox.showerror("Error","Enter roll No and view report first",parent=self.root) 
            else:
                curs.execute("select * from result where roll=?",(self.rollNo_val.cget("text"),))
                row=curs.fetchone()   
                if row ==None:
                    messagebox.showerror("Eror","No record found",parent=self.root) 
                else:
                    op=messagebox.askyesno("Confirm","Do tou really want to delete",parent=self.root)
                    if op==True:
                        
                        curs.execute("delete from result where roll=?",(self.rollNo_val.cget("text"),))
                      
                        con.commit()
                        messagebox.showinfo("Delete","Deleted succesfully",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    

    


if __name__=="__main__":
    root= Tk()
 
    obj= ReportClass(root)
    root.mainloop()   