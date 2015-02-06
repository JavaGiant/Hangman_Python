# Name: Carson Smith
# hangman.py
#
# Problem: A program to play the children's game, hangman! This program DOES NOT
# have graphics.
#           
# Certification of Authenticity:  
#
#   I certify that this lab is entirely my own work.
#   
# Shell Version of game commented out and located at bottom of the screen. I think it is still in tact! (I hope it wasn't required to be - I had to do a lot of fiddling around!)
#
## I ran into a weird error at the very end if the user hits the "YES" button to play again. I'm unsure of what the problem is and was going to come ask you. The "NO" button (if they click that they
## do not want to play again) functions correctly though..
##
##
########### wordlistcarson.txt was added to dropbox along with hangman.py!
import random
from graphics import *

def wasClicked(pt, rect): #This function creates working buttons.

    if pt == None:
        return False
    else:
        mouseX = pt.getX()
        mouseY = pt.getY()
        buttonX1 = rect.getP1().getX()
        buttonX2 = rect.getP2().getX()
        buttonY1 = rect.getP1().getY()
        buttonY2 = rect.getP2().getY()

        if mouseX > buttonX1 and mouseX < buttonX2:
            if mouseY > buttonY1 and mouseY < buttonY2:
                return True
        else:
            return False

def readWords(): #Reads the file containing possible words

    infile = open("wordlistcarson.txt", "r")
    word = infile.read()
    words = word.split("\n")
    return words
    
def wordPicker(): #Selects a word from the file

    words = readWords()
    position = random.randint(0,(len(words)-1))
    keyword = words[position]

    return keyword


def lengthOfWord(keyword): #Determines how long the word is (Useful for shell version!)
    
    length = []
    for ch in keyword:
        length.append("_")
    return length

def winningWord(keyword): #Creates a check for the guessed version of word versus the winning version to see if
                          #the user has won

    winningWord = []
    for ch in keyword:
        winningWord.append(ch)
    return winningWord
        

def correctGuessCheck(guess, keyword, blanks, underscores): #Checks to see if the guess is correct... has some extra stuff in it for shell version

    for i in range(len(keyword)):
        if keyword[i] == guess:
            blanks[i] = guess
            underscores[i].setText(guess)
    return blanks
        

def hangman():

################    #Producing the GUI: #########################
#################################################################
    ##########################################

    
    win = GraphWin("Hangman", 500, 500)


    #Instructions Info:
    instructBox = Rectangle(Point(0,0), Point(500,50))
    instructBox.setFill("Black")
    instructBox.draw(win)

    instructions = Text(Point(250,25), "Enter a letter and click to play hangman!")
    instructions.setTextColor("White")
    instructions.draw(win)

    #User Guess:

    guessBox = Rectangle(Point(0,400), Point(500,500))
    guessBox.setFill("Black")
    guessBox.draw(win)

    guessEntry = Entry(Point(310,450), 10)
    guessEntry.setFill("White")
    guessEntry.draw(win)

    guessText = Text(Point(200,450), "Enter a letter:")
    guessText.setTextColor("White")
    guessText.draw(win)

######## I was going to use a submit button, but I couldn't get it to work in all cases with certain words. I wasn't sure why, so I just made it where the
######## user could click anywhere in order to submit the letter. HOWEVER, the buttons for the final "play again?" do work.

