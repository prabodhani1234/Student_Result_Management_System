from tkinter import *

addsubject_window = Tk()
addsubject_window.title("Exam Result Management System")
addsubject_window.configure(bg='#DFD6D6')
addsubject_window.geometry("700x500") # window size
addsubject_window.maxsize(width=700, height=500)  # window maximize


# main text
text1 = Label(addsubject_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 22, "bold"),
              fg="white", bg="#285C9F", width=700, height=3)
text1.pack()

text2=Label(addsubject_window,text="ADD NEW SUBJECT...",font=("Times New Roman", 17),
            fg="#E33737", bg="#DFD6D6")
text2.place(y=110,x=20)

label1=Label(addsubject_window,text="Subject Code\t   :",font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=10,pady=4)
label1.place(x=115,y=242)

entry1=Entry(addsubject_window,font=16)
entry1.place(x=280,y=242,width=280, height=30)


label2= Label(addsubject_window,text="Subject Name \t   :",font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=10,pady=4)
label2.place(x=115,y=274)

entry2=Entry(addsubject_window,font=11)
entry2.place(x=280,y=274,width=280, height=30)

button1 = Button(addsubject_window, text="BACK", font=("arial", 11),bg="#5E96D2",padx=18,pady=1)
button1.place(x=370, y=330)

button2 = Button(addsubject_window, text="SUBMIT", font=("arial", 11),bg="#5E96D2",padx=14,pady=1)
button2.place(x=467, y=330)

addsubject_window.mainloop()