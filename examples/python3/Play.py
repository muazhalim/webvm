import platform
import os
import curses
from Direction import Direction
from Game import Game

def displayMenu(stdscr, option, size, difficulty, placeObstacles):
    """Display the main menu."""
    stdscr.clear()
    if size == 0: sizeString = "Small"
    elif size == 1: sizeString = "Medium"
    elif size == 2: sizeString = "Large"

    if difficulty == 0: difficultyString = "Easy"
    elif difficulty == 1: difficultyString = "Medium"
    elif difficulty == 2: difficultyString = "Hard"

    obstacleString = "On" if placeObstacles else "Off"

    stdscr.addstr(0, 0, "SNAKE\n")
    stdscr.addstr(1, 0, ("> " if option == 0 else "  ") + "Play")
    stdscr.addstr(2, 0, ("> " if option == 1 else "  ") + f"Size: {sizeString}")
    stdscr.addstr(3, 0, ("> " if option == 2 else "  ") + f"Difficulty: {difficultyString}")
    stdscr.addstr(4, 0, ("> " if option == 3 else "  ") + f"Obstacles: {obstacleString}")
    stdscr.addstr(5, 0, ("> " if option == 4 else "  ") + "Quit")
    stdscr.refresh()

def playGame(size, difficulty, placeObstacles):
    """Initialize and play the game Snake."""
    if size == 0: height, width = 20, 20
    elif size == 1: height, width = 30, 30
    elif size == 2: height, width = 40, 40

    if difficulty == 0: speed = 0.075
    elif difficulty == 1: speed = 0.05
    elif difficulty == 2: speed = 0.025

    game = Game(height, width, speed, placeObstacles)
    game.play()

def processKey(stdscr):
    """Process the user input for menu navigation."""
    global option, size, difficulty, placeObstacles, play, quit

    key = stdscr.getch()

    if key == curses.KEY_UP and option > 0:
        option -= 1
    elif key == curses.KEY_DOWN and option < 4:
        option += 1
    elif key == curses.KEY_LEFT:
        if option == 1 and size > 0 and size <= 2:
            size -= 1
        elif option == 2 and difficulty > 0 and difficulty <= 2:
            difficulty -= 1
        elif option == 3:
            placeObstacles = not placeObstacles
    elif key == curses.KEY_RIGHT:
        if option == 1 and size >= 0 and size < 2:
            size += 1
        elif option == 2 and difficulty >= 0 and difficulty < 2:
            difficulty += 1
        elif option == 3:
            placeObstacles = not placeObstacles
    elif key == ord('\n'):
        if option == 0:
            play = True
        elif option == 4:
            quit = True

def main(stdscr):
    global option, size, difficulty, placeObstacles, play, quit

    curses.curs_set(0)  # Hide the cursor
    stdscr.keypad(True)  # Enable arrow keys

    while not quit:
        displayMenu(stdscr, option, size, difficulty, placeObstacles)
        processKey(stdscr)

        # Play the game
        if play:
            playGame(size, difficulty, placeObstacles)
            play = False

# Global Variables
option = 0
size = 0
difficulty = 0
placeObstacles = False
play = False
quit = False

if __name__ == "__main__":
    # Run the game inside the curses wrapper for cross-platform compatibility
    curses.wrapper(main)
