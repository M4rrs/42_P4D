import sys


def convert(x, morse: dict):
    return morse.get(x)


def main():
    NESTED_MORSE = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        " ": "/",  # Space character
    }
    try:
        assert len(sys.argv) == 2, "Assertion Error: bad arguments."

        string = (str(sys.argv[1])).upper()
        # assert (string).isalnum(), (
        assert all(x.isalnum() or x.isspace() for x in string), (
            "Assertion Error: Non-alphanumeric characters found."
        )

        morseString = " ".join(map(lambda x: convert(x, NESTED_MORSE), string))
        print(morseString)

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
