from random import randint

def display_welcome_banner():
    welcome_banner = """
                    Welcome to Five To Win!

        This is a dice game between two players, the user
        and a computer opponent. The game is played in rounds. 

        In each round: 

        - Player rolls two dice and check parity.

        - Parity is whether a number is even or odd.

        - If the parity of both the dice rolls is even, the player gets one point.

        - Else if the parity of both the dice rolls is odd, the computer gets one point. 

        - The game continues until a player reaches 5 or more points. 

    """

    print(welcome_banner)
    
    
def roll_dice():
    return randint(1, 6)




















user_input = int(input ("What picture of a dice do you want to see. Type two numbers from 1 - 6. Example: 3,5"))




def get_die(num):      #you must choose number from 1 to 6
    
    


    if user_input == [1,2] :
        print("The dice shows ⚀ , ⚁")

if user_input == [1,3] :
    print("The dice shows ⚀ , ⚂")
    
if user_input == [1,4] :
    print("The dice shows ⚀ , ⚃")   
    
if user_input == [1,5] :
    print("The dice shows ⚀ , ⚄")      
    
if user_input == [1,6] :
    print("The dice shows ⚀ , ⚅")     
    
if user_input == [2,1] :
    print("The dice shows ⚁ , ⚀")

if user_input == [2,3] :
    print("The dice shows ⚁ , ⚂")

if user_input == [2,4] :
    print("The dice shows ⚁ , ⚃")

if user_input == [2,5] :
    print("The dice shows ⚁ , ⚄")

if user_input == [2,6] :
    print("The dice shows ⚁ , ⚅")

if user_input == [3,1] :
    print("The dice shows ⚂ , ⚀")

if user_input == [3,2] :
    print("The dice shows ⚂ , ⚁")
    
if user_input == [3,4] :
    print("The dice shows ⚂ , ⚃") 

if user_input == [3,5] :
    print("The dice shows ⚂ , ⚄")
    
if user_input == [3,6] :
    print("The dice shows ⚂ , ⚅")
    
if user_input == [4,1] :
    print("The dice shows ⚃ , ⚀") 
    
if user_input == [4,2] :
    print("The dice shows ⚃ , ⚁")
    
if user_input == [4,3] :
    print("The dice shows ⚃ , ⚂")
    
if user_input == [4,5] :
    print("The dice shows ⚃ , ⚄")
    
if user_input == [4,6] :
    print("The dice shows ⚃ , ⚅")
    
if user_input == [5,1] :
    print("The dice shows ⚄ , ⚀")  
    
if user_input == [5,2] :
    print("The dice shows ⚄ , ⚁")
    
if user_input == [5,3] :
    print("The dice shows ⚄ , ⚂")
    
if user_input == [5,4] :
    print("The dice shows ⚄ , ⚃")
    
if user_input == [5,6] :
    print("The dice shows ⚄ , ⚅")
    
if user_input == [6,1] :
    print("The dice shows ⚅ , ⚀")
    
if user_input == [6,2] :
    print("The dice shows ⚅ , ⚁")
    
if user_input == [6,3] :
    print("The dice shows ⚅ , ⚂")
    
if user_input == [6,4] :
    print("The dice shows ⚅ , ⚃")
    
if user_input == [6,5] :
    print("The dice shows ⚅ , ⚄")
    
if user_input == [1,1] :
    print("The dice shows ⚀ , ⚀")
    
if user_input == [2,2] :
    print("The dice shows ⚁ , ⚁")
    
if user_input == [3,3] :
    print("The dice shows ⚂ , ⚂")
    
if user_input == [4,4] :
    print("The dice shows ⚃ , ⚃")
    
if user_input == [5,5] :
    print("The dice shows ⚄ , ⚄")
    
if user_input == [6,6] :
    print("The dice shows ⚅ , ⚅")

else:
    print("Please type a valid number.")
    
    
    
    
    
return user_input
    
pass 














def is_even (num):
    return num % 2 == 0

def is_odd (num):
    return num % 2 != 0
display_welcome_banner()


 



def show_stats(round_number, roll_1, roll_2):
  print(f"Round number: {round_number}")
  print(f"The dice shows {roll_1}, {roll_2}")

def display_scoreboard(user_score, computer_score):
        scoreboard = f"""
            User Score: {user_score}
            Computer Score: {computer_score}
       """
user_score = 0
computer_score = 0
round_number = 0
still_playing = True

user_name = input("Enter your name: ")

while still_playing:
    input("Roll dice (press enter): ")

    round_number += 1
    roll_1 = roll_dice()
    roll_2 = roll_dice()

    print(f"Round number: {round_number}")
    print(f"The dice shows {roll_1}, {roll_2}")
    

    if  is_even(roll_1) :
        user_score += 1 

    elif  is_odd (roll_2):
        computer_score += 1


    print(f"User Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    print("-------------------------------------")
    
    
    if(user_score >= 5 or computer_score >= 5):

        if(user_score > computer_score):
            print("You won!")

        else:
            print("You lose!")

        still_playing = False
    
    
    
    
    
    
        return user_input
    
    pass 
