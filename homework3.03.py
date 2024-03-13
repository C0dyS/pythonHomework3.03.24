
from googletrans import Translator

translator = Translator()


def remove(my_dict,word):
    del my_dict[word]
    return my_dict

def find_translation(my_dict,word):
    if word in my_dict:
        return my_dict.get(word)
    else:
        translated_word = translator.translate(word, src='en', dest='fr')
        my_dict[word] = translated_word.text
    return translated_word.text

def change_translation(my_dict,word,translated_word):
    my_dict[word]=translated_word
    return my_dict
def check_translation(my_dict,word):
    return my_dict.get(word)

def main():
    eng_to_fr_dict = {}
    while True:
        try:
            choice = int(input('''Please choose:
                1 - Translate word (checks, if word not found translated and add to dictionary)
                2 - Remove translation
                3 - Change translation
                4 - Check for translation (only checks)
                5 - Exit
                '''))
            if choice == 1:
                word_var = str(input('Type word to translate: ').lower())
                print(find_translation(eng_to_fr_dict, word_var))
            elif choice == 2:
                word_var = str(input('Type word to remove: ').lower())
                print(remove(eng_to_fr_dict, word_var))
            elif choice == 3:
                word_var, word_var2 = map(str, input('Type word and then its translation: ').split())
                word_var = word_var.lower()
                word_var2 = word_var2.lower()
                print(change_translation(eng_to_fr_dict, word_var, word_var2))
            elif choice == 4:
                word_var = str(input('Type word to check: ').lower())
                print(check_translation(eng_to_fr_dict, word_var))
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print('Invalid input. Please enter a valid number.')

main()