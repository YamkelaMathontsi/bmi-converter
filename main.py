from tkinter import *
from tkinter import messagebox

# giving a title to the window and adding a heading
root = Tk()
root.title("BMI Calculator")
root.geometry("600x500")
root.config(bg="orange")
heading = Label(root, text='Ideal Body Mass Index Calculator')
heading.place(x=250, y=0)

frame = Frame(root, width=500, height=200, borderwidth=1, relief='ridge', bg="aqua")
frame.place(x=50, y=50)

# giving funcionality to the weight entry
weight = Label(frame, text="Weight(kg):", bg="blue")
weight.place(x=10, y=10)
weight_entry = Entry(frame)
weight_entry.place(x=140, y=10)

# giving funcionality to the height entry
height = Label(frame, text="Height(cm):", bg="gold")
height.place(x=10, y=50)
height_entry = Entry(frame)
height_entry.place(x=145, y=50)

# giving functionality to the gender drop down
gender = Label(frame, text="Gender:", bg="yellow")
gender.place(x=10, y=90)

# giving functionality to age label entry
age = Label(frame, text="Age:", bg="red")
age.place(x=10, y=140)
age_entry = Entry(frame, state='readonly')
age_entry.place(x=150, y=140)

options = ['Select...', 'Male', "Female"]
variable = StringVar(frame)
variable.set(options[0])


def activate(value):
    variable.set(value)
    if value != "Select...":
        age_entry.config(state='normal')
    else:
        age_entry.config(state='readonly')


gender_menu = OptionMenu(frame, variable, *options, command=activate)
gender_menu.place(relx=0.3, rely=0.4)

def bmi_calc():
    try:
        float(weight_entry.get())
        float(height_entry.get())
        float(age_entry.get())
        if variable.get() == "Select...":
            raise ValueError
        elif variable.get() == "Male":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + 11.5
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        elif variable.get() == "Female":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + (
                        0.03 * float(age_entry.get())) + 11
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
    except ValueError:
        messagebox.showerror(title=None, message='Gender was not specified or invalid entry was given')
        delete()

# placing the calculate button and giving it functionality

calculate = Button(root, text="Calculate your Ideal Body Mass Index", width=50, command=bmi_calc)
calculate.place(x=120, y=280)

# placing labels in the window giving them functionality

bmi = Label(root, text="BMI:")
bmi.place(x=50, y=350)
bmi_field = Entry(root, state='readonly')
bmi_field.place(x=100, y=350)
ideal_bmi = Label(root, text='Ideal BMI:')
ideal_bmi.place(x=300, y=350)
ideal_field = Entry(root, state='readonly')
ideal_field.place(x=400, y=350)

# defining delete

def delete():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    age_entry.config(state='normal')
    bmi_field.config(state='normal')
    ideal_field.config(state='normal')
    age_entry.delete(0, END)
    bmi_field.delete(0, END)
    ideal_field.delete(0, END)
    age_entry.config(state='readonly')
    bmi_field.config(state='readonly')
    ideal_field.config(state='readonly')
    weight_entry.focus()
    variable.set(options[0])

#giving clear button functionality

clear = Button(root, text='Clear', command='delete', width=20)
clear.place(x=100, y=400)

#giving exit button functionality

exit = Button(root, text='Exit', command='exit', width=20)
exit.place(x=390, y=400)

root.mainloop()







