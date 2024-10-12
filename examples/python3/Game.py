import random
import time
import platform
import os
import curses
from KeyListener import KeyListener
from Square import Square
from Snake import Snake
from Direction import Direction

class Game:
    """The game of Snake."""

    def __init__(self, height, width, speed, placeObstacles=False):
        # Integer height of the plane
        self.height = height
        # Integer width of the plane
        self.width = width
        # Integer delay between frames of the game
        self.speed = speed
        # Integer score that is the length of the snake
        self.score = 0
        # The snake, starting on the left side of the plane
        self.snake = Snake(Square(height // 2, width // 2, self.width))
        # Boolean indicating whether to place obstacles or not
        self.placeObstacles = placeObstacles
        # Set of squares representing obstacles
        self.obstacles = set()
        # Square representing the food
        self.food = None

    def play(self, stdscr):
        """Play the game with curses."""
        previousDirection = None

        # Initialize the key listener with stdscr (from curses)
        listener = KeyListener(stdscr)
        listener.start()

        # Place the first food
        self.placeFood()

        # Main game loop
        while not self.gameOver() and not listener.quit:
            # Clear the screen
            stdscr.clear()
            self.display(stdscr, listener.paused)

            # Delay movement for the specified time
            time.sleep(self.speed)

            # Update the current direction
            currentDirection = listener.direction

            # Snake cannot immediately reverse direction
            if currentDirection == Direction.opposite(previousDirection):
                currentDirection = previousDirection

            # Move the snake if not paused
            if not listener.paused:
                self.move(currentDirection)

            # Store previous direction
            previousDirection = currentDirection

        # End the key listener
        listener.end()

        # Pause for 1 second
        time.sleep(1)

    def move(self, currentDirection):
        """Move the snake."""
        next = self.nextSquare(currentDirection)

        if next:
            # Snake gets a food and grows by 1 square
            if next == self.food:
                self.snake.grow(next)
                self.placeFood()
                if self.placeObstacles:
                    self.placeObstacle()

                self.score += 1
            # Snake moves to next square
            else:
                self.snake.advance(next)

    def display(self, stdscr, paused):
        """Display the game on the screen."""
        string = ""

        pausedString = "| PAUSED |"
        pausedString = pausedString if len(pausedString) + 2 <= self.width and paused else ""
        string += "+" + pausedString.center(self.width, "-") + "+\n"

        for row in reversed(range(self.height)):
            string += "|"
            for column in range(self.width):
                # Print the snake
                if Square(row, column, self.width) in self.snake:
                    string += "O"
                # Print an obstacle
                elif Square(row, column, self.width) in self.obstacles:
                    string += "&"
                # Print the food
                elif Square(row, column, self.width) == self.food:
                    string += "+"
                # Print an empty space
                else:
                    string += " "
            string += "|\n"

        # Display the score in the bottom border
        scoreString = "| SCORE: " + str(self.score) + " |"
        scoreString = scoreString if len(scoreString) + 2 <= self.width else "| " + str(self.score) + " |"
        string += "+" + scoreString.center(self.width, "-") + "+\n"

        # Print to stdscr instead of regular print (since curses is used)
        stdscr.addstr(string)
        stdscr.refresh()

    # ... (other methods like gameOver, nextSquare, placeFood, placeObstacle remain unchanged) ...

def main(stdscr):
    """Main function to run the game with curses."""
    game = Game(height=20, width=20, speed=0.1, placeObstacles=False)
    game.play(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)  # Ensure proper curses handling
