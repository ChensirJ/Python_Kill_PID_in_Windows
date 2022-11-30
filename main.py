import os
from netstat import *
from tkinter import *
from tkinter.messagebox import *

temp_netstat_list = []
netstat_object_list = []
pid_set = set()

win_width = 400
win_height = 150
title = "Kill Process"

root = Tk()
root.title(title)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width - win_width) / 2)
y = int((screen_height - win_height) / 2)

root.geometry("%sx%s+%s+%s" % (win_width, win_height, x, y))

root.resizable(False, False)

frame = Frame(root)
frame.place(rely=.5, relx=.5, x=-80, y=-40, width=245, height=100)

Label(frame, text="Port").grid(row=0)

port_var = StringVar()
Entry(frame, textvariable=port_var).grid(row=0, column=1, columnspan=2, padx=10)


def kill_process():
    if port_var.get() == "" or port_var.get() is None:
        showerror("Error", "Please input port number!")
        return

    netstat_list = os.popen("netstat -ano | findstr \"" + port_var.get() + "\"").read().split(" ")

    for i in netstat_list:
        if '\n' in i:
            netstat_object_list.append(netstat(temp_netstat_list[0], temp_netstat_list[1], temp_netstat_list[2],
                                               temp_netstat_list[3], str(i).replace("\n", "")))
            pid_set.add(str(i).replace("\n", ""))
        elif i != '':
            temp_netstat_list.append(i)

    for i in netstat_object_list:
        print(i)

    showinfo("Info", os.popen("taskkill /f /pid " + pid_set.pop()).read())


def reset():
    port_var.set("")


Button(frame, text="Confirm", command=kill_process, width=8).grid(row=1, column=1, pady=8)
Button(frame, text="Reset", command=reset, width=8).grid(row=1, column=2, padx=2, pady=8)

root.mainloop()
