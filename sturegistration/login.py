from tkinter import *
from tkinter import messagebox
import mysql.connector

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

root = Tk()
root.title("New user Registration")
root.geometry("1250x700+210+100")
root.config(bg=background)
root.resizable(False,False)


def register():
  root.destroy
  import main



#icon image
image_icon = PhotoImage(file="C:/Users/DESKTOP/Desktop/python/sturegistration/logo.png")   #image dalna baki he
root.iconphoto(False,image_icon)

#background
frame = Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimage = PhotoImage(file="C:/Users/DESKTOP/Desktop/python/sturegistration/login.png")
Label(frame,image=backgroundimage).pack()


adminaccess = Entry(frame,width=15,fg="#000",border=0,bg="#e8ecf7",font=("Arial Bold",20))
adminaccess.focus()
adminaccess.place(x=520,y=280)




########User entry
def password_enter(e):
  code.delete(0,'end')


def password_leave(e):
  if code.get()=='':
    code.insert(0,"Password")



code = Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=("Arial Bold",20))
code.insert(0,"UserID")
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>",password_leave)
code.place(x=500,y=380)




########################## Button
button_mode = True

def hide():
  global button_mode

  if button_mode:
    eyeButton.config(image=closeeye,activebackground="white")
    code.config(show="*")
    button_mode = False
  else:
    eyeButton.config(image=openeye,activebackground="white")
    code.config(show="")
    button_mode = True



openeye = PhotoImage(file="C:/Users/DESKTOP/Desktop/python/sturegistration/eye.png")
closeeye = PhotoImage(file="C:/Users/DESKTOP/Desktop/python/sturegistration/eye.png")

eyeButton = Button(root,image=openeye,bg="#375174",bd=0,command=hide,height="50",width="50")
eyeButton.place(x=780,y=470)



################################################
regis_button = Button(root,text="ADD NEW USER",bg="#455c88",fg="white",width=13,height=1,font=("Arial",16,"bold"),bd=0,command=register)
regis_button.place(x=530,y=600)


root.mainloop()