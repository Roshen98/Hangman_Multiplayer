import random

alphabetLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

categories = ['songs','holidays','celebrities','weather','countries','subjects']

subjects = ['physics', 'calculus', 'coding', 'world history', 'us history', 
'geometry', 'math', 'biology', 'chemistry', 'english', 'psychology']

songs = ['Perfect','Rewrite The Stars','Nothing','Dandelions','Count On Me',
'To My Youth']

holidays = ['Christmas','Halloween','Thanks Giving','New Year','Lunar New Year','Easter',
'Labor Day','Independence Day','Memorial Day','Valentine','Mid-Autumn Festival']

celebrities = ['Ed Sheeran','Keshi','Bruno Mars','Ariana Grande','Messi','Queen Elizabeth',
'Yao Ming','Roger Federer','Katy Perry', 'Joe Biden', 'Vladimir Putin','Jeff Bezos',
'']

weather = ['Rainy Day','Sunny Day','Cloudy Day','Clear Day','Snowy','Windy',
'Storm','Thunderstorm','Tornados','Huriccanes','Typhoons','Blizzard','Drought']

countries = ['South Korea', 'Iraq', 'Iran', 'China', 'Mexico',
'Russia', 'Canada', 'Japan','Switzerland','Germany','Australia',
'United Kingdom','United States','Sweden','Netherlands','Norway']

def pole():
    print(
        '''
        _____
        |   |
            |
            |
            |
            |
            |
        ''')
        
def headPole():
    print(
        '''
        _____
        |   |
        O   |
            |
            |
            |
            |
        ''')
        
def bodyPole():
    print(
        '''
        _____
        |   |
        O   |
        |   |
            |
            |
            |
        ''')

def leftArmPole():
    print(
        '''
        _____
        |   |
        O   |
       /|   |
            |
            |
            |
        ''')
        
def rightArmPole():
    print(
        '''
        _____
        |   |
        O   |
       /|\  |
            |
            |
            |
        ''')
        
def leftLegPole():
    print(
        '''
        _____
        |   |
        O   |
       /|\  |
       /    |
            |
            |
        ''')
        
def dead():
    print(
        '''
        _____
        |   |
        O   |
       /|\  |
       / \  |
            |
            |
        ''')
        
def selectCategory():
    # returns the valid category 
    '''
    index = 1;
    for each in categories:
        print(str(index) + '.', each)
        index+=1
    '''
    
    for number, word in enumerate(categories):
        print(str(number+1) + '.', word)
    
    while True:
        options = input('Pick your category: ')
        if options in ['1','2','3','4','5','6']:
            return options
        else:
            print('Invalid Category!')

def playerCategory(p1,p2):
    # return the chosen player and his category
    while True:
        # string concatenation
        chosenPlayer = input('Which player starts first[' + p1 + '/' + p2 +']')
        if chosenPlayer == p1 or chosenPlayer == p2:
            category = selectCategory()
            return [chosenPlayer, category]
        else:
            print('Invalid player name!')
    
    
def playerVsPlayer():
    # two player game mode
    print('Please enter the names of the players.')
    player1 = input('Player1 : ')
    player2 = input('Player2 : ')
    chosenPlayer, category = playerCategory(player1,player2)
    guessedString = ''
    chances = 6
    pole()
    answer = randomItem(category)
    guessedString = underscoreGenerator(answer, guessedString)
    repeatedLetter = []
    if chosenPlayer == player2:
        player2 = player1
        player1 = chosenPlayer
    currentPlayer = player1
    while True:
        printGuessedString(guessedString)
        print()
        if guessedString == answer:
            return 'Congratulations! The word is: ' + answer + '!\n' + currentPlayer + ' wins!'
        print(currentPlayer+"'s turn")
        letter = pickLetter()
        if letter.lower() not in repeatedLetter and letter.upper() not in repeatedLetter:
            repeatedLetter.append(letter)
        else:
            print('Letter picked already! Please pick another one!')
            continue
        print('Letters Picked:', repeatedLetter)
        
        temp = guessedString # _ _ _ _ _ _ _ 
        guessedString = updateGuess(guessedString,answer,letter)
        if guessedString == temp: # if the player guesses the letter wrong
            chances -= 1
            currentPlayer = switchTurn(currentPlayer, player1, player2)
        displayPole(chances)
        if chances == 0:
            return 'Game Over! Both of you lost! The word is: ' + answer 

