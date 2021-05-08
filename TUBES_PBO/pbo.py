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

def write(master,nama,oc,pin):
	
	if( (is_number(nama)) or (is_number(oc)==0) or (is_number(pin)==0)or nama==""):
		messagebox.showinfo("Terjadi Kesalahan","Silahkan coba lagi")
		master.destroy()
		return 

	f1=open("rek_Record.txt",'r')
	rek_no=int(f1.readline())
	rek_no+=1
	f1.close()

	f1=open("rek_Record.txt",'w')
	f1.write(str(rek_no))
	f1.close()

	fdet=open(str(rek_no)+".txt","w")
	fdet.write(pin+"\n")
	fdet.write(oc+"\n")
	fdet.write(str(rek_no)+"\n")
	fdet.write(nama+"\n")
	fdet.close()

	frec=open(str(rek_no)+"-rec.txt",'w')
	frec.write("Date                             Setoran      Penarikan     Saldo\n")
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
	frec.close()
	
	messagebox.showinfo("Notifikasi","Nomor rekening anda adalah :"+str(rek_no))
	master.destroy()
	return

def crdt_write(master,amt,rek,nama):

	if(is_number(amt)==0):
		messagebox.showinfo("Terjadi Kesalahan","Silahkan coba lagi")
		master.destroy()
		return 

	fdet=open(rek+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	amti=int(amt)
	cb=amti+camt
	fdet=open(rek+".txt",'w')
	fdet.write(pin)
	fdet.write(str(cb)+"\n")
	fdet.write(rek+"\n")
	fdet.write(nama+"\n")
	fdet.close()
	frec=open(str(rek)+"-rec.txt",'a+')
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
	frec.close()
	messagebox.showinfo("Notifikasi","Uang berhasil disetor.")
	master.destroy()
	return

def debit_write(master,amt,rek,nama):

	if(is_number(amt)==0):
		messagebox.showinfo("Terjadi Kesalahan","Silahkan coba lagi")
		master.destroy()
		return 
			
	fdet=open(rek+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	if(int(amt)>camt):
		messagebox.showinfo("Terjadi kesalahan","Saldo anda tidak cukup.")
	else:
		amti=int(amt)
		cb=camt-amti
		fdet=open(rek+".txt",'w')
		fdet.write(pin)
		fdet.write(str(cb)+"\n")
		fdet.write(rek+"\n")
		fdet.write(nama+"\n")
		fdet.close()
		frec=open(str(rek)+"-rec.txt",'a+')
		frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n")
		frec.close()
		messagebox.showinfo("Notifikasi","Uang berhasil ditarik.")
		master.destroy()
		return

def Cr_Amt(rek,nama):
	creditwn=tk.Tk()
	creditwn.geometry("1366x768")
	creditwn.title("Credit Amount")
	creditwn.configure(bg="red")
	fr1=tk.Frame(creditwn,bg="blue")
	l_title=tk.Message(creditwn,text="BANK MINO",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Impact","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(creditwn,relief="raised",text="Enter Amount to be credited: ")
	e1=tk.Entry(creditwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(creditwn,text="Credit",relief="raised",command=lambda:crdt_write(creditwn,e1.get(),rek,nama))
	b.pack(side="top")
	creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),rek,nama))

def De_Amt(rek,nama):
	debitwn=tk.Tk()
	debitwn.geometry("1366x768")
	debitwn.title("Debit Amount")	
	debitwn.configure(bg="red")
	fr1=tk.Frame(debitwn,bg="blue")
	l_title=tk.Message(debitwn,text="BANK MINO",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Impact","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(debitwn,relief="raised",text="Enter Amount to be debited: ")
	e1=tk.Entry(debitwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(debitwn,text="Debit",relief="raised",command=lambda:debit_write(debitwn,e1.get(),rek,nama))
	b.pack(side="top")
	debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),rek,nama))

def disp_bal(rek):
	fdet=open(rek+".txt",'r')
	fdet.readline()
	bal=fdet.readline()
	fdet.close()
	messagebox.showinfo("Balance",bal)

def disp_tr_hist(rek):
	disp_wn=tk.Tk()
	disp_wn.geometry("900x600")
	disp_wn.title("Riwayat Transaksi")
	disp_wn.configure(bg="black")
	fr1=tk.Frame(disp_wn,bg="blue")
	l_title=tk.Message(disp_wn,text="BANK MINO",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Impact","50","bold"))
	l_title.pack(side="top")
	fr1=tk.Frame(disp_wn)
	fr1.pack(side="top")
	l1=tk.Message(disp_wn,text="Riwayat transaksi terakhir akun anda :",padx=100,pady=20,width=1000,bg="blue",fg="green",relief="raised")
	l1.pack(side="top")
	fr2=tk.Frame(disp_wn)
	fr2.pack(side="top")
	frec=open(rek+"-rec.txt",'r')
	for line in frec:
		l=tk.Message(disp_wn,anchor="w",text=line,relief="raised",width=2000)
		l.pack(side="top")
	b=tk.Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy)
	b.pack(side="top")
	frec.close()

