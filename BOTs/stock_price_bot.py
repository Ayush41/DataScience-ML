import tkinter as tk
from tkinter import messagebox
import yfinance as yf


def get_stock_price():
    return 2+2


root = tk.Tk()
root.title("Stock Price Checker")
root.geometry("400x350")


# Stock SYmbol Entry Feild
symbol_label = tk.Label(root,text = "Enter Stock Symbol(eg.,GOOG,AMZN) :")
symbol_label.pack(pady=10)

symbol_entry = tk.Entry(root,width=30)
symbol_entry.pack(pady=5)

#Btn to fetch stock price

get_price_btn = tk.Button(root, text="Get Stock Price", command=get_stock_price)
get_price_btn.pack(pady=20)

# Stock price label
price_label = tk.Label(root, text="",font=("Helvetica",12),justify="left")
price_label.pack(pady=10)

root.mainloop()