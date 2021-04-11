from tkinter import *

window = Tk() # initialise
window.title("Mile to Km Converter")
#window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

def action(m=1.60934):
    res = round(float(entry.get()) * m)
    result_label.config(text=res, padx=100, pady=20, font=("Courier", 25))
    print(res)

# Labels
miles_label = Label(text="Miles")
miles_label.config(padx=150, pady=40, font=("Courier", 25))
miles_label.grid(row=0, column=5)


km_label = Label(text="Km")
km_label.config(padx=10, pady=20, font=("Courier", 25))
km_label.grid(row=2, column=5)

equal_to_label = Label(text="Is Equal To")
equal_to_label.config( font=("Courier", 25))
equal_to_label.grid(row=2, column=3)

result_label = Label(text="0")
result_label.config(padx=100, pady=20, font=("Courier", 25))
result_label.grid(row=2, column=4)

calculate_button = Button(text="Calculate", command=action)
calculate_button.config( font=("Courier", 25))
calculate_button.grid(row=3, column=4)


#Entries
entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="0")
#Gets text in entry
print(entry.get())
entry.grid(row=0, column=4)





window.mainloop()


