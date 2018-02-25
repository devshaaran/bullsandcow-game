class Bullcowgame:

    secretword = "black"
    wordlength = int(len(secretword))

    def guesstake(self):
            for i in range(0, 5):                    #hello
                while True:
                    guess = input("please enter your guess ,but make sure it is " + str(self.wordlength) + " letters:")
                    wordlengthguess = int(len(guess))
                    if wordlengthguess == self.wordlength:
                        break
                        break
                    else:
                        print("please make sure to enter a word only having " + str(self.wordlength) + " letters")       #hell0
                bulls = 0
                cows = 0
                for j in range(0, self.wordlength):
                    for k in range(0, self.wordlength):
                        if k == j and guess[j] == self.secretword[k]:
                            bulls = bulls + 1
                        elif k != j and guess[j] == Bullcowgame.secretword[k]:
                            cows = cows + 1
                        else:
                            cows = cows
                            bulls = bulls

                print("bulls = " + str(bulls))
                print("cows = " + str(cows))
                if bulls == self.wordlength and i == 1:
                    print("unbeleivable!!! , you found the word in " + str(i) + "try")
                    return
                elif bulls == self.wordlength and i >= 1:
                    print("bravo!!!, you found the word in " + str(i) + " tries")
                    return




def name():

    name_candidate = input("please enter your name: ")
    return name_candidate
name = name()

def age():

    while True:
        try:
            age_person = int(input("please enter your age: "))
            if age_person > 200:
                print("Iam sure you aren't that old")
            elif age_person != 0:
                return(age_person)
            else:
                print("zero can't be a valid age")
        except ValueError:
            print("please enter a valid number")
ages = age()

def gender():

    while True:
            sex = input("please enter your gender(m/f/o): ")
            if sex == 'm':
                return sex
            elif sex == 'f':
                return sex
            elif sex == 'o':
                return sex
            else:
                print("please enter your gender")
sex = gender()

def designation():
    if ages >= 18 and sex == 'm':
        desig = "Mr."
        return desig
    if ages >= 18 and sex == 'f' or ages >= 18 and sex =='o':
        desig = "Ms."
        return desig
    else:
        desig = "Master."
        return desig

desig = designation()

def intro():

    print("welcome to bulls and cow game")
    print("Hello " + desig + name + " ,hope you enjoy this game")


intro()
playgame = Bullcowgame()
playgame.guesstake()

while True:
    response = input("would you like to play again(y/n): ")
    if response[0] == 'y':
        print("thank you for playing this game")
        playgame.guesstake()
        break
    elif response[0] == 'n':
        print("thanks for playing the game , hope you liked it")
        break
        break
    else:
        print("please type either y or n")


