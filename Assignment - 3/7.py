try :
    f = open("ans7.txt")
except OSError as err:
    print("OS Error : ", err)

data = f.read()
f.close()

# now we have access to data where data variable corresponds to the content of the text file opened

from collections import Counter

words = data.split()

word_freq = Counter(words) 

print(word_freq)

