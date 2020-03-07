#1. Make an empty screen
#2. Print event.key attribute whenever a pygame.KEYDOWN event happens
import pygame
import sys #Lets us exit the game when the player quits
def check_events():
    """Checks to see if a key was pressed"""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: #Prints the pressed key
            print(event.key)
        if event.type == pygame.QUIT: #Quits if the exit button is hit
            sys.exit()



def run_game():
    """Function that runs our clicking game"""
   
    #Initialize pygame
    pygame.init()

    #Initializing the screen surface
    screen = pygame.display.set_mode((1200,800)) #Creating sreen and setting dimensions
    pygame.display.set_caption("Number Game!")

    while True:
        """Main loop for the game"""

        #Drawing the screen:
        screen.fill((230,0,0)) #Red background
        check_events() #Checks for events and prints them
        pygame.display.flip() #Redraws the entire display

run_game()
