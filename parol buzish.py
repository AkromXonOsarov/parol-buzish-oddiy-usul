from random import randint

userPass = input("Parolni kiriting: ")

password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

guessPass = ""
while guessPass != userPass:
    guessPass = ""
    for letter in range(len(userPass)):
        guessLetter = password[randint(0,20)]
        guessPass += str(guessLetter)

    print("Parol topildi:", guessPass)


