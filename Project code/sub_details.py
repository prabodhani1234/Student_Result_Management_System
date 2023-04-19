from tkinter import *

sub_details_window = Tk()
sub_details_window.title("Exam Result Management System")
sub_details_window.configure(bg='#DFD6D6')
sub_details_window.geometry("700x500") # window size
sub_details_window.maxsize(width=700, height=500)  # window maximize


# main text
text1 = Label(sub_details_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 22, "bold"),
              fg="white", bg="#285C9F", width=700, height=3)
text1.pack()

text2=Label(sub_details_window,text="ALL SUBJECT DETAILS...",font=("Times New Roman", 17),
            fg="#E33737", bg="#DFD6D6")
text2.place(y=110,x=20)

label1=Label(sub_details_window,text='SUBJECT CODE',font=('arial',11),bg='#797979')
label1.place(x=140,y=212,width=200,height=30)

label1=Label(sub_details_window,text='SUBJECT NAME',font=('arial',11),bg='#797979')
label1.place(x=342,y=212,width=200,height=30)

label1=Label(sub_details_window,text='',font=('arial',11))
label1.place(x=140,y=244,width=200,height=30)

label1=Label(sub_details_window,text='',font=('arial',11))
label1.place(x=342,y=244,width=200,height=30)

label1=Label(sub_details_window,text='',font=('arial',11))
label1.place(x=140,y=276,width=200,height=30)

label1=Label(sub_details_window,text='',font=('arial',11))
label1.place(x=342,y=276,width=200,height=30)

label1=Label(sub_details_window,text='',font=('arial',11))
label1.place(x=140,y=308,width=200,height=30)

label1=Label(sub_details_window,text='',font=('arial',11))
label1.place(x=342,y=308,width=200,height=30)

button1 = Button(sub_details_window, text="BACK", font=("arial", 11),bg="#5E96D2",padx=18,pady=1)
button1.place(x=449, y=360)

sub_details_window.mainloop()