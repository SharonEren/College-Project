from Detector import main_app
from create_classifier import train_classifer
from create_dataset import start_capture
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox,PhotoImage

from gender_prediction import ageAndgender, emotion

#from PIL import ImageTk, Image
#from gender_prediction import emotion,ageAndgender
names = set()


class MainUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global names
        with open("nameslist.txt", "r") as f:
            x = f.read()
            z = x.rstrip().split(" ")
            for i in z:
                names.add(i)
        self.title_font = tkfont.Font(family='Helvetica', size=16, weight="bold")
        self.title("Face Recognizer")
        self.resizable(False, False)
        self.geometry("1350x800")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.active_name = None
        container = tk.Frame(self)
        container.grid(sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (HomePage,StartPage, AbstPage, PageOne, PageTwo, PageThree, PageFour):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("HomePage")

    def show_frame(self, page_name):
            frame = self.frames[page_name]
            frame.tkraise()

    def on_closing(self):

        if messagebox.askokcancel("Quit", "Are you sure?"):
            global names
            f =  open("nameslist.txt", "a+")
            for i in names:
                    f.write(i+" ")
            self.destroy()

class HomePage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            render1 = PhotoImage(file='project1.png')
            img = tk.Label(self, image=render1)
            img.image = render1
            #img.place(x=0,y=0)
            img.grid(row=0, column=0, rowspan=4, sticky="nsew")
            
            #label = tk.Label(self, text="        Home Page        ", font=self.controller.title_font,fg="#263942")
            #label.grid(row=0, sticky="ew")
            button1 = tk.Button(self, text="Proceed",font=('Helvetica', 16,'bold'), fg="#ffffff", bg="#263942",command=lambda: self.controller.show_frame("StartPage"))
            button2 = tk.Button(self, text="  Close  ",font=('Helvetica', 16,'bold'), fg="#ffffff", bg="#263942",command=self.on_closing)
            button3 = tk.Button(self, text="Abtract", font=('Helvetica', 16,'bold'), fg="#ffffff", bg="#263942",command=lambda: self.controller.show_frame("AbstPage"))
            button1.place(x=540,y=460)
            button2.place(x=700,y=460)
            button3.place(x=640,y=550)


        def on_closing(self):
            if messagebox.askokcancel("Quit", "Are you sure?"):
                global names
                with open("nameslist.txt", "w") as f:
                    for i in names:
                        f.write(i + " ")
                self.controller.destroy()

class StartPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            #load = Image.open("homepagepic.png")
            #load = load.resize((250, 250), Image.ANTIALIAS)
            logo = PhotoImage(file='logo.png')
            img1 = tk.Label(self, image=logo)
            img1.image = logo
            img1.grid(row=0, column=1, rowspan=3, sticky="nsew")

            render = PhotoImage(file='homepagepic.png')
            img = tk.Label(self, image=render)
            img.image = render
            img.grid(row=3, column=1, rowspan=4, sticky="nsew")

            
            
            
            button1 = tk.Button(self, text="   Add a User  ",font='Helvetica 14 bold',width=10, fg="#ffffff", bg="#263942",command=lambda: self.controller.show_frame("PageOne"))
            button2 = tk.Button(self, text="   Check a User  ",font='Helvetica 14 bold',width=10, fg="#ffffff", bg="#263942",command=lambda: self.controller.show_frame("PageTwo"))
            button3 = tk.Button(self, text="Home",width=10,font='Helvetica 14 bold',  fg="#ffffff",bg="#263942", command=lambda: self.controller.show_frame("HomePage"))
            button4 = tk.Button(self, text="Quit",width=10,font='Helvetica 14 bold',  fg="#ffffff",bg="#263942", command=self.on_closing)
            button1.place(x=350,y=500)#.grid(row=4, column=2, ipady=2, ipadx=1)
            button2.place(x=550,y=500)#.grid(row=4, column=3, ipady=2, ipadx=2)
            button3.place(x=350,y=600)#.grid(row=5, column=2, ipady=2, ipadx=32)
            button4.place(x=550,y=600)#.grid(row=5, column=3, ipady=2, ipadx=32)


        def on_closing(self):
            if messagebox.askokcancel("Quit", "Are you sure?"):
                global names
                with open("nameslist.txt", "w") as f:
                    for i in names:
                        f.write(i + " ")
                self.controller.destroy()

class AbstPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            #load = Image.open("homepagepic.png")
            #load = load.resize((250, 250), Image.ANTIALIAS)
            logo = PhotoImage(file='logo.png')
            img1 = tk.Label(self, image=logo)
            img1.image = logo
            img1.grid(row=0, column=1, rowspan=3, sticky="nsew")

            render = PhotoImage(file='homepagepic.png')
            img = tk.Label(self, image=render)
            img.image = render
            img.grid(row=1, column=2, rowspan=4, sticky="nsew")

            
            label = tk.Label(self, text='''Abstract Page

Facial Expression conveys non-verbal cues, which plays an important roles in

interpersonal relations. The Facial Expression Recognition system is the process

of identifying the emotional state of a person. In this system captured image is

compared with the trained dataset available in database and then emotional state

of the image will be displayed.

This system is based on image processing and machine learning. For designing a

robust facial feature descriptor, we apply the Local Binary Pattern.

Local Binary Pattern (LBP) is a simple yet very efficient texture operator

which labels the pixels of an image by thresholding the neighborhood of each

pixel and considers the result as a binary number.
''', font=self.controller.title_font,fg="#263942",justify='left')
            label.grid(row=3,column=1, sticky="ew")
            #button1 = tk.Button(self, text="   Add a User  ",font='Helvetica 14 bold',width=10, fg="#ffffff", bg="#263942",command=lambda: self.controller.show_frame("PageOne"))
            #button2 = tk.Button(self, text="   Check a User  ",font='Helvetica 14 bold',width=10, fg="#ffffff", bg="#263942",command=lambda: self.controller.show_frame("PageTwo"))
            button3 = tk.Button(self, text="Home",width=10,font='Helvetica 14 bold',  fg="#ffffff",bg="#263942", command=lambda: self.controller.show_frame("HomePage"))
            button4 = tk.Button(self, text="Quit",width=10,font='Helvetica 14 bold',  fg="#ffffff",bg="#263942", command=self.on_closing)
            #button1.place(x=900,y=500)#.grid(row=4, column=2, ipady=2, ipadx=1)
            #button2.place(x=1100,y=500)#.grid(row=4, column=3, ipady=2, ipadx=2)
            button3.place(x=900,y=600)#.grid(row=5, column=2, ipady=2, ipadx=32)
            button4.place(x=1100,y=600)#.grid(row=5, column=3, ipady=2, ipadx=32)


        def on_closing(self):
            if messagebox.askokcancel("Quit", "Are you sure?"):
                global names
                with open("nameslist.txt", "w") as f:
                    for i in names:
                        f.write(i + " ")
                self.controller.destroy()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        logo = PhotoImage(file='logo.png')
        img1 = tk.Label(self, image=logo)
        img1.image = logo
        img1.grid(row=0, column=1, rowspan=3,  sticky="nsew")

        tk.Label(self, text="Enter the name", fg="#263942", font='Helvetica 14 bold').place(x=400,y=300)#.grid(row=6, column=1, pady=10, padx=5)
        self.user_name = tk.Entry(self, borderwidth=3,width=20, bg="lightgrey", font='Helvetica 11')
        self.user_name.place(x=550,y=300)#.grid(row=6, column=2, pady=10, padx=10)
        
        self.buttoncanc = tk.Button(self, text="Prev",width=10,font='Helvetica 14 bold', bg="#ffffff", fg="#263942", command=lambda: controller.show_frame("StartPage"))
        self.buttonext = tk.Button(self, text="Next",width=10,font='Helvetica 14 bold', fg="#ffffff", bg="#263942", command=self.start_training)
        self.buttoncanc.place(x=400,y=350)#.grid(row=7, column=1, pady=10, ipadx=5, ipady=4)
        self.buttonext.place(x=550,y=350)#.grid(row=7, column=2, pady=10, ipadx=5, ipady=4)
        
        self.buttoncanc1 = tk.Button(self, text="Home",width=10,font='Helvetica 14 bold', bg="#ffffff", fg="#263942", command=lambda: controller.show_frame("HomePage"))
        self.buttonext1 = tk.Button(self, text="Quit",width=10,font='Helvetica 14 bold', fg="#ffffff", bg="#263942", command=self.on_closing)
        self.buttoncanc1.place(x=400,y=400)#.grid(row=8, column=1, pady=10, ipadx=5, ipady=4)
        self.buttonext1.place(x=550,y=400)#.grid(row=8, column=2, pady=10, ipadx=5, ipady=4)
    def start_training(self):
        global names
        if self.user_name.get() == "None":
            messagebox.showerror("Error", "Name cannot be 'None'")
            return
        elif self.user_name.get() in names:
            messagebox.showerror("Error", "User already exists!")
            return
        elif len(self.user_name.get()) == 0:
            messagebox.showerror("Error", "Name cannot be empty!")
            return
        name = self.user_name.get()
        names.add(name)
        self.controller.active_name = name
        self.controller.frames["PageTwo"].refresh_names()
        self.controller.show_frame("PageThree")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Are you sure?"):
            global names
            with open("nameslist.txt", "w") as f:
                for i in names:
                    f.write(i + " ")
            self.controller.destroy()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global names
        self.controller = controller

        logo = PhotoImage(file='logo.png')
        img1 = tk.Label(self, image=logo)
        img1.image = logo
        img1.grid(row=0, column=1, rowspan=3,  sticky="nsew")
        
        tk.Label(self, text="Select user", fg="#263942", font='Helvetica 14 bold').place(x=300,y=250)#.grid(row=5, column=1, padx=10, pady=10)
        self.menuvar = tk.StringVar(self)
        self.dropdown = tk.OptionMenu(self, self.menuvar, *names)
        self.dropdown.config(bg="lightgrey")
        self.dropdown["menu"].config(bg="lightgrey")
        self.buttonext = tk.Button(self, text="Next",font='Helvetica 14 bold',width=10, command=self.nextfoo, fg="#ffffff", bg="#263942")
        self.dropdown.place(x=450,y=250)#.grid(row=5, column=1, ipadx=8, padx=10, pady=10)

        self.buttoncanc = tk.Button(self, text="Prev",font='Helvetica 14 bold',width=10, command=lambda: controller.show_frame("StartPage"), bg="#ffffff", fg="#263942")
        
        self.buttoncanc.place(x=300,y=350) #.grid(row=6, ipadx=5, ipady=4, column=1, pady=10)
        self.buttonext.place(x=450,y=350)#grid(row=6, ipadx=5, ipady=4, column=2, pady=10)
        
        self.buttoncanc1 = tk.Button(self, text="Home", bg="#ffffff", fg="#263942",width=10,font='Helvetica 14 bold', command=lambda: controller.show_frame("HomePage"))
        self.buttonext1 = tk.Button(self, text="Quit", fg="#ffffff", bg="#263942",width=10,font='Helvetica 14 bold', command=self.on_closing)
        self.buttoncanc1.place(x=300,y=450)
        self.buttonext1.place(x=450,y=450)

    def nextfoo(self):
        if self.menuvar.get() == "None":
            messagebox.showerror("ERROR", "Name cannot be 'None'")
            return
        self.controller.active_name = self.menuvar.get()
        self.controller.show_frame("PageFour")

    def refresh_names(self):
        global names
        self.menuvar.set('')
        self.dropdown['menu'].delete(0, 'end')
        for name in names:
            self.dropdown['menu'].add_command(label=name, command=tk._setit(self.menuvar, name))

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Are you sure?"):
            global names
            with open("nameslist.txt", "w") as f:
                for i in names:
                    f.write(i + " ")
            self.controller.destroy()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        logo = PhotoImage(file='logo.png')
        img1 = tk.Label(self, image=logo)
        img1.image = logo
        img1.grid(row=0, column=1, rowspan=3,  sticky="nsew")

        self.numimglabel = tk.Label(self, text="Number of images captured = 0", font='Helvetica 22 bold', fg="#263942")
        self.numimglabel.place(x=450,y=250)#.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)
        
        self.capturebutton = tk.Button(self, text="Capture Data Set",font='Helvetica 14 bold',  fg="#ffffff", bg="#263942", command=self.capimg)
        self.trainbutton = tk.Button(self, text="Train The Model", font='Helvetica 14 bold', fg="#ffffff", bg="#263942",command=self.trainmodel)
        self.capturebutton.place(x=450,y=350)#.grid(row=1, column=0, ipadx=5, ipady=4, padx=10, pady=20)
        self.trainbutton.place(x=650,y=350)#.grid(row=1, column=1, ipadx=5, ipady=4, padx=10, pady=20)

        self.home1 = tk.Button(self, text="Home",font='Helvetica 14 bold',  fg="#ffffff", bg="#263942", command=lambda: self.controller.show_frame("StartPage"))
        self.quit1 = tk.Button(self, text="Quit", font='Helvetica 14 bold', fg="#ffffff", bg="#263942",command=self.on_closing)
        self.home1.place(x=550,y=450)#.grid(row=1, column=0, ipadx=5, ipady=4, padx=10, pady=20)
        self.quit1.place(x=650,y=450)#.grid(row=1, column=1, ipadx=5, ipady=4, padx=10, pady=20)

    def capimg(self):
        self.numimglabel.config(text=str("Captured Images = 0 "))
        messagebox.showinfo("INSTRUCTIONS", "We will Capture 300 pic of your Face.")
        x = start_capture(self.controller.active_name)
        self.controller.num_of_images = x
        self.numimglabel.config(text=str("Number of images captured = "+str(x)))

    def trainmodel(self):
        if self.controller.num_of_images < 300:
            messagebox.showerror("ERROR", "No enough Data, Capture at least 300 images!")
            return
        train_classifer(self.controller.active_name)
        messagebox.showinfo("SUCCESS", "The modele has been successfully trained!")
        self.controller.show_frame("PageFour")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Are you sure?"):
            global names
            with open("nameslist.txt", "w") as f:
                for i in names:
                    f.write(i + " ")
            self.controller.destroy()

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        logo = PhotoImage(file='logo.png')
        img1 = tk.Label(self, image=logo)
        img1.image = logo
        img1.grid(row=0, column=1, rowspan=3,  sticky="nsew")


        label = tk.Label(self, text="Emotion Detection", font='Helvetica 22 bold')
        label.place(x=500,y=250)#.grid(row=,column=0, sticky="ew")
        #button1 = tk.Button(self, text="Face Recognition", font='Helvetica 14 bold', command=self.openwebcam, fg="#ffffff", bg="#263942")
        button2 = tk.Button(self, text="Emotion Detection", font='Helvetica 14 bold', command=self.emot, fg="#ffffff", bg="#263942")
        #button3 = tk.Button(self, text="Gender and Age Prediction", command=self.gender_age_pred, fg="#ffffff", bg="#263942")
        button3 = tk.Button(self, text="Quit",width=10, font='Helvetica 14 bold', command=self.on_closing, fg="#ffffff", bg="#263942")
        button4 = tk.Button(self, text="Home",width=10, font='Helvetica 14 bold', command=lambda: self.controller.show_frame("StartPage"), bg="#ffffff", fg="#263942")
        #button1.place(x=450,y=450)#.grid(row=1,column=0, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)
        button2.place(x=550,y=450)#.grid(row=1,column=1, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)
        button3.place(x=500,y=550)#.grid(row=2,column=0, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)
        button4.place(x=650,y=550)#.grid(row=2,column=1, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)

    def openwebcam(self):
        main_app(self.controller.active_name)
    def gender_age_pred(self):
       ageAndgender()
    def emot(self):
        emotion()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Are you sure?"):
            global names
            with open("nameslist.txt", "w") as f:
                for i in names:
                    f.write(i + " ")
            self.controller.destroy()


app = MainUI()
app.iconphoto(False, tk.PhotoImage(file='icon.ico'))
app.mainloop()

