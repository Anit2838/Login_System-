from tkinter import *
from tkinter import messagebox

def login():
    user = username.get()
    code = password.get()
    
    if user == "parvat" and code == "1234":
        root = Toplevel(screen)
        root.title("Bill")
        root.geometry("1280x720+150+80")  # Corrected size format
        root.configure(bg="#d7dae2")
        root.resizable(False, False)
        
    elif user == "" or code == "":
        messagebox.showerror("Invalid", "Please enter username and password")
    elif user == "":
        messagebox.showerror("Invalid", "Username is required")
    elif code == "":
        messagebox.showerror("Invalid", "Password is required")
    elif user != "parvat":
        messagebox.showerror("Invalid", "Please enter valid username")
    elif code != "1234":
        messagebox.showerror("Invalid", "Please enter valid password")

def main_screen():
    global screen, username, password
    
    screen = Tk()
    screen.geometry("1280x720+150+80")  # Corrected size format
    screen.configure(bg="#d7dae2")
    
    # Absolute path to login.png
    image_icon = PhotoImage(file="C:/a/login.png")
    screen.iconphoto(False, image_icon)
    screen.title("Login System")
    
    lblTitle = Label(screen, text="Login System", font=("Arial", 50, "bold"), fg="black", bg="#d7dae2")
    lblTitle.pack(pady=50)
    
    bordercolor = Frame(screen, bg="black", width=800, height=400)
    bordercolor.pack()
    
    mainframe = Frame(bordercolor, bg="#d7dae2", width=800, height=400)
    mainframe.pack(padx=20, pady=20)
    
    Label(mainframe, text="Username", font=("Arial", 30, "bold"), bg="#d7dae2").place(x=100, y=50)
    Label(mainframe, text="Password", font=("Arial", 30, "bold"), bg="#d7dae2").place(x=100, y=150)
    
    username = StringVar()
    password = StringVar()
    
    entry_username = Entry(mainframe, textvariable=username, width=12, bd=2, font=("Arial", 30))
    entry_username.place(x=400, y=50)
    entry_password = Entry(mainframe, textvariable=password, width=12, bd=2, font=("Arial", 30), show="*")
    entry_password.place(x=400, y=150)
    
    def reset():
        entry_username.delete(0, END)
        entry_password.delete(0, END)
    
    Button(mainframe, text="Login", height=2, width=23, bg="#ed3833", fg="white", bd=0, command=login).place(x=100, y=250)
    Button(mainframe, text="Reset", height=2, width=23, bg="#1089ff", fg="white", bd=0, command=reset).place(x=300, y=250)
    Button(mainframe, text="Exit", height=2, width=23, bg="#00bd56", fg="white", bd=0, command=screen.destroy).place(x=500, y=250)
    
    screen.mainloop()

if __name__ == "__main__":
    main_screen()
