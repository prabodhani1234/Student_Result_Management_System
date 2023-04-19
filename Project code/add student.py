from tkinter import *

addstudent_window = Tk()
addstudent_window.title("Exam Result Management System")
addstudent_window.configure(bg='#DFD6D6')
addstudent_window.geometry("700x500") # window size
addstudent_window.maxsize(width=700, height=500)  # window maximize


# main text
text1 = Label(addstudent_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 22, "bold"),
              fg="white", bg="#285C9F", width=700, height=3)
text1.pack()

text2=Label(addstudent_window,text="ADD NEW STUDENT...",font=("Times New Roman", 17),
            fg="#E33737", bg="#DFD6D6")
text2.place(y=110,x=20)

label1 =Label(addstudent_window,text="Registration Form", width=20,font=("bold",15),bg="#DFD6D6")
label1.place(x=240,y=150)

label2= Label(addstudent_window,text="Registration Number  :",font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=10,pady=4)
label2.place(x=115,y=210)

entry1=Entry(addstudent_window,font=11)
entry1.place(x=280,y=210,width=280, height=30)

label3=Label(addstudent_window,text="Index Number\t   :",font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=10,pady=4)
label3.place(x=115,y=242)

entry2=Entry(addstudent_window,font=16)
entry2.place(x=280,y=242,width=280, height=30)


label4= Label(addstudent_window,text="Full Name \t   :",font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=10,pady=4)
label4.place(x=115,y=274)

entry3=Entry(addstudent_window,font=11)
entry3.place(x=280,y=274,width=280, height=30)

label5=Label(addstudent_window,text="Address\t\t   :",font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=10,pady=4)
label5.place(x=115,y=306)

entry4=Entry(addstudent_window,font=16)
entry4.place(x=280,y=306,width=280, height=30)

label5=Label(addstudent_window,text="Gender\t\t   :",font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=10,pady=4)
label5.place(x=114,y=338)

var=IntVar()
Radiobutton(addstudent_window,text="Male",padx= 5,variable= var,value=1,bg="#DFD6D6").place(x=290,y=340)
Radiobutton(addstudent_window,text="Female",padx= 20,variable= var, value=2,bg="#DFD6D6").place(x=370,y=340)


label6= Label(addstudent_window,text="Email Address\t   :",font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=10,pady=4)
label6.place(x=115,y=370)

entry5=Entry(addstudent_window,font=11)
entry5.place(x=280,y=370,width=280, height=30)

label7=Label(addstudent_window,text="Phone Number\t   :",font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=10,pady=4)
label7.place(x=115,y=402)

entry6=Entry(addstudent_window,font=16)
entry6.place(x=280,y=402,width=280, height=30)

button1 = Button(addstudent_window, text="BACK", font=("arial", 11),bg="#5E96D2",padx=18,pady=1)
button1.place(x=370, y=450)

button2 = Button(addstudent_window, text="SUBMIT", font=("arial", 11),bg="#5E96D2",padx=14,pady=1)
button2.place(x=467, y=450)


addstudent_window.mainloop()