from tkinter import*
from PIL import Image,ImageTk
from course import CourseClass 
from student import StudentClass
from result import ResultClass
from report import ReportClass
from loginPage import LoginClass
from student_result_view import StudentResultClass
import os

class Start:
    def __init__(self, root ):
        self.root= root
        self.root.title("STUDENT  RESULT  MANAGMENT  SYSTEM")
        self.root.geometry("700x550+300+100")       
        self.root.config(bg="white")     
        self.root.resizable(False,False)
        
        student_btn=Button(self.root,text="STUDENT",bg="light blue",font=("",12,"bold"),command=self.student).place(x=0,y=0,width=350,height=550)
        admin_btn=Button(self.root,text="TEACHER",bg="grey",font=("",12,"bold"),command=self.teacher).place(x=350,y=0,width=350,height=550)


    def student(self):
        self.new_win= Toplevel(self.root)
        self.new_obj=StudentResultClass(self.new_win) 
        # self.root.destroy()

    def teacher(self): 
        self.root.destroy()
        os.system("Python loginPage.py")




if __name__=="__main__":
    root= Tk()
 
    obj= Start(root)
    root.mainloop()    
        