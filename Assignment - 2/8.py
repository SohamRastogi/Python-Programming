import hashlib 

sentence = "welcome to Python Programming it is a very easy to learn language"

list = sentence.split(" ")

list_encoded = []

for i in list :
    hash_value = hashlib.sha256(i.encode()).hexdigest()
    list_encoded.append(hash_value)

print(list_encoded)
