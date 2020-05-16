import os
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 

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
  
def save():

    ###check if job_id exists
    job_id = row_job_id.get()
    offers = os.listdir("offers")
    if(job_id in offers):
        failed( screen7, "offer already exists")

    else:
        company_name = row_company_name.get()
        profile_description = row_profile_description.get()
        mission_description = row_mission_description.get()
        data = open("offers/"+job_id, "w")
        data.write(job_id+"\n")
        data.write(company_name+"\n")
        data.write(profile_description+"\n")
        data.write(mission_description+"\n")
        data.close()

        saved(screen7,  "offer created successfuly")

def Addnewjoboffer():
    global row_job_id
    global row_company_name
    global row_profile_description
    global row_mission_description
    global screen7
    row_job_id= StringVar()
    row_company_name= StringVar()
    row_profile_description= StringVar()
    row_mission_description= StringVar()

    screen7 = Toplevel(screen)
    screen7.title("Info")
    screen7.geometry("500x500")
    Label(screen7, text = "Please enter  a code for the job offer: Job ID (should be unique)").pack()
    Entry(screen7, textvariable = row_job_id).pack()
    Label(screen7, text = "Please enter Company name:").pack()
    Entry(screen7, textvariable = row_company_name).pack()
    Label(screen7, text = "Please enter requested profile description").pack()
    Entry(screen7, textvariable = row_profile_description).pack()
    Label(screen7, text = "Please enter mission description").pack()
    Entry(screen7, textvariable = row_mission_description).pack()
    Button (screen7, text = "Save", command = save).pack()
    Button(screen7, text = "Back", command =lambda : back(screen7)).pack()
    
    
def update2():

    # job_id = row_job_id

    company_name = row_company_name.get()
    profile_description = row_profile_description.get()
    mission_description = row_mission_description.get()
    data = open("offers/"+job_id, "w")
    data.write(job_id+"\n")
    data.write(company_name+"\n")
    data.write(profile_description+"\n")
    data.write(mission_description+"\n")
    data.close()

    saved(screen9, "Offer updated")
    
def update1():
    global job_id
    global row_company_name
    global row_profile_description
    global row_mission_description
    global screen9
    row_job_id= StringVar()
    row_company_name= StringVar()
    row_profile_description= StringVar()
    row_mission_description= StringVar()

    offer_option = row_offer_option.get()
    data = open("offers/"+offer_option, "r")
    offer_details = data.read().splitlines()
    screen9 = Toplevel(screen)
    screen9.title("update offer")
    screen9.geometry("500x500")
    # Label(screen9, text = "Please enter  a code for the job offer: Job ID (should be unique)").pack()
    # e1 = Entry(screen9, textvariable = row_job_id, state=DISABLED)
    # e1.pack()
    # e1.insert(0, offer_details[0])
    job_id = offer_details[0]
    Label(screen9, text = "Please enter Company name:").pack()
    e2 = Entry(screen9, textvariable = row_company_name)
    e2.pack()
    e2.insert(0, offer_details[1])
    Label(screen9, text = "Please enter requested profile description").pack()
    e3 = Entry(screen9, textvariable = row_profile_description)
    e3.pack()
    e3.insert(0, offer_details[2])
    Label(screen9, text = "Please enter mission description").pack()
    e4 = Entry(screen9, textvariable = row_mission_description)
    e4.pack()
    e4.insert(0, offer_details[3])
    Button (screen9, text = "update", command = update2).pack()
    Button(screen9, text = "Back", command =lambda : back(screen9)).pack()    
    
    
    
    
def update():
    screen8 = Toplevel(screen)
    screen8.title("update offer")
    screen8.geometry("400x300")
    all_offers = os.listdir("offers")
    Label(screen8, text = "Please choose one of the\noffers id below to udate",font = ("Calibri", 17)).pack()

    #drop down list for existing offers
    offers = os.listdir("offers")
    global row_offer_option
    row_offer_option = StringVar()
    row_offer_option.set(offers[0]) # default value

    list = OptionMenu(screen8, row_offer_option, *offers).pack()

    Button(screen8, text = "OK", command = update1).pack()
    Button(screen8, text = "Back", command =lambda : back(screen8)).pack()
    
    
    
def delete1():
    offer_option3 = raw_offer_option2.get()
    os.remove("offers/"+offer_option3)
    dn1 = tk.Label(screen10, text = "Offer removed successfuly", fg = "green", font = ("Calibri", 11))
    dn1.pack()
    screen10.after(1500, dn1.destroy)


def delete():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("Delete offer(s)")
    screen10.geometry("400x400")

    offers = os.listdir("offers")
    global raw_offer_option2
    Label(screen10, text = "Please choose one of the offers\nid below to delete",font = ("Calibri", 17)).pack()
    raw_offer_option2 = StringVar()
    raw_offer_option2.set(offers[0]) # default value

    list = OptionMenu(screen10, raw_offer_option2, *offers).pack()
    Button(screen10, text = "OK", command = delete1).pack()
    Button(screen10, text = "Back", command =lambda : back(screen10)).pack()



def filter_applications():
    filter  = raw_filter.get()
    #first ditroy all applications
    for widget in screen15.winfo_children():
        # if(widget.winfo_class() == 'Label'):
        widget.destroy()
    #display filtred  applications
    Label(screen15, text = "List of all the applications:\n",font = ("Calibri", 17)).pack()
    Label(screen15, text = "To filter by offer enter id offer \n").pack()
    Entry(screen15, textvariable = raw_filter).pack()
    Button(screen15, text = "filter", command = filter_applications).pack()
    all_app = os.listdir("applications")
    for app in all_app:
        if(filter in app):
            Label(screen15, text = app).pack()
    


def brows():
    global screen15
    screen15 = Toplevel(screen)
    screen15.title("List all applications")
    screen15.geometry("400x400")
    all_app = os.listdir("applications")
    global raw_filter
    global app_lab
    raw_filter = StringVar()

    Label(screen15, text = "List of all the applications:\n",font = ("Calibri", 17)).pack()
    Label(screen15, text = "To filter by offer enter id offer \n").pack()
    Entry(screen15, textvariable = raw_filter).pack()
    Button(screen15, text = "filter", command = filter_applications).pack()
    global app_labs
    app_labs = []
    global i
    i = 0
    for app in all_app:
        app_labs.append( Label(screen15, text = app) )
        app_labs[i].pack()
        i += 1

    Button(screen15, text = "Back", command =lambda : back(screen15)).pack()



def admin_form():
    screen6 = Toplevel(screen)
    screen6.title("admin Dashboard")
    screen6.geometry("400x400")
    Label(screen6, text = "Welcome to the dashboard",font = ("Calibri", 17)).pack()
    Button(screen6, text = "Add new offer", command =Addnewjoboffer).pack()
    Button(screen6, text = "Update offer", command =update).pack()
    Button(screen6, text = "Delete offer", command =delete).pack()
    Button(screen6, text = "Brows all applications", command = brows).pack()
    Button(screen6, text = "Back", command =lambda : back(screen6)).pack()
    
# def seeker_features 
#seekerform
    
    
    
    
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
        admin_login_success()

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




