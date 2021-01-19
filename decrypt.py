# Load dictionary
dictionary = list(open("words.txt").read().splitlines())


def matchWords(current_guess):
    matches = []

    for word in dictionary:
        if current_guess.__contains__(word):
            matches.append(word)

    return matches


def main(input_msg):
    # Declarations
    max_words = 0
    best_key = 0
    decrypted_msg = ""
    most_words = []

    # Try every key up to the max size of a 16 bit signed integer
    for key in range(-26, 26):
        current_guess = ""
        matched_words = []

        # Shift the message by the current key
        for c in list(input_msg):
            if c != "":
                c = chr(ord(c) - key)
            current_guess = current_guess + str(c)

        # See how much sense this guess makes
        matched_words = matchWords(current_guess)

        # Update the best guess
        if len(matched_words) > max_words:
            max_words = len(matched_words)
            best_key = key
            decrypted_msg = current_guess
            most_words = matched_words

        print("Guessing...")
        print("KEY=" + str(key))
        print("RESULT=" + current_guess)
        print("FOUND=" + str(matched_words))
        print("-------------------------------------------------------------")

    print("")
    print("*************************************************************")
    print("Best guess: ")
    print("Key = " + str(best_key))
    print("Message = " + decrypted_msg)
    print("Found words = " + str(most_words))
    print("*************************************************************")


inputMsg = input("Please enter the encrypted message: ").lower()
main(inputMsg)
