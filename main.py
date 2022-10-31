import os
import time
import tkinter as tk


def shutdown_30_min():
    root.withdraw()
    timer = 1 * 60
    time.sleep(timer)
    shutdown_command = "shutdown /s /t 00"
    os.system(shutdown_command)


def shutdown_60_min():
    root.withdraw()
    timer = 60 * 60
    time.sleep(timer)
    shutdown_command = "shutdown /s /t 00"
    os.system(shutdown_command)


def shutdown_90_min():
    root.withdraw()
    timer = 90 * 60
    time.sleep(timer)
    shutdown_command = "shutdown /s /t 00"
    os.system(shutdown_command)


def shutdown_120_min():
    root.withdraw()
    timer = 120 * 60
    time.sleep(timer)
    shutdown_command = "shutdown /s /t 00"
    os.system(shutdown_command)


root = tk.Tk()
root['bg'] = 'seashell3'
root.title('Таймер выключения компьютера')
root.geometry('430x105+600+200')
root.resizable(width=False, height=False)

tk.Label(text='Через сколько минут выключить компьютер ? ', font=('Consalas', 13, 'bold'), bg='seashell3').pack()
tk.Button(text='30 минут', height=2, width=9, font=('Consalas', 11, 'bold'), relief=tk.GROOVE, bd=6,
          bg='SkyBlue1', command=shutdown_30_min).place(x=15, y=35)
tk.Button(text='60 минут', height=2, width=9, font=('Consalas', 11, 'bold'), relief=tk.GROOVE, bd=6,
          bg='SkyBlue1', command=shutdown_60_min).place(x=115, y=35)
tk.Button(text='90 минут', height=2, width=9, font=('Consalas', 11, 'bold'), relief=tk.GROOVE, bd=6,
          bg='SkyBlue1', command=shutdown_90_min).place(x=215, y=35)
tk.Button(text='120 минут', height=2, width=9, font=('Consalas', 11, 'bold'), relief=tk.GROOVE, bd=6,
          bg='SkyBlue1', command=shutdown_120_min).place(x=315, y=35)

root.mainloop()
