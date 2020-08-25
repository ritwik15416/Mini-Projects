from random import randint
rps = ["Rock","Paper","Scissors"]
def game(player,comp):
    ys = 0
    cs = 0
    if player not in rps:
        print("Invalid entry!")
    elif(player==comp):
        pass
    elif(player=="Rock" and comp=="Paper"):
        cs += 1
    elif(player=="Scissors" and comp=="Rock"):
        cs += 1
    elif(player=="Paper" and comp=="Scissors"):
        cs += 1
    else:
        ys += 1
    ts = ys-cs
    return ts
def replay(chance):
    if chance == "y":
        play()
    else:
        print("Game over!")
def play():
    games = int(input("How many games do you want to play?: "))
    iter = 0
    while iter<games:
        player = input("Rock/Paper/Scissors: ").title()
        item = randint(0,len(rps)-1)
        comp = rps[item]
        total_score = game(player,comp)
        iter += 1
    if total_score > 0:
        print("You won by: ",total_score,"point(s)")
    elif total_score == 0:
        print("Match Draw!")
    else:
        print("You lost by: ",abs(total_score),"point(s)")
    print("********************************************")
    chance = input("Do you want to play again? (y/n): ")
    replay(chance)
play()



