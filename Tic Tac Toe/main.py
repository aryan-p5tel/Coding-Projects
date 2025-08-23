
import tkinter

#Setting up the Window

window = tkinter.Tk()
window.title("Tic Tac Toe Game")
window.geometry("400x400")
window.configure(background = "lightblue")

#adding elements to the window
label1=tkinter.Label(window, text="Tic Tac Toe",fg = "black", bg = "lightblue", font = ("Arial", 12))

#this will allow the label to be displayed in the window
label1.pack(pady=20)  # Adds some vertical padding

#very important and starts GUI loop
window.mainloop()

##in progress

#Uses columns and rows to position elements
