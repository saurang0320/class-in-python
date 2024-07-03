import tkinter as tk

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone_number = phone_entry.get()
    address = address_entry.get()

    output_text.config(state=tk.NORMAL)  
    output_text.delete(1.0, tk.END)  
    output_text.insert(tk.END, f"Name: {name}\n")
    output_text.insert(tk.END, f"Email: {email}\n")
    output_text.insert(tk.END, f"Phone Number: {phone_number}\n")
    output_text.insert(tk.END, f"Address: {address}\n")
    output_text.config(state=tk.DISABLED)  

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def clear_output():
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.config(state=tk.DISABLED)

def main():
    global name_entry, email_entry, phone_entry, address_entry, output_text
    
    root = tk.Tk()
    root.title("User Information Form")
    
    tk.Label(root, text="Name: ").grid(row=0, column=0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)
    
    tk.Label(root, text="Email: ").grid(row=1, column=0)
    email_entry = tk.Entry(root)
    email_entry.grid(row=1, column=1)
    
    tk.Label(root, text="Phone Number: ").grid(row=2, column=0)
    phone_entry = tk.Entry(root)
    phone_entry.grid(row=2, column=1)
    
    tk.Label(root, text="Address: ").grid(row=3, column=0)
    address_entry = tk.Entry(root)
    address_entry.grid(row=3, column=1)
    
    # Submit Button
    submit_button = tk.Button(root, text="Submit", command=submit_form)
    submit_button.grid(row=4, column=0, columnspan=2)
    
    # Delete Button
    delete_button = tk.Button(root, text="Delete", command=clear_output)
    delete_button.grid(row=6, column=0, columnspan=2)
    
    # Output Text Widget
    output_text = tk.Text(root, height=10, width=40)
    output_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    output_text.config(state=tk.DISABLED)  
    
    root.mainloop()

if __name__ == "__main__":
    main()
