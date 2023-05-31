'''This program will display each alternative character uppercase and lowercase'''

word = "Hello Word"
final_word = ""

for i in range (len(word)):
    if i % 2 == 0: # every even letter will be uppercase, odd - lowercase
        final_word += word [i].upper()
    else:
        final_word += word [i].lower()

print(final_word)

'''This program will display each alternative word uppercase and lowercase'''

sentence = "I am learning to code"
split_sentence = sentence.split() # each word will have own index
final_sentence = " "

for i in range(len(split_sentence)):
    if i % 2 == 0:  # every even letter will be uppercase, odd - lowercase
        final_sentence += split_sentence [i].lower() + " "
    else:
        final_sentence += split_sentence [i].upper() + " "
                            
print(final_sentence)

'''I tried to use " ".join(), but it will give spase between each letter, how do I make space between words with " ".join() method?'''


'''sentence = "I am learning to code"
split_sentence = sentence.split() # each word will have own index
final_sentence = []

for i in range(len(split_sentence)):
    if i % 2 == 0:  # every even letter will be uppercase, odd - lowercase
        final_sentence += split_sentence [i].lower()
    else:
        final_sentence += split_sentence [i].upper()
        
        " ".join(final_sentence )
                            
print(final_sentence)'''

