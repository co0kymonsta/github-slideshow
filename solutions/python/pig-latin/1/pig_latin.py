def translate(text):
    return " ".join(translate_word(word) for word in text.split())

def translate_word(text):
        
    vowels = ['a', 'e', 'i', 'o', 'u']
    latin = ['xr', 'yt']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    if text.startswith(tuple(vowels)) or text.startswith(tuple(latin)):
        text += 'ay'
        return text  
        
    idx = text.find('qu')
    if text.find('qu') != -1 and all(letter in consonants for letter in text[:idx]):
        idx = text.find('qu')
        text = text[idx +2:] + text[:idx + 2]
        text += 'ay'
        return text

    
    idx = text.find('y')
    if text.find('y') > 0 and all(letter in consonants for letter in text[:idx]):
        text = text[idx:] + text[:idx]
        text += 'ay'
        return text


    if text.startswith(tuple(consonants)):
        while text[0] in consonants:
            text = text[1:] + text[0]
        text += 'ay'
        return text


    