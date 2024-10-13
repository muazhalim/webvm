# List of all source files
SRCS = $(wildcard *.c)

# Automatically generate program names from source files
PROGS = $(patsubst %.c,%,$(SRCS))

# Flags for the C compiler
CFLAGS := -Wall -Wextra -O2 -I$(PWD)   # Include path to the current directory where termbox.h is located
LDLIBS := -L$(PWD) -ltermbox           # Link the local termbox library

# Default rule for compiling all programs
all: $(PROGS)

# Rule for compiling any generic C file
%: %.c
	$(CC) $(CFLAGS) $(LDLIBS) -o $@ $<

# Clean rule to remove compiled programs
clean:
	rm -f $(PROGS)

.PHONY: all clean