def switchTurn(player, p1, p2):
    # returns the next player
    if player == p1:
        return p2
    else:
        return p1
    
    
def playerVsAI():
    # one player game mode with AI
    print()
    guessedString = ''
    chances = 6
    category = selectCategory()
    pole()
    answer = randomItem(category)
    guessedString = underscoreGenerator(answer, guessedString)
    repeatedLetter = []
    while True:
        printGuessedString(guessedString)
        print()
        if guessedString == answer:
            return 'Congratulations! The word is: ' + answer
        letter = pickLetter()
        if letter.lower() not in repeatedLetter and letter.upper() not in repeatedLetter:
            repeatedLetter.append(letter)
        else:
            print('Letter picked already! Please pick another one!')
            continue
        print('Letters Picked:', repeatedLetter)
            
        temp = guessedString # _ _ _ _ _ _ _ 
        guessedString = updateGuess(guessedString,answer,letter)
        if guessedString == temp:
            chances -= 1
        displayPole(chances)
        if chances == 0:
            return 'Game Over! The word is: ' + answer 
        
        

def displayPole(chance):
    # prints the pole to the console based on the lives left
    if chance == 6:
        pole()
    elif chance == 5:
        headPole()
    elif chance == 4:
        bodyPole()
    elif chance == 3:
        leftArmPole()
    elif chance == 2:
        rightArmPole()
    elif chance == 1:
        leftLegPole()
    else:
        dead()
    
    
def printGuessedString(string):
    # displaying the string in a clear way
    for x in string:
        print(x, end = ' ')
    print()

def updateGuess(guessedString, answer, letter):
    # returns the updated guess string if the player typed a letter thats in the answer
    # no matter if its upper or lower case [both cases are identified]
    letterCapital = False # boolean
    if letter in alphabetLower:
        capitalLetter = alphabetUpper[alphabetLower.index(letter)]
    else:
        letterCapital = True
        lowercaseLetter = alphabetLower[alphabetUpper.index(letter)]
    while True:
        if letter in answer:
            # get index of the letter in the answer and change to '_' (first occurence)
            index = answer.index(letter)
            guessedString = changeLetterByIndex(letter,guessedString,index)
            answer = changeLetterByIndex('_', answer, index)
        else:
            if letterCapital:
                letter = lowercaseLetter
            else:
                letter = capitalLetter
            
            if letter in answer:
                continue
            
            else:
                break
        
    return guessedString
# letter    t, l _ t _ _ _, 2
def changeLetterByIndex(letter,string,index):
    # returns an edited string based on the given index
    newString = ''
    for x in range(len(string)):
        if x == index:
            newString+=letter
        else:
            newString+=string[x]
    return newString


def pickLetter():
    # returns the valid letter entered by the player
    while True:
        letter = input('Pick a letter: ')
        if letter in alphabetLower or letter in alphabetUpper:
            return letter
        else:
            print('Invalid Letter!')
    
def underscoreGenerator(item, guessedString):
    # returns the generated underscores for players to see how many letters for the word
    for x in range(len(item)):
        if item[x] == ' ':
            guessedString += ' '
        else:
            guessedString += '_'
    return guessedString
    

# categories = ['songs','holidays','celebrities','weather','countries','subjects']

def randomItem(category):
    # returns the randomized categories for the game
    
    category = int(category) - 1
    if category == 0:
        return random.choice(songs)
    elif category == 1:
        return random.choice(holidays)
    elif category == 2:
        return random.choice(celebrities)
    elif category == 3:
        return random.choice(weather)
    elif category == 4:
        return random.choice(countries)
    else:
        return random.choice(subjects)
    

   
def menu():
    # the game menu which prints game over if the user selects quit(3)
    while True:
        print('Welcome to the Hangman Game!')
        print('1. Player vs AI')
        print('2. Player vs Player')
        print('3. Quit')
        
        option = input()
        if option == '1':
            print(playerVsAI())
        elif option == '2':
            print(playerVsPlayer())
        elif option == '3':
            return 'Game Over'
        else:
            print('Invalid Choice\n')

if __name__ == '__main__':
    # main function
    print(menu())
    











