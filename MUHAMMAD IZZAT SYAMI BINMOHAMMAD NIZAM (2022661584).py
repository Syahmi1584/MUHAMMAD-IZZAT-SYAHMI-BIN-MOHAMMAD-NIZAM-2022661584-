import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
database = "Comic Nusantara")


mycursor = mydb.cursor()

root = tk.Tk()
root['bg'] ='#b2beb5'
root.title("Comic Bundle")
root.geometry("700x600")

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 15, 'bold')
font3 = ('Arial', 10, 'bold')
font4 = ('Arial', 10,)

main_label = tk.Label(root, text="WELCOME TO NUSANTARA COMICS !", font = font1, bg="#b2beb5")
main_label.pack()

sec_label = tk.Label(root, text="PICK A SERIES "+"OR BUNDLE THEM !", font = font2, bg="#b2beb5")
sec_label.pack()

frame = tk.Frame(root)
frame.pack()

price_list = [3,10]
total_price = 0

#frame and label
buyer_info_frame = tk.LabelFrame(frame, text="Buyer Information", font = font3, bg="#b2beb5")
buyer_info_frame.grid(row=0, column=0, pady=20)


name_label =tk.Label(buyer_info_frame, text="Name:", bg="#b2beb5", font = font4)
name_label.grid(row=0, column=0, pady=5, sticky="w")

address_label =tk.Label(buyer_info_frame, text="Address:", bg="#b2beb5", font = font4)
address_label.grid(row=0, column=1, sticky="w")

email_label =tk.Label(buyer_info_frame, text="Email:", bg="#b2beb5", font = font4)
email_label.grid(row=0, column=2, sticky="w")

def purchase():
    global total_price
    if (name_entry.get()==""):
        messagebox.showerror(title="Error", message = "Please insert your name")

    elif (address_entry.get()==""):
         messagebox.showerror(title="Error", message = "Please insert your address")
    
    elif (email_entry.get()==""):
        messagebox.showerror(title="Error", message = "Please insert your Email")
    
    else:
        total_price = int(series_quantity_spinbox.get()) * price_list[0] + int(bundle_quantity_spinbox.get()) * price_list[1]
        name_label = tk.Label(purchase_frame, text=f'Name: {name_entry.get()}' )
        name_label.grid(row=0, column=0, pady=20, padx=20)

        total_label = tk.Label(purchase_frame, text=f'Total RM:  {total_price}')
        total_label.grid(row=0, column=1, padx=30)

        purchase_result_label = tk.Label(purchase_frame, text="Thanks For Your Purchase ! ", font= font3, bg="#b2beb5")
        purchase_result_label.grid(row=0, column=2, padx=20)
       
    sql = ("INSERT INTO `buyer information` (Buyer_Name, User_Address, User_Email, Comic_Series, Comic_Volume, Comic_Quantity, Comic_Bundle, Bundle_Quantity, Total_Price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    val = (name_entry.get(), address_entry.get(), email_entry.get(), series_combobox.get(), series_volume_spinbox.get(), series_quantity_spinbox.get(), bundle_combobox.get(), bundle_quantity_spinbox.get(), total_price)

    mycursor.execute(sql, val)
    mydb.commit()

#entry box
name_entry =tk.Entry(buyer_info_frame,)
name_entry.grid(row=1, column=0, padx=10, pady=5)

address_entry =tk.Entry(buyer_info_frame)
address_entry.grid(row=1, column=1, padx=10)

email_entry =tk.Entry(buyer_info_frame)
email_entry.grid(row=1, column=2, padx=10)

for widget in buyer_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)



#series_vol_label
series_frame = tk.LabelFrame(frame, text="Pick a Series, RM3 each", font = font3, bg="#a9a9a9",)
series_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

series_label = tk.Label(series_frame, text="Series", bg="#a9a9a9", font = font4)
series_label.grid(row=0, column=0, pady=10)

volume_label = tk.Label(series_frame, text="Volume", bg="#a9a9a9", font = font4)
volume_label.grid(row=0, column=1)

quantity_label = tk.Label(series_frame, text="Quantity", bg="#a9a9a9", font = font4)
quantity_label.grid(row=0, column=2)

#series entry(combobox and spinbox)
series_value = ["Avatar", 
                "Awang Khenit", 
                "Atomen", 
                "Aspalela", 
                "Aku, Engkau, dan Jamal"]

series = tk.StringVar(root)
series_combobox = ttk.Combobox(series_frame, values=series_value, textvariable=series, state="readonly")
series_combobox.grid(row=1, column=0, padx=10, pady=10)

series_volume_spinbox = tk.Spinbox(series_frame, from_=1, to=5, state="readonly")
series_volume_spinbox.grid(row=1, column=1, padx=10)

series_quantity = tk.IntVar()
series_quantity_spinbox = tk.Spinbox(series_frame, from_=0, to=10, state="readonly")
series_quantity_spinbox.grid(row=1, column=2, padx=10)

for widget in series_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

#bundle label

bundle_frame = tk.LabelFrame(frame, text="Bundle Selection, RM 10 each", font = font3, bg="#b2beb5")
bundle_frame.grid(row=2, column=0,)

bundle_label = tk.Label(bundle_frame, text="Bundle", bg="#b2beb5", font = font4)
bundle_label.grid(row=0, column=0)

quantity_label = tk.Label(bundle_frame, text="Quantity", bg="#b2beb5", font = font4)
quantity_label.grid(row=0, column=1)

#bundle combobox and quntity spinbox
bundle_volume = [
    "Avatar Bundle (1-4)", 
    "Awang Khenit Bundle (1-4)", 
    "Atomen Bundle (1-4)",
    "Aspalela Bundle (1-4)", 
    "Aku, Engkau, dan Jamal Bundle (1-4)"]

bundle = tk.StringVar(root)
bundle_combobox = ttk.Combobox(bundle_frame, values = bundle_volume, textvariable=bundle, state="readonly")
bundle_combobox.grid(row=1, column=0, padx=10, pady=10)

bundle_quantity_spinbox = tk.Spinbox(bundle_frame, from_=0, to=10)
bundle_quantity_spinbox.grid(row=1, column=1, padx=10)

#purchase details
purchase_frame = tk.LabelFrame(frame, text="Purchase Details", font = font3, bg="#b2beb5")
purchase_frame.grid(row=3, column=0, pady=20)

purchase_button = tk.Button(frame, text="PURCHASE", command=purchase)
purchase_button.grid(row=4, column=0, pady=10)


for widget in bundle_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

root.mainloop()