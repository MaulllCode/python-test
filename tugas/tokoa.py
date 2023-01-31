kota = "luar"
belanja = 290000

if(kota == "mlg"):
    if(belanja <= 50000):
        print("Ongkir kota malang Rp.20000")
    elif(belanja < 100000):
        print("Ongkir kota malang Rp.10000") 
    elif(belanja >= 100000):
        print("Ongkir kota malang Gratis")
elif(kota == "luar"):
    if(belanja <= 100000):
        print("Minimal Belanja Rp.300000")
    elif(belanja < 300000):
        print("Ongkir luar kota malang Rp.20000")
    elif(belanja >= 300000):
        print("Ongkir luar kota malang Gratis")
