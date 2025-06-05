try :
    f = open("ans18.txt" , "r")
except OSError as err :
    print("OS error : " , err)

from collections import Counter 

data = f.read()

f.close()



def max_frequency_word(word_dict):
    if not word_dict:  # Check if dictionary is empty
        return "Error: Dictionary is empty."

    # Find the word with the highest frequency
    max_word = max(word_dict, key=word_dict.get)
    
    return max_word, word_dict[max_word]

words = data.split()
word_freq = Counter(words)

print(max_frequency_word(word_freq))
