import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hall_booking"
)

mycursor = mydb.cursor()

#Define untuk Message Warning for GUI 1
def show_second_gui():
    # Warning user x masukkan details utk GUI 1
    if not full_name_entry.get() or not email_entry.get():
        messagebox.showwarning("Warning", "Please fill in all the required fields.")
        return

    # Hide GUI 1 untuk masuk GUI 2
    full_name_label.grid_remove()
    full_name_entry.grid_remove()
    email_label.grid_remove()
    email_entry.grid_remove()
    next_button.grid_remove()

    # Grid for GUI2
    from_time_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    from_time_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    until_time_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    until_time_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    calendar_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    calendar_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    event_name_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
    event_name_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    hall_name_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
    hall_name_combobox.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    #button
    submit_button.grid(row=5, column=0, padx=10, pady=10)
    update_button.grid(row=5, column=1, padx=10, pady=10)
    delete_button.grid(row=5, column=2, padx=10, pady=10)


#Define untuk Message Warning for GUI 2
def submit_booking():
    # Warning user x masukkan details utk GUI 2
    if not from_time_combobox.get() or not until_time_combobox.get() or not calendar_entry.get() or not event_name_entry.get() or not hall_name_combobox.get():
        messagebox.showwarning("Warning", "Please fill in all the required fields.")
        return

    # Take data untuk print at terminal
    full_name = full_name_entry.get()
    email = email_entry.get()
    from_time = from_time_combobox.get()
    until_time = until_time_combobox.get()
    calendar_date = calendar_entry.get()
    event_name = event_name_entry.get()
    hall_name = hall_name_combobox.get()

    # Insert hall data dlm database
    insert_hall_sql = "INSERT INTO halls (hall_name) VALUES (%s)"
    insert_hall_val = (hall_name,)

    try:
        mycursor.execute(insert_hall_sql, insert_hall_val)
        mydb.commit()
        messagebox.showinfo("Success", "Hall information has been successfully inserted.")
    except Exception as e:
        messagebox.showerror("Error", f"Error inserting hall data: {e}")

    # Insert booking data dlm database
    insert_booking_sql = "INSERT INTO `booking info` (full_name, email, hall_name, time_from, time_to, date, event_name) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    insert_booking_val = (full_name, email, hall_name, from_time, until_time, calendar_date, event_name)

    try:
        mycursor.execute(insert_booking_sql, insert_booking_val)
        mydb.commit()
        messagebox.showinfo("Success", "Booking information has been successfully inserted.")
    except Exception as e:
        messagebox.showerror("Error", f"Error inserting booking data: {e}")
#update function
def update_booking():
    # Check if required fields are filled
    if not from_time_combobox.get() or not until_time_combobox.get() or not calendar_entry.get() or not event_name_entry.get() or not hall_name_combobox.get():
        messagebox.showwarning("Warning", "Please fill in all the required fields.")
        return

    # Get all the data
    full_name = full_name_entry.get()
    email = email_entry.get()
    from_time = from_time_combobox.get()
    until_time = until_time_combobox.get()
    calendar_date = calendar_entry.get()
    event_name = event_name_entry.get()
    hall_name = hall_name_combobox.get()

    # Update booking information
    update_booking_sql = "UPDATE `booking info` SET full_name = %s, email = %s, hall_name = %s, time_from = %s, time_to = %s, date = %s WHERE event_name = %s"
    update_booking_val = (full_name, email, hall_name, from_time, until_time, calendar_date, event_name)

    try:
        mycursor.execute(update_booking_sql, update_booking_val)
        mydb.commit()
        messagebox.showinfo("Success", "Booking information has been successfully updated.")
    except Exception as e:
        messagebox.showerror("Error", f"Error updating booking data: {e}")

#delete function
def delete_booking():
    # Check if the event name is provided
    if not event_name_entry.get():
        messagebox.showwarning("Warning", "Please provide an Event Name to delete.")
        return

    event_name = event_name_entry.get()

    delete_booking_sql = "DELETE FROM `booking info` WHERE event_name = %s"
    delete_booking_val = (event_name,)

    try:
        mycursor.execute(delete_booking_sql, delete_booking_val)
        mydb.commit()
        messagebox.showinfo("Success", "Booking information has been successfully deleted.")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting booking data: {e}")


##############################################     START MAKING GUI     ##########################################
root = tk.Tk()
root.title("Hall Booking Application")
root.configure(bg="#FFB6C1")
font_label = ("Courier", 12)  
font_button = ("Helvetica", 12, "bold") 


#----------------------------Things in GUI 1----------------------------------------

# Full name
full_name_label = tk.Label(root, text="Full Name:", bg="#FFB6C1", font=font_label)  
full_name_entry = tk.Entry(root)

#email
email_label = tk.Label(root, text="Email:", bg="#FFB6C1", font=font_label)  
email_entry = tk.Entry(root)

#button utk next gui
next_button = tk.Button(root, text="Next", command=show_second_gui, bg="#FF69B4", fg="white", font=font_button)  

#----------------------------Things in GUI 2----------------------------------------

# FROM
from_time_label = tk.Label(root, text="From:", bg="#FFB6C1", font=font_label)  
from_time_combobox = ttk.Combobox(root, values=[f"{i:02d}:00" for i in range(24)], state="readonly")

#TO
until_time_label = tk.Label(root, text="To:", bg="#FFB6C1", font=font_label)  
until_time_combobox = ttk.Combobox(root, values=[f"{i:02d}:00" for i in range(24)], state="readonly")

#DATE (CALENDAR)
calendar_label = tk.Label(root, text="Date:", bg="#FFB6C1", font=font_label)  
calendar_entry = DateEntry(root, date_pattern='dd/mm/yy')

#event name
event_name_label = tk.Label(root, text="Event Name:", bg="#FFB6C1", font=font_label)  
event_name_entry = tk.Entry(root)

#hall name
hall_name_label = tk.Label(root, text="Hall Name:", bg="#FFB6C1", font=font_label)  
hall_name_combobox = ttk.Combobox(root, values=["Dewan Perdana", "Dewan Seri Merbok", "Dewan Seri Jerai", "Dewan Sarjana 1", "Dewan Sarjana 2"], state="readonly")

#buttons (submit, update, delete)
submit_button = tk.Button(root, text="Submit", command=submit_booking, bg="#FF69B4", fg="white", font=font_button)  
update_button = tk.Button(root, text="Update", command=update_booking, bg="#FF69B4", fg="white", font=font_button)  
delete_button = tk.Button(root, text="Delete", command=delete_booking, bg="#FF69B4", fg="white", font=font_button)  

# Grid utk GUI 1
full_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
full_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Grid email
email_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
email_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Grid Button
next_button.grid(row=2, columnspan=2, pady=10)

root.mainloop()