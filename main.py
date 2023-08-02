from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

window = customtkinter.CTk()
window.title("Calculator")

entry_1 = customtkinter.CTkEntry(master=window, width = 400, height = 70,font = ("standard",16) ,placeholder_text="0")
entry_1.grid(row=0, column=1, columnspan = 4,pady=10, padx=10)


def button_click(number):
    entry_1.delete(0, END)
    entry_1.insert(0, number)


def change_appearance_mode_event(values: str):
    customtkinter.set_appearance_mode(values)


appearance_mode_optionemenu = customtkinter.CTkOptionMenu(window, values=["Light", "Dark", "System"],
                                                                       command=change_appearance_mode_event)
appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))



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

button_plus = customtkinter.CTkButton(window, text="+", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click())
button_plus.grid(row=1, column=4, padx=1, pady=2)
button_sub = customtkinter.CTkButton(window, text="-", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click())
button_sub.grid(row=2, column=4, padx=1, pady=2)
button_mul = customtkinter.CTkButton(window, text="x", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click())
button_mul.grid(row=3, column=4, padx=1, pady=2)
button_div = customtkinter.CTkButton(window, text="/", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click())
button_div.grid(row=4, column=4, padx=1, pady=2)

button_equal = customtkinter.CTkButton(window, text="=", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click())
button_equal.grid(row=5, column=4, padx=1, pady=2)
button_dot = customtkinter.CTkButton(window, text=".", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click())
button_dot.grid(row=5, column=3, padx=1, pady=2)
button_clear = customtkinter.CTkButton(window, text="C", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click())
button_clear.grid(row=5, column=2, padx=1, pady=2)
button_remove = customtkinter.CTkButton(window, text="R", width=70, height=70, border_width=0, corner_radius=8, command=lambda: button_click())
button_remove.grid(row=5, column=1, padx=1, pady=2)


window.mainloop()