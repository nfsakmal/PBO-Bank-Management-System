import sqlite3 as sq
from time import sleep
import datetime as dt

class Bank():
    def __init__(self):
        try:
            self.conn = sq.connect("bank_mino.db")
            self.cur = self.conn.cursor()
        except Exception as e:
            print(e)
        print("Main Menu")
        print("1. Penarikan")
        print("2. Penyetoran")
        print("3. Saldo")
        print("4. Buka Rekening")
        print("5. Rincian Akun")
        print("6. Perbarui Akun")
        print("7. Keluar")
        while True:
            ch = int(input("Pilihan = "))
            if ch == 1:
                self.tarik_saldo()
            elif ch == 2:
                self.setor_saldo()
            elif ch == 3:
                self.print_saldo()
            elif ch == 4:
                self.create_akun()
            elif ch == 5:
                self.detail_akun()
            elif ch == 6:
                self.update_akun()
            elif ch == 7:
                self.cur.close()
                self.conn.close()
                sleep(1)
                exit()
            else:
                print("Input salah, pilihan 1-7")

    def tarik_saldo(self):
        accNo = int(input("Masukkan nomor rekening = "))
        query = ("select NoRek from Accounts where NoRek > 0")
        self.cur.execute(query)
        temp = self.cur.fetchall()
        data_accNo = [i[0] for i in temp]
        counter = 0
        trails = 2
        if accNo in data_accNo:
            PIN = int(input("Masukkan PIN = "))
            query = (f"select PIN from Accounts where NoRek = {accNo}")
            self.cur.execute(query)
            data_PIN = self.cur.fetchall()[0][0]
            while counter != 3:
                if data_PIN == PIN:
                    withBal = int(input("Jumlah Penarikan = "))
                    query = (f"select Saldo from Accounts where NoRek = {accNo}")
                    self.cur.execute(query)
                    accBal = self.cur.fetchall()[0][0]
                    if withBal > accBal:
                        print("Saldo anda tidak cukup")
                    else:
                        accBal -= withBal
                        print(f"Sisa saldo anda = {accBal}")
                        query = (f"update Accounts set Saldo = {accBal} where NoRek = {accNo}")
                        self.cur.execute(query)
                        self.conn.commit()
                    break
                else:
                    print("PIN Salah, coba lagi.")
                    if trails > 0:
                        print(f"Tersisa {trails} Percobaan memasukkan PIN.")
                    trails -= 1
                    counter += 1
                    if counter == 3:
                        print("PIN salah ketiga kalinya, coba lagi nanti")
                        break
                    PIN = int(input("Masukkan PIN = "))
                    continue
        else:
            print("Data tidak ditemukan di database")

    def setor_saldo(self):
        accNo = int(input("Masukkan nomor rekening = "))
        query = ("select NoRek from Accounts where NoRek > 0")
        self.cur.execute(query)
        temp = self.cur.fetchall()
        data_accNo = [i[0] for i in temp]
        counter = 0
        trails = 2
        if accNo in data_accNo:
            PIN = int(input("Masukkan PIN = "))
            query = (f"select PIN from Accounts where NoRek = {accNo}")
            self.cur.execute(query)
            data_PIN = self.cur.fetchall()[0][0]
            while counter != 3:
                if data_PIN == PIN:
                    depBal = int(input("Masukkan jumlah yang ingin disetor = "))
                    query = (f"select Saldo from Accounts where NoRek = {accNo}")
                    self.cur.execute(query)
                    accBal = self.cur.fetchall()[0][0]
                    accBal += depBal
                    print(f"Saldo anda sekarang = {accBal}")
                    query = (f"update Accounts set Saldo = {accBal} where NoRek = {accNo}")
                    self.cur.execute(query)
                    self.conn.commit()
                    break
                else:
                    print("PIN Salah, coba lagi.")
                    if trails > 0:
                        print(f"Tersisa {trails} Percobaan memasukkan PIN.")
                    trails -= 1
                    counter += 1
                    if counter == 3:
                        print("PIN salah ketiga kalinya, coba lagi nanti")
                        break
                    PIN = int(input("Masukkan PIN = "))
                    continue
        else:
            print("Data tidak ditemukan di database")

    def print_saldo(self):
        accNo = int(input("Masukkan nomor rekening = "))
        query = ("select NoRek from Accounts where NoRek > 0")
        self.cur.execute(query)
        temp = self.cur.fetchall()
        data_accNo = [i[0] for i in temp]
        counter = 0
        trails = 2
        if accNo in data_accNo:
            PIN = int(input("Masukkan PIN = "))
            query = (f"select PIN from Accounts where NoRek = {accNo}")
            self.cur.execute(query)
            data_PIN = self.cur.fetchall()[0][0]
            while counter != 3:
                if data_PIN == PIN:
                    query = (f"select Saldo from Accounts where NoRek = {accNo}")
                    self.cur.execute(query)
                    accBal = self.cur.fetchall()[0][0]
                    print(f"Saldo = {accBal}")
                    break
                else:
                    print("PIN Salah, coba lagi.")
                    if trails > 0:
                        print(f"Tersisa {trails} Percobaan memasukkan PIN.")
                    trails -= 1
                    counter += 1
                    if counter == 3:
                        print("PIN salah ketiga kalinya, coba lagi nanti")
                        break
                    PIN = int(input("Masukkan PIN = "))
                    continue
        else:
            print("Data tidak ditemukan di database")

    def create_akun(self):
        name = input("Masukkan Nama = ")
        gender = input("Jenis Kelamin = ")
        y, m, d = input("Tanggal Lahir (tahun-bulan-tanggal)= ").split("-")
        dob = dt.date(int(y), int(m), int(d))
        age = int(input("Umur = "))
        mob = int(input("Nomor Telepon = "))
        bal = int(input("Saldo Pembuka = "))
        PIN = int(input("4 Digit PIN, harap diingat = "))
        emailaddress = input("Masukkan Email : ")
        homeaddress = input("Masukkan Alamat : ")
        query = (f"insert into Accounts (Nama, JK, TTL, Umur, NoTelp, Saldo, PIN) values ('{name}', '{gender}', '{dob}', {age}, {mob}, {bal}, {PIN});")
        self.cur.execute(query)
        self.conn.commit()
        query = (f"select NoRek from Accounts where Nama = '{name}'")
        self.cur.execute(query)
        accno = self.cur.fetchall()
        print(f"Akun berhasil dibuat dengan nomor rekening {accno[0][0]} .")
        queryC = (f"insert into customer (norek, cNama, cEmail, cAddress, cNoTelp) values ('{accno[0][0]}', '{name}', '{emailaddress}', '{homeaddress}', '{mob}')")
        self.cur.execute(queryC)
        self.conn.commit()

    def detail_akun(self):
        accNo = int(input("Masukkan nomor rekening = "))
        query = ("select NoRek from Accounts where NoRek > 0")
        self.cur.execute(query)
        temp = self.cur.fetchall()
        data_accNo = [i[0] for i in temp]
        counter = 0
        trails = 2
        if accNo in data_accNo:
            PIN = int(input("Masukkan PIN = "))
            query = (f"select PIN from Accounts where NoRek = {accNo}")
            self.cur.execute(query)
            data_PIN = self.cur.fetchall()[0][0]
            while counter != 3:
                if data_PIN == PIN:
                    query = (f"select * from Accounts where NoRek = {accNo}")
                    cursor = self.cur.execute(query)
                    accDetails = self.cur.fetchall()[0]
                    names = [description[0] for description in cursor.description]
                    print("Rincian akun sebagai berikut : \n")
                    for i in range(8):
                        print(f"{names[i]} = {accDetails[i]}")
                    break
                else:
                    print("PIN Salah, coba lagi.")
                    if trails > 0:
                        print(f"Tersisa {trails} Percobaan memasukkan PIN.")
                    trails -= 1
                    counter += 1
                    if counter == 3:
                        print("PIN salah ketiga kalinya, coba lagi nanti")
                        break
                    PIN = int(input("Masukkan PIN = "))
                    continue
        else:
            print("Data tidak ditemukan di database")

    def update_akun(self):
        accNo = int(input("Masukkan nomor rekening = "))
        query = ("select NoRek from Accounts where NoRek > 0")
        self.cur.execute(query)
        temp = self.cur.fetchall()
        data_accNo = [i[0] for i in temp]
        counter = 0
        trails = 2
        if accNo in data_accNo:
            PIN = int(input("Masukkan PIN = "))
            query = (f"select PIN from Accounts where NoRek = {accNo}")
            self.cur.execute(query)
            data_PIN = self.cur.fetchall()[0][0]
            while counter != 3:
                if data_PIN == PIN:
                    query = (f"select * from Accounts where NoRek = {accNo}")
                    cursor = self.cur.execute(query)
                    accDetails = self.cur.fetchall()[0]
                    names = [description[0] for description in cursor.description]
                    print("Rincian akun sebagai berikut : \n")
                    for i in range(8):
                        print(f"{names[i]} = {accDetails[i]}")
                    field = input("\nEnter name of the field you would like to update (Exactly Same & One at a time) = ")
                    # Find the field type
                    query = (f"select typeof({field}) from Accounts where NoRek = {accNo};")
                    t = self.cur.execute(query)
                    Type = t.fetchall()[0][0]
                    if Type == 'integer':
                        value = int(input("Enter new value for the field = "))
                    else:
                        value = input("Enter new value for the field = ")
                    query = (f"update Accounts set {field} = {value} where NoRek = {accNo};")
                    self.cur.execute(query)
                    self.conn.commit()
                    print("Record Successfully Updated..! New Details as follows:\n")
                    query = (f"select * from Accounts where NoRek = {accNo}")
                    cursor = self.cur.execute(query)
                    accDetails = self.cur.fetchall()[0]
                    names = [description[0] for description in cursor.description]
                    for i in range(8):
                        print(f"{names[i]} = {accDetails[i]}")
                    print("\nThanks for using our service\n")
                    break
                else:
                    print("PIN Salah, coba lagi.")
                    if trails > 0:
                        print(f"Tersisa {trails} Percobaan memasukkan PIN.")
                    trails -= 1
                    counter += 1
                    if counter == 3:
                        print("PIN salah ketiga kalinya, coba lagi nanti")
                        break
                    PIN = int(input("Masukkan PIN = "))
                    continue
        else:
            print("Data tidak ditemukan di database")

if __name__ == "__main__":
    a = Bank()
    a
