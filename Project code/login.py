from tkinter import*

login_window = Tk()
login_window.title("Exam Result Management System")
login_window.configure(bg='#DFD6D6')
login_window.geometry("700x470")  # window size
login_window.maxsize(width=700, height=470)  # window maximize


# main text
text1 = Label(login_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 22, "bold"),
            fg="white", bg="#285C9F", width=700, height=3)
text1.pack()

text2=Label(login_window,text="WELCOME...",font=("Times New Roman", 18),
            fg="#E33737", bg="#DFD6D6")
text2.place(y=110,x=20)

image1 = PhotoImage(file="C:/Users/user/Desktop/EXAM RESULT SYSTEM/IMAGES/login.png")
label1 = Label(login_window, image=image1)
label1.pack(padx=0,pady=38)

label2=Label(login_window,text= "LOGIN",font=("arial",16),bg='#DFD6D6')
label2.place(x=317,y=220)

username_label= Label(login_window,text="User Name\t:",font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=20,pady=8)
username_label.place(x=180,y=260)

entry_1=Entry(login_window,font=11)
entry_1.place(x=350,y=260,width=200, height=37)

password_label=Label(login_window,text="Password\t:",font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=20,pady=8)
password_label.place(x=180,y=310)

entry_2=Entry(login_window,show="*",font=16)
entry_2.place(x=350,y=310,width=200, height=37)

button1 = Button(login_window, text="LOGIN", font=("arial", 11),bg="#5E96D2",padx=18,pady=1)
button1.place(x=459, y=360)


login_window.mainloop()