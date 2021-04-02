import tkinter as tk

window = tk.Tk()
window.title('Temperature converter')
window.geometry('260x50')
window.rowconfigure(0, minsize=10, weight=1)
window.columnconfigure([0, 1, 2, 3], minsize=10, weight=1)


def convert_f_to_c():
    lbl_celsius["text"] = f"{(int(end_temperature.get()) - 32) * 5 / 9}+\N{DEGREE CELSIUS}'"


end_temperature = tk.Entry(width=10)
lbl_fah = tk.Label(text="\N{DEGREE FAHRENHEIT}", width=5)
btn_convert = tk.Button(text='\N{RIGHTWARDS BLACK ARROW}', width=5, command=convert_f_to_c)
lbl_celsius = tk.Label(width=12)

end_temperature.grid(row=0, column=0)
lbl_fah.grid(row=0, column=1, sticky='w')
btn_convert.grid(row=0, column=2, sticky='w')
lbl_celsius.grid(row=0, column=3, sticky='w')

window.mainloop()
