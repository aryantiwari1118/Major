import tkinter as tk
# Create the main application window
root = tk.Tk()
root.title("Simple UI Example")

# Create a function to be called when the button is clicked
def button_click():
    label.config(text="Button Clicked!")
    
#Functions for navbar button

def show_home():
    label.config(text="Home Page")

def show_about():
    label.config(text="About Page")

def show_contact():
    label.config(text="Contact Page")    

# Create a label
label = tk.Label(root, text="Press the button")
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Start Diagnosis", command=button_click)
button.pack(side="right",pady=50)
button.place(x=20, y=50)


#Navbar buttons
home_button = tk.Button(root, text="Home", command=show_home)
home_button.pack(side="left", padx=10)

about_button = tk.Button(root, text="About", command=show_about)
about_button.pack(side="left", padx=10)

contact_button = tk.Button(root, text="Contact", command=show_contact)
contact_button.pack(side="left", padx=10)

#aligning the navbar buttons 

home_button.place(x=20,y=100)
about_button.place(x=80,y=100)
contact_button.place(x=120,y=100)


# Start the main event loop
root.mainloop()



