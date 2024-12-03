import tkinter as tk 

#main window
root = tk.Tk()
root.title("Test")
root.geometry("400x500")

#label
label = tk.Label(root,text="welcome to tkinter",font=("Arial", 16))
label.pack(pady=10)

#entry
entry_label = tk.Label(root, text="Enter ur name:")
entry_label.pack(pady=5)
entry= tk.Entry(root, width=30)
entry.pack()

#button
def greet():
    name = entry.get()
    if name:
        greeting_label.config(text=f"Hello, {name}!")
    else:
        greeting_label.config(text="pls Enter ur name")
button = tk.Button(root, text="Greet Me", command=greet)
button.pack(pady=10)

#label dynamic
greeting_label= tk.Label(root, text="",font=("Arial",14), fg="green")
greeting_label.pack()

#checkbutton
def toggle_text():
    if var.get():
        toggle_label.config(text="is checked")
    else:
        toggle_label.config(text="is unchecked")


var= tk.IntVar()
check_button = tk.Checkbutton(root,text="check Me", variable=var , command=toggle_text )
check_button.pack(pady=5)

toggle_label = tk.Label(root, text="")
toggle_label.pack()


#listbox
list_label=tk.Label(root, text="select ur friut:")
list_label.pack(pady=5)
listbox = tk.Listbox(root, height=3)
fruits=["apple","benana","cherry"]
for fruit in fruits:
    listbox.insert(tk.END, fruit)
listbox.pack()


#use button in listbox
def show_selection():
    selected = listbox.get(listbox.curselection())
    selection_label.config(text=f"u selected: {selected}")

select_button = tk.Button(root, text="show selection", command=show_selection)
select_button.pack(pady=5)

selection_label = tk.Label(root, text="")
selection_label.pack()

root.mainloop()