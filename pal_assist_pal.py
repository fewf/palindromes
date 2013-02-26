import re
import readline

def main(pal):
    while True:
        print "What would you like to do?"
        print "A: Start a Palindrome"
        print "B: Edit Current Palindrome"
        print "C: Save Current Palindrome"
        print "D: Read All Palindromes"
        print "E: Search For a Palindome"
        print "F: Exit "
        answer = raw_input()
        if answer == "A":
            startPalindrome(pal)
        elif answer == "B":
            editPalindrome(pal)
        elif answer == "C":
            savePalindrome(pal)
        elif answer == "D":
            showPalindromes()
        elif answer == "E":
            searchPalindromes()
        elif answer == "F":
            break
        else:
            print "Huh? I only understand letters A-F"

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
        # find the largest palindrome in a string of text
        # first idea: check for palindromes in substrings approaching the center of the string
        rawPal = self.justLetters()
        palLength = len(rawPal)
        go = True
        array = findLongestPal(rawPal)
        counter = 1
        while (go):
            print array
            arrayCopy = array[:]
            counter += 1
            i = 0
            for piece in arrayCopy:
                if piece[0:1] != "{" and piece[0:1] != "[" and len(piece) > 1:
                    newArray = findLongestPal(piece, counter)
                    array[array.index(piece):array.index(piece)+1]= newArray
                i += 1
            go = False
            for piece in array:
                if piece[0:1] != "{" and piece[0:1] != "["  and len(piece) > 1:
                    go = True
                    break

        print " ".join(array)
        # for i in range(1,palLength/2):
        #     testPal = Palindrome(rawPal[i:-i])
        #     if testPal.isPalindrome():
        #         palindromeToCheck = rlinput("Palindromized:", rawPal[0:i] + " {" + testPal.text + "} " + rawPal[-i:])
        #         break
        # next idea:
        # stop = False
        # counter = 1
        # for i in range (palLength,0,-1):
        #     for o in range (counter):
        #         print "from " + str(o) + " to " + str(i+o) + ": " + rawPal[o:(i+o)]
        #         lapWar = rawPal.find(rawPal[o:i+o][::-1])
        #         twixtPal = rawPal[i+o:lapWar]
        #         if lapWar != -1 and twixtPal:
        #             print "o is " + str(o)
        #             print "i is " + str(i)
        #             print "o+i is " + str(o + i)
        #             print "lapWar is " + str(lapWar)
        #             prePal = rawPal[:o]
        #             leftPal = rawPal[o:i+o]
        #             rightPal = rawPal[lapWar:lapWar + i]
        #             postPal = rawPal[lapWar + i:]

        #             print prePal + "{" + leftPal + "}" + twixtPal + "{" + rightPal + "}" + postPal if twixtPal else prePal + "{" + leftPal + "}" + postPal


        #             # print rawPal[:o] + "{" + rawPal[o:i+o] + "}" + rawPal[i+o:lapWar] + "{" + rawPal[lapWar:lapWar + i] + "}" + rawPal[lapWar + i:]
        #             stop = True
        #             break
        #     if stop: break
        #     counter += 1    

class Tree(object):
    def __init__(self, string):
        self.pre = None
        self.left = None
        self.twixt = None
        self.right = None
        self.post = None
        self.string = string
        self.length = len(string)

    def __str__(self):
        if self.isNub():
            return self.string
        else:
            return self.pre.string + self.left + self.twixt.string + self.right + self.post.string
            # print self.pre
            # print self.left
            # print self.twixt
            # print self.right
            # print self.post

    def isNub(self):
        return True if not(self.pre) else False

def findLongestPal(rawPal, count = 1):
    palLength = len(rawPal)
    stop = False
    counter = 1
    for i in range (palLength,0,-1):
        for o in range (counter):
            # print "from " + str(o) + " to " + str(i+o) + ": " + rawPal[o:(i+o)]
            lapWar = rawPal.find(rawPal[o:i+o][::-1], i+o)

            if lapWar != -1:
                # print "o is " + str(o)
                # print "i is " + str(i)
                # print "o+i is " + str(o + i)
                # print "lapWar is " + str(lapWar)
                twixtPal = rawPal[i+o:lapWar]
                prePal = rawPal[:o]
                leftPal = rawPal[o:i+o]
                rightPal = rawPal[lapWar:lapWar + i]
                postPal = rawPal[lapWar + i:]

                return [prePal, "{"*count + leftPal + "}"*count, twixtPal, "{"*count + rightPal + "}"*count, postPal]
                # return [[prePal, twixtPal, postPal], ["{"*count + leftPal + "}"*count,  "{"*count + rightPal + "}"*count]]

                # print rawPal[:o] + "{" + rawPal[o:i+o] + "}" + rawPal[i+o:lapWar] + "{" + rawPal[lapWar:lapWar + i] + "}" + rawPal[lapWar + i:]
        counter += 1
    return ["[" + rawPal + "]"]  

