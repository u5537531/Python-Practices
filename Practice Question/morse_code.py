def morse_translator(text):
    # Morse code representation for each alphabet
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..'
    }

    # Split the text into words and translate each character
    morse_translated = []
    for word in text.upper().split():
        morse_word = []
        for char in word:
            if char in morse_code_dict:
                morse_word.append(morse_code_dict[char])
        morse_translated.append(' '.join(morse_word))

    return ' / '.join(morse_translated)
print(morse_translator("HELLO WORLD"))
print(morse_translator("Python")) 
print(morse_translator("Morse Code"))