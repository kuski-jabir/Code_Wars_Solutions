#Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. 
# Spaces will be included only when more than one word is present.

def spin_words(sentence):
    spinned_sentence = []
    for i in sentence.split():
        if len(i) >= 5:
            i = i[::-1]
        spinned_sentence.append(i)
    return " ".join(spinned_sentence)