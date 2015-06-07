"""
Translates words into a version of Pyg Latin
in which the user can choose the suffix too
Created by: Barbora Doslikova
Date: 05/06/2015
Version: 3.0
"""

# returns the combined user's word and suffix of choice
# translated into pyg latin
def translates():
    word = input("Enter a word:")
    suffix = input("Enter a suffix:")

    if word.isalpha() and suffix.isalpha():
        print("Your word translates to " + combine(word, suffix) + " in the Generic Translator!")
    else:
        print ("Looks like you entered an incorrect word or a suffix, please try again.")
        translates()
    
# returns the combined word and suffix
# converted to lower case
def combine(word, suffix):
    return transform(word).lower() + suffix.lower()

# returns the word in which the 1st letter is added to the end
def transform(word):
    word = word[1:len(word)] + word.lower()[0]
    return word

print ("Welcome to the Generic Translator!")
translates()
