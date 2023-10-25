# Projeto Final: Conclusão da Trilha de Desenvolvimento Web
# Projeto 4: Conversor de Moedas com Validação de Dados
# Discente: Airton Crisma Loureiro dos Santos



import customtkinter
from tkinter import *
from currency_converter import ECB_URL, SINGLE_DAY_ECB_URL
from currency_converter import CurrencyConverter
from forex_python.converter import CurrencyRates
from os import system
import requests
import json
from colorama import init, Fore, Back, Style


app = customtkinter.CTk()
app.config(bg="#202630")
app.geometry("400x450")
app.title("Conversor de Moedas")

head_label=customtkinter.CTkLabel(app, text="CONVERSOR DE MOEDAS", font=('Arial',20,'bold'),fg_color="#202630", text_color="#08b7f8",width=1)
head_label.place(x=90,y=40)

from_label=customtkinter.CTkLabel(app, text="Da Moeda", font=('Arial',15,'bold'),fg_color="#202630", text_color="#11f481",width=1)
from_label.place(x=10,y=150)

to_label=customtkinter.CTkLabel(app, text="Para Moeda", font=('Arial',15,'bold'),fg_color="#202630", text_color="#11f381",width=1)
to_label.place(x=248,y=150)


currency_list=["BRL","USD","INR","GBP","KYD","EUR","CHF","BND","CAD","AUD","LYD","SGD","NZD","ILS","TRY","JPY"]

Variable1=StringVar()
variable2=StringVar()
txt=StringVar()

def convert():
    from_currency=Variable1.get()
    to_currency=variable2.get()
    c = CurrencyConverter(ECB_URL)
    #c = CurrencyConverter(SINGLE_DAY_ECB_URL)
    #c=CurrencyRates
    amt = c.convert(float(amount_entry.get()),from_currency,to_currency)
    amount=float("{:.3f}".format(amt))
    txt.set(amount)
    result_label=customtkinter.CTkLabel(app,textvariable=txt,font=('Arial',30,'bold'),fg_color="#202630",text_color="#FFFFFF",width=50)
    result_label.place(x=130,y=350)

def reset():
    amount_entry.delete(0,END)


from_menu=customtkinter.CTkComboBox(app,variable=Variable1,values=currency_list, font=('Arial',12,'bold'),dropdown_font=('Arial',12,'bold'),fg_color="#FFFFFF",text_color="#c813c2",button_color="#1f78b4",button_hover_color="#00ff00",border_color="#FFFFFF",dropdown_fg_color="#FFFFFF",dropdown_hover_color="#00FF00",dropdown_text_color="#000000")
from_menu.place(x=10,y=180)

to_menu=customtkinter.CTkComboBox(app,variable=variable2,values=currency_list, font=('Arial',12,'bold'),dropdown_font=('Arial',12,'bold'),fg_color="#FFFFFF",text_color="#c813c2",button_color="#1f78b4",button_hover_color="#00ff00",border_color="#FFFFFF",dropdown_fg_color="#FFFFFF",dropdown_hover_color="#00FF00",dropdown_text_color="#000000")
to_menu.place(x=250,y=180)


amount_entry=customtkinter.CTkEntry(app,font=('Arial',20,'bold'),text_color="#c813c2",justify=CENTER,width=370,fg_color="#FFFFFF",border_color="#FFFFFF")
amount_entry.place(x=18,y=240)


convert_button=customtkinter.CTkButton(app,command=convert,text="Converter",font=('Arial',20,'bold'),text_color="#FFFFFF",fg_color="#00d700",hover_color="#44ff1f")
convert_button.place(x=50,y=300)

reset_button=customtkinter.CTkButton(app,command=reset,text="Limpar",font=('Arial',20,'bold'),text_color="#FFFFFF",fg_color="#eade00",hover_color="#ecf000")
reset_button.place(x=200,y=300)




app.mainloop()


