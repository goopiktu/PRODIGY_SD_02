from tkinter import *
import random
# GUI
root = Tk()
root.title("Number Guessing Game")

guessCounter = 0
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


def generateNumber(): 
    return random.randint(1,10)





def bot():
    global guessCounter
    
    userGuess = int(e.get())
    
    #while userGuess != computerNumber: 
    guessCounter += 1
    if computerNumber < userGuess:
        txt.insert(END, "Too High\n")
        txt.insert(END, e.get()  + '\n')
    elif computerNumber > userGuess:
        txt.insert(END, "Too Low\n")
        txt.insert(END, e.get()  + '\n')
    else:
        txt.insert(END, f"YOU GUESSED IT it's {computerNumber}\n")
        txt.insert(END, f"{guessCounter} ATTEMPTS\n")  
        Attempts.set(f"Attempts: {guessCounter}")
    
    e.delete(0, 'end')


     

Attempts = StringVar()
Attempts.set("Attempts: ")

lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Number Guessing Game", font=FONT_BOLD).grid(
    sticky= W, row=0, column=0, padx=15)



attempts = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, textvariable=Attempts, font=FONT_BOLD).grid(
    sticky= W, row=1, column=0, padx=15)
 
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=2, column=0, columnspan=1, padx=15)
txt.insert(END, "Generating random number from 1-10 \n")
computerNumber = generateNumber()
 
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
 
e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=60)
e.grid(row=3, column=0)
 
send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=bot).grid(row=3, column=1)
 
root.mainloop()