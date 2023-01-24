import os,sys,time,random
from datetime import datetime



def menu():
	os.system('clear')
	print("""
[1] Facebook Hacking (high level+)
[2] Gmail Hacking (high level+)
[3] Twitter Hacking (medium level)
[x] Close
""")
	men=input('option>>')
	target=input("Target Account: ")
	file=input("Password List: ")
	files=open(file,'r').read().split("\n")
	v="--[\033[1;32mHacking has been started!\033[0m]--"
	for i in str(v):
		print(i,end='')
		sys.stdout.flush()
		time.sleep(0.1)
	print('\n')
	xc='--[\033[1;32mCracking the binary\033[0m]--'
	for i in str(xc):
		print(i,end='')
		sys.stdout.flush()
		time.sleep(0.1)
	print('\n')
	c=0
	for pwd in files:
		c+=1
		print(f"[{c}] {target}||{pwd}[\033[31mIncorrect\033[0m]")
		time.sleep(random.randint(1,8)/7)
menu()
	
	