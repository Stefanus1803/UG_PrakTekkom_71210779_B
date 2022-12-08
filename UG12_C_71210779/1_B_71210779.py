print("SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERLUBANG")
print("=" * 55)
inputan = int(input("Masukkan Angka : "))
print(' '*(inputan - 2), "*")
for piramida in range ((inputan - 2) ,0 , -1):
    print(' '* (piramida - 1), "**")
print ("**" * inputan)