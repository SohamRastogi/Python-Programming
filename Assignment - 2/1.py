def unique_char_count(paragraph):
    word_map = {}
    words = paragraph.lower().split()
    
    for word in words:
        word_map[word] = len(set(word)) 
    
    return word_map

paragraph = "This is a simple test Testing unique character count"
print(unique_char_count(paragraph))

