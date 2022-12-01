def funPalindrome(word):
    word = word.lower()
    Palindrome = 'Yes' if word == word[::-1] else 'No'
    return f'{Palindrome}\nJika Dibalik: {word[::-1]}'
    
word = str(input('Masukan word: '))
print(funPalindrome(word))