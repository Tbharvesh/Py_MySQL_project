import mysql.connector as sqltor
import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

mycon=sqltor.connect(host='localhost',username='root',password='Tab04082003@',database='project1')
if mycon.is_connected():
    print("successfully connected to the database")
else:
    print("Error connecting to MySQL Database")
cur=mycon.cursor()

choice=None
ch='Y'

def insert_record():
    def submit():
        cid = int(cid_entry.get())
        cname = cname_entry.get()
        phn = phn_entry.get()
        email = email_entry.get()
        age = int(age_entry.get())
        room_no = int(room_no_entry.get())
        room_type = room_type_entry.get()
        check_in = check_in_entry.get()
        check_out = check_out_entry.get()
        cost = cost_entry.get()

        try:
            mycon = sqltor.connect(host='localhost', username='root', password='Tab04082003@', database='project1')
            if mycon.is_connected():
                print("Successfully connected to the database")
                cur = mycon.cursor()
                st = "INSERT INTO customer (cid, cname, phn, email, age) VALUES ({},'{}','{}','{}',{})".format(cid, cname, phn, email, age)
                cur.execute(st)
                mycon.commit()
                cur.close()
                mycon.close()
                messagebox.showinfo("Success", "Record inserted successfully.")
            else:
                print("Error connecting to MySQL Database")
        except Exception as e:
            print("Error:", e)
            messagebox.showerror("Error", "An error occurred while inserting the record.")

    # Tkinter GUI window
    root = tk.Tk()
    root.title("Insert Customer Record")
    window_width = 400
    window_height = 600
    root.geometry(f"{window_width}x{window_height}")

   
    cid_label = tk.Label(root, text="CID:")
    cid_label.pack()
    cid_entry = tk.Entry(root)
    cid_entry.pack()

    cname_label = tk.Label(root, text="Customer Name:")
    cname_label.pack()
    cname_entry = tk.Entry(root)
    cname_entry.pack()

    phn_label = tk.Label(root, text="Phone No.:")
    phn_label.pack()
    phn_entry = tk.Entry(root)
    phn_entry.pack()

    email_label = tk.Label(root, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(root)
    email_entry.pack()

    age_label = tk.Label(root, text="Age:")
    age_label.pack()
    age_entry = tk.Entry(root)
    age_entry.pack()

    room_no_label = tk.Label(root, text="Room No.:")
    room_no_label.pack()
    room_no_entry = tk.Entry(root)
    room_no_entry.pack()

    room_type_label = tk.Label(root, text="Room Type:")
    room_type_label.pack()
    room_type_entry = tk.Entry(root)
    room_type_entry.pack()

    check_in_label = tk.Label(root, text="Check-in Date:")
    check_in_label.pack()
    check_in_entry = tk.Entry(root)
    check_in_entry.pack()

    check_out_label = tk.Label(root, text="Check-out Date:")
    check_out_label.pack()
    check_out_entry = tk.Entry(root)
    check_out_entry.pack()

    cost_label = tk.Label(root, text="Cost:")
    cost_label.pack()
    cost_entry = tk.Entry(root)
    cost_entry.pack()

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack()




def display_records():
    def fetch_records():
        try:
            mycon = sqltor.connect(host='localhost', username='root', password='Tab04082003@', database='project1')
            if mycon.is_connected():
                print("Successfully connected to the database")
                cur = mycon.cursor()
                cur.execute("SELECT * FROM customer, booking_details WHERE customer.cid = booking_details.cid")
                data = cur.fetchall()
                for row in data:
                    tree.insert("", "end", values=row)
                cur.close()
                mycon.close()
            else:
                print("Error connecting to MySQL Database")
        except Exception as e:
            print("Error:", e)
            messagebox.showerror("Error", "An error occurred while fetching records.")

    # Tkinter GUI window
    root = tk.Tk()
    root.title("Display Customer and Booking Details")
    

    
    tree = ttk.Treeview(root, columns=("cid", "cname", "phn", "email", "age", "Room_No", "Room_Type", "check_in", "check_out", "cost"), show="headings")
    tree.heading("cid", text="CID")
    tree.heading("cname", text="Customer Name")
    tree.heading("phn", text="Phone No.")
    tree.heading("email", text="Email")
    tree.heading("age", text="Age")
    tree.heading("Room_No", text="Room No.")
    tree.heading("Room_Type", text="Room Type")
    tree.heading("check_in", text="Check-in Date")
    tree.heading("check_out", text="Check-out Date")
    tree.heading("cost", text="Cost")
    tree.pack()

    fetch_button = tk.Button(root, text="Fetch Records", command=fetch_records)
    fetch_button.pack()


def update_records():
    pass

# main window
root = tk.Tk()
root.title("Hotel Management System")
# heading_label = tkinter.Label(root, text="Hotel Management System", font=("Helvetica", 16, "bold"))
# heading_label.pack(pady=20)
# buttons
insert_button = tk.Button(root, text="Insert Record", command=insert_record)
display_button = tk.Button(root, text="Display Records", command=display_records)
update_button = tk.Button(root,text="Update Records",command=update_records)
exit_button = tk.Button(root, text="Exit", command=root.quit)

empty_columns = 2


insert_button.grid(row=3, column=empty_columns, padx=30, pady=50)
display_button.grid(row=3, column=empty_columns + 1, padx=30, pady=50)
exit_button.grid(row=3, column=empty_columns + 2, padx=30, pady=50)


window_width = 400
window_height = 100
root.geometry(f"{window_width}x{window_height}")

# Start the GUI
root.mainloop()

