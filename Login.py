from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class loginPage:
    def __init__(self, window):
        self.wn = window
        self.wn.title("Login")
        self.wn.geometry("500x500")

        self.login_image=ImageTk.PhotoImage(Image.open("Icons/login.png").resize((150, 150)))
        self.login_lbl=Label(self.wn, image=self.login_image)
        self.login_lbl.image=self.login_image
        self.login_lbl.place(x=180, y=20)
        self.uname_img=ImageTk.PhotoImage(Image.open("Icons/uname.png").resize((25, 25)))
        self.user_lbl=Label(self.wn, image=self.uname_img)
        self.user_lbl.image=self.uname_img
        self.user_lbl.place(x=50, y=197)
        self.pass_img=ImageTk.PhotoImage(Image.open("Icons/pword.png").resize((25, 25)))
        self.pword_lbl=Label(self.wn, image=self.pass_img)
        self.pword_lbl.image=self.pass_img
        self.pword_lbl.place(x=50, y=237)

        self.uname_lbl=Label(self.wn, text='Username:',font=('arial', 11))
        self.uname_lbl.place(x=80, y=200)
        self.pass_lbl=Label(self.wn, text='Password:',font=('arial', 11))
        self.pass_lbl.place(x=80, y=240)
        self.type_lbl=Label(self.wn, text='Type :', font=('arial', 11))
        self.type_lbl.place(x=80, y=280)

        self.uname_ent=Entry(self.wn, font=('arial', 12), width=22)
        self.uname_ent.place(x=180, y=200)
        self.pass_ent=Entry(self.wn, font=('arial', 12), width=22)
        self.pass_ent.place(x=180, y=240)
        self.type_ent=ttk.Combobox(self.wn, font=('arial', 12), width=20, state='readonly')
        self.type_ent['values']=('User','Admin')
        self.type_ent.place(x=180, y=280)

        self.login_btn=Button(self.wn, text='Login', height=2, width=12)
        self.login_btn.place(x=120, y=340)
        self.reset_btn=Button(self.wn, text='Reset', height=2, width=12)
        self.reset_btn.place(x=250, y=340)
        self.reg_btn=Button(self.wn, text='Register', height=2, width=12)
        self.reg_btn.place(x=180,y=400)

window=Tk()
loginPage(window)
window.mainloop()