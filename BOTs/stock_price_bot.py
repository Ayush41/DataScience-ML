import tkinter as tk
from tkinter import messagebox
import yfinance as yf


def get_stock_price():
    stock_symbol = symbol_entry.get()

    if not stock_symbol:
        messagebox.showwarning("Input Error","Please enter a stock symbol")
        return
    
    try:
        #fetching stock data from yfinance
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.history(period = "1d")

        # Checking Data Availability
        if stock_info.empty:
            # messagebox.showerror(""Error", "Could not retrieve stock data. Please check the symbol.")")
            messagebox.showerror("Error", "Could not retrieve stock data. Please check the symbol.")

            return
        
        # Getting latest stock price
        stock_price = stock_info['Close'].iloc[0]

        # Updating the label with stock price
        # price_label.config(text=f""Current price of {stock_symbol.upper()} is ${stock_price:.f}")
        price_label.config(text=f"Current price of {stock_symbol.upper()} is ${stock_price:.2f}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


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