#! python3
# main game loop and core logic
'''
Program: Battleship
Description: This program will be a functional two player game of battleship. This
    file contains the main game loop and core logic.
Output: A game of battleship.
Authors: Brynn Hare, Micah Borghese, Katelyn Accola, Nora Manolescu, and Kyle Johnson
Creation date: 9/4/2024
'''

import sys

player1 = 1
player2 = 2


# class Game:
    # def __init__(self):
    #     pass
    
    # def draw_boards(self):
    #     player1_board.draw()
    #     player2_board.draw()

    #     ship = player2_ships.get_1x4("B", 5, orientation="horizontal")  # my example: ship on Player 2's board
    #     # note that this returns a list of tuples representing the squares the ship occupies
    #     player2_ships.remove_ship(ship)  # remove ship from Player 2's board

    #     screen.blit(player1_board.surface, (0,0))
    #     screen.blit(player2_board.surface, ((WIDTH + 50) // 2, 0)) 

    # def update(self):
    #     screen.fill(Colors().get_white())
    #     self.draw_boards()
    #     pygame.display.update()

class Board: # Nora can do this 
    def __init__(self, player_num):
        self.player_num = player_num
        self.board = [["~" for _ in range(10)] for _ in range(10)]
        self.map = [] # keep track of coordinates?

        # Ship: O
        # Ship hit: X
        # Ship sunk: *
        # Open spot: ~
        # Missfire: .

    def display_board(self):
        # Display columns denoted A-J
        print() #add a leading space for the board
        print(" ".join(chr(ord('A') + i) for i in range(10)))

        # Display rows denoted 1-10
        for i, row in enumerate(self.board):
            print(" ".join(row) + f" {i + 1}")
        print() #add a trailing space for the board

    def display_opponent_board(self):
        # To display the opponent's board, only showing the sunk ships (replace unsunk ships with '~')
        # Display columns denoted A-J
        print()  # Add a leading space for the board
        print("  " + " ".join(chr(ord('A') + i) for i in range(10)))  # Column labels A-J with space before them
        
        # Display rows denoted 1-10
        for i, row in enumerate(self.board):
            # Replace non-sunk ships with '~'
            display_row = ['~' if cell == 'O' else cell for cell in row]
            # Print the row with the row number
            print(f"{i + 1:2} " + " ".join(display_row))  # Row number with space and row content
            
        print()  # Add a trailing space for the board

    def place_ships(self, ship): # ship needs to be an array of ints
        #add the ships into the board
        # ship will be a size array(ex [1,2])
        orientation = "none" # forcing the player to select a boat orientation each round
        while (orientation != "h") and (orientation != "v"): #continue to ask for the ship orientation if not answered with an h or v
            orientation_input = input("Would you like your ship to be horizontal or vertical?\nEnter 'h' for horizontal. Enter 'v' for vertical.\n") #prompt user for orientation
            orientation = orientation_input.lower() #make the user input lowercase
        invalid_location = True
        while invalid_location:
            location = input("Enter the upper leftmost coordinate you would like your ship to be placed at: ") #location will be a string for ex A1
            location = list(location) #store as an array 
            if len(location) == 3: 
                location[1] = 10
            else: 
                location[1]= int(location[1])
            location[0] = location[0].lower()
            if (location[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) and (location[1] in range(1,11)):
                invalid_location = False
        if ship[0] == 1: #horizontal?
            for i in range(ship[1]): # add a mark for each of the ship units
                self.board[location[1]-1][ord(location[0].lower()) - 97] = "O"
                location[0] = chr(ord(location[0]) + 1)
        else: #vertical?
            for i in range(ship[0]): # add a mark for each of the ship units
                self.board[location[1]-1][ord(location[0].lower()) - 97] = "O"
                location[1] = location[1]+1
                


    def is_empty(self):
        # Check if spot is free
        pass

    def fire(self):
        #make guess, check if guess is valid and then update board
        # return 0 for miss, 1 for hit, and 2 for a sink
        pass

    def game_over(self):
        # return true if the board has no more unsunk ships, false otherwise
        for rows in self.board:
            for space in rows:
                if space == "O":
                    return False
        return True


class Ships: 
    #class that handles 1b; assigning the correct number of ships to a user
    def __init__(self, player_num):
        self.player_num = player_num #this will be put in by us each time they switch, to reprsent player 1 or 2
        self.num_ships = 0 #this is provided by the player later (must be numbers 1-5 inclusively)
        self.ship_types = [] #empty list to hold the sizes of the ships

    def choose_ships(self): #the player must select the number of ships they want to have
        num_ships = int(input("Choose the number of ships for your board (1-5): "))
        self.num_ships = num_ships
        while (1 > self.num_ships > 5): #checking for invalid ship values
             new_num = int(input("Invalid number of ships. Select a new number: ")) #prompt for another number ***THIS CAN BE CHANGED JUST AN INITIAL PHASE***
             self.num_ships = new_num #assign the new number to be the number of ships

    def load_types(self): #this forms the list with the sizes of the ships
        i = 1 #initializing for the while loop
        while i < (self.num_ships + 1): #while the current ship number is less than one extra than the number of ships chosen
            self.ship_types.append([1, i]) #append to the list. [1, 1] represents 1 x 1. [1, 2] represents 1 x 2...etc.
            i += 1 #increase the while loop

    def place(self, board): #place the ships on the board
        # I think we can just call the place_ship from board instead to be simpler and delete this function
        board.place_ships()
        pass

    def fire(self, location):
        #check the board to see if a hit and if so determine if the ship was sunk
        #return a 0 for a miss, a 1 for a hit, and a 2 for a sink
        pass

    # def orientation()

    #need to have a function that allows for the players to turn the pieces (swap the x and y values of the list?)
    #need to connect to the gameboard class to "remember" where the pieces are located

class Fire:
    # need a function to account for "firing" that needs to check that it is a valid space, if yes reply with hit or miss
    #need a function to update the board
    pass

class SwitchPlayers:
    #this can be used anytime to move from player 1 to 2 
    #the main purpose of this class is to give the players a warning that a turn will switch. This prevents the opposing player's board from displaying, spoiling the secrecy of the game
    def __init__(self):
        self.player_num = 1 #initialized by starting with player 1
    
    def change(self):
        if self.player_num == 1:
            self.player_num = 2
        else: 
            self.player_num == 1
            
    def begin_turn(self):
        print("Begin Player", self.player_num,"'s Turn (Press Enter)") #Begins player turn waits till theres an input
        input() #require an enter to confirm the start of a turn
        
    def end_turn(self):
        print("End Player", self.player_num,"'s Turn (Press Enter)") #display that the turn is ending
        input() #require an enter to confirm ending a turn
        self.change() #switch players after the confirmation of a turn ending


class DestroyShip: 
    #needs to keep track of the ship_types list and the board, if a ship is gone it sunk
    pass

class DisplayBoard:
    #class responsible for displaying the board
    #differentiate miss with hit
    pass

class GameOver:
    #Change to function
    #display the correct player as the winner if they sunk all other ships
    pass

if __name__ == '__main__':
    #start the game and initialize the boards, ships, and players
    boards = [Board(player1), Board(player2)] # store boards in an array to access easier
    # board1 = Board(player1) #board1 represents player 1's board
    # board2 = Board(player2) #board2 represents player 2's board
    ships1 = Ships(player1) #create an ships class for player 1
    ships2 = Ships(player2) #create an ships class for player 2
    currentplayer = SwitchPlayers() #object that controls who the current player is

    #begin the game setup for player1
    currentplayer.begin_turn() #prompt player 1 to begin first turn 
    ships1.choose_ships() #prompt player 1 with the number of ships to select
    ships1.load_types() #create the list of ships for player 1
    boards[0].display_board() #display the blank board
    for ship in ships1.ship_types: #depending on the number of ships picked
        # ships1.place(boards[0]) #place the ships
        boards[0].place_ships(ship) #making the board class write in the ship to the board as its placed
        boards[0].display_board() #display the current state of the board after each ship placement
    currentplayer.end_turn() #confirm the end of player 1's setup turn and make player 2 the new current player


    #begin the game setup for player2
    currentplayer.begin_turn() #prompt play 2 to being first setup turn
    ships2.choose_ships() #prompt player 2 with the number of ships to select
    ships2.load_types() #create the list of ships for player 2
    boards[1].display_board() #display the blank board
    for ship in ships2.ship_types: #depending on the number of ships picked
        boards[1].place_ships(ship) #place the ships
        boards[1].display_board() #display the current state of the board after each ship placement
    currentplayer.end_turn() #end player 2's setup turn and make the current player player 1

    # main game loop to be repeated until there is a winner
    gameOver = False
    while not gameOver:
        currentplayer.begin_turn() # start the next turn
        currentboard = currentplayer.player_num -1 # keep track of which board we are looking at
        if currentboard == 0: # also keep track of the opponents board
            oponentboard = 1
        else:
            opponentboard = 0
        boards[currentboard].display_board() # display their own board to see what opponent has hit
        player_continue = True # boolean to keep track of if the current player gets to keep guessing
        while player_continue == True: 
            boards[opponentboard].display_opponent_board() # display their opponents board
            guess_coordinate = input("Input the coordinate you want to fire at ") # take in input as string, should add error detection
            fire = boards[opponentboard].fire() # fire and store output
            if fire == 0: # fire and if output is 0 its a miss
                print("MISS")
                boards[opponentboard].display_opponent_board() # after a miss display board
                player_continue == False # break loop for next player
                currentplayer.end_turn() #end turn
            elif fire == 1:
                print("HIT") # if hit, continue in loop
                if boards[opponentboard].game_over: # check if theres any more ships on the boards
                    gameOver = True
            else:
                print("SUNK BATTLESHIP") # if 2 is returned, ship is sunk
                if boards[opponentboard].game_over:
                    gameOver = True


        
    





    
    
