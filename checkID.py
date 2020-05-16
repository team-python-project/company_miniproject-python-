from tkinter import *
u=StringVar()
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
    
