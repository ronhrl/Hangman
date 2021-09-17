MAX_TRIES = 6
HANGMAN_PHOTOS = {1: "x-------x", 2: """x-------x
|
|
|
|
|
""", 3: """x-------x
|       |
|       0
|
|
|
""", 4: """x-------x
|       |
|       0
|       |
|
|
""", 5: """x-------x
|       |
|       0
|     / | \\
|       
|
""", 6: """x-------x
|       |
|       0
|     / | \\
|     /   
|
""", 7: """x-------x
|       |
|       0
|     / | \\
|     /   \\
|
"""}


def print_open_screen():
    print("""Welcome to the game hangman
      _    _                                         
     | |  | |                                        
     | |__| |  __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                          __/ |                      
                         |___/""")
    print(MAX_TRIES)


def choose_word(file_path_to_choose_word, index_to_chose_word):
    open_file = open(file_path_to_choose_word, 'r')
    list_of_unique_words = list()
    list_of_all_words = list()
    count_of_words = 0
    for line in open_file:
        for word in line.split(" "):
            count_of_words += 1
            list_of_all_words.append(word)
            if word not in list_of_unique_words:
                list_of_unique_words.append(word)
            else:
                continue
    word_to_guess = list_of_all_words[(index_to_chose_word - 1) % count_of_words]
    return word_to_guess


def check_win(secret_word_check_win, old_letters_guessed_check_win):
    i = 0
    count_of_correct = 0
    while i < len(secret_word_check_win):
        j = 0
        while j < len(old_letters_guessed_check_win):
            if secret_word_check_win[i] == old_letters_guessed_check_win[j]:
                count_of_correct += 1
                j += 1
                break
            j += 1
        i += 1
    if count_of_correct == len(secret_word_check_win):
        return True
    else:
        return False


def show_hidden_words(secret_word_to_show, old_letters_guessed_to_show):
    i = 0
    str_to_guess = ""
    while i < len(secret_word_to_show):
        j = 0
        while j < len(old_letters_guessed_to_show):
            if secret_word_to_show[i] == old_letters_guessed_to_show[j]:
                str_to_guess += old_letters_guessed_to_show[j]
                j += 1
                break
            j += 1
            if j == len(old_letters_guessed_to_show):
                str_to_guess += " _ "
                break
        i += 1
    return str_to_guess


def check_valid_input(letter_guessed, old_letter_guessed):
    lower = letter_guessed.lower()
    if not letter_guessed.isalpha():
        return False
    elif len(letter_guessed) > 1:
        return False
    elif lower in old_letter_guessed:
        return False
    else:
        return True


def print_hangman(num_of_wrong_tries):
    print(HANGMAN_PHOTOS[num_of_wrong_tries])


def try_update_letter_guessed(letter_guessed, old_letters_guessed_update):
    is_valid = check_valid_input(letter_guessed, old_letters_guessed_update)
    if is_valid:
        old_letters_guessed_update.append(letter_guessed)
        return True
    else:
        print("X")
        old_letters_guessed_update.sort()
        arrow = "->"
        print_string_arrows = arrow.join(old_letters_guessed_update)
        print(print_string_arrows)
        return False


if __name__ == '__main__':
    print_open_screen()
    file_path = input("Enter file path: \n")
    index = input("Enter index: \n")
    print("Let's start!\n")
    num_of_tries = 1
    print_hangman(num_of_tries)
    secret_word = choose_word(file_path, int(index))
    old_letters_guessed = list()
    print(show_hidden_words(secret_word, old_letters_guessed))
    has_won = False
    while num_of_tries <= 6:
        if check_win(secret_word, old_letters_guessed):
            print("WIN")
            has_won = True
            break
        guessed_letter = input("Please choose a letter: ")
        if not try_update_letter_guessed(guessed_letter, old_letters_guessed):
            continue
        else:
            if guessed_letter not in secret_word:
                num_of_tries += 1
                print(":-(")
                print_hangman(num_of_tries)
                print(show_hidden_words(secret_word, old_letters_guessed))
            else:
                print(show_hidden_words(secret_word, old_letters_guessed))
    if not has_won:
        print("LOOSE")
