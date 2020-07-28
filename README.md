# Rock-Paper-Scissors
* This is a Rock-Paper-Scissors game between the user and computer. The user/player has to enter his choice (case insensitive) while the computer randomly chooses between rock/paper/scissors.
* If a player enters something other than RPS, then s/he loses a game and program throws an error "Invalid entry!"
* game function takes in 2 required parameters player and comp. They are the user's entry and the computer's choice respectively. This function returns a total score (difference between player's score and computer's score).
* replay function takes in chance, which is either y or n. It gives player a chance to play further or quit.
* play function doesn't take any parameters. It asks how many games the player wants to play and starts the game loop. At the end, winner is declared (if not a draw) along with the margin of points. replay function is called inside this play() function.
* At the end, play() function is called.
```
How many games do you want to play?: 3
Rock/Paper/Scissors: paper
Rock/Paper/Scissors: rock
Rock/Paper/Scissors: scissors
Match Draw!
********************************************
Do you want to play again? (y/n): y
How many games do you want to play?: 1
Rock/Paper/Scissors: paper
You won by:  1 point(s)
********************************************
Do you want to play again? (y/n): y
How many games do you want to play?: 1
Rock/Paper/Scissors: sdasd
Invalid entry!
Match Draw!
********************************************
Do you want to play again? (y/n): n
Game over!

```
