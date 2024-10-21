print('''
              _________________________________
             /( ) ( )  ____________ ( ) ( )   /|
            /( )\( )\ / __  ____  /( )\( )\  //
           / /_\ /_\ / /  / /  / / /_\ /_\  //
          / ________/ /  / /  / /_______   //
         / / ________/  /_/  /_______  /  //
        / / /_______        ________/ /  //
       / / ________/       /_______  /  //
      / / /______    __   ________/ /  //
     /_/______   /  / /  / ________/  //
    /( ) ( )  / /  / /  / / ( ) ( )  //
   /( )\( )\ / /__/ /__/ / ( )\( )\ //
  / /_\ /_\ /___________/  /_\ /_\ //
 /________________________________//
|________________________________|| 
 \  ( ) ( )  ____________  ( ) ( )\\
  \ /( )/( ) \  ___  ___ \ /( )/( )\\
   \ /_\ /_\  \ \  \ \  \ \ /_\ /_\ \\
    \  ________\ \  \ \  \ \_______  \\
     \ \  ________\  \_\  \_______ \  \\
      \ \ \________        _______\ \  \\
       \ \  _______\       \________ \  \\
        \ \ \________   _    _______\ \  \\
         \ \________ \  \ \  \  _______\  \\
          \  ( ) ( )\ \  \ \  \ \  ( ) ( ) \\
           \ /( )/( )\ \__\ \__\ \ /( )/( ) \\
            \ /_\ /_\ \___________\ /_\ /_\  \\ 
             \________________________________\|
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n')

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n')
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is house with 3 doors. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose?\n")
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")

else:
    print("You fell in to a hole. Game Over.")