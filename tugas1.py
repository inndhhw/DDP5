#JAWABAN N0 1 

kendaraan = ['Palisade', 'Mobil', 120, 'hitam', 2]
print("kendaraan saya")
print(kendaraan)
print("========")

#Tambahkan daari list tersebut dengan value : [harga kendaraan, tipe kendaraan]
#Kendaraan.append(910000000)
#Kendaraan.append("Metic")
kendaraan.extend([910000000, "Metic"]) 
print(kendaraan)
print("========")

#Tambahkan setelah jenis kendaraan dengan value (merk kendaraan)
kendaraan.insert(2,'palisade')
print(kendaraan)
print("=========")