def findLongestPalInTree(tree):
    text = tree.string
    stop = False
    counter = 1
    for i in range (tree.length,0,-1):
        for o in range (counter):
            # print "from " + str(o) + " to " + str(i+o) + ": " + rawPal[o:(i+o)]
            lapWar = text.find(text[o:i+o][::-1])
            twixtPal = text[i+o:lapWar]
            if lapWar != -1 and twixtPal:
                # print "o is " + str(o)
                # print "i is " + str(i)
                # print "o+i is " + str(o + i)
                # print "lapWar is " + str(lapWar)
                prePal = text[:o]
                leftPal = text[o:i+o]
                rightPal = text[lapWar:lapWar + i]
                postPal = text[lapWar + i:]

                tree.pre = Tree(prePal) if len(prePal) > 1 else prePal
                tree.left = leftPal
                tree.twixt = Tree(twixtPal) if len(twixtPal) > 1 else twixtPal
                tree.right = rightPal
                tree.post = Tree(postPal) if len(postPal) > 1 else postPal

                stop = True
                break
                # return [prePal, "{"*count + leftPal + "}"*count, twixtPal, "{"*count + rightPal + "}"*count, postPal]
                # return [[prePal, twixtPal, postPal], ["{"*count + leftPal + "}"*count,  "{"*count + rightPal + "}"*count]]

                # print rawPal[:o] + "{" + rawPal[o:i+o] + "}" + rawPal[i+o:lapWar] + "{" + rawPal[lapWar:lapWar + i] + "}" + rawPal[lapWar + i:]
        if stop: break
        counter += 1
    if not(stop): tree = tree.string

def loopTree(tree):
    if tree.isNub():
        findLongestPalInTree(tree)
        if isinstance(tree, Tree):
            for branch in [tree.pre, tree.twixt, tree.post]:
                if isinstance(branch, Tree):
                    newTree = branch
                    loopTree(newTree)
        else:
            pass
    elif isinstance(tree, Tree):
            for branch in [tree.pre, tree.twixt, tree.post]:
                if isinstance(branch, Tree):
                    newTree = branch
                    loopTree(newTree)



def mirror(string):
    procString = removePunct(string)
    if string.endswith("%%"):
        leftString = string[:-3]
    else:
        leftString = string
    rightString = procString[::-1]
    return leftString + " " + rightString

def removePunct(string):
    string = re.sub("[\W\d\s]", "", string).lower()
    return string

def addSpaces(palindrome):
    space = raw_input("Add a space? Give word to add space behind. If ambiguous, surround to-be-spaced word with %'s and 2 chars before and after, when done ")
    if re.search('(..)%(.+)%(..)', space):
        match = re.search(r'(..)%(.+)%(..)', space)
        start = palindrome.find(match.group(1) + match.group(2) + match.group(3)) + 2
        if start != 1:
            palindrome = palindrome[0:start] + " " + match.group(2) + " " + palindrome[start + len(match.group(2)):]
    elif palindrome.find(space):
        pal_array = palindrome.partition(space)
        palindrome = " ".join(pal_array)
    return palindrome

def isPalindrome(palText):
    palText = removePunct(palText)
    palLength = len(palText)
    firstHalf = palText[0:palLength/2]
    secondHalf = palText[palLength/2 + palLength%2:]
    return True if firstHalf == secondHalf[::-1] else False

def rlinput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return raw_input(prompt)
   finally:
      readline.set_startup_hook()
  
def editPalindrome(pal):
    palindromeToCheck = rlinput("Edit Mode:", pal.text)
    if isPalindrome(palindromeToCheck):
        pal.text = palindromeToCheck
        print pal.text
    else:
        palindromeToCheck = rlinput("Err, what you sent was no palindrome, bucko: ", pal.text)

def savePalindrome(pal):
    f = open("palindromes.txt", "a")
    f.write(pal.text + "\n")
    f.close()

def showPalindromes():
    f = open("palindromes.txt", "r")
    lines = f.readlines()
    for line in lines:
        print line

def startPalindrome(pal):
    prepalindrome = raw_input("Start your palindrome: ")
    palindrome.text = mirror(prepalindrome)
    editPalindrome(pal)

def palindromize(pal):
    # find the largest palindrome in a string of text
    palText = removePunct(pal.text)
    # first idea: check for palindromes in substrings approaching the center of the string
    palLength = len(palText)
    for i in range(1,palLength/2):
        testPal = palText[i:-i]
        if isPalindrome(testPal):
            palindromeToCheck = rlinput("Palindromized:", palText[0:i] + " {" + testPal + "} " + palText[-i:])
            break;

    # 2nd idea:
    # oneLessPal1 = palText[0:palLength/2 + palLength%2]





# palindrome = Palindrome("Todd erase", True)
# print palindrome.text
# print palindrome.isPalindrome()
# print palindrome.isOdd()
# print palindrome.firstHalf()
# print palindrome.secondHalf()

# palindrome2 = Palindrome("hukjfdjytutrystgrhgfjkiy tuki tyeat watjykiiu dtvfv zrhth todd erasesgfgfdhfry yt ytr yy ty trrtgfdfd tr whthtj  yj6idfdsjjkytkyt tr sa red dot iohgfjgfjykiyt tu triutrsrfg abcdeedcba detjut ru sryykiyfa")


# palindrome2 = Palindrome("son i sac fgre greer  casinos  grgdsdht Todd erase    gwerykliuegghtrj    nos in gt7uaeref greanison                 sa red dot   fghfjatagadfs        stopgfrfWGTTVW pots treefcdsfaw")
palindrome2 = Palindrome("atoodbppblootbtodderasetoosrdfdrpootfsareddotctoofebfbeqootd")
palindrome2.palindromize()

# pal = findLongestPal("atodotb")

# print pal

# palindrome.text = "b le  gi p qw  m m Todd erases a red dot lorem ipsum "
# main(palindrome)

# palindromize(palindrome)dbppbl

# root = Tree("atootbtodderasetootfsareddotctootd")

# loopTree(root)
# # x = str(root)
# # print x

# print root.string
# print root.pre
# print root.pre.pre
# print root.pre.left
# print root.pre.twixt
# print root.pre.right
# print root.pre.post
# print root.left
# print root.twixt
# print root.right
# print root.post