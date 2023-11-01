import tkinter as  tk

window = tk.Tk()
window.config(height=500, width=500)
window.title("Click Timer")

frame = tk.Frame(
    master=window,
    background="#F5ED62",
    width=300,
    height=300
)
frame.pack()

label = tk.Label(
    master=frame, 
    text="0",
    font=("MS UI Gothic", 30, "bold"),
    foreground="#FFFFFF", 
    background="#F5ED62",
)

label.place(relx=0.5, rely=0.5, anchor="center")

label_text = 0

def on_release(event):
    global label_text
    label_text = 0
    event.widget["text"] = str(label_text) 

def on_press(event):
    global label_text
    label_text += 1
    event.widget["text"] = str(label_text) 


label.bind("<Button-1>", on_press)
label.bind("<ButtonRelease-1>", on_release)


window.mainloop()
    