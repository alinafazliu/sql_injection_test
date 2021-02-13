import tkinter as tk
from tkinter import  Label, Button, messagebox
import requests
import penetration as p
import re
import unittest



regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 
        r'(?::\d+)?' 
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def give_result(url):
    if p.scan_sql_injection(url):
        return 'The website is vulnerable'
    else:
        return 'The website is safe'

def check_injection():
   if verify_url(url.get()):
    messagebox.showinfo("Results",give_result(url.get()))
   else:
    messagebox.showerror("Results","You have inputed an invalid url") 

def verify_url(url):
    return re.match(regex,url) is not None

master = tk.Tk()
master.title("Sql injector checker")
master.configure(bg='#001f3f')
master.geometry('500x350')
url = tk.StringVar(master)
tk.Label(master,fg="#489af6",bg="#001f3f", font=(None, 13), text="Give Url below to check if website can be injected:").grid(row=0,column=1,padx=(20,0),pady=(100,0))
e1 = tk.Entry(master, width= 50, textvariable=url)
e1.grid(row=1, column=1,padx=(20,0), pady=(10, 0))
tk.Button(master,fg="#489af6",bg="#001f3f", font=(None, 13), text ="Check",command=check_injection).grid(row=2,column=1,padx=(30,0),pady=(15,0))


master.mainloop()
