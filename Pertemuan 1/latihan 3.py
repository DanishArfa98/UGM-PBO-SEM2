NIU = int(input("NIU BERAPA BOS = "))
ntugas = int(input("nilai tugas = "))
nlaporan = int(input("nilai laporan = "))

rata = (ntugas+nlaporan)/2
if rata < 40 :
    print("nilai akhir : K ")
else:
    nUjian = int(input("nilai ujian = "))
    nakhir = (0.25*ntugas) + (0.25*nlaporan) + (0.50*nUjian)
    if 80 <= nakhir <= 100 :
        print("nilai A")
    elif 70 <= nakhir < 80 :
        print("nilai B")
    elif 60 <= nakhir < 70 :
        print("nilai C")
    elif 50 <= nakhir < 60 :
        print("nilai D")
    else:
        print("nilai E")