
from tkinter import*

root = Tk()

def checkLength(P):
    letters = "ABCDEFGHJKLMNPQRSTUVXYWZIO"
    let = {}
    global lsum
    lsum = 0
    for i in range(len(letters)):
        let[letters[i]] = 10 + i
    if len(P) > 0:
        if P[0].isalpha():
            if len(P) == 1:
                ver.config(state = DISABLED)
                return True
            else:
                if P[len(P)-1].isdigit():
                    if len(P) == 10:
                        ver.config(state = NORMAL)
                        lsum = lsum + let[P[0]]//10 + (let[P[0]]%10)*9
                        for i in range(len(P)-1):
                            if i != len(P)-2:
                                lsum = lsum + int(P[i+1])*(8-i)
                            else:
                                lsum = lsum + int(P[i+1])*1
                    else:
                        ver.config(state = DISABLED)
                    return True
                else:
                    return False
                
        else:
            return False
    return True

def showmsg():
    if lsum != 0:
        if lsum % 10 == 0:
            label.config(text = "Correct")
        else:
            label.config(text = "Incorrect", fg = "red")

label = Label(root)
reg = root.register(checkLength)
idl = Entry(root, validate = 'key', validatecommand = (reg, "%P"))
ver = Button(root, text = "Verify", state = DISABLED, command = showmsg)

idl.grid(row = 0, column = 0, sticky = E+W)
ver.grid(row = 1, columnspan = 2)
label.grid(row = 2)

root.mainloop()




