from tkinter import Button, Tk, Label
from time import sleep

def start():
    sec = 0
    while True:
        city = Label(
            text = sec, 
            background = "#28C8E1", 
            justify = "center", 
            font = "Arial 14")
        city.place(x = 90, y = 100)

        sleep(1)

        sec += 1

if __name__ == "__main__":
    inter = Tk()
    inter.geometry("325x390+300+100")
    inter.resizable(False,False)
    inter.title("Sec")
    inter.configure(background = "#28C8E1")
    inter.update_idletasks()

    city = Label(text = "0", 
                background = "#28C8E1", 
                justify = "center", 
                font = "Arial 14")
    city.place(x = 90, y = 100)

    btn = Button(
        inter, 
        text = "Start",
        command = start
    )
    btn.place(x = 90, y = 150)

    inter.mainloop()