##    submitButton = Rectangle(Point(200,470), Point(330, 490))
##    submitButton.setOutline("Cyan")
##    submitButton.setFill("White")
##    submitButton.draw(win)
##
##    guessSubmitText = Text(Point(265,480), "Submit")
##    guessSubmitText.draw(win)

    #Letters Guessed Box:

    guessedLettersBox = Rectangle(Point(400,50), Point(500,400))
    guessedLettersBox.setFill("Cyan")
    guessedLettersBox.draw(win)

    guessedLettersInfo = Text(Point(450,100), "Guessed" +"\n" + "Letters:")
    guessedLettersInfo.setTextColor("Black")
    guessedLettersInfo.draw(win)

    #Letters Guessed Display

    lg0 = Text(Point(440,120), "_")
    lg1 = Text(Point(450,120), "_")
    lg2 = Text(Point(460,120), "_")
    lg3 = Text(Point(440,130), "_")
    lg4 = Text(Point(450,130), "_")
    lg5 = Text(Point(460,130), "_")
    lg6 = Text(Point(440,140), "_")
    lg7 = Text(Point(450,140), "_")
    lg8 = Text(Point(460,140), "_")
    lg9 = Text(Point(440,150), "_")
    lg10 = Text(Point(450,150), "_")
    lg11 = Text(Point(460,150), "_")
    lg12 = Text(Point(440,160), "_")
    lg13 = Text(Point(450,160), "_")
    lg14 = Text(Point(460,160), "_")
    lg15 = Text(Point(440,170), "_") 
    lg16 = Text(Point(450,170), "_") 
    lg17 = Text(Point(460,170), "_")

    lettersGuessed = [lg0,lg1,lg2,lg3,lg4,lg5,lg6,lg7,lg8,lg9,lg10,lg11,lg12,lg13,lg14,lg15,lg16,lg17]        # Store the lettersGuessed into a list in order to
                                                                                                              # draw them as needed later

    #Lives remaining box:

    livesRemainingBox = Rectangle(Point(0,50), Point(100,400))
    livesRemainingBox.setFill("Cyan")
    livesRemainingBox.draw(win)

    livesRemainingInfo = Text(Point(50,100), "Lives" + "\n" + "Remaining:")
    livesRemainingInfo.setFill("Black")
    livesRemainingInfo.draw(win)

    numOfLivesRemaining = Text(Point(50, 175), "7")
    numOfLivesRemaining.setStyle("bold")
    numOfLivesRemaining.setSize(15)
    numOfLivesRemaining.draw(win)

     
    #Underscores for word length:
    un0 = Text(Point(200,100), "_")
    un1 = Text(Point(210,100), "_")
    un2 = Text(Point(220,100), "_")
    un3 = Text(Point(230,100), "_")
    un4 = Text(Point(240,100), "_")
    un5 = Text(Point(250,100), "_")
    un6 = Text(Point(260,100), "_")
    un7 = Text(Point(270,100), "_")
    un8 = Text(Point(280,100), "_")
    un9 = Text(Point(290,100), "_")

    underscores = [un0,un1,un2,un3,un4,un5,un6,un7,un8,un9]     #Same as above, store underscores
                                                                #in a list in order to draw them
                                                                #as needed later.

    #You lose screen:

    loseScreen = Rectangle(Point(100,50),Point(400,400))
    loseScreen.setFill("Red")

    loseText = Text(Point(250,100), "YOU LOSE!")
    loseText.setStyle("bold")
    loseText.setSize(20)

    #You win screen:
    winScreen = Rectangle(Point(100,50),Point(400,400))
    winScreen.setFill("Blue")

    winText = Text(Point(250,100), "YOU WIN!")
    winText.setStyle("bold")
    winText.setSize(20)

    #Play Again Buttons:

    yesButton = Rectangle(Point(150,225), Point(225,250))
    yesButton.setFill("Black")
    
    yesButtonText = Text(Point(187.5, 237.5), "YES")
    yesButtonText.setTextColor("White")
    
    noButton = Rectangle(Point(275,225), Point(350,250))
    noButton.setFill("Black")

    noButtonText = Text(Point(312.5, 237.5), "NO")
    noButtonText.setTextColor("White")
    
    #Drawing the hangman:

    head = Circle(Point(250,200),25)
    body = Line(Point(250,225),Point(250,300))
    leftArm = Line(Point(250,225), Point(225,250))
    rightArm = Line(Point(250,225), Point(275,250))
    leftLeg = Line(Point(250,300),Point(225,350))
    rightLeg = Line(Point(250,300), Point(275,350))

    #Drawing the Gallows:

    gallowsTop = Rectangle(Point(200,150), Point(350,130))
    gallowsTop.setFill("Brown")
    gallowsTop.draw(win)

    gallowsHeight = Rectangle(Point(313,355), Point(333,150))
    gallowsHeight.setFill("Brown")
    gallowsHeight.draw(win)

    gallowsBase = Rectangle(Point(225,350), Point(350,360))
    gallowsBase.setFill("Brown")

    rope = Line(Point(250,140),Point(250,175))
    rope.draw(win)
    #gallowsBase.draw(win)

    gallowsBase2 = Rectangle(Point(275,350), Point(350,360))
    gallowsBase2.setFill("Brown")
    gallowsBase2.draw(win)


