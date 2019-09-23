import os
from Tkinter import *
from invoke_training_service import startTraining
from invoke_predict_service import startPredict
from speechtext import reverse
from leapvisualiser import visualiser
from Leapcontrolpanel import controlpanel
def main():
    root=Tk()
    button1=Button(root, text="         Training     ", command=startTraining)
    button2=Button(root, text="    Predict   ", command=startPredict)
    button3=Button(root, text="Speech to ASLA", command=reverse)
    button4=Button(root, text="         Exit     ", command=terminate)
    button5=Button(root, text="         Visualiser    ", command=visualiser)
    button6=Button(root, text="     control panel ", command=controlpanel)              
    button1.grid(row=0, column=0, sticky=W)
    button2.grid(row=0, column=2, sticky=E)
    button3.grid(row=2, column=0, sticky=W)
    button4.grid(row=2, column=2, sticky=E)
    button5.grid(row=1, column=1, sticky=E)
    button6.grid(row=3, column=1, sticky=E)
    """button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()"""
    root.mainloop()

def terminate():
    quit()

if __name__ == "__main__":
    main()
