import Face_Recognition as fr
import Object_detection as od
import tkinter as tk
import threading


root = tk.Tk()
root.title('Detectron2 - Control Panel')
root.iconbitmap('Resources/UI Icons/main icon.ico')
root.geometry("700x700")
root.config(bg="white")

# Config our column rows and cols
#Grid.rowconfigure(root, index=0, weight=1)
tk.Grid.columnconfigure(root, index=0, weight=1)


# Header label text:
homeLabel = tk.Label(root, text="Detectron2\nSecurity Surveillance System", font="Bahnschrift 15", bg='dodger blue', fg="white", height=2, padx=20)
homeLabel.grid(row=0, column=0, columnspan=4, sticky="nsew")


# Create Mode Button
combo_img = tk.PhotoImage(file='Resources/UI Icons/combo.png')
combo_img = combo_img.subsample(3, 3)

mode_btn = tk.Button(root, image=combo_img, command=fr.face_recog, bg='dodger blue')
mode_btn.grid(row=1, column=0, pady=20, padx=20, ipadx=50)


surveillance_img = tk.PhotoImage(file='Resources/UI Icons/surveillance.png')
surveillance_img = surveillance_img.subsample(3, 3)

surveillance_btn = tk.Button(root, image=surveillance_img, command=od.object_detection, bg='dodger blue')
surveillance_btn.grid(row=1, column=1, pady=20, padx=20, ipadx=50)


exit_img = tk.PhotoImage(file='Resources/UI Icons/exit.png')
exit_img = exit_img.subsample(3,3)

Exit_btn = tk.Button(root, image=exit_img, command=exit, bg='dodger blue')
Exit_btn.grid(row=8, column=0, columnspan=2, pady=20, padx=20, ipadx=50)

root.mainloop()