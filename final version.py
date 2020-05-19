import os
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import*

#some 3afsus 
def back(window):
    window.destroy()
#####################
    #
    #
    # success and fail messages
    #
    #
#####################
def saved(window,msg):
    saved = tk.Label(window, text = msg , fg = "green", font = ("Calibri", 11))
    saved.pack()
    window.after(1500, saved.destroy)

def updated():
    updated = tk.Label(screen9, text = "Offer updated", fg = "green", font = ("Calibri", 11))
    updated.pack()
    screen9.after(1500, updated.destroy)

def failed(window,msg):
    saved = tk.Label(window, text = msg , fg = "red", font = ("Calibri", 11))
    saved.pack()
    window.after(1500, saved.destroy)
    

    #admin features
def save_job():
    f=open("IDS.txt","a")
    f.close() 
    f=open("IDS.txt","r")
    h=False

    if h== False:
        l=[]
        l.append(u.get())
        f = open("IDS.txt","a")
        for i in l:
            f.write(str(i)+" ")
        f.close()
        l=[u.get(),b.get(),b1.get(),b2.get(),b3.get(),b4.get(),c.get(),c1.get(),c2.get(),c3.get()]
        f1=open("jobs.txt","a")
        for i in l:
            f1.write(i+";")
        f1.write("\n")
        f1.close()
        global p2
        showinfo('Résultat','information applied.\nAu revoir !')
        p2.destroy()
def save_jobs():
    file = open('jobs.txt', "r")
    mn=False
    ml=[]
    for line in file:
      gp=""
      mn=False
      if line[0].upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
       for nbv in line:
          if (nbv != ";") and (mn==False):
              gp=gp+nbv
          else:
              mn=True
       ml.append(gp)
       
    file.close()
    h=False
    
    if u.get() in ml:
        showinfo('Résultat','id existe choose another.\nAu revoir !')
        Label(p,text="id exist choose another ID ",bg="#A0A0A0",fg="#FF0000").pack()
        h=True
    if h== False:
        l=[]
        l.append(u.get())
        f = open("IDS.txt","a")
        for i in l:
            f.write(str(i)+" ")
        f.close()
        l=[u.get(),b.get(),b1.get(),b2.get(),b3.get(),b4.get(),c.get(),c1.get(),c2.get(),c3.get()]
        f1=open("jobs.txt","a")
        for i in l:
            f1.write(i+";")
        f1.write("\n")
        f1.close()
        p
        showinfo('Résultat','information applied.\nAu revoir !')
        p.destroy()        
