print("~~~ Selamat Datang di Kalkulator Sederhana ~~~")    
inputan = str(input("Masukkan operator matematika : "))
mau = "y"
while mau != "t":
    if inputan == "+":
        x = int(input("Mau penjumlahan berapa : "))
        y = int(input("print berapa banyak : "))
        for i in range(1,y+1):
            jum = i + x
            print(f"{i} + {x} = {jum}")
            x -= 1
    
    elif inputan == "-":
        x = int(input("Mau pengurangan berapa : "))
        y = int(input("print berapa banyak : "))
        for i in range(1,y+1):
            jum = i - x
            print(f"{i} - {x} = {jum}")
            x -= 1

    elif inputan == "x":
        x = int(input("Mau perkalian berapa : "))
        y = int(input("print berapa banyak : "))
        for i in range(1,y+1):
            jum = i * x
            print(f"{i} X {x} = {jum}")
            x -= 1
    
    elif inputan == ":":
        x = int(input("Mau pembagian berapa : "))
        y = int(input("Print berapa banyak : "))
        for i in range(1,y+1):
            jum = i / x
            print(f"{i} : {x} = {jum}")
            x -= 1
    else:
        print("Maaf, Operator Matematika yang anda cari belum tersedia.")
        exit()
    print()
    nanya = str(input("Apakah anda ingin menghitung lagi? (Y/T): "))
    if nanya.lower() == 'y':
        mau = 'y'
    else:
        mau = 't'
print()
print("<<< Terima Kasih dan Sampai Jumpa Lagi >>>")