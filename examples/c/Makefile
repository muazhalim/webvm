# List of all source files
SRCS = $(wildcard *.c)

# Automatically generate program names from source files
PROGS = (patsubst(patsubst %.c,%,(SRCS))

# Define the games you want to compile
GAMES := invaders minesweeper snake sokoban sudoku tetris

# Flags for the C compiler
CFLAGS := -Wall -Wextra -O2 -I$(PWD)   # Include path to the current directory where termbox.h is located
LDLIBS := -L$(PWD) -ltermbox           # Link the local termbox library

# Default rule for compiling all games
all: $(PROGS)

# Rule for compiling any generic C file
%: %.c
	(CC)(CC) (CFLAGS) (LDLIBS)−o(LDLIBS) -o @ $<

# Clean rule to remove compiled programs and games
clean:
	rm -f $(PROGS)

.PHONY: all clean
