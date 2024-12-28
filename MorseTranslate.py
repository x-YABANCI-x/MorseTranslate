MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',    'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',   'V': '...-', 'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',  '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

# yazıyı mors koduna çevirme fonksiyonu
def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char != " ":
            morse_code.append(MORSE_CODE_DICT.get(char, ''))
        else:
            morse_code.append("/")
    return " ".join(morse_code)

# mors kodunu yazıya çevirme fonksiyonu
def morse_to_text(morse):
    morse_code_dict_reverse = {v: k for k, v in MORSE_CODE_DICT.items()}
    text = []
    for code in morse.split(" "):
        if code != " ":
            text.append(morse_code_dict_reverse.get(code, ''))
        else:
            text.append("/")
    return "".join(text)

print("Lütfen yapmak istediğiniz işlemi seçin:")
print("1) Text to Morse")
print("2) Morse to Text")

choice = input("Seçiminizi yapın (1 veya 2): ")

if choice == '1':
    # text to morse
    text = input("Bir metin girin : ")
    morse_code = text_to_morse(text)
    print("Text to Morse :", morse_code)

elif choice == '2':
    # morse to text
    morse_text = input("Bir Mors kodu girin: ")
    normal_text = morse_to_text(morse_text)
    print("Morse to Text:", normal_text)

else:
    print("Geçersiz seçim. Lütfen 1 veya 2 girin.")
