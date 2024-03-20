# letter converted to morse
textToMorse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "..--.",
    ":": "---...",
    ";": "-.-.-.",
    "\"": ".-..-.",
    "'": ".----.",
    "+": ".-.-.",
    "-": "-....-",
    "/": "-..-.",
    "=": "-...-"
}

while True:
    myString = input("\nWrite the sentence you want to convert: ")
    for letter in myString:  # For separating letter
        print(textToMorse[letter.lower()], end=" ")

    question = input("\nWould you like to convert a sentence again [Type 'y' to continue or any other letter to exit]? ")
    if question.lower() == "y":
        continue
    else:
        print("Exiting Converter")
        break
