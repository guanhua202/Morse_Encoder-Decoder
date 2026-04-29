print("Код Морзе")

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

select_func = int(input("Зашифровать/Расшифровать (1, 2): "))

def encrypt_to_morse(message):
    for letter in message:
        if letter in letters:
            for i in range(0, len(letters)):
                if letter == letters[i]:
                    print(morse[i], end=" ")

    print()

def decrypt_to_en(message):
    decrypt_word = ""
    for letter in message.split():
        if letter in morse:
            for i in range(0, len(letters)):
                if letter == morse[i]:
                    decrypt_word += letters[i] + " "
    
    print(decrypt_word)

if select_func == 1:
    message = str(input("Введите сообщение для зашифровки: ")).upper()
    encrypt_to_morse(message)
elif select_func == 2:
    message = str(input("Введите сообщение для расшифровки: "))
    decrypt_to_en(message)