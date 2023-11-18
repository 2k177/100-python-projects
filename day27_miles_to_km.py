from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


def button_clicked():
    # print("I got clicked")
    miles = input_text.get()
    # print(miles)
    result_km = int(miles) * 1.6
    result_label.config(text=result_km)

# Input label
input_text = Entry(width=10)
input_text.grid(column=1, row=0)
# input_text.config(height=1, width=5)

#miles Label
my_label = Label(text="Miles")
my_label.grid(column=2, row=0)
my_label.config(padx=5, pady=5)

is_equal_label = Label(text="is equal to ")
is_equal_label.grid(column=0, row=1)

result_label = Label(text=" ")
result_label.grid(column=1, row=1)


km_label = Label(text="km")
km_label.grid(column=2, row=1)


#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)






window.mainloop()

