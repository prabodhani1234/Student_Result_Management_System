import tkinter as tk
from tkinter import Entry

LARGE_FONT = ("Verdana", 16)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Student Result Management", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Student",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        button3 = tk.Button(self, text="Teachers",
                            command=lambda: controller.show_frame(PageOne))
        button3.pack()

        button4 = tk.Button(self, text="Admin",
                            command=lambda: controller.show_frame(PageTwo))
        button4.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome Student", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label1 = tk.Label(self, text="Student Result Management", font=LARGE_FONT)
        label1.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))

        label2 = tk.Label(self, text="Index No", font=LARGE_FONT)

        label2.pack(pady=10, padx=10)
        global password
        password = Entry(self, show='*')
        password.pack()
        button3 = tk.Button(self, text="Search",
                            command=lambda: controller.show_frame(PageTwo))

        button3.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = SeaofBTCapp()
app.mainloop()
