import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Student Attendance System")

students = 25
dates = 17

tk.Label(root, text="CSE-01 Attendance",
         font=("Arial", 14, "bold")).grid(row=0, column=0)

tk.Label(root, text="Roll No").grid(row=1, column=0)

# Date headings
for d in range(dates):
    tk.Label(root, text=f"{d+1:02d}-03-2026").grid(row=1, column=d+1)

# Roll numbers
for s in range(students):
    roll = f"2025DCSBT{10001+s}"
    tk.Label(root, text=roll).grid(row=s+2, column=0)

#sig=tk.Label(root,text="Class Teacher Signature",font=("bold")).grid(row=28,column=0,pady=20)

vars = [tk.IntVar() for var in range(students * dates)]

def save():
    with open("check.txt", "w") as f:
        for v in vars:
            f.write(str(v.get()) + "\n")

def load():
    try:
        with open("check.txt", "r") as f:
            data = f.readlines()

        for i in range(len(data)):
            if i< len(vars):
                vars[i].set(int(data[i]))
    except FileNotFoundError:
        pass

count_labels = []

for d in range(dates):
    prst_lbl = tk.Label(root, text="Present: 0")
    prst_lbl.grid(row=students+2, column=d+1, padx=10,pady=10)
    count_labels.append(prst_lbl)

def update():
    save()

    for d in range(dates):
        count = 0
        for s in range(students):
            index = s * dates + d
            count += vars[index].get()

        count_labels[d].config(text="Present: "+str(count))
        

k = 0
for s in range(students):
    for d in range(dates):
        tk.Checkbutton(
            root,
            variable=vars[k],
            command=update
        ).grid(row=s+2, column=d+1)
        k += 1

def save_exit():
    save()
    messagebox.showinfo("Attendance saved succesfully")
    root.destroy()

save_btn=tk.Button(root,text="save",command=save_exit).grid(row=30,column=17,pady=30)

load()
update()

root.mainloop()