#-------------------------------
#--------------------------------------------
#-----fonction pour remplir les champs de job par ladmin-------
def add():
    global p
    p=Tk()
    p.title("Add ")
    p.geometry("250x700")
    p['bg']="#A0A0A0"
    
    a=Label(p,text="Add new job offer:",fg="black",bg="#A0A0A0")
    a.pack()
    a.config(font=("Courier", 10))
    
    fr=Frame(p,bg="#F8F8FF",borderwidth=2,relief=RAISED)
    fr.pack()
    
    
    
    g=Label(fr,text="Job ID",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    global u
    u=StringVar()
    u=Entry(fr,bg='#FFFAFA')
    u.pack()
    u.focus_set()
    #Button(fr,text="ENTER",command=ID).pack()
    
    
    
    
    g=Label(fr,text="company information",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    
    
    g=Label(fr,text="name",bg="#F8F8FF").pack()
    global b
    b=StringVar()
    b=Entry(fr,bg='#FFFAFA')
    b.pack()
    b.focus_set()
    
    g=Label(fr,text="adresse",bg="#F8F8FF").pack()
    global b1
    b1=StringVar()
    b1=Entry(fr,bg='#FFFAFA')
    b1.pack()
    b1.focus_set()
    
    g=Label(fr,text="phone num",bg="#F8F8FF").pack()
    global b2
    b2=StringVar()
    b2=Entry(fr,bg='#FFFAFA')
    b2.pack()
    b2.focus_set()
    
    
    
    g=Label(fr,text="email",bg="#F8F8FF").pack()
    global b3
    b3=StringVar()
    b3=Entry(fr,bg='#FFFAFA')
    b3.pack()
    b3.focus_set()
    
    
    g=Label(fr,text="domain",bg="#F8F8FF").pack()
    global b4
    b4=StringVar()
    b4=Entry(fr,bg='#FFFAFA')
    b4.pack()
    b4.focus_set()
    


    g=Label(fr,text="profile description",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    
    g=Label(fr,text="degree",bg="#F8F8FF").pack()
    global c
    c=StringVar()
    c=Entry(fr,bg='#FFFAFA')
    c.pack()
    c.focus_set()
    
    g=Label(fr,text="qualification",bg="#F8F8FF").pack()
    global c1
    c1=StringVar()
    c1=Entry(fr,bg='#FFFAFA')
    c1.pack()
    c1.focus_set()
    
    g=Label(fr,text="experience",bg="#F8F8FF").pack()
    global c2
    c2=StringVar()
    c2=Entry(fr,bg='#FFFAFA')
    c2.pack()
    c2.focus_set()
    
    g=Label(fr,text="adresse",bg="#F8F8FF").pack()
    global c3
    c3=StringVar()
    c3=Entry(fr,bg='#FFFAFA')
    c3.pack()
    c3.focus_set()
    
    
    f1=Frame(fr,bg="#F8F8FF",borderwidth=2,relief=RAISED)
    f1.pack()
    Button(f1,text="ENTER",command=save_jobs).pack()
    
    
    p.mainloop()
      
    
    
def update2():
    global ln
    global p2
    p2=Tk()
    p2.title("Add ")
    p2.geometry("250x700")
    p2['bg']="#A0A0A0"
    
    a=Label(p2,text="Add new job offer:",fg="black",bg="#A0A0A0")
    a.pack()
    a.config(font=("Courier", 10))
    
    fr=Frame(p2,bg="#F8F8FF",borderwidth=2,relief=RAISED)
    fr.pack()
    
    
    
    g=Label(fr,text="Job ID",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    global u
    u=StringVar()
    u=Entry(fr,bg='#FFFAFA')
    u.pack()
    u.focus_set()
    u.insert(0, ln[0])
    #Button(fr,text="ENTER",command=ID).pack()
    
    
    
    
    g=Label(fr,text="company information",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    
    
    g=Label(fr,text="name",bg="#F8F8FF").pack()
    global b
    b=StringVar()
    b=Entry(fr,bg='#FFFAFA')
    b.pack()
    b.focus_set()
    b.insert(0, ln[1])
    g=Label(fr,text="adresse",bg="#F8F8FF").pack()
    global b1
    b1=StringVar()
    b1=Entry(fr,bg='#FFFAFA')
    b1.pack()
    b1.focus_set()
    b1.insert(0, ln[2])
    g=Label(fr,text="phone num",bg="#F8F8FF").pack()
    global b2
    b2=StringVar()
    b2=Entry(fr,bg='#FFFAFA')
    b2.pack()
    b2.focus_set()
    b2.insert(0, ln[3])
    
    
    g=Label(fr,text="email",bg="#F8F8FF").pack()
    global b3
    b3=StringVar()
    b3=Entry(fr,bg='#FFFAFA')
    b3.pack()
    b3.focus_set()
    b3.insert(0, ln[4])
    
    g=Label(fr,text="domain",bg="#F8F8FF").pack()
    global b4
    b4=StringVar()
    b4=Entry(fr,bg='#FFFAFA')
    b4.pack()
    b4.focus_set()
    b4.insert(0, ln[5])


    g=Label(fr,text="profile description",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    
    g=Label(fr,text="degree",bg="#F8F8FF").pack()
    global c
    c=StringVar()
    c=Entry(fr,bg='#FFFAFA')
    c.pack()
    c.focus_set()
    c.insert(0, ln[6])
    g=Label(fr,text="qualification",bg="#F8F8FF").pack()
    global c1
    c1=StringVar()
    c1=Entry(fr,bg='#FFFAFA')
    c1.pack()
    c1.focus_set()
    c1.insert(0, ln[7])
    g=Label(fr,text="experience",bg="#F8F8FF").pack()
    global c2
    c2=StringVar()
    c2=Entry(fr,bg='#FFFAFA')
    c2.pack()
    c2.focus_set()
    c2.insert(0, ln[8])
    g=Label(fr,text="adresse",bg="#F8F8FF").pack()
    global c3
    c3=StringVar()
    c3=Entry(fr,bg='#FFFAFA')
    c3.pack()
    c3.focus_set()
    c3.insert(0, ln[9])
    
    f1=Frame(fr,bg="#F8F8FF",borderwidth=2,relief=RAISED)
    f1.pack()
    Button(f1,text="ENTER",command=save_job).pack()
    
    
    p2.mainloop()
      
    
def update1():
    y=open("jobs.txt","r")
    gh=False
    for o in y:
       
       if user.get() in o :
           s=o
           gh= True
           

    if gh==True :
            j=0
            r=""
            global ln
            ln=[]
            for x in s:
              if s[j]!=";":
                r=r+s[j]
              else:
                ln.append(r)
                r=""
              j=j+1

            f = open("jobs.txt","r")

            lines = f.readlines()

            f.close()


            f = open("jobs.txt","w")

            for line in lines:
             if line!=s:
              f.write(line+"\n")

            f.close()
            update2()

        
    else:
           showinfo('Résultat','information not applied.\nAu revoir !')        
    y.close()
    
    
    
def update():
    ft=Tk()
    ft.title("The list ")
    ft.geometry("300x120")
    ft['bg']="#3e5462"
    a=Label(ft,text="if you are creeting a job offer:",fg="yellow",bg="#3e5462")
    a.pack()
    a.config(font=("Courier", 10))
    fr=Frame(ft,bg="#3e5462",borderwidth=5,relief=RAISED)
    fr.pack()
    Label(fr,text="job id",fg="white",bg="#3e5462").pack(side="left")
    global user
    user=StringVar()
    user=Entry(fr,bg='#FFFAFA')
    user.pack()

    BoutonQuitter = Button(ft, text ='Quitter', command = ft.destroy )
    BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)
    Texte = StringVar()

    BoutonNext = Button(ft, text ='Next', command = update1 )
    BoutonNext.pack(side = LEFT, padx = 5, pady = 5)
    Texte = StringVar() 
     
    ft.mainloop()
    
def delete1():
    y=open("jobs.txt","r")
    gh=False
    for o in y:
       
       if user.get() in o :
           s=o
           gh= True
           

    if gh==True :
            

            f = open("jobs.txt","r")

            lines = f.readlines()

            f.close()


            f = open("jobs.txt","w")

            for line in lines:
             if line!=s:
              f.write(line+"\n")

            f.close()
            showinfo('Résultat','information deleted.\nAu revoir !')

        
    else:
           showinfo('Résultat','information not applied.\nAu revoir !')        
    y.close()
    
    
    


def delete():
    ftn=Tk()
    ftn.title("The list ")
    ftn.geometry("300x120")
    ftn['bg']="#3e5462"
    a=Label(ftn,text="if you are creeting a job offer:",fg="yellow",bg="#3e5462")
    a.pack()
    a.config(font=("Courier", 10))
    fr=Frame(ftn,bg="#3e5462",borderwidth=5,relief=RAISED)
    fr.pack()
    Label(fr,text="job id",fg="white",bg="#3e5462").pack(side="left")
    global user
    user=StringVar()
    user=Entry(fr,bg='#FFFAFA')
    user.pack()

    BoutonQuitter = Button(ftn, text ='Quitter', command = ftn.destroy )
    BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)
    Texte = StringVar()

    BoutonNext = Button(ftn, text ='Next', command = delete1 )
    BoutonNext.pack(side = LEFT, padx = 5, pady = 5)
    Texte = StringVar() 
     
    ftn.mainloop()


    


def brows():
    f=Tk()
    f.title("The list ")
    f.geometry("400x120")
    f['bg']="#3e5462"
    a=Label(f,text="Brows the list of job seekers:",fg="yellow",bg="#3e5462")
    a.pack()
    a.config(font=("Courier", 10))
    fr=Frame(f,bg="#3e5462",borderwidth=5,relief=RAISED)
    fr.pack()
    

    Label(fr,text="All the job seekers that applied for",fg="white",bg="#3e5462").pack(side="left")
    Checkbutton(fr,text="job offers",fg="white",bg="#3e5462",command=solution1).pack()
    
  
    
    Checkbutton(fr,text="the same job offer",fg="white",bg="#3e5462",command=solution2).pack()
    
    BoutonQuitter = Button(f, text ='Quitter', command = f.destroy )
    BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)
    Texte = StringVar() 
    
    f.mainloop()
    


def solution1():
        global i
        i=0
        f=open("apply.txt","r")
        global p
        p=[]
        for a in f:
           if a[0].upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
              p.append(a)   
        f.close()
        global t
        t=Tk()
        t.title("recherche ")
        t.geometry("600x700")
        t['bg']="#A0A0A0"
        global q 
        q=["job ID: ","personal information: ID card: ","                     name: ","                     adresse: ","                     phone num: ","education: university degree: ","           others:","professional information: experience: ","                     skills: "]
        r=""
        j=0
        l=[]
        s=str(p[i])
        for x in s:
            if s[j]!=";":
                r=r+s[j]
            else:
                l.append(r)
                r=""
            j=j+1
        nb=0
        for b in l :
            cn=q[nb]+l[nb]
            global ab
            ab=Label(t,text=cn,fg="black",bg="#A0A0A0")
            ab.pack()
            ab.config(font=("Courier", 10))
            nb+=1
        global v
        v=l[0]
        Button(t,text="back",command=backbutton1).pack()
        Button(t,text="next",command=nextbutton1).pack()
        Button(t,text="previous",command=prevbutton1).pack()
   
        t.mainloop()
def prevbutton1() :
            global i
            global t
            q=["job ID: ","personal information: ID card: ","                     name: ","                     adresse: ","                     phone num: ","education: university degree: ","           others:","professional information: experience: ","                     skills: "]
            for w in t.winfo_children():
                w.destroy()
            if i > 0:
               i-=1
            else:
                i=0
        
            r=""
            j=0
            l=[]
            s=str(p[i])
            for x in s:
                if s[j]!=";":
                    r=r+s[j]
                else:
                    l.append(r)
                    r=""
                j=j+1
                nb=0
            for b in l :
                    cn=q[nb]+l[nb]
                    ab=Label(t,text=cn,fg="black",bg="#A0A0A0")
                    ab.pack()
                    ab.config(font=("Courier", 10))
                    nb+=1
            global v
            v=l[0]
            Button(t,text="back",command=backbutton1).pack()
            Button(t,text="next",command=nextbutton1).pack()
            Button(t,text="previous",command=prevbutton1).pack()
        
            t.mainloop()
  
def nextbutton1() :
             global i
             global t
             q=["job ID: ","personal information: ID card: ","                     name: ","                     adresse: ","                     phone num: ","education: university degree: ","           others:","professional information: experience: ","                     skills: "]
             for w in t.winfo_children():
                 w.destroy()
                 if i < (len(p)-1):
                    i+=1
                 else:
                      i=(len(p)-1)
        
             r=""
             j=0
             l=[]
             s=str(p[i])
             for x in s:
                 if s[j]!=";":
                   r=r+s[j]
                 else:
                      l.append(r)
                      r=""
                 j=j+1
                 nb=0
             for b in l :
                   cn=q[nb]+l[nb]
                   ab=Label(t,text=cn,fg="black",bg="#A0A0A0")
                   ab.pack()
                   ab.config(font=("Courier", 10))
                   nb+=1
             global v
             v=l[0]
             Button(t,text="back",command=backbutton1).pack()
             Button(t,text="next",command=nextbutton1).pack()
             Button(t,text="previous",command=prevbutton1).pack()
        
             t.mainloop()
  
           
def backbutton1() :
          global i
          global t
          i=0
          global p
          p=[]
          t.destroy()
          t.mainloop()
        
def solution2():
    f=Tk()
    f.title("The list ")
    f.geometry("300x120")
    f['bg']="#3e5462"
    a=Label(f,text="id job:",fg="yellow",bg="#3e5462")
    a.pack()
    a.config(font=("Courier", 10))
    fr=Frame(f,bg="#3e5462",borderwidth=5,relief=RAISED)
    fr.pack()
    global i
    i=0

    
################BOUTON ID#############""    

    Label(fr,text="your id card",fg="white",bg="#3e5462").pack(side="left")
    global user
    user=StringVar()
    user=Entry(fr,bg='#FFFAFA')
    user.pack()
################# BOTUON QUITTTTTTERR###############""""
    BoutonQuitter = Button(f, text ='Quitter', command = f.destroy )
    BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)
    Texte = StringVar()
#################BOUTOOOOOOOOOON NEXT##############
    BoutonNext = Button(f, text ='Next', command = sol )
    BoutonNext.pack(side = LEFT, padx = 5, pady = 5)
    Texte = StringVar() 
     
    f.mainloop()
def sol2(l):
    
    q=["job ID: ","personal information: ID card: ","                     name: ","                     adresse: ","                     phone num: ","education: university degree: ","           others:","professional information: experience: ","                     skills: "]
    global t
    t=Tk()
    t.title("recherche ")
    t.geometry("600x700")
    t['bg']="#A0A0A0"
    nb=0
    for b in l :
         cn=q[nb]+l[nb]
         global ab
         ab=Label(t,text=cn,fg="black",bg="#A0A0A0")
         ab.pack()
         ab.config(font=("Courier", 10))
         nb+=1
    Button(t,text="back",command=backbutton1).pack()
    Button(t,text="next",command=nextbutton1).pack()
    Button(t,text="previous",command=prevbutton1).pack()
    t.mainloop()
def sol():
    global user
    global i
    file = open('apply.txt', "r")
    mn=False
    global p
    p=[]
    for line in file:
      gp=""
      mn=False
      if line[0].upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
       for nbv in line:
          if (nbv != ";") and (mn==False):
              gp=gp+nbv
          else:
              mn=True
       if gp == user.get():
           p.append(line)
    if p==[]:
        showinfo('Résultat','there are no posts.\nAu revoir !')
    else:
     r=""
     j=0
     l=[]
     s=str(p[i])
     for x in s:
        if s[j]!=";":
           r=r+s[j]
        else:
             l.append(r)
             r=""
        j=j+1


     sol2(l)

    file.close()



def admin_form():
    screen6 = Toplevel(screen)
    screen6.title("admin Dashboard")
    screen6.geometry("400x400")
    Label(screen6, text = "Welcome to the dashboard",font = ("Calibri", 17)).pack()
    Button(screen6, text = "Add new offer", command =add).pack()
    Button(screen6, text = "Update offer", command =update).pack()
    Button(screen6, text = "Delete offer", command =delete).pack()
    Button(screen6, text = "Brows all applications", command = brows).pack()
    Button(screen6, text = "Back", command =lambda : back(screen6)).pack()
    

#seekerform
    
    
    
def seeker_form():
    f=Tk()
    f.title("recherche ")
    f.geometry("600x100")
    f['bg']="#A0A0A0"
    
    a=Label(f,text="type the job offer ID, domain (computer science, business…) or location:",fg="black",bg="#A0A0A0")
    a.pack()
    a.config(font=("Courier", 10))
    fr=Frame(f,bg="#F8F8FF",borderwidth=2,relief=RAISED)
    fr.pack()
    global element
    global i
    i=0
    element=StringVar()
    element=Entry(fr,bg='#FFFAFA')
    element.pack()
    Button(fr,text="ENTER",command=resultat).pack()
    Button(fr,text="quitter",command=f.destroy).pack()
    f.mainloop()
def resultat():
    f=open("jobs.txt","r")
    global p
    p=[]
    for a in f:
       if element.get() in a:
          p.append(a)
    f.close()
    global t
    t=Tk()
    t.title("recherche ")
    t.geometry("600x700")
    t['bg']="#A0A0A0"
    global q
    q=["job ID: ","company information: name: ","                     adresse: ","                     phone num: ","                     email: ","                     domain: ","profile description: degree: ","                     qualification: ","                     experience: ","                     adresse: "]
    r=""
    j=0
    l=[]
    s=str(p[i])
    for x in s:
        if s[j]!=";":
            r=r+s[j]
        else:
            l.append(r)
            r=""
        j=j+1
    nb=0
    for b in l :
         cn=q[nb]+l[nb]
         global ab
         ab=Label(t,text=cn,fg="black",bg="#A0A0A0")
         ab.pack()
         ab.config(font=("Courier", 10))
         nb+=1
    global v
    v=l[0]
    Button(t,text="back",command=backbutton).pack()
    Button(t,text="next",command=nextbutton).pack()
    Button(t,text="previous",command=prevbutton).pack()
    Button(t,text="apply",command=applybutton).pack()
    Button(t,text="update",command=updatebutton).pack()
    t.mainloop()
def nextbutton() :
    global i
    global t
    for w in t.winfo_children():
        w.destroy()
    if i < (len(p)-1):
        i+=1
    else:
        i=(len(p)-1)
        
    r=""
    j=0
    l=[]
    s=str(p[i])
    for x in s:
        if s[j]!=";":
            r=r+s[j]
        else:
            l.append(r)
            r=""
        j=j+1
    nb=0
    for b in l :
         cn=q[nb]+l[nb]
         ab=Label(t,text=cn,fg="black",bg="#A0A0A0")
         ab.pack()
         ab.config(font=("Courier", 10))
         nb+=1
    global v
    v=l[0]  
    Button(t,text="back",command=backbutton).pack()
    Button(t,text="next",command=nextbutton).pack()
    Button(t,text="previous",command=prevbutton).pack()
    Button(t,text="apply",command=applybutton).pack()
    Button(t,text="update",command=updatebutton).pack()
    t.mainloop()
def prevbutton() :
    global i
    global t
    for w in t.winfo_children():
        w.destroy()
    if i > 0:
        i-=1
    else:
        i=0
        
    r=""
    j=0
    l=[]
    s=str(p[i])
    for x in s:
        if s[j]!=";":
            r=r+s[j]
        else:
            l.append(r)
            r=""
        j=j+1
    nb=0
    for b in l :
         cn=q[nb]+l[nb]
         ab=Label(t,text=cn,fg="black",bg="#A0A0A0")
         ab.pack()
         ab.config(font=("Courier", 10))
         nb+=1
    global v
    v=l[0]
    Button(t,text="back",command=backbutton).pack()
    Button(t,text="next",command=nextbutton).pack()
    Button(t,text="previous",command=prevbutton).pack()
    Button(t,text="apply",command=applybutton).pack()
    Button(t,text="update",command=updatebutton).pack()
    t.mainloop()
def backbutton() :
    global i
    global t
    i=0
    global p
    p=[]
    t.destroy()
    t.mainloop()
    
def saveapply():
    global v
    c=[v,aa.get(),ab.get(),ac.get(),ad.get(),ba.get(),bb.get(),ca.get(),cb.get()]
    k=open("apply.txt","a")
    for i in c:
       k.write(i+";")
    k.write("\n")
    global page
    showinfo('Résultat','information applied.\nAu revoir !')
    page.destroy()

def applybutton():

    global page
    page=Tk()
    page.title("apply")
    page.geometry("250x500")
    page['bg']="#A0A0A0"
    
    a=Label(page,text="apply for a job:",fg="black",bg="#A0A0A0")
    a.pack()
    a.config(font=("Courier", 10))
    
    fr=Frame(page,bg="#F8F8FF",borderwidth=2,relief=RAISED)
    fr.pack()
    g=Label(fr,text="Personnel information",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    g=Label(fr,text="ID card",bg="#F8F8FF").pack()
    global aa
    aa=StringVar()
    aa=Entry(fr,bg='#FFFAFA')
    aa.pack()
    g=Label(fr,text="name",bg="#F8F8FF").pack()
    global ab
    ab=StringVar()
    ab=Entry(fr,bg='#FFFAFA')
    ab.pack()
    g=Label(fr,text="address",bg="#F8F8FF").pack()
    global ac
    ac=StringVar()
    ac=Entry(fr,bg='#FFFAFA')
    ac.pack()
    g=Label(fr,text="phone number",bg="#F8F8FF").pack()
    global ad
    ad=StringVar()
    ad=Entry(fr,bg='#FFFAFA')
    ad.pack()
    g=Label(fr,text="education",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    g=Label(fr,text="university degree",bg="#F8F8FF").pack()
    global ba
    ba=StringVar()
    ba=Entry(fr,bg='#FFFAFA')
    ba.pack()
    g=Label(fr,text="others",bg="#F8F8FF").pack()
    global bb
    bb=StringVar()
    bb=Entry(fr,bg='#FFFAFA')
    bb.pack()
    g=Label(fr,text="Professional information",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    g=Label(fr,text="experience",bg="#F8F8FF").pack()
    global ca
    ca=StringVar()
    ca=Entry(fr,bg='#FFFAFA')
    ca.pack()
    g=Label(fr,text="skills",bg="#F8F8FF").pack()
    global cb
    cb=StringVar()
    cb=Entry(fr,bg='#FFFAFA')
    cb.pack()
    Button(fr,text="ENTER",command=saveapply).pack()
    page.mainloop()
def updatebutton() :
    ft=Tk()
    ft.title("The list ")
    ft.geometry("300x120")
    ft['bg']="#3e5462"
    a=Label(ft,text="if you are seeking for a job:",fg="yellow",bg="#3e5462")
    a.pack()
    a.config(font=("Courier", 10))
    fr=Frame(ft,bg="#3e5462",borderwidth=5,relief=RAISED)
    fr.pack()
    Label(fr,text="your id card",fg="white",bg="#3e5462").pack(side="left")
    global user
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()

    BoutonQuitter = Button(ft, text ='Quitter', command = ft.destroy )
    BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)
    Texte = StringVar()

    BoutonNext = Button(ft, text ='Next', command = check )
    BoutonNext.pack(side = LEFT, padx = 5, pady = 5)
    Texte = StringVar() 
     
    ft.mainloop()
def check() :
    global v
    y=open("apply.txt","r")
    gh=False
    for o in y:
       
       if user.get() in o and v in o :
           s=o
           gh= True
           

    if gh==True :
            j=0
            r=""
            global ln
            ln=[]
            for x in s:
              if s[j]!=";":
                r=r+s[j]
              else:
                ln.append(r)
                r=""
              j=j+1
            
            f = open("apply.txt","r")

            lines = f.readlines()

            f.close()


            f = open("apply.txt","w")

            for line in lines:
             if line!=s:
              f.write(line+"\n")

            f.close()
            ln.pop(0)
            checkbutton()

        
    else:
           showinfo('Résultat','information not applied.\nAu revoir !')        
    y.close()
    
def checkbutton() :
    global page
    page=Tk()
    page.title("apply")
    page.geometry("250x500")
    page['bg']="#A0A0A0"
    
    a=Label(page,text="apply for a job:",fg="black",bg="#A0A0A0")
    a.pack()
    a.config(font=("Courier", 10))
    
    fr=Frame(page,bg="#F8F8FF",borderwidth=2,relief=RAISED)
    fr.pack()
    g=Label(fr,text="Personnel information",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    g=Label(fr,text="ID card",bg="#F8F8FF").pack()
    global aa
    aa=StringVar()
    aa=Entry(fr,bg='#FFFAFA')
    aa.pack()
    aa.insert(0, ln[0])
    g=Label(fr,text="name",bg="#F8F8FF").pack()
    global ab
    ab=StringVar()
    ab=Entry(fr,bg='#FFFAFA')
    ab.pack()
    ab.insert(0, ln[1])
    g=Label(fr,text="address",bg="#F8F8FF").pack()
    global ac
    ac=StringVar()
    ac=Entry(fr,bg='#FFFAFA')
    ac.pack()
    ac.insert(0, ln[2])
    g=Label(fr,text="phone number",bg="#F8F8FF").pack()
    global ad
    ad=StringVar()
    ad=Entry(fr,bg='#FFFAFA')
    ad.pack()
    ad.insert(0, ln[3])
    g=Label(fr,text="education",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    g=Label(fr,text="university degree",bg="#F8F8FF").pack()
    global ba
    ba=StringVar()
    ba=Entry(fr,bg='#FFFAFA')
    ba.pack()
    ba.insert(0, ln[4])
    g=Label(fr,text="others",bg="#F8F8FF").pack()
    global bb
    bb=StringVar()
    bb=Entry(fr,bg='#FFFAFA')
    bb.pack()
    bb.insert(0, ln[5])
    g=Label(fr,text="Professional information",bg="#F8F8FF",font = "Helvetica 16 bold italic").pack()
    g=Label(fr,text="experience",bg="#F8F8FF").pack()
    global ca
    ca=StringVar()
    ca=Entry(fr,bg='#FFFAFA')
    ca.pack()
    ca.insert(0, ln[6])
    g=Label(fr,text="skills",bg="#F8F8FF").pack()
    global cb
    cb=StringVar()
    cb=Entry(fr,bg='#FFFAFA')
    cb.pack()
    cb.insert(0, ln[7])
    Button(fr,text="ENTER",command=saveapply).pack()
    page.mainloop()
    ##3afsus 
def admin_login_success():
    admin_form()

def seeker_login_success():
    seeker_form()


def incorrect_password():
    ip = tk.Label(screen2, text = "Incorrect password!", fg = "red", font = ("Calibri", 11))
    ip.pack()
    screen2.after(1500, ip.destroy)


def user_not_found():
    unf = tk.Label(screen2, text = "User not found!", fg = "red", font = ("Calibri", 11))
    unf.pack()
    screen2.after(1500, unf.destroy)

   
    
def register_form():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x300")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter details below to register", font = ("Calibri", 17)).pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username *").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password *").pack()
    password_entry = Entry(screen1, textvariable = password, show="*")
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register admin", width = 10, height = 1, command = register_admin).pack()
    Button(screen1, text = "Register seeker", width = 10, height = 1, command = register_seeker).pack()
    Button(screen1, text = "Back", command =lambda : back(screen1)).pack()
    
    
def login_form():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x300")
    Label(screen2, text = "Please enter details below to log in", font = ("Calibri", 17)).pack()
    Label(screen2, text = "").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text = "Username *").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "Password *").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify, show = "*")
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Admin login", width = 10, height = 1, command = admin_login_verify).pack()
    Button(screen2, text = "Seeker login", width = 10, height = 1, command = seeker_login_verify).pack()
    Button(screen2, text = "Back", command =lambda : back(screen2)).pack()
   
        
    
    
def register_admin():

    username_info = username.get()
    password_info = password.get()

    file=open("admin", "a")
    I=[username_info," ",password_info,"\n"]
    file.writelines(I)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    saved(screen1, "Admin registration Successful")
    
def register_seeker():

    username_info = username.get()
    password_info = password.get()

    file=open("seeker", "a")
    I=[username_info," ",password_info,"\n"]
    file.writelines(I)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    saved(screen1, "Seeker registration Successful") 
    
    
##registration of admin   and verification if he wants to login  
    
def admin_login_verify():
    global username_verify
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    file1 = open("admin", "r")
    line = file1.readline()
    j=0
    k=0
    while line and (j != 2):
        j=0
        if username1 in line:
          j=1
        if password1 in line:
          j+=1
        line = file1.readline()
        k=max(j,k)
    if j==2 :
        admin_login_success()

    elif k==1 :
        incorrect_password()

    else:
        user_not_found()
    global screen2

 


##registration of seeker  and verification if he wants to login  

    
    
def seeker_login_verify():
    global username_verify
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    file1 = open("seeker", "r")
    line = file1.readline()
    j=0
    k=0
    while line and (j != 2):
        j=0
        if username1 in line:
          j=1
        if password1 in line:
          j+=1
        line = file1.readline()
        k=max(j,k)
    if j==2 :
        seeker_login_success()

    elif k==1 :
        incorrect_password()

    else:
        user_not_found()


def main_screen():
    global screen
    screen = Tk()
    screen.title ("Job offers")
    screen.geometry ("300x250")
    
    Label(text = "Select your choice ", width="300", height ="2", font = ("Calibri", 30)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login_form).pack()
    Label(text="").pack()
    Button(text= "Register", height = "2", width = "30", command = register_form).pack()
    Label(text="").pack()
    

    screen.mainloop()
main_screen()




