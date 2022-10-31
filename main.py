import os
import time

# import PySimpleGUI as sg
#
# sg.theme('DarkAmber')  # Add a touch of color
# # All the stuff inside your window.
# layout = [[sg.Text('Some text on Row 1')],
#           [sg.Text('Хотите ли вы запустить таймер на выключения компьютера ?'), sg.InputText()],
#           [sg.Text('Через сколько минут выключить компьютер ? '), sg.InputText()],
#           [sg.Button('Ok'), sg.Button('Cancel')]]
#
#
# # Create the Window
# window = sg.Window('Sleep timer', layout)
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
#         break
#     print('You entered ', values[0], values[1])
#
# window.close()


shutdown = input("Хотите ли вы запустить таймер на выключения компьютера ?").lower()
if shutdown == "да":
    timer = float(input('Через сколько минут выключить компьютер ? '))
    timer = timer * 60
    time.sleep(timer)
    shutdown_command = "shutdown /s /t 00"
    os.system(shutdown_command)
if shutdown == "нет":
    exit()
