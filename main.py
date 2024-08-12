from tkinter import *
from tkinter import messagebox
from random import choice,randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_ps():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [ choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [ choice(symbols) for _ in range( randint(2, 4))]
    password_num = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbol + password_num

    shuffle(password_list)

    password = "".join(password_list)

    ps_entry.insert(0, f"{password}")

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website_data = web_entry.get()
    email_data = email_entry.get()
    ps_data = ps_entry.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": ps_data,
        }
    }

    if len(website_data) == 0 or len(ps_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            web_entry.delete(0, END)
            ps_entry.delete(0, END)

# find pasword
def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email:{email} \nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")







# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.minsize(width=300, height=300)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#lables
wesite_lable = Label(text="Website:")
wesite_lable.grid(column =0, row=1)
email_lable = Label(text="Email/Username:")
email_lable.grid(column=0, row=2)
pw_lable = Label(text="Password:")
pw_lable.grid(column=0, row=3)

#entrys
web_entry = Entry(width=32)
web_entry.grid(column=1, row= 1)
web_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(column=1, row= 2, columnspan= 2)
email_entry.insert(0, "nithin@gmail.com")
ps_entry = Entry(width=32)
ps_entry.grid(column=1, row=3)

#buttons
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", command=generate_ps)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add",width=44, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()