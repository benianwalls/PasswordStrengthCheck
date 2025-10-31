
from tkinter import *
from tester import check_strength, score, pwned_check  # import functions
from tkinter import ttk
root = Tk()
root.title("Password Strength Checker")



frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="Enter your password: ").grid(column=0, row=0, sticky="W")
#password entry field
password_entry = ttk.Entry(frm, width=30, )
password_entry.grid(column=1, row=0, columnspan=2, sticky ="W" )

# Label for result output
result_label = ttk.Label(frm, text="", wraplength=300)
result_label.grid(column=0, row=2, columnspan=3, pady=10, sticky="W")

def check_password():
    password = password_entry.get()
    if not password:
        result_label.config(text="Please enter a password.")
       
        return
    count = pwned_check(password)
    if pwned_check(password) > 0:
        result_label.config(text = f"Password has been compromised {count} times! Please choose a different password.")
    else:
        msgs = "Password not found in any data breaches.\n"
        result_label.config(text = msgs + score(password)) 
        
# Buttons
ttk.Button(frm, text="Check Password", command=check_password).grid(column=0, row=1,)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)

root.mainloop()


    
    

