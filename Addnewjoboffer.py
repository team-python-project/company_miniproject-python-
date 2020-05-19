from tkinter import *

#--------fonction pour  verifier l'id et ajouter le job info dans le fichier jobs--------
def save_jobs():
    f=open("IDS.txt","r")
    s = f.readline()
    f.close() 
    l=s.split()
    if str(u.get()) in l:
        u.set("")
        messagebox.showwarning(" \n id existe choose another \n") 
        Label(p,text="id exist choose another ID ",bg="#A0A0A0",fg="#FF0000").pack()
    else:
        l.append(u.get())
        f = open("IDS.txt","w")
        for i in l:
            f.write(str(i)+" ")
        f.close()
        l=[u.get(),b.get(),b1.get(),b2.get(),b3.get(),b4.get(),c.get(),c1.get(),c2.get(),c3.get()]
        f1=open("jobs.txt","a")
        for i in l:
            f1.write(i+" ")
        f1.write("\n")
        f1.close()
        
#-------------------------------
#--------------------------------------------
#-----fonction pour remplir les champs de job par ladmin-------
def add():
    global p
    p=Tk()
    p.title("Add ")
    p.geometry("250x250")
    p['bg']="#A0A0A0"
    
    a=Label(p,text="Add new job offer:",fg="black",bg="#A0A0A0")
    a.pack()
    a.config(font=("Courier", 10))
    
    fr=Frame(p,bg="#F8F8FF",borderwidth=2,relief=RAISED)
    fr.pack()
    
    
    
    g=Label(fr,text="Job ID",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    global u
    u=StringVar()
    a1=Entry(fr,textvariable=u,bg='#FFFAFA')
    a1.pack()
    a1.focus_set()
    #Button(fr,text="ENTER",command=ID).pack()
    
    
    
    
    g=Label(fr,text="company information",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    
    
    g=Label(fr,text="name",bg="#F8F8FF").pack()
    global b
    b=StringVar()
    a1=Entry(fr,textvariable=b,bg='#FFFAFA')
    a1.pack()
    a1.focus_set()
    
    g=Label(fr,text="adresse",bg="#F8F8FF").pack()
    global b1
    b1=StringVar()
    a1=Entry(fr,textvariable=b1,bg='#FFFAFA')
    a1.pack()
    a1.focus_set()
    
    g=Label(fr,text="phone num",bg="#F8F8FF").pack()
    global b2
    b2=StringVar()
    a1=Entry(fr,textvariable=b2,bg='#FFFAFA')
    a1.pack()
    a1.focus_set()
    
    
    
    g=Label(fr,text="email",bg="#F8F8FF").pack()
    global b3
    b3=StringVar()
    a1=Entry(fr,textvariable=b3,bg='#FFFAFA')
    a1.pack()
    a1.focus_set()
    
    
    g=Label(fr,text="domaine",bg="#F8F8FF").pack()
    global b4
    b4=StringVar()
    a1=Entry(fr,textvariable=b4,bg='#FFFAFA')
    a1.pack()
    a1.focus_set()
    


    g=Label(fr,text="profile description",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    
    g=Label(fr,text="degree",bg="#F8F8FF").pack()
    global c
    c=StringVar()
    a1=Entry(fr,textvariable=c,bg='#FFFAFA')
    a1.pack()
    a1.focus_set()
    
    g=Label(fr,text="qualification",bg="#F8F8FF").pack()
    global c1
    c1=StringVar()
    a1=Entry(fr,textvariable=c1,bg='#FFFAFA')
    a1.pack()
    a1.focus_set()
    
    g=Label(fr,text="exoerience",bg="#F8F8FF").pack()
    global c2
    c2=StringVar()
    a1=Entry(fr,textvariable=c2,bg='#FFFAFA')
    a1.pack()
    a1.focus_set()
    
    g=Label(fr,text="adresse",bg="#F8F8FF").pack()
    global c3
    c3=StringVar()
    a1=Entry(fr,textvariable=c3,bg='#FFFAFA')
    a1.pack()
    a1.focus_set()
    
    
    f1=Frame(fr,bg="#F8F8FF",borderwidth=2,relief=RAISED)
    f1.pack()
    Button(f1,text="ENTER",command=save_jobs).pack()
    
    
    p.mainloop()
      
add()   