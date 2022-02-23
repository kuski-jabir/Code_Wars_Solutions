#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    new_text = []
    for i in text.split():
        if i.isalnum() == False:
            i = i
        else:
            i = i[1:] + i[0] + 'ay'
        new_text.append(i)

    return " ".join(new_text)