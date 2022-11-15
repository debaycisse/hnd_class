import tkinter as tk
from tkinter import Label
from PIL import Image,ImageTk

# window = tk.Tk()

# window.title("Title here")
# window.geometry("500x600")

# def exitt():
#     exit()

# def move():
#     x = 0; y = 0
#     label.place(x=x+1, y=y+1)

# img = Image.open("./icons8-car-roof-box-48.png")
# photo = ImageTk.PhotoImage(img)

# label = tk.Label(image=photo)
# label.place(x=0, y=0)

# btn = tk.Button(window, command=move, text='Move')
# btn.place(x=0, y=200)




# window.mainloop()



# import tkinter as tk
# from tkinter import Label

window = tk.Tk()

window.title("Title here")
window.geometry("500x600")

def printt():
    firstname = fname.get()
    lastname = lname.get()
    country = sel_country.get()
    print(f"Your full name is {firstname} {lastname}, a citizen {country} Country.")

def exitt():
    exit()


fname = tk.StringVar()
lname = tk.StringVar()
countries = ['Nigeria','Ghana','Germany']
sel_country = tk.StringVar()

# Registration title
label = tk.Label(window, text='Registration Form', relief='solid', width=20, font=('arial', 10, 'bold'), height=2)
label.pack(fill='both', padx=80, pady=20)

# First name
label2 = tk.Label(window, text='First Name ', relief='solid', width=20, font=('arial', 10, 'bold'), height=1)
label2.place(x=80, y=130)

entry_1 = tk.Entry(window, textvariable=fname)
entry_1.place(x=250, y=130, height=21, width=170)

# Last name
label3 = tk.Label(window, text='Last Name ', relief='solid', width=20, font=('arial', 10, 'bold'), height=1)
label3.place(x=80, y=190)

entry_2 = tk.Entry(window, textvariable=lname)
entry_2.place(x=250, y=190, height=21, width=170)

# Country
label4 = tk.Label(window, text='Country ', relief='solid', width=20, font=('arial', 10, 'bold'), height=1)
label4.place(x=80, y=250)

droplist = tk.OptionMenu(window, sel_country, *countries)
sel_country.set("Select your country")
droplist.place(x=250, y=250, height=23, width=170)


# Buttons
b1 = tk.Button(window, text='Login', width=12, bg='brown', fg='white', command=printt)
b1.place(x=80, y=350)

b2 = tk.Button(window, text='Exit', width=12, bg='brown', fg='white', command=exitt)
b2.place(x=291, y=350)


# label = tk.Label(window, text="Label", font=('Verdana', 30, "bold"), bg='#ed23aa', fg='yellow', relief='solid'); 
# label.pack(fill='both', padx=70, expand=True)
# label.place(x=5, y=0)
# label.grid(row=2, column=1)

# label2 = Label(None, text="Label 2"); label2.pack()
# label2.mainloop()

# button = tk.Button(window, text='Submit', fg='#433dea', bg='green', relief='groove')
# button.place(x=0, y=150)

window.mainloop()