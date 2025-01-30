import curses           # this module allows styling of the terminal (ie. coloring, etc)
from curses import wrapper              # wrapper (is a func) initializes the curses module
import time
import queue        # FIFO

maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "O"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " "],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    [" ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["X", "#", "#", "#", "#", "#", "#", "#", "#"]
]


def print_maze(maze, stdscr, path=[]): # path=[] is a default list passed as an argument (you dont need to call that in a func)
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):          # i will iterate through each row (basically it will be the row number)
        for j, value in enumerate(row):   # j will iterate through all of the values in a row (basically it will be the column number of that value)
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            else:    
                stdscr.addstr(i, j*2, value, BLUE)      # i and j will be the position(*2 so that it spreads out a little bit thus maintaining space between each position so that it dosen't look too squishy), value will be the thing which is at that position (ie. either #, O or X)
# basically it will print the whole 2D maze


def find_start(maze, start):
    for i, row in enumerate(maze):          
        for j, value in enumerate(row): 
            if value == start:
                return i, j         # returns i, j => coordinates of the start pointe ie.O
    return None


def find_path(maze, stdscr):
    start = "O"
    end ="X"
    start_pos = find_start(maze, start)

    q = queue.Queue()      # setting up the queue and finding the neighbours (our goal is to find the shortest path from start to end ie. BFS)
    q.put((start_pos, [start_pos]))
        # put method is used for inserting
# [start_pos] is a list which will contain all the nodes we come across while reaching from start to end

    visited = set()     # visited is a set which will contain all the positions which we have currently visited

    while not q.empty():        
        current_pos, path = q.get()     # get gives whatever element is at the end of the queue ie.current_pos
        #start_pos, [start_pos]
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)         # to slow down the proces in order for us to see
        stdscr.refresh()

        if maze[row][col] == end:       # end = "X"
            return path
        
        neighbours = find_neighbours(maze, row, col)
        for neighbour in neighbours:    # to check if the neighbour is an obstacle or not
            if neighbour in visited:
                continue        # we don't process it if it is already visited

            r, c = neighbour
            if maze[r][c] == '#':
                continue

            new_path = path + [neighbour]       # adding two lists (ie. add those empty spaces from neighbours list with the path)
            q.put((neighbour, new_path))
            visited.add(neighbour)      # makeit visited so that it dosen't visit it again



def find_neighbours(maze, row, col):       # func to find empty spaces in the path from start to end
    neighbours = []

    if row > 0:      # checks empty spaces in UP direction (means all the other rows except the first row which is at 0 pstn)
        neighbours.append((row - 1, col))


    if row + 1 < len(maze):       # checks empty spaces in DOWN direction (means all the other rows except the last row which is at len(maze) pstn)
        neighbours.append((row + 1, col))

    if col > 0:          # checks empty spaces in LEFT direction
        neighbours.append((row, col - 1))    

    if col + 1 < len(maze[0]):    # checks empty spaces in RIGHT direction (maze[0] means length of the first row ie. no. of columns)
        neighbours.append((row, col + 1))

    return neighbours    


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)




