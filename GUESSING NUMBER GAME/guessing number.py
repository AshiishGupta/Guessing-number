print('please set reference number')
num=int(input())

#num = 10
chance = 1
while chance<=5:
    print("Enter any guesses")
    guess_num = int(input())
    if (guess_num > num):
        print("your guessed number is greater than the number")
        print("try again!!!")
        print("you have ",5 - chance,"left")
        chance = chance + 1
    elif  (guess_num < num):
        print("your guessed number is lesser than the number")
        print("you have ", 5 - chance, " chances left")
        chance = chance + 1
    else :
        print("YOU GOT THE NUMBER, YOU WON!!!")
        print("CONGRATS")
        print("you take ",chance,"chances to won")

if chance > 5:
    print("YOU LOSE!!!! \n TRY AGAIN!!!!")
    print("No guesses left", "GAME OVER!!")
