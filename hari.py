hari = "jumat"
upacara = 0
produktif = 0
if(hari == "senin"):
    if(upacara == 1):
        print("Senin = Abu-abu Putih dan almamater")
    if(produktif == 1):
        print("Senin = Abu-abu Putih dan katelpak")
    else:
        print("Senin = Abu-abu Putih")
elif(hari == "selasa"):
    if(produktif == 1):
        print("Selasa = Abu-abu Putih dan katelpak")
    else:
        print("Selasa = Abu-abu Putih")
elif(hari == "rabu"):
    if(produktif == 1):
        print("Rabu = Batik dan katelpak")
    else:
        print("Rabu = Batik")
elif(hari == "kamis"):
    if(produktif == 1):
        print("Kamis = Batik dan katelpak")
    else:
        print("Kamis = Batik")
elif(hari == "jumat"):
    if(produktif == 1):
        print("Jumat = Pramuka dan katelpak")
    else:
        print("Jumat = Pramuka")
elif(hari == "sabtu"):
    print("Libur")
elif(hari == "minggu"):
    print("Libur")