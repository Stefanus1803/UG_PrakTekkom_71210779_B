def funPalindrome(kata):
    palindrome = False
    kata = kata.lower()
    reverse_list = []
    akhir = len(kata)-1
    
    for i in kata(akhir, -1, -1):
        reverse_list.append(kata[i])
    terbalik = "".join(reverse_list)
    if terbalik == kata:
        palindrome = True
        print("Yes")
    else:
        print("No")
    return palindrome

kata = str(input("Masukkan Kata: "))
