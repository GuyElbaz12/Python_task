import os
"""The os module is imported to use os.system for clearing the terminal screen during the game."""

def print_opening_screen():
    """printing the opening screen"""
    print("""
     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___/  
    """)

def choose_word(index):
    """This function reads a list of words from an array. The words are split into a list, and the word at the specified index is returned."""
    with open(r'C:\Users\User\Desktop\words.txt', 'r') as file:
        words = file.read().split()
    return words[index]

def print_hangman(num_of_tries):
    """This function prints the hangman picture based on the number of incorrect tries"""
    HANGMAN_PHOTOS = {
        0: """
           ____
          |    |
          |
          |
          |
          |
        =========
        """,
        1: """
           ____
          |    |
          |    O
          |
          |
          |
        =========
        """,
        2: """
           ____
          |    |
          |    O
          |    |
          |
          |
        =========
        """,
        3: """
           ____
          |    |
          |    O
          |   /|
          |
          |
        =========
        """,
        4: """
           ____
          |    |
          |    O
          |   /|\\
          |
          |
        =========
        """,
        5: """
           ____
          |    |
          |    O
          |   /|\\
          |   /
          |
        =========
        """,
        6: """
           ____
          |    |
          |    O
          |   /|\\
          |   / \\
          |
        =========
        """
    }
    print(HANGMAN_PHOTOS.get(num_of_tries, ""))

def show_hidden_word(secret_word, old_letters_guessed):
    """This function returns a string that represents the current state of the guessed word. """
    hidden_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word += letter
        else:
            hidden_word += "_"
    return hidden_word

def check_valid_input(letter_guessed, old_letters_guessed):
    """This function checks if the guessed letter is valid"""
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed not in old_letters_guessed

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """This function add guessed letter to te list if not correct and while repeat on a letter or input a unvalid letter print x  and than the list"""
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        return False

def print_sorted_guessed_letters(old_letters_guessed):
    """This function prints the guessed letters"""
    sorted_letters = sorted(old_letters_guessed)
    print(" -> ".join(sorted_letters))

def check_win(secret_word, old_letters_guessed):
    '''This function checks if the player has won by verifying that all letters in the secret word have been guessed.'''
    return all(letter in old_letters_guessed for letter in secret_word)

def main():
    print_opening_screen()
    index = int(input("Enter the position (index) for the word in the file: "))

    secret_word = choose_word(index)

    old_letters_guessed = []
    MAX_TRIES = 6
    num_of_tries = 0

    while num_of_tries < MAX_TRIES:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print_hangman(num_of_tries)
        print(show_hidden_word(secret_word, old_letters_guessed))
        letter_guessed = input("Guess a letter: ").lower()

        if not try_update_letter_guessed(letter_guessed, old_letters_guessed):
            print("X")
            print_sorted_guessed_letters(old_letters_guessed)
            continue

        if check_win(secret_word, old_letters_guessed):
            print(secret_word)
            print("WIN")
            return

        if letter_guessed not in secret_word:
            num_of_tries += 1

    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))
    print("LOSE")

if __name__ == "__main__":
    main()
