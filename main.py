from tkinter import *
import customtkinter
from customtkinter import ThemeManager

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

window = customtkinter.CTk()
window.title("Calculator")

entry_1 = customtkinter.CTkEntry(master=window, width = 400, height = 70,font = ("standard",16) ,placeholder_text="0")
entry_1.grid(row=0, column=1, columnspan = 4,pady=10, padx=10)


def button_click(number):
    current = entry_1.get()
    entry_1.delete(0, END)
    entry_1.insert(0, str(current) +str(number))

def button_clear():
    entry_1.delete(0,END)

def button_add():
    first_number = entry_1.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry_1.delete(0,END)

def button_sub():
    first_number = entry_1.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry_1.delete(0,END)

def button_mul():
    first_number = entry_1.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry_1.delete(0,END)

def button_div():
    first_number = entry_1.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry_1.delete(0,END)

def button_equal():
        second_number = entry_1.get()
        entry_1.delete(0,END)
        
        if math == "addition":
            entry_1.insert(0, f_num + float(second_number))
        elif math == "subtraction":
            entry_1.insert(0, f_num - float(second_number))
        elif math == "multiplication":
            entry_1.insert(0, f_num * float(second_number))
        elif math == "division":
            entry_1.insert(0, f_num / float(second_number))
    

def change_appearance_mode_event(values: str):
    customtkinter.set_appearance_mode(values)

def set_default_color_theme(values: str):
    """ set color theme or load custom theme file by passing the path """
    ThemeManager.load_theme(values)


appearance_mode_optionemenu = customtkinter.CTkOptionMenu(window, width=20, height=50, corner_radius=8, values=["Light", "Dark", "System"],
                                                                       command=change_appearance_mode_event)
appearance_mode_optionemenu.grid(row=0, column=0, padx=1, pady=2)

set_default_color_theme_optionmenu = customtkinter.CTkOptionMenu(window, width=20, height=50, corner_radius=8, values=["blue", "dark-blue", "green"],
                                                                       command=set_default_color_theme)
set_default_color_theme_optionmenu.grid(row=1, column=0, padx=1, pady=2)



button_1 = customtkinter.CTkButton(window, text="1",  width=70, height=70, border_width=0, corner_radius=8,command=lambda: button_click(1))
button_1.grid(row=3, column=1, padx=1, pady=2)
button_2 = customtkinter.CTkButton(window, text="2",  width=70, height=70, border_width=0, corner_radius=8,command=lambda: button_click(2))
button_2.grid(row=3, column=2, padx=1, pady=2)
button_3 = customtkinter.CTkButton(window, text="3",  width=70, height=70, border_width=0, corner_radius=8,command=lambda: button_click(3))
button_3.grid(row=3, column=3, padx=1, pady=2)

button_4 = customtkinter.CTkButton(window, text="4",  width=70, height=70, border_width=0, corner_radius=8,command=lambda: button_click(4))
button_4.grid(row=2, column=1, padx=1, pady=2)
button_5 = customtkinter.CTkButton(window, text="5",  width=70, height=70, border_width=0, corner_radius=8,command=lambda: button_click(5))
button_5.grid(row=2, column=2, padx=1, pady=2)
button_6 = customtkinter.CTkButton(window, text="6",  width=70, height=70, border_width=0, corner_radius=8,command=lambda: button_click(6))
button_6.grid(row=2, column=3, padx=1, pady=2)

button_7 = customtkinter.CTkButton(window, text="7", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click(7))
button_7.grid(row=1, column=1, padx=1, pady=2)
button_8 = customtkinter.CTkButton(window, text="8",  width=70, height=70, border_width=0, corner_radius=8,command=lambda: button_click(8))
button_8.grid(row=1, column=2, padx=1, pady=2)
button_9 = customtkinter.CTkButton(window, text="9", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click(9))
button_9.grid(row=1, column=3, padx=1, pady=2)

button_0 = customtkinter.CTkButton(window, text="0",  width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click(0))
button_0.grid(row=4, column=2, padx=1, pady=2)
button_brac1 = customtkinter.CTkButton(window, text="(",  width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click('('))
button_brac1.grid(row=4, column=1, padx=1, pady=2)
button_brac2 = customtkinter.CTkButton(window, text=")", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click(')'))
button_brac2.grid(row=4, column=3, padx=1, pady=2)

button_plus = customtkinter.CTkButton(window, text="+", width=70, height=70, border_width=0, corner_radius=8, command=lambda:  button_add())# [button_click('+'), button_add()])
button_plus.grid(row=1, column=4, padx=1, pady=2)
button_subt = customtkinter.CTkButton(window, text="-", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_sub())#[button_click('-'), button_sub()])
button_subt.grid(row=2, column=4, padx=1, pady=2)
button_mult = customtkinter.CTkButton(window, text="x", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_mul())#[button_click('x'), button_mul()])
button_mult.grid(row=3, column=4, padx=1, pady=2)
button_divd = customtkinter.CTkButton(window, text="/", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_div())#[button_click('/'), button_div()])
button_divd.grid(row=4, column=4, padx=1, pady=2)

button_equal1 = customtkinter.CTkButton(window, text="=", width=70, height=70, border_width=0, corner_radius=8, command=button_equal)
button_equal1.grid(row=5, column=4, padx=1, pady=2)
button_dot = customtkinter.CTkButton(window, text=".", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click('.'))
button_dot.grid(row=5, column=3, padx=1, pady=2)
button_clear1 = customtkinter.CTkButton(window, text="C", width=70, height=70, border_width=0, corner_radius=8, command=button_clear)
button_clear1.grid(row=5, column=2, padx=1, pady=2)
button_remove1 = customtkinter.CTkButton(window, text="R", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click())
button_remove1.grid(row=5, column=1, padx=1, pady=2)


window.mainloop()
