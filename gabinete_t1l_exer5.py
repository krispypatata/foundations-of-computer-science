'''
Keith Ginoel Gabinete
2020-03670
BS CS
'''
'''
Create a program that converts a word into its Pig Latin equivalent. 
According to Wikipedia, "Pig Latin is a language game or argot in which 
words in English are altered, usually by adding a fabricated suffix or 
by moving the onset or initial consonant or consonant cluster of a word to the
end of the word and adding a vocalic syllable to create such a suffix." 

The goal of converting a word to Pig Latin is to conceal the words from those who do not know the rules.

These are the rules in converting a word in English to Pig Latin:
1. For words that begin with consonant sounds, all letters before the initial vowel are placed
at the end of the word sequence. Then, "ay" is added.
2. When words begin with consonant clusters (multiple consonants that form one sound),
the whole sound is added to the end when speaking or writing. Then, "ay" is added.
3. For words that begin with vowel sounds, just add "ay" to the end of the word.

Your program must have at least one function, isPigLatin, that accepts a string and returns the
Pig Latin equivalent of the string.

The output of the program must be a list containing all the PigLatin versions of the inputs.

'''
def isPigLatin(eng_word):                   # define a function that will translate an English word to Pig Latin

    eng_word = eng_word.lower()             # convert all the letters in the given English word to lowercase letters
    consonants = "bcdfghjklmnpqrstvwxyz"    # assign a string that stores all the consonant letters in the alphabet
    pig_word = ""                           # assign an emptry string that will store the Pig Latin version of the English word
    first_consonants = ""                   # assign an empty string that will be used to store all the consonant letters of the English word before its first vowel letter

    for letter in eng_word:                 # express the English word as a sequence in for loop (so we'lll be able to assess each letter in the English word string)
                                            # Write a condition that will determine if the first letter/s of the given English word is/are consonant/s
                                            # If so, those letters will be removed from the beggining of the word and will be placed to the end of the word

        if letter in consonants:
            eng_word = eng_word.replace(letter, "", 1) # to remove/erase a consonant letter at the beggining of the English word, use the replace string funtion
                                                       # replace the consonant at the beginning of the string with an empty substring
                                                       # set the count value of the replace string function to 1 so it will only remove the one copy of that consonant at the beginning of the whole string
            
            first_consonants = first_consonants + letter  # store the removed consonant letter from our string to the empty string first_consonants
        
        # The loop will then be terminated if it already encountered a vowel letter in the given English word
        else:
            break

    pig_word = pig_word + eng_word + first_consonants + "ay" # store the new value of the english word(with consonant letters removed at its beginning part) to the empty string pig_word
                                                             # concatenate the removed consonants to the string pig_word
                                                             # add the string "ay" to complete the Pig Latin version of the English Word
    
    return pig_word                         # return the resulting pig_word string to terminate the definition function


def translist(list1):                       # define a function that will translate all the English words in a given list with the help of our definition function isPigLatin
    
    newlist = []                            # assign a new empty list that will store the Pig Latin versions of all the English words from our given list
    
    # express our given list as a sequence in a loop for us to use our isPigLatin function to each string contained inside the list
    for eng_word in list1:
        # append the translated word to our empty newlist
        newlist.append(eng_word + " ==> " + isPigLatin(eng_word))   

    # add a print statement for the "Output" title
    print("\nOutput:")

    return newlist                          # return the contents of our new list to terminate the definition function


def inputWords():                           # define a function definition that will ask for an english word input from the user
    
    # Ask the user for how many English words does he/she want to translate.
    number_words = int(input("How many English words would you like to translate to Pig Latin? "))
    
    # print an empty string just so there's an empty row that separates the number_words input and the next (to be defined) input 
    print("")

    list1 = []                              # assign a list that will store all the English words entered by the user

    count = 0                               # initialization part for our while loop     
    while count < number_words:             # write a loop that will ask the user to enter inputs for n times
        
        eng_word = str(input("Enter an english word: ")) # typecast the input so the english word will be stored as a string in our list
        list1.append(eng_word)                           # append the English word to our list
        count += 1                                       # increment the value of count

    return list1                            # return the list containing all the English words entered by the user

print("\n\tWelcome! This program converts words into their Pig Latin equivalents.", end="\n\n")

# invoke our translist and inputWords definition functions
# express the resulting list (from our definition function translist()) as sequence in a for loop so we can print every element of it separately in new lines
for pair in translist(inputWords()):           
    print(pair) # print all the Pig Latin versions of the English words
