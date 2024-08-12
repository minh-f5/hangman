

def get_word():
    word = input("Enter the hidden word: ").lower()
    return word

def get_lives():
    lives = int(input("Enter number of lives: "))
    if lives>0:
         return lives
    else:
        print(" please enter one number is greater than 0")






def get_guess(word,guessed_letters):

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter 
        else:
            display_word += "_"

    return display_word

                


    
    
def assess_guess(secret_word,guessed_letter,lives_left):
    # secret_word = get_word()
    word_len=len(secret_word)
    guessed_letter = []
    wrong_guessed_letter=[]
    error_count=0
    # lives=get_lives()
    

    print("Let's go!")
    print(f"This word has {word_len} letters" )
    print("Secret Word:", get_guess(secret_word, guessed_letter))
    while lives_left >0:
        guess= input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("You must enter a single letter.")
            continue
        if guess in guessed_letter:
            print("You already guessed that letter. Please enter another letter: ")
            continue 
        guessed_letter.append(guess)
        if guess not in secret_word:
            lives_left -=1
            wrong_guessed_letter.append(guess)
            error_count+=1
            print(f"No letter '{guess}'  in the word.")
            print(f"You have {lives_left} lives.")
            print(f"you have {error_count} times get wrong letter")
            print(wrong_guessed_letter)
            
               

        else:
            appearence_count = secret_word.count(guess)
            print(f"Letter '{guess}' appear(s) {appearence_count} times.")
        current_status = get_guess(secret_word, guessed_letter)
        print("Secret Word:", current_status)  
        if "_" not in current_status:
            print("Congratulations! You guessed the word.")
            break     
    
    if "_" in current_status:

        print(f"You don't have any life! The word was: {secret_word}")
    
         




def main():
    
    secret_word = get_word()
    lives_left=get_lives()
    guessed_letter = []
    assess_guess(secret_word,guessed_letter,lives_left)
    

main()







