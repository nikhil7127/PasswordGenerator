import random as r
from tkinter import *
small=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
cap =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
number =["1","2","3","4","5","6","7","8","9","0"]
lists = small+cap+number
from check_pass_secure import check 
from tkinter import *
color="#66b3ff"
window = Tk()
window.geometry("500x400")
Label(window,text="",height="15").place(x=0,y=80)
Label(window,text="",height="15").place(x=494,y=80)
window["bg"] = color
def show():
    Label(window,text="                              ",bg=color).place(x=240,y=60)
    Label(window,text="                                                                                ",bg=color).place(x=140,y=70)
    Label(window,text="                                                                                                                           ",bg=color).place(x=180,y=80)
    global password
    try:
        password=""
        ks = int(a.get())
        if(ks<8 or ks>25):
            raise EnvironmentError
        for k in range(0,int(ks)):
            rs = r.randint(0,len(lists)-1)
            password += lists[rs]
        if(check(password)):
            Label(window,text="",height="15",bg="#00ff55").place(x=0,y=80)
            Label(window,text="",height="15",bg="#00ff55").place(x=494,y=80)
            
            Label(window,text=a.get(),bg=color).place(x=240,y=60)
            if(ks<16):
                Label(window,text=password,bg=color).place(x=210,y=80)
            if(ks>15 and ks<21):
                Label(window,text=password,bg=color).place(x=195,y=80)
            if(ks>20):
                Label(window,text=password,bg=color).place(x=180,y=80)
                
        else:
            print(password)
            show()
    except:
        Label(window,text="",height="15",bg="#FF6A4D").place(x=0,y=80)
        Label(window,text="",height="15",bg="#ff6a4d").place(x=494,y=80)
        Label(window,text="invalid input(8 characters atleast and integer)",bg=color).place(x=140,y=70)


a = Entry(window)
a.pack()   
Button(window,text="submit!",command=show).place(x=230,y=30)

window.mainloop()
