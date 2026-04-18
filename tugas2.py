# Validasi nama
nama_benar = "rido sucipta dama"  # ganti dengan nama pendek yang benar

nama = input("Masukan nama anda: ")

if nama == nama_benar:
    print("Nama benar, lanjut program...\n")
    
    # Input angka
    angka = int(input("Masukkan angka (1-10): "))
    
    if 1 <= angka <= 10:
        # Tabel perkalian
        for i in range(1, 11):
            print(f"{angka} x {i} = {angka * i}")
    else:
        print("Angka harus antara 1 sampai 10")
else:
    print("Silahkan coba lagi")
