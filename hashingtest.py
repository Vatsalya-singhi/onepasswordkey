import hashlib
from tkinter import *
import tkinter.messagebox as tm

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Domain")
        self.label_2 = Label(self, text="Master Key")
        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=15)
        self.entry_2.grid(row=1, column=15)
        self.logbtn = Button(self, text="Generate", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=5)
        self.pack()

    def _login_btn_clickked(self):
        domain = self.entry_1.get()
        key = self.entry_2.get()
        tot=key+domain
        word='#@'
        for i in range(len(tot)):
            x=chr(ord(tot[i])+2)
            if i%2==0:
                word+=x.lower()
            else:
                word+=x.upper()
        j=int(hashlib.sha1(word.encode()).hexdigest(),16)%(10**8)
        final=word+str(j)
        tm.showinfo("The unique password generated",final)
        
root = Tk()
lf = LoginFrame(root)
root.mainloop()
