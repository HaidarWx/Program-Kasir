print("----------------- Program Kasir Sederhana-----------------")


print ("---------------------- Menu Makanan -----------------")
print("1. Bakmi - Rp 15000")
print("2. Soto Tangkar - Rp 9000")
print("3. Mie Rebus - Rp 11000")
nomor=int(input("Masukan Pilihan: "))

porsi=int(input("Berapa Porsi: "))

if nomor == 1:
       
       totalmkn = porsi*15000
       totalmkn=int(totalmkn)
       print (porsi," porsi Bakmi = Rp", totalmkn)
       mkn=("Bakmi")
elif nomor == 2:
       totalmkn=porsi*9000
       print (porsi," porsi Soto Tangkar = Rp", totalmkn)
       mkn=("Soto Tangkar")
elif nomor==3:
       totalmkn=porsi*11000
       print (porsi, " porsi Mie Rebus = Rp", totalmkn)
       mkn=("Mie Rebus")
else:
       print("Pilihan tidak ada, silahkan masukan lagi!!")
      


print("\n----------------- Menu Minuman -----------------")
print("1. Es teh - Rp 2000")
print("2. Es jeruk - Rp 3500")
print("3. Es kopi - Rp 4000")
nomor=int(input("Masukan Pilihan: "))
gelas=int(input("Berapa Gelas: "))

if nomor==1:
       totalmnm=gelas*2000
       print (gelas," Es Teh = Rp", totalmnm)
       mnm=(" Gelas Es Teh")
elif nomor==2:
       totalmnm=gelas*3500
       print (gelas, " Gelas Es Jeruk = Rp", totalmnm)
       mnm=("Es Jeruk")
elif nomor==3:
       totalmnm=gelas*4000
       print (gelas, " Gelas Es Kopi = Rp", totalmnm)
       mnm=("Es Kopi")
else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      

totalsemua=totalmkn+totalmnm


print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
if uang >= totalsemua :
    kembalian=int(uang-totalsemua)
    print("Kembalian :",kembalian)

    print("\n==================================")
    print("========== S T R U K   B E L I =========")
    print("==================================")
    print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
    print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
    print ("Tagihan\t\t: Rp",totalsemua)
    print ("Dibayar\t\t: Rp",uang)
    print ("Kembalian\t: Rp",kembalian)
    print("==================================")
    print("==================================")
    
else :
    print("         Uang Anda Kurang           ")