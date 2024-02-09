from tkinter import*
from PIL import Image,ImageTk
from course import CourseClass 
from student import StudentClass
from result import ResultClass
from report import ReportClass
from tkinter import ttk,messagebox
# from start import Start
import os
import sqlite3


class RMS:
    def __init__(self, root ):
        self.root= root
        self.root.title("STUDENT  RESULT  MANAGMENT  SYSTEM")
        self.root.geometry("1350x700+0+0")       
        self.root.config(bg="purple")    
        self.root.resizable(False,False) 

        # icons
        # self.logo_dash=Image.open("images/logo.png")
        # self.logo_dash=self.logo_dash.resize((40,50),Image.ANTIALIAS)
        # self.logo_dash=ImageTk.PhotoImage(self.logo_dash)
        

        


        # title
        title= Label(self.root, text="STUDENT RESULT MANAGMENT SYSTEM",compound=LEFT,font=("Aerial Black",20,"bold"),bg="red").place(x=0,y=0,relwidth=1,height=50)

        # menu
        M_frame= LabelFrame(self.root,text="Menus",font=("",15),bg="white")
        M_frame.place(x=10,y=70,width=1340,height=80)
        
        btn_course= Button(M_frame,text="COURSE",font=("goudy old style",15,"bold"),bg="light blue",cursor="hand2",command=self.add_course)
        btn_course.place(x=20,y=5,width=200,height=40)

        btn_student= Button(M_frame,text="STUDENTS",font=("goudy old style",15,"bold"),bg="light blue",cursor="hand2",command=self.add_student)
        btn_student.place(x=240,y=5,width=200,height=40)
        
        btn_result= Button(M_frame,text="RESULT",font=("goudy old style",15,"bold"),bg="light blue",cursor="hand2",command=self.add_result)
        btn_result.place(x=460,y=5,width=200,height=40)
        
        btn_view= Button(M_frame,text="VIEW RESULT",font=("goudy old style",15,"bold"),bg="light blue",cursor="hand2",command=self.view_report)
        btn_view.place(x=680,y=5,width=200,height=40)

        btn_logout= Button(M_frame,text="LOGOUT",font=("goudy old style",15,"bold"),bg="light blue",cursor="hand2",command=self.log_out)
        btn_logout.place(x=900,y=5,width=200,height=40)

        btn_exit= Button(M_frame,text="EXIT",font=("goudy old style",15,"bold"),bg="light blue",cursor="hand2",command=self.exit_screen)
        btn_exit.place(x=1120,y=5,width=200,height=40)


        # footer
        footer= Label(self.root,text="Student Result Managment\nContact Us for any Technical Issue: 901xxxxx90",font=("",12),bg="grey")
        footer.pack(side=BOTTOM,fill=X)
        


        # uodate details 
        self.course_cnt= Label(self.root,text="TOTAL COURSE\n[ 0 ]",font=("",20,"bold"),bd=10,relief=RIDGE)
        self.course_cnt.place(x=400,y=530,width=300,height=100)

        self.student_cnt= Label(self.root,text="TOTAL STUDENTS\n[ 0 ]",font=("",20,"bold"),bd=10,relief=RIDGE)
        self.student_cnt.place(x=710,y=530,width=300,height=100) 

        self.results_cnt= Label(self.root,text="TOTAL RESULTS\n[ 0 ]",font=("",20,"bold"),bd=10,relief=RIDGE)
        self.results_cnt.place(x=1020,y=530,width=300,height=100) 

        self.update_details()


    def add_course(self):
        self.new_win= Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win) 

    def add_student(self):
        self.new_win= Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)       

    def add_result(self):
        self.new_win= Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win) 


    def view_report(self):
        self.new_win= Toplevel(self.root)
        self.new_obj=ReportClass(self.new_win) 

    def log_out(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout",parent=self.root)
        if op==True:
            self.root.destroy()
            # self.new_win= Toplevel(self.root)
            # self.new_obj=Start(self.new_win) 
            os.system("python loginPage.py")


    def exit_screen(self):
        op=messagebox.askyesno("Confirm","Do you really want to exit",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python start.py")


    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        curs=con.cursor()
        try:
            curs.execute("select * from course")
            row=curs.fetchall()
            # print(len(row))
            self.course_cnt.config(text=f"TOTAL COURSE\n[ {str(len(row))} ]")

            curs.execute("select * from student")
            row=curs.fetchall()
            self.student_cnt.config(text=f"TOTAL STUDENTS\n[ {str(len(row))} ]")

            curs.execute("select * from result")
            row=curs.fetchall()
            self.results_cnt.config(text=f"TOTAL RESULT\n[ {str(len(row))} ]")

            self.course_cnt.after(200,self.update_details)



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")       
            
                





if __name__=="__main__":
    root= Tk()
 
    obj= RMS(root)
    root.mainloop()    
        