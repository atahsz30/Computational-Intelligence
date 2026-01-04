import customtkinter as ctk
import Pred_Others, Pred_MultiCategory, Pred_MLP

gui = ctk.CTk()

gui.geometry("230x345")

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


def Predict(box, m):
    mdl = m.get("1.0", "end")
    mdl = int(mdl[:-1])
    x = Content()
    if 0 < mdl <= 5:
        if mdl <= 3:
            p = Pred_Others
            prediction = p.prediction(x, mdl)
        elif mdl == 4:
            p = Pred_MultiCategory
            prediction = p.prediction(x)
        elif mdl == 5:
            p = Pred_MLP
            prediction = p.prediction(x)
        res.delete("0.0", "end")
        if prediction > 0:
            box.insert("0.0", " X")
        else:
            box.insert("0.0", " O")
    else:
        res.delete("0.0", "end")
        box.insert("0.0", " !!")


def Content():
    s = []
    for x in datum:
        for y in x:
            s.append(y)
    return s


def reset():
    res.delete("0.0", "end")
    for btn in btnList:
        btn.configure(fg_color="white")
    for i in range(len(datum)):
        for j in range(len(datum[0])):
            datum[i][j] = -1


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
res = ctk.CTkTextbox(gui, height=30, width=40, fg_color="green", font=("", 20))
bPred = ctk.CTkButton(gui, text="Predict", width=60, height=35, font=("", 17), command=lambda: Predict(res, Model))
bReset = ctk.CTkButton(gui, text="Reset", width=60, height=35, font=("", 17), command=lambda: reset())
Model = ctk.CTkTextbox(gui, height=30, width=40, fg_color="green", font=("", 20))
MName = ctk.CTkTextbox(gui, height=30, width=80, font=("", 17))
MName.insert("1.0", "Model : ")


btnList = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10,
           b11, b12, b13, b14, b15, b16, b17, b18, b19, b20,
           b21, b22, b23, b24, b25]

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
bPred.place(x=20, y=240)
bReset.place(x=100, y=240)
res.place(x=180, y=240)
Model.place(x=110, y=290)
MName.place(x=20, y=290)

gui.mainloop()
