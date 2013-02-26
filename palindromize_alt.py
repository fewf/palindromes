import re

class Palindrome:
    text = ""

    def __init__(self, prePal, start = False):
        if start:
            rightString = re.sub("[\W\d\s]", "", prePal).lower()[::-1]
            self.text = prePal + " " + rightString
        else:
            self.text = prePal

    def firstHalf(self):
        return self.justLetters()[0:len(self.justLetters())/2]

    def secondHalf(self):
        return self.justLetters()[len(self.justLetters())/2 + len(self.justLetters())%2:]

    def justLetters(self):
        return re.sub("[\W\d\s]", "", self.text).lower()

    def isOdd(self):
        return True if len(self.justLetters()) % 2 else False

    def isPalindrome(self):
        return True if self.firstHalf() == self.secondHalf()[::-1] else False

    def palindromize(self):

        palArray = [self.justLetters()]
        counter = 0
        go = True
        while (go):
            arrayCopy = palArray[:]
            counter += 1
            i = 0
            go = False
            for index in range(len(arrayCopy)):
                if not(arrayCopy[index].startswith("{")) and not(arrayCopy[index].startswith("[")) and len(arrayCopy[index]) > 1:
                    newArray = findLongestPal(arrayCopy[index], counter)
                    palArray[index:index+1]= newArray
                    go = True
                i += 1


        print " ".join(palArray)

def findLongestPal(justLetters, iters = 1):
    # Takes any arbitrary string of only letters (no digits, spaces or
    # punctuation) and will find largest palindrome and return an array of:
    # 
    # [ any chars before the left half of the largest palindrome,
    #   left half of the palindrome ("to" in "toot") in curly brackets,
    #   any chars between left and right halves of the palindrome,
    #   right half of the palindrome ("ot" in "toot") in curly brackets,
    #   any chars after right half of the largest palindrome ]
    # 
    # i.e., "abtocdotef" will return ["ab", "{to}", "cd", "{ot}", "ef"]
    # 
    # If no palindrome is found will return an array of the original string
    # with square brackets around it.
    #
    # i.e., "abcdefghjikl" will return ["[abcdefghijkl]"]
    #
    # arg iter represents how many curly brackets to put around for keeping
    # track of recurring calls

    palLength = len(justLetters)
    counter = 1

    # DOUBLE LOOP OF WONDER:
    # "i" represents the length of a substring being inspected starting at
    # the full length of the string and decrementing until 1. "counter" 
    # represents the number of substrings of length i in the string and by 
    # incrementing "o" from 0 to "counter", o becomes the position in the 
    # string to start a substring and "i+o" will be the end position of the 
    # substring. this ultimately looks at every substring of the original
    # sting of length more than one

    # ie, the string "abcde" would be analyzed in this order:
    # abcde
    # abcd
    # bcde
    # abc
    # bcd
    # cde
    # ab
    # bc
    # cd
    # de

    for i in range (palLength,1,-1):
        for o in range (counter):

            # leftHalf being the substring being checked for it reverse in the string
            # rightHalf being the reverse of leftHalf
            leftHalf = justLetters[o:i+o]
            rightHalf = leftHalf[::-1]

            # make that search, only looking to the right of leftHalf
            rightPos = justLetters.find(rightHalf, i+o)

            if rightPos != -1:

                # prePal, twixtPal and postPal chop up the substrings that are
                # before, between and after the palindrome found.
                prePal = justLetters[:o]

                twixtPal = justLetters[i+o:rightPos]

                postPal = justLetters[rightPos + i:]

                palArray = [prePal, "{"*iters + leftHalf + "}"*iters, twixtPal, "{"*iters + rightHalf + "}"*iters, postPal]

                # remove empty strings from the palindrome
                palArray = [x for x in palArray if x]

                return palArray

        counter += 1

    # if you got down here, there's no palindrome in the string
    return ["[" + justLetters + "]"]  

palindrome2 = Palindrome("Boston ode: fdwqtas do not sob. Todd erase(the fulcrum is here!)s a red dot. Son, I sack fdwqtas casinos.")
palindrome2.palindromize()