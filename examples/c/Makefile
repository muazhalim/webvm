# List of all source files
SRCS = $(wildcard *.c)

# Automatically generate program names from source files
PROGS = $(patsubst %.c,%,$(SRCS))

# Flags for the C compiler
CFLAGS := -Wall -Wextra -O2 -I$(PWD)   # Include path to the current directory where termbox.h is located
LDLIBS := termbox.o                    # Link the termbox.o object file

# Default rule for compiling all programs
all: $(PROGS)

# Rule for compiling any generic C file
%: %.c
	$(CC) $(CFLAGS) $(LDLIBS) -o $@ $<

# Clean rule to remove compiled programs
clean:
	rm -f $(PROGS) termbox.o

.PHONY: all clean
