import tkinter as tk

window = tk.Tk()
window.title('Введите домашний адрес')
window.geometry('360x300')
window.resizable(width=False, height=False)

frame_name = tk.Frame()
frame_name.pack(anchor='nw')
label_name = tk.Label(master=frame_name, text=(" " * 25 + 'Имя:'))
label_name.pack(side='left')
field_name = tk.Entry(master=frame_name, width=40)
field_name.pack()

frame_surname = tk.Frame()
frame_surname.pack(anchor='nw')
label_surname = tk.Label(master=frame_surname, text=" " * 16 + 'Фамилия:')
label_surname.pack(side='left')
field_surname = tk.Entry(master=frame_surname, width=40)
field_surname.pack()

frame_address1 = tk.Frame()
frame_address1.pack(anchor='nw')
label_address1 = tk.Label(master=frame_address1, text=" " * 20 + 'Адрес1:')
label_address1.pack(side='left')
field_address1 = tk.Entry(master=frame_address1, width=40)
field_address1.pack()

frame_address2 = tk.Frame()
frame_address2.pack(anchor='nw')
label_address2 = tk.Label(master=frame_address2, text=" " * 20 + 'Адрес2:')
label_address2.pack(side='left')
field_address2 = tk.Entry(master=frame_address2, width=40)
field_address2.pack()

frame_city = tk.Frame()
frame_city.pack(anchor='nw')
label_city = tk.Label(master=frame_city, text=" " * 22 + 'Город:')
label_city.pack(side='left')
field_city = tk.Entry(master=frame_city, width=40)
field_city.pack()

frame_region = tk.Frame()
frame_region.pack(anchor='nw')
label_region = tk.Label(master=frame_region, text=" " * 20 + 'Регион:')
label_region.pack(side='left')
field_region = tk.Entry(master=frame_region, width=40)
field_region.pack()

frame_index = tk.Frame()
frame_index.pack(anchor='nw')
label_index = tk.Label(master=frame_index, text='Почтовый индекс:')
label_index.pack(side='left')
field_index = tk.Entry(master=frame_index, width=40)
field_index.pack()

frame_country = tk.Frame()
frame_country.pack(anchor='nw')
label_country = tk.Label(master=frame_country, text=" " * 20 + 'Страна:')
label_country.pack(side='left')
field_country = tk.Entry(master=frame_country, width=40)
field_country.pack()

frame_buttons = tk.Frame(relief=tk.RAISED, borderwidth=2)
frame_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
button_clear = tk.Button(master=frame_buttons, text='Очистить')
button_clear.pack(side='right', padx=5, pady=5)
button_send = tk.Button(master=frame_buttons, text='Отправить')
button_send.pack(side='right', padx=5, pady=5)



window.mainloop()
