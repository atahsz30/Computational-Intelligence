import customtkinter as ctk

gui = ctk.CTk()

gui.geometry("230x280")

datum = [[-1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1]]


def stateChanger(button, index):
    row = (index - 1) // 5
    col = (index - 1) % 5
    if button.cget("fg_color") == "white":
        button.configure(fg_color="black")
        datum[row][col] = 1
    else:
        button.configure(fg_color="white")
        datum[row][col] = -1


def save(btnLabel):
    data = Content()
    dLabel = btnLabel.cget("text")
    address = "DataSet.txt"
    if dLabel == "X":
        data += "1\n"
    else:
        data += "-1\n"
    f = open(address, "a")
    f.write(data)
    f.close()


def Content():
    s = ""
    for x in datum:
        for y in x:
            s += str(y) + ","
    return s


def reset():
    for btn in btnList:
        btn.configure(fg_color="white")
    for i in range(len(datum)):
        for j in range(len(datum[0])):
            datum[i][j] = -1


def label(btn):
    if btn.cget("text") == "X":
        btn.configure(text="O")
    else:
        btn.configure(text="X")


b1 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b1, 1))
b2 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b2, 2))
b3 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b3, 3))
b4 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b4, 4))
b5 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b5, 5))
b6 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b6, 6))
b7 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b7, 7))
b8 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b8, 8))
b9 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b9, 9))
b10 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b10, 10))
b11 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b11, 11))
b12 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b12, 12))
b13 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b13, 13))
b14 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b14, 14))
b15 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b15, 15))
b16 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b16, 16))
b17 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b17, 17))
b18 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b18, 18))
b19 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b19, 19))
b20 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b20, 20))
b21 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b21, 21))
b22 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b22, 22))
b23 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b23, 23))
b24 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b24, 24))
b25 = ctk.CTkButton(gui, text="", width=40, height=40, fg_color="white", command=lambda: stateChanger(b25, 25))

btnList = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10,
           b11, b12, b13, b14, b15, b16, b17, b18, b19, b20,
           b21, b22, b23, b24, b25]
bSave = ctk.CTkButton(gui, text="Save", width=60, height=30, font=("", 17), command=lambda: save(bLabel))
bReset = ctk.CTkButton(gui, text="Reset", width=60, height=30, font=("", 17), command=lambda: reset())
bLabel = ctk.CTkButton(gui, text="X", width=30, height=30, font=("", 20), command=lambda: label(bLabel))

b1.grid(row=0, column=0, padx=3, pady=3)
b2.grid(row=0, column=1, padx=3, pady=3)
b3.grid(row=0, column=2, padx=3, pady=3)
b4.grid(row=0, column=3, padx=3, pady=3)
b5.grid(row=0, column=4, padx=3, pady=3)
b6.grid(row=1, column=0, padx=3, pady=3)
b7.grid(row=1, column=1, padx=3, pady=3)
b8.grid(row=1, column=2, padx=3, pady=3)
b9.grid(row=1, column=3, padx=3, pady=3)
b10.grid(row=1, column=4, padx=3, pady=3)
b11.grid(row=2, column=0, padx=3, pady=3)
b12.grid(row=2, column=1, padx=3, pady=3)
b13.grid(row=2, column=2, padx=3, pady=3)
b14.grid(row=2, column=3, padx=3, pady=3)
b15.grid(row=2, column=4, padx=3, pady=3)
b16.grid(row=3, column=0, padx=3, pady=3)
b17.grid(row=3, column=1, padx=3, pady=3)
b18.grid(row=3, column=2, padx=3, pady=3)
b19.grid(row=3, column=3, padx=3, pady=3)
b20.grid(row=3, column=4, padx=3, pady=3)
b21.grid(row=4, column=0, padx=3, pady=3)
b22.grid(row=4, column=1, padx=3, pady=3)
b23.grid(row=4, column=2, padx=3, pady=3)
b24.grid(row=4, column=3, padx=3, pady=3)
b25.grid(row=4, column=4, padx=3, pady=3)
bSave.place(x=15, y=240)
bReset.place(x=90, y=240)
bLabel.place(x=170, y=240)
gui.mainloop()
