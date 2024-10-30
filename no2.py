print("Ini adalah program sederhana untuk menghitung luas bangun datar")
print("Pilih Menu angka 1-3 : \n1. Persegi\n2. Lingkaran\n3. Segitiga")
pilihmenu = int(input("Silahkan pilih menu dengan mengetikan angka 1-3 : "))

match pilihmenu:
    case 1:
        print("Ini adalah menu untuk menghitung luas persegi")
        sisi = int(input("Silahkan masukan nilai yang mau di hitung: "))
        hitung = sisi * sisi
        print(f"luas persegi adalah : {hitung}")

     case 2:
        print("Luas Lingkaran = phi*r*r")
        r= int(input("Masukan Angka anda"))
        phi= 3.14
        luas= phi*r*r
        print(int(luas))

     case 3:
        print("Ini adalah operasi luas segitiga")
        alas= int(input('Masukan alas:'))
        tinggi= int(input('Masukan tinggi:'))

        luas_segitiga= int(1/2*alas*tinggi)
        print(f"luas segitiga = 1/2 *', alas, '*', tinggi. '=', luas_segitiga")
    case _:    
        print("Pilihan tidak valid, silahkan pilih antar 1-3")