##################################### GUI COMPLETE ###########################################################

    
    #guess = input("Enter a single letter to guess! ")
    play = True
    while play == True:
        lives = 7
        keyword = wordPicker()
        winner = winningWord(keyword)
        print(keyword)
        z = 0
        displayWord = lengthOfWord(keyword)
        for i in range(len(keyword)):
            underscores[i].setSize(10)
            underscores[i].draw(win)
        for i in range(17):
            lettersGuessed[i].setSize(10)
            lettersGuessed[i].draw(win)

        while lives > 0:
            click = win.getMouse()
            guess = guessEntry.getText()
            temp = 1
            lettersGuessed[z].setText(guess)
            while temp == 1:
                if len(guess) == 1 and lives != 0:
                    displayWord = correctGuessCheck(guess,keyword, displayWord,underscores)
                    #underScoreConverter(displayWord, underscores, guess)
                    if guess not in keyword:
                        if lives == 6:
                            numOfLivesRemaining.setText("6")
                            head.draw(win)
                        if lives == 5:
                            body.draw(win)
                            numOfLivesRemaining.setText("5")
                        if lives == 4:
                            leftArm.draw(win)
                            numOfLivesRemaining.setText("4")
                        if lives == 3:
                            rightArm.draw(win)
                            numOfLivesRemaining.setText("3")
                        if lives == 2:
                            leftLeg.draw(win)
                            numOfLivesRemaining.setText("2")
                        if lives == 1:
                            rightLeg.draw(win)
                            numOfLivesRemaining.setText("1")
                        lives = lives - 1
                    temp = 0
                    z = z + 1
                if displayWord == winner:
                    lives = -1
        if lives == -1:
            winScreen.draw(win)
            winText.draw(win)
            click = win.checkMouse()
            yesButton.draw(win)
            yesButtonText.draw(win)
            noButton.draw(win)
            noButtonText.draw(win)
            instructions.setText("Play Again?")
            click = win.getMouse()                  #This block of code tests which button they clicked
            if click != None:
                buttonType = wasClicked(click, yesButton)
                if buttonType == True:
                    play = True
                elif buttonType == False:
                    buttonType = wasClicked(click, noButton)
                    if buttonType == True:
                        win.close()
        if lives == 0:
            print("You lost! The word was: ", keyword)
            numOfLivesRemaining.setText("0")
            loseScreen.draw(win)
            loseText.draw(win)
            click = win.checkMouse()
            yesButton.draw(win)
            yesButtonText.draw(win)
            noButton.draw(win)
            noButtonText.draw(win)
            instructions.setText("Play Again?")
            click = win.getMouse()
            if click != None:                   #This block of code tests which button they clicked
                buttonType = wasClicked(click, yesButton)
                if buttonType == True:
                    play = True
                elif buttonType == False:
                    buttonType = wasClicked(click, noButton)
                    if buttonType == True:
                        win.close()
                






















        

#########Shell Version#####################################################
##    while lives > 0:
##        guess = input("Enter a single letter to guess! ")
##        if len(guess) == 1 and lives != 0:
##            displayWord = correctGuessCheck(guess,keyword, displayWord)
##            if guess not in keyword:
##                lives = lives - 1
##                print(str(guess) + " was not in the word!")
##                print("You have " + str(lives) + " more guesses!")
##            print(displayWord)
##            if displayWord == winner:
##                lives = -1
##        else:
##            print("You either put in too many letters, or nothing at all!")
##            guess = input("Enter a single letter to guess!")
##
##    if lives == -1:
##        print("You win!")
##    if lives == 0:
##        print("You lost! The word was: ", keyword)



    
    
    
