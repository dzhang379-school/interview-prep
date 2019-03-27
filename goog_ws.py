
def checkWord(curWord):
    dictionary = ['car', 'crab', 'bar']
    return (curWord in dictionary)

def buildCheck(curWord, letters):

    if len(letters) == 0 and not checkWord(curWord):
        return curWord

    newWords = []

    for i in range(len(letters)):
        tempLetters = [x for x in letters]
        del tempLetters[i]
        newWord = curWord + letters[i]
        newWords.append(newWord)
        for i in range(len(newWords)):
            if checkWord(newWords[i]):
                print(newWords[i])
                quit()
        buildCheck(newWord, tempLetters)

def getShortest(input):

    letters = []

    for i in range(len(input)):
        if input[i].isalpha():
            letters.append(input[i])

    buildCheck('', letters)
    print('No word can be made with the given letters')

getShortest('bc104ra')