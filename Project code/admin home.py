from tkinter import *

admin_window = Tk()
admin_window.title("Exam Result Management System")
admin_window.configure(bg='#DFD6D6')
admin_window.geometry("700x450")  # window size
admin_window.maxsize(width=700, height=450)  # window maximize


# main text
text1 = Label(admin_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 22, "bold"),
              fg="white", bg="#285C9F", width=700, height=3)
text1.pack()

text2=Label(admin_window,text="ADMIN DASHBOARD...",font=("Times New Roman", 17),
            fg="#E33737", bg="#DFD6D6")
text2.place(y=110,x=20)

image1 = PhotoImage(file="C:/Users/user/Desktop/EXAM RESULT SYSTEM/IMAGES/admin image.png")
label1 = Label(admin_window, image=image1)
label1.place(y=164, x=305)

# Button
button1 = Button(admin_window, text="ADD NEW STUDENT", font=("arial", 15), padx=30, pady=1)
button1.place(y=170, x=20)

button2 = Button(admin_window, text="ADD NEW SUBJECT", font=("arial", 15), padx=30, pady=1)
button2.place(y=220, x=20)

button3 = Button(admin_window, text="ALL SUBJECT DETAILS", font=("arial", 15), padx=15, pady=1)
button3.place(y=270, x=20)

button4 = Button(admin_window, text="REGISTERED STUDENT ", font=("arial", 15), padx=9, pady=1)
button4.place(y=320, x=20)

button5 = Button(admin_window, text="ALL STUDENT RESULT ", font=("arial", 15), padx=15, pady=1)
button5.place(y=370, x=20)


admin_window.mainloop()
