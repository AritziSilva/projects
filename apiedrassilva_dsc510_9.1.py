"""
 File: Assignment 9.1. py
    Author: Aritzi Piedras-Silva
    Date: 10/27/2019
    Course: DSC 510 - Introduction to programing
    Desc: This program will perform 3 essential operations
    it will process a .txt file, calculate all the words listed, and output the number of occurrences of every word
    this program will include a new function called process_file

"""
# import
import string


# gets the word and the the number of times the word is said
def add_words(word, dictionary):
    # this will catch if the word is mentioned in the txt.
    for words in word:
        if words not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] = dictionary[word] +1


# this function will pull out each words from the text for it to be readable
def process_line(line, dictionary):
    # deletes all punctuation
    line = line.translate(line.maketrans('', '', string.punctuation))
    # slices the each word out
    line = line.split()
    # changes caps to lower case
    line = line.lower()
    # eliminates the spaces
    words = line.rsplit()
    for word in words:
        # the words get pulled and figured out the frequency
        add_words(words, dictionary)


# this function replaces pretty_print
def process_file(dictionary,new_file):
    sorted_list = list()
    with open("{}.text".format(new_file),'w') as ne:
        # this sets up the header
        ne.write('Individual word \t \t \t \t \t \t Count' + '\n \n \n -------------------------------')
        for key, value in list(dictionary.items()):
            sorted_list.append(value, key)
            sorted_list.sort(reverse=True)
        for key, value in sorted_list[:]:
            print(key,value)


# this function will access the over all file and re named program
def main():
    #   gets list started
    dictionary = {}
    # accesses the text
    gba_file = open('gettysburg.txt','r')
    #   prompts the user for the name of their file
    new_file = input('Please enter a new name for the file:')
    #   reads the text and creates the dictionary
    for line in gba_file:
        process_line(line, dictionary)
    #   calls the function
    process_file(dictionary, new_file)
    with open("{}.text".format(new_file),'r+') as ne:
        edit = ne.readlines()
        ne.writelines(edit)
        #   grabs the total words in the text
        ne.write('Total words listed: {}')
        ne.seek(0)
    # lets us know that everything is completed
    print('Your file has been saved!! ')


if __name__ == "__main__":
    main()




