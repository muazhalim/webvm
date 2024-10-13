# List of all source files
SRCS = $(wildcard *.c)

# Automatically generate program names from source files
PROGS = $(patsubst %.c,%,$(SRCS))

# Define the games you want to compile
GAMES := invaders minesweeper snake sokoban sudoku tetris

# Flags for the C compiler
CFLAGS := -Wall -Wextra -O2 -I$(PWD)/termbox/src   # Added the path to the local termbox headers
LDLIBS := -L$(PWD)/termbox -ltermbox  # Link the local termbox library

# Default rule for compiling all games
all: $(PROGS) $(GAMES)

# Rule for compiling any generic C file
%: %.c
	$(CC) $(CFLAGS) $(LDLIBS) -o $@ $<

# Clean rule to remove compiled programs and games
clean:
	rm -f $(PROGS) $(GAMES)

.PHONY: all clean
