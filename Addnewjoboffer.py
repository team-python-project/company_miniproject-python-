from tkinter import *

def ID():
    u.get()
    f=open("IDS.txt","r")
    s = f.readline()
    f.close() 
    print(s)
    l=s.split()
    print(l)
    if str(u) in l:
        messagebox.showwarning(" \n id exist \n")
        
        
    else:
        l.append(u)
        print(l)
        f = open("IDS.txt","w")
        for i in l:
            f.write(str(i)+" ")
        f.close() 
        
        
        
def add():
    f=Tk()
    f.title("Add ")
    f.geometry("250x250")
    f['bg']="#A0A0A0"
    
    a=Label(f,text="Add new job offer:",fg="black",bg="#A0A0A0")
    a.pack()
    a.config(font=("Courier", 10))
    
    fr=Frame(f,bg="#F8F8FF",borderwidth=2,relief=RAISED)
    fr.pack()
    
    
    
    g=Label(fr,text="Job ID",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()
    a=user
    Button(fr,text="ENTER",command=ID).pack()
    
    
    
    
    g=Label(fr,text="company information",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    
    
    g=Label(fr,text="name",bg="#F8F8FF").pack()
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()
    
    g=Label(fr,text="adresse",bg="#F8F8FF").pack()
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()
    
    g=Label(fr,text="phone num",bg="#F8F8FF").pack()
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()
    
    g=Label(fr,text="e-mail",bg="#F8F8FF").pack()
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()
    
    g=Label(fr,text="profile description",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    
    g=Label(fr,text="degree",bg="#F8F8FF").pack()
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()
    
    g=Label(fr,text="qualifications",bg="#F8F8FF").pack()
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()
    
    g=Label(fr,text="experience",bg="#F8F8FF").pack()
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()
    
    g=Label(fr,text="mission description",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()
    

    f.mainloop()
add()  