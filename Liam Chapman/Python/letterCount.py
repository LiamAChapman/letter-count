__author__ = 'Liam Chapman'
__email__ = "liamanthonychapman@gmail.com"


import sys


def main():
    '''
        Main.
        
        Check the number of command line arguments.
        Either use the supplied file, or if missing ask for user input.
        '''
    if(len(sys.argv) == 2):
        fileName = sys.argv[1]
        getLetterCountFromFile(fileName)
    else:
        inputText = input("Enter File Name:> ")
        getLetterCountFromFile(inputText)



def getLetterCountFromFile(fileName):
    '''
        Open file for reading.
        
        Try to open file (read only).
        Get letterCount array.
        Close file and return array.
        If IOError show error message.
        '''
    try:
        with open(fileName,"r") as f:
            letterCount = countLetters(f)
            displayLetterCount(letterCount)
            return letterCount
    except IOError:
        print("Sorry I can not find the file: \"{0}\"".format(fileName))
        pass



def countLetters(f):
    '''
        Add count of letter into array.
        
        Initialise an array with 26 elements (one for each letter of the alphabet).
        For each letter in the line, check it is an alpha character.
        Set all characters to uppercase and find ascii value.
        Find index in letterCount array by zeroing ascii value.
        Increment counter at the given array index.
        Close file and return the array
        '''
    letterCount = [0] * 26
    for line in f:
        for letter in line:
            if(letter.isalpha()):
                letterCount[ord(letter.upper()) - 65] += 1
    return letterCount

def displayLetterCount(letterCount):
    
    '''
        Display the quantity of each letter
        
        For each element in the letterCount array, print its count value
        and  the character it represents (adding the ascii offset)
        '''
    for counter, x in enumerate(letterCount):
        if x > 0:
            print("{0} Appears {1} times".format(chr((counter + 65)),str(x)))


main()