def logged_in_menu(rek,nama):
	rootwn=tk.Tk()
	rootwn.geometry("1366x768")
	rootwn.title("BANK MINO-"+nama)
	rootwn.configure(background='red')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	l_title=tk.Message(rootwn,text="BANK\n MINO",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Impact","50","bold"))
	l_title.pack(side="top")
	label=tk.Label(text="Masuk Sebagai : "+nama,relief="flat",bg="black",fg="white",anchor="center",justify="center")
	label.pack(side="top")
	img2=tk.PhotoImage(file="credit.gif")
	myimg2=img2.subsample(2,2)
	img3=tk.PhotoImage(file="debit.gif")
	myimg3=img3.subsample(2,2)
	img4=tk.PhotoImage(file="balance1.gif")
	myimg4=img4.subsample(2,2)
	img5=tk.PhotoImage(file="transaction.gif")
	myimg5=img5.subsample(2,2)
	b2=tk.Button(image=myimg2,command=lambda: Cr_Amt(rek,nama))
	b2.image=myimg2
	b3=tk.Button(image=myimg3,command=lambda: De_Amt(rek,nama))
	b3.image=myimg3
	b4=tk.Button(image=myimg4,command=lambda: disp_bal(rek))
	b4.image=myimg4
	b5=tk.Button(image=myimg5,command=lambda: disp_tr_hist(rek))
	b5.image=myimg5
	img6=tk.PhotoImage(file="logout.gif")
	myimg6=img6.subsample(2,2)
	b6=tk.Button(image=myimg6,relief="raised",command=lambda: logout(rootwn))
	b6.image=myimg6

	b2.place(x=100,y=150)
	b3.place(x=100,y=220)
	b4.place(x=900,y=150)
	b5.place(x=900,y=220)
	b6.place(x=500,y=400)

def logout(master):
	messagebox.showinfo("Notifikasi","Anda berhasil keluar.")
	master.destroy()
	Main_Menu()

def check_log_in(master,nama,acc_num,pin):
	if(check_acc_nmb(acc_num)==0):
		master.destroy()
		Main_Menu()
		return

	if( (is_number(nama))  or (is_number(pin)==0) ):
		messagebox.showinfo("Terjadi Kesalahan","Silahkan coba lagi")
		master.destroy()
		Main_Menu()
	else:
		master.destroy()
		logged_in_menu(acc_num,nama)

def log_in(master):
	master.destroy()
	loginwn=tk.Tk()
	loginwn.geometry("1366x768")
	loginwn.title("Log in")
	loginwn.configure(bg="red")
	fr1=tk.Frame(loginwn,bg="blue")
	l_title=tk.Message(loginwn,text="BANK MINO",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Impact","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(loginwn,text="Masukkan nama :",relief="flat")
	l1.pack(side="top")
	e1=tk.Entry(loginwn)
	e1.pack(side="top")
	l2=tk.Label(loginwn,text="Nomor rekening :",relief="flat")
	l2.pack(side="top")
	e2=tk.Entry(loginwn)
	e2.pack(side="top")
	l3=tk.Label(loginwn,text="PIN :",relief="flat")
	l3.pack(side="top")
	e3=tk.Entry(loginwn,show="•")
	e3.pack(side="top")
	b=tk.Button(loginwn,text="Submit",command=lambda: check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	b1=tk.Button(text="HOME",relief="raised",bg="black",fg="white",command=lambda: home_return(loginwn))
	b1.pack(side="top")
	loginwn.bind("<Return>",lambda x:check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	
def Create():
	crwn=tk.Tk()
	crwn.geometry("1366x768")
	crwn.title("Buat Akun Baru")
	crwn.configure(bg="red")
	fr1=tk.Frame(crwn,bg="blue")
	l_title=tk.Message(crwn,text="BANK MINO",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Impact","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(crwn,text="Masukkan nama akun :",relief="raised")
	l1.pack(side="top")
	e1=tk.Entry(crwn)
	e1.pack(side="top")
	l2=tk.Label(crwn,text="Enter opening credit :",relief="raised")
	l2.pack(side="top")
	e2=tk.Entry(crwn)
	e2.pack(side="top")
	l3=tk.Label(crwn,text="Masukkan PIN :",relief="raised")
	l3.pack(side="top")
	e3=tk.Entry(crwn,show="•")
	e3.pack(side="top")
	b=tk.Button(crwn,text="Submit",command=lambda: write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	crwn.bind("<Return>",lambda x:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	return

def Main_Menu():
	rootwn=tk.Tk()
	rootwn.geometry("1366x768")
	rootwn.title("BANK MINO")
	rootwn.configure(background='red')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	bg_image = tk.PhotoImage(file ="Skipper.gif")
	x = tk.Label (image = bg_image)
	x.place(y=-400)
	l_title=tk.Message(text="BANK\n MINO",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Impact","50","bold"))
	l_title.pack(side="top")
	imgc1=tk.PhotoImage(file="new.gif")
	imglo=tk.PhotoImage(file="login.gif")
	imgc=imgc1.subsample(2,2)
	imglog=imglo.subsample(2,2)
	b1=tk.Button(image=imgc,command=Create)
	b1.image=imgc
	b2=tk.Button(image=imglog,command=lambda: log_in(rootwn))
	b2.image=imglog
	img6=tk.PhotoImage(file="quit.gif")
	myimg6=img6.subsample(2,2)
	b6=tk.Button(image=myimg6,command=rootwn.destroy)
	b6.image=myimg6
	b1.place(x=800,y=300)
	b2.place(x=800,y=200)	
	b6.place(x=920,y=400)
	rootwn.mainloop()

Main_Menu()
