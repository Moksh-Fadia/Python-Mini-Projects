import curses           # this module allows styling of the terminal (ie. coloring, etc)
from curses import wrapper              # wrapper (is a func) initializes the curses module
import time
import random

def start_screen(stdscr):
    stdscr.clear()          # clears the screen first
    stdscr.addstr("Welcome to the Speed Typing Test!\n")       # adds text to the screen
    stdscr.addstr("Press any key to begin!")        
    stdscr.refresh()        # refreshes the screen
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):       
    stdscr.addstr(target)      # adds the target_text to the screen
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]    # each character of target will be stored as correct_char
        color = curses.color_pair(1)    #display whataver the user types correclty in Cyan color

        if char != correct_char:
            color = curses.color_pair(2)    #display whataver the user types incorreclty in Red color

        stdscr.addstr(0, i, char, color)   # i will be incremented and it will be overriding each character in the target_text


def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()  # strip removes all the default \n, trailing white space characters from the lines


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)        # it means do not stop time/delay even if user hasn't pressed any key (keep the time going on)

    while True:
        time_elapsed = max(time.time() - start_time, 1)     # if time.time() - start_time = 0, then it will give the max value from the brackets (0,1) which is 1

        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
# (time_elapsed / 60) = our writing time in minutes (coz it orignially gives in seconds)
# len(current_text) / (time_elapsed / 60) = number of characters per minute
# (len(current_text) / (time_elapsed / 60)) / 5 = number of words per minute

        stdscr.clear() 
        display_text(stdscr, target_text, current_text, wpm)       
        stdscr.refresh()

        if "".join(current_text) == target_text:   # "".join(list) -> joins/converts all the words of the list into a string [list to string]
            stdscr.nodelay(False)       # wait for the user to hit a key (ie. show what is on the screen before exiting)
            break   #[outside of while loop]

        try:    # to prevent any crash if the user dosen't type any key
            key = stdscr.getkey()       
        except:
            continue    # continue goes back at the start of the while loop

        if ord(key) == 27:          # ordinal/ASCII value of a key is its numeric representation (eg: ord(escape) = 27); means if user presses ecape key the loop will break and will be exited from terminal
            break   #[outside of while loop]

        if key in ("KEY_BACKSPACE", '\b', "\x7f"): #these are all forms of writing backspace key in different operating systems
            if len(current_text) > 0:
                current_text.pop()      # deletes the last character from the list
        elif len(current_text) < len(target_text):      # to check we don't exceed the length of the target_text
            current_text.append(key)        # it appends whatever the user types into the current_text list

    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:     # to play as many times as you want
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press any key to continue....")
        key = stdscr.getkey()

        if ord(key) == 27:      # escape key
            break

wrapper(main)           # wrapper func calls the main and also initializes the curser module

