import smtplib
from tkinter import *

bg = '#cf0a0a'
fg = '#ababab'

sender = 'username'
password = 'password'

def send_mail(receiver,message):
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(sender,password)
    s.sendmail(sender,receiver,message)
    s.quit()
root = Tk()
root.title = 'Email sender @mumeido'
root.geometry('600x450')
root.configure(bg=bg)


Label(root,text="Email Sender",font=('Helvetica',30),fg=fg,bg=bg).place(x=190,y=10)
Label(root,text="Send to:",font=('Helvetica',20),fg=fg,bg=bg).place(x=0,y=70)
Label(root,text="Message:",font=('Helvetica',20),fg=fg,bg=bg).place(x=0,y=110)

rec_name = Entry(root,font=("",17),width = 30)
rec_name.place(x=120,y=70)
msg = Text(root,height = 10, width = 30,font =("",17))
msg.place(x=120,y=110)
Button(root,text=" SEND ",font =("Helvetica",10),fg=fg,command=lambda : 
    send_mail(rec_name.get(),msg.get("1.0",END))).place(x=280,y=400)
root.mainloop()

