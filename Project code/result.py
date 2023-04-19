from tkinter import *
from tkinter import messagebox

def print_massage():
    messagebox.showinfo('Successful Massage', 'Print Successful')

result_window = Tk()
result_window.title("Exam Result Management System")
result_window.configure(bg='#DFD6D6')
result_window.geometry("700x600") # window size
result_window.maxsize(width=700, height=600)  # window maximize


# main text
text1 = Label(result_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 22, "bold"),
              fg="white", bg="#285C9F", width=700, height=3)
text1.pack()

text2=Label(result_window,text="RESULT",font=("Times New Roman", 21,'bold'),
            fg="#E33737", bg="#DFD6D6")
text2.pack()

label1=Label(result_window,text="Registration Number  :",font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=10,pady=4)
label1.place(x=115,y=180)

label2=Label(result_window,font=("arial", 11), fg="#333333")
label2.place(x=280,y=180,width=280, height=30)

label3=Label(result_window,text="Index Number\t   :",font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=10,pady=4)
label3.place(x=115,y=212)

label4=Label(result_window,font=("arial", 11), fg="#333333")
label4.place(x=280,y=212,width=280, height=30)

label5=Label(result_window,text="Name\t\t   :",font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=10,pady=4)
label5.place(x=115,y=244)

label6=Label(result_window,font=("arial", 11), fg="#333333")
label6.place(x=280,y=244,width=280, height=30)

label6=Label(result_window,text="SUBJECT",bg='#797979')
label6.place(x=140,y=300,width=200,height=30)

label6=Label(result_window,text="MARKS ",bg='#797979')
label6.place(x=342,y=300,width=100,height=30)

label6=Label(result_window,text="GRADE ",bg='#797979')
label6.place(x=444,y=300,width=100,height=30)

label7=Label(result_window,bg='#FFFFFF')
label7.place(x=140,y=333,width=200,height=30)

label7=Label(result_window,bg='#FFFFFF')
label7.place(x=342,y=333,width=100,height=30)

label7=Label(result_window,bg='#FFFFFF')
label7.place(x=444,y=333,width=100,height=30)

label8=Label(result_window,bg='#FFFFFF')
label8.place(x=140,y=366,width=200,height=30)

label8=Label(result_window,bg='#FFFFFF')
label8.place(x=342,y=366,width=100,height=30)

label8=Label(result_window,bg='#FFFFFF')
label8.place(x=444,y=366,width=100,height=30)

label9=Label(result_window,bg='#FFFFFF')
label9.place(x=140,y=399,width=200,height=30)

label9=Label(result_window,bg='#FFFFFF')
label9.place(x=342,y=399,width=100,height=30)

label9=Label(result_window,bg='#FFFFFF')
label9.place(x=444,y=399,width=100,height=30)

label10=Label(result_window,text='TOTAL',bg='#FFFFFF')
label10.place(x=140,y=445,width=200,height=30)

label10=Label(result_window,bg='#FFFFFF')
label10.place(x=342,y=445,width=202,height=30)

label11=Label(result_window,text='TOTAL',bg='#FFFFFF')
label11.place(x=140,y=478,width=200,height=30)

label11=Label(result_window,bg='#FFFFFF')
label11.place(x=342,y=478,width=202,height=30)

button1 = Button(result_window, text="Print", font=("arial", 11),bg="#5E96D2",command=print_massage,padx=15,pady=1)
button1.place(x=472, y=524)

result_window.mainloop()