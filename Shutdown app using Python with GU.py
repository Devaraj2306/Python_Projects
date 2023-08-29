#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import tkinter as tk
from tkinter import Button

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")

sut = tk.Tk()
sut.title("Shutdown")
sut.geometry("300x310")
sut.configure(bg="black")

r_button = Button(sut, text="Restart", font=("Times New Roman", 20, "bold"), relief=tk.RAISED, cursor="plus", command=restart)
r_button.place(x=80, y=35, height=50, width=150)

rt_button = Button(sut, text="Restart Time", font=("Times New Roman", 15, "bold"), relief=tk.RAISED, cursor="plus", command=restart_time)
rt_button.place(x=80, y=100, height=50, width=150)

rg_button = Button(sut, text="Log Out", font=("Times New Roman", 15, "bold"), relief=tk.RAISED, cursor="plus", command=logout)
rg_button.place(x=80, y=165, height=50, width=150)

st_button = Button(sut, text="Shut Down", font=("Times New Roman", 15, "bold"), relief=tk.RAISED, cursor="plus", command=shutdown)
st_button.place(x=80, y=230, height=50, width=150)

sut.mainloop()


# In[ ]:




