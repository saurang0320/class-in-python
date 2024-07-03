import tkinter as tk

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone_number = phone_entry.get()
    address = address_entry.get()
    
    # Format user details
    user_details = f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\nAddress: {address}\n\n"
    
    # Insert user details into the text widget
    output_text.insert(tk.END, user_details)
    
    # Clear input fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def clear_output():
    # Clear all text in the text widget
    output_text.delete(1.0, tk.END)

def edit_selected():
    # Get the selected text from the text widget
    selected_text = output_text.get(tk.SEL_FIRST, tk.SEL_LAST)
    
    # Extract the user details from selected text
    details = selected_text.strip().split("\n")
    edited_details = []
    
    # Iterate through each detail to edit
    for detail in details:
        field, value = detail.split(": ", 1)
        new_value = tk.simpledialog.askstring("Edit", f"Enter new value for {field}", initialvalue=value)
        if new_value is not None:
            edited_details.append(f"{field}: {new_value}")
        else:
            edited_details.append(f"{field}: {value}")
    
    # Join edited details into a formatted string
    edited_user_details = "\n".join(edited_details) + "\n\n"
    
    # Insert edited user details back into the text widget
    output_text.delete(tk.SEL_FIRST, tk.SEL_LAST)
    output_text.insert(tk.SEL_FIRST, edited_user_details)

def main():
    global name_entry, email_entry, phone_entry, address_entry, output_text
    
    root = tk.Tk()
    root.title("User Information Form")
    
    # Labels and Entry fields for user input
    tk.Label(root, text="Name: ").grid(row=0, column=0, sticky="w")
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(root, text="Email: ").grid(row=1, column=0, sticky="w")
    email_entry = tk.Entry(root)
    email_entry.grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(root, text="Phone Number: ").grid(row=2, column=0, sticky="w")
    phone_entry = tk.Entry(root)
    phone_entry.grid(row=2, column=1, padx=5, pady=5)
    
    tk.Label(root, text="Address: ").grid(row=3, column=0, sticky="w")
    address_entry = tk.Entry(root)
    address_entry.grid(row=3, column=1, padx=5, pady=5)
    
    # Submit Button
    submit_button = tk.Button(root, text="Submit", command=submit_form)
    submit_button.grid(row=4, column=0, columnspan=2, pady=10)
    
    # Text widget to display user details
    output_text = tk.Text(root, height=15, width=60)
    output_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    
    # Edit Button
    edit_button = tk.Button(root, text="Edit", command=edit_selected)
    edit_button.grid(row=6, column=0, pady=10)
    
    # Delete Button
    delete_button = tk.Button(root, text="Delete All", command=clear_output)
    delete_button.grid(row=6, column=1, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
