import curses
from curses import wrapper
import queue
import time


maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    MAG = curses.color_pair(3)
    RED = curses.color_pair(2)
    # index , value
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            # multiplying to add more space
            stdscr.addstr(i,j *2, value,MAG)
            


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j

    return None


# standard output screen
def main(stdscr):
    #curses.init_pair(1, curses.FOREGROUND_COLOR, curses.BACKGROUND_COLOR)
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    mag_n_black = curses.color_pair(3)

    stdscr.clear()
    # stdscr.addstr(row_pos,col_pos "string to write",color)
    # stdscr.addstr(0,0, "Hello World!",mag_n_black)
    print_maze(maze,stdscr)
    stdscr.refresh()
    stdscr.getch() # get character, waits for an enterred character



if __name__ == "__main__":
    print("lets go")
    wrapper(main)
    print("Done")
    