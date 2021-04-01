import tkinter as tk

window = tk.Tk()
window.title('Введите домашний адрес')
window.geometry('350x300')

frame_name = tk.Frame()
frame_name.pack(anchor='nw')
label_name = tk.Label(master=frame_name, text='Имя:')
label_name.pack(side='left')
field_name = tk.Entry(master=frame_name, width=40)
field_name.pack()

frame_surname = tk.Frame()
frame_surname.pack(anchor='nw')
label_surname = tk.Label(master=frame_surname, text='Фамилия:')
label_surname.pack(side='left')
field_surname = tk.Entry(master=frame_surname, width=40)
field_surname.pack()

frame_address1 = tk.Frame()
frame_address1.pack(anchor='nw')
label_address1 = tk.Label(master=frame_address1, text='Адрес1:')
label_address1.pack(side='left')
field_address1 = tk.Entry(master=frame_address1, width=40)
field_address1.pack()

frame_address2 = tk.Frame()
frame_address2.pack(anchor='nw')
label_address2 = tk.Label(master=frame_address2, text='Адрес2:')
label_address2.pack(side='left')
field_address2 = tk.Entry(master=frame_address2, width=40)
field_address2.pack()

frame_city = tk.Frame()
frame_city.pack(anchor='nw')
label_city = tk.Label(master=frame_city, text='Город:')
label_city.pack(side='left')
field_city = tk.Entry(master=frame_city, width=40)
field_city.pack()


window.mainloop()

"""label1 = tk.Label(text='Hello!')
label1.pack()

label2 = tk.Label(
    text="Label2",
    fg="white",
    bg='black',
    width=20,
    height=20
)
label2.pack()

button1 = tk.Button(text='Push the Button')
button1.pack()

button2 = tk.Button(
    text='Button2',
    width=25,
    height=5,
    bg='blue',
    fg='yellow'
)
button2.pack()"""

"""name_field = tk.Entry(width=40)
name_field.insert(0, 'What is your name')
name_field.pack()"""

"""frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.BOTH, expand=True)

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack(fill=tk.BOTH, expand=True)

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack(fill=tk.BOTH, expand=True)"""

"""frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I'm at (0,0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)"""

"""for i in range(3):
    window.columnconfigure(i, weight=1, minsize=100)
    window.rowconfigure(i, weight=1, minsize=100)

    for j in range(0, 3):
        frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label1 = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label1.pack(padx=5, pady=5)"""

"""window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky='n')

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky='s')"""
