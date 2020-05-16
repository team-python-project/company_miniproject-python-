from tkinter import *
from admin import admin
from client import client

f=Tk()
f.title("welcome")
f.geometry("250x250")
f['bg']="#A0A0A0"
a=Label(f,text="we are hiring!!! \n join us",fg="#606060",bg="#A0A0A0")
a.pack()
a.config(font=("Courier", 15))

#***frame1**********************************************************************
ft=Frame(f,bg="#F8F8FF",borderwidth=2,relief=RAISED, width=400, height=400)
ft.pack()
Label(ft,text="login",fg="#000000",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()

#****frame2************************************************************************

fr=Frame(ft,bg="#F8F8FF",borderwidth=0,relief=RAISED)
fr.pack()

#*****user button to login (in frame2)**********************************************

Label(fr,text="username:",bg="#F8F8FF").pack()
user=StringVar()
a1=Entry(fr,textvariable=user,bg='#FFFAFA')
a1.pack()

Label(fr,text="password:",bg="#F8F8FF").pack()
mdp=StringVar()

a1=Entry(fr,textvariable=mdp,show="*",bg='#FFFAFA')
a1.focus_set()
a1.pack()

#******* les butoonsenter/exit******************************************************
#///////////verif le mdp/////////////////////
def check():
    
    if mdp.get()=="ADMIN":
        admin(user.get())
    elif mdp.get()=="JOBSEEKER":
        client(user.get()) 
    else:
        messagebox.showwarning(" \n mot de passe incoreect \n")
        #Label(f,text="mot de passe incorrect",fg="red").pack()
        mdp.set("")
#//////////////////////////////////////////////////


Button(fr,text="ENTER",command=check).pack()
g=Button(fr,text="Exit",command=f.destroy)
g.pack()
    





f.mainloop()