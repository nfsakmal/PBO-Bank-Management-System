import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime


def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def check_acc_nmb(num):
	try:
		fpin=open(num+".txt",'r')
	except FileNotFoundError:
		messagebox.showinfo("Terjadi Kesalahan","Silahkan coba lagi")
		log_in(masukscreen)
	fpin.close()
	return 

def home_return(master):
	master.destroy()
	Main_Menu()

def write(master,name,oc,pin):
	
	if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==""):
		messagebox.showinfo("Terjadi Kesalahan","Silahkan coba lagi")
		master.destroy()
		return 

	f1=open("Accnt_Record.txt",'r')
	accnt_no=int(f1.readline())
	accnt_no+=1
	f1.close()

	f1=open("Accnt_Record.txt",'w')
	f1.write(str(accnt_no))
	f1.close()

	fdet=open(str(accnt_no)+".txt","w")
	fdet.write(pin+"\n")
	fdet.write(oc+"\n")
	fdet.write(str(accnt_no)+"\n")
	fdet.write(name+"\n")
	fdet.close()

	frec=open(str(accnt_no)+"-rec.txt",'w')
	frec.write("Date                             Credit      Debit     Saldo\n")
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
	frec.close()
	
	messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
	master.destroy()
	return

def crdt_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Terjadi Kesalahan","Silahkan coba lagi")
		master.destroy()
		return 

	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	amti=int(amt)
	cb=amti+camt
	fdet=open(accnt+".txt",'w')
	fdet.write(pin)
	fdet.write(str(cb)+"\n")
	fdet.write(accnt+"\n")
	fdet.write(name+"\n")
	fdet.close()
	frec=open(str(accnt)+"-rec.txt",'a+')
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
	frec.close()
	messagebox.showinfo("Notifikasi","Uang berhasil ditarik.")
	master.destroy()
	return

def debit_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Terjadi Kesalahan","Silahkan coba lagi")
		master.destroy()
		return 
			
	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	if(int(amt)>camt):
		messagebox.showinfo("Terjadi kesalahan","Saldo anda tidak cukup.")
	else:
		amti=int(amt)
		cb=camt-amti
		fdet=open(accnt+".txt",'w')
		fdet.write(pin)
		fdet.write(str(cb)+"\n")
		fdet.write(accnt+"\n")
		fdet.write(name+"\n")
		fdet.close()
		frec=open(str(accnt)+"-rec.txt",'a+')
		frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n")
		frec.close()
		messagebox.showinfo("Notifikasi","Uang berhasil disetor.")
		master.destroy()
		return

def Cr_Amt(accnt,name):
	tarikscreen=tk.Tk()
	tarikscreen.geometry("600x300")
	tarikscreen.title("Penarikan")
	tarikscreen.configure(bg="orange")
	fr1=tk.Frame(tarikscreen,bg="blue")
	l_title=tk.Message(tarikscreen,text="BANK MINO",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Impact","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(tarikscreen,relief="raised",text="Masukkan jumlah uang yang ingin ditarik : ")
	e1=tk.Entry(tarikscreen,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(tarikscreen,text="Credit",relief="raised",command=lambda:crdt_write(tarikscreen,e1.get(),accnt,name))
	b.pack(side="top")
	tarikscreen.bind("<Return>",lambda x:crdt_write(tarikscreen,e1.get(),accnt,name))


def De_Amt(accnt,name):
	setorscreen=tk.Tk()
	setorscreen.geometry("600x300")
	setorscreen.title("Setoran")	
	setorscreen.configure(bg="orange")
	fr1=tk.Frame(setorscreen,bg="blue")
	l_title=tk.Message(setorscreen,text="BANK MINO",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Impact","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(setorscreen,relief="raised",text="Masukkan jumlah uang yang ingin disetor : ")
	e1=tk.Entry(setorscreen,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(setorscreen,text="Debit",relief="raised",command=lambda:debit_write(setorscreen,e1.get(),accnt,name))
	b.pack(side="top")
	setorscreen.bind("<Return>",lambda x:debit_write(setorscreen,e1.get(),accnt,name))




def disp_bal(accnt):
	fdet=open(accnt+".txt",'r')
	fdet.readline()
	bal=fdet.readline()
	fdet.close()
	messagebox.showinfo("Saldo",bal)

def disp_tr_hist(accnt):
	historyscreen=tk.Tk()
	historyscreen.geometry("900x600")
	historyscreen.title("Transaction History")
	historyscreen.configure(bg="orange")
	fr1=tk.Frame(historyscreen,bg="blue")
	l_title=tk.Message(historyscreen,text="BANK MINO",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Impact","50","bold"))
	l_title.pack(side="top")
	fr1=tk.Frame(historyscreen)
	fr1.pack(side="top")
	l1=tk.Message(historyscreen,text="Your Transaction History:",padx=100,pady=20,width=1000,bg="blue",fg="orange",relief="raised")
	l1.pack(side="top")
	fr2=tk.Frame(historyscreen)
	fr2.pack(side="top")
	frec=open(accnt+"-rec.txt",'r')
	for line in frec:
		l=tk.Message(historyscreen,anchor="w",text=line,relief="raised",width=2000)
		l.pack(side="top")
	b=tk.Button(historyscreen,text="Quit",relief="raised",command=historyscreen.destroy)
	b.pack(side="top")
	frec.close()

def logged_in_menu(accnt,name):
	masukscreen=tk.Tk()
	masukscreen.geometry("1366x768")
	masukscreen.title("BANK MINO-"+name)
	masukscreen.configure(background ='orange')
	fr1=tk.Frame(masukscreen)
	fr1.pack(side="top")
	l_title=tk.Message(masukscreen,text="BANK\n MINO",relief="flat",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Impact","50","bold"))
	l_title.pack(side="top")
	label=tk.Label(text="Masuk Sebagai : " + name,relief="flat",bg="black",fg="white",anchor="center",justify="center")
	label.pack(side="top")
	img2=tk.PhotoImage(file="credit.gif")
	myimg2=img2.subsample(2,2)
	img3=tk.PhotoImage(file="debit.gif")
	myimg3=img3.subsample(2,2)
	img4=tk.PhotoImage(file="Saldo1.gif")
	myimg4=img4.subsample(2,2)
	img5=tk.PhotoImage(file="transaction.gif")
	myimg5=img5.subsample(2,2)
	button2=tk.Button(image=myimg2,command=lambda: Cr_Amt(accnt,name))
	button2.image=myimg2
	button3=tk.Button(image=myimg3,command=lambda: De_Amt(accnt,name))
	button3.image=myimg3
	button4=tk.Button(image=myimg4,command=lambda: disp_bal(accnt))
	button4.image=myimg4
	button5=tk.Button(image=myimg5,command=lambda: disp_tr_hist(accnt))
	button5.image=myimg5
	
	img6=tk.PhotoImage(file="logout.gif")
	myimg6=img6.subsample(2,2)
	button6=tk.Button(image=myimg6,relief="raised",command=lambda: logout(masukscreen))
	button6.image=myimg6

	
	button2.place(x=100,y=225)
	button3.place(x=100,y=300)
	button4.place(x=100,y=450)
	button5.place(x=100,y=525)
	button6.place(x=100,y=375)

	
def logout(master):
	
	messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
	master.destroy()
	Main_Menu()

def check_log_in(master,name,acc_num,pin):
	if(check_acc_nmb(acc_num)==0):
		master.destroy()
		Main_Menu()
		return

	if( (is_number(name))  or (is_number(pin)==0) ):
		messagebox.showinfo("Terjadi Kesalahan","Silahkan coba lagi")
		master.destroy()
		log_in(masukscreen)
	else:
		master.destroy()
		logged_in_menu(acc_num,name)


def log_in(master):
	master.destroy()
	loginscreen=tk.Tk()
	loginscreen.geometry("1366x768")
	loginscreen.title("Log in")
	loginscreen.configure(bg="orange")
	fr1=tk.Frame(loginscreen,bg="blue")
	l_title=tk.Message(loginscreen,text="BANK MINO",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Impact","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(loginscreen,text="Masukkan Username :",relief="raised")
	l1.pack(side="top")
	e1=tk.Entry(loginscreen)
	e1.pack(side="top")
	l2=tk.Label(loginscreen,text="Nomor Rekening :",relief="raised")
	l2.pack(side="top")
	e2=tk.Entry(loginscreen)
	e2.pack(side="top")
	l3=tk.Label(loginscreen,text="PIN :",relief="raised")
	l3.pack(side="top")
	e3=tk.Entry(loginscreen,show="•")
	e3.pack(side="top")
	b=tk.Button(loginscreen,text="Submit",command=lambda: check_log_in(loginscreen,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	button1=tk.Button(text="HOME",relief="raised",bg="black",fg="white",command=lambda: home_return(loginscreen))
	button1.pack(side="top")
	loginscreen.bind("<Return>",lambda x:check_log_in(loginscreen,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	

def Create():
	createscreen=tk.Tk()
	createscreen.geometry("600x300")
	createscreen.title("Create Account")
	createscreen.configure(bg="orange")
	fr1=tk.Frame(createscreen,bg="blue")
	l_title=tk.Message(createscreen,text="BANK MINO",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Impact","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(createscreen,text="Enter Name:",relief="raised")
	l1.pack(side="top")
	e1=tk.Entry(createscreen)
	e1.pack(side="top")
	l2=tk.Label(createscreen,text="Enter opening credit:",relief="raised")
	l2.pack(side="top")
	e2=tk.Entry(createscreen)
	e2.pack(side="top")
	l3=tk.Label(createscreen,text="Enter desired PIN:",relief="raised")
	l3.pack(side="top")
	e3=tk.Entry(createscreen,show="*")
	e3.pack(side="top")
	b=tk.Button(createscreen,text="Submit",command=lambda: write(createscreen,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	createscreen.bind("<Return>",lambda x:write(createscreen,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	return

def Main_Menu():

	masukscreen=tk.Tk()
	masukscreen.geometry("1366x768")
	masukscreen.title("BANK MINO")
	masukscreen.configure(background='orange')
	fr1=tk.Frame(masukscreen)
	fr1.pack(side="top")
	bg_image = tk.PhotoImage(file ="Skipper.gif")
	x = tk.Label (image = bg_image)
	x.place(y=-400)
	l_title=tk.Message(text="BANK \n MINO",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Impact","50","bold"))
	l_title.pack(side="top")
	imgc1=tk.PhotoImage(file="new.gif")
	imglo=tk.PhotoImage(file="login.gif")
	imgc=imgc1.subsample(2,2)
	imglog=imglo.subsample(2,2)

	button1=tk.Button(image=imgc,command=Create)
	button1.image=imgc
	button2=tk.Button(image=imglog,command=lambda: log_in(masukscreen))
	button2.image=imglog
	img6=tk.PhotoImage(file="quit.gif")
	myimg6=img6.subsample(2,2)

	button6=tk.Button(image=myimg6,command=masukscreen.destroy)
	button6.image=myimg6
	button1.place(x=800,y=300)
	button2.place(x=800,y=200)	
	button6.place(x=920,y=400)

	masukscreen.mainloop()

Main_Menu()
