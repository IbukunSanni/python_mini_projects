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

def main(stdscr):

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    blue_and_black = curses.color_pair(2)
    stdscr.clear()
    stdscr.addstr(6,5, "Hello World!",blue_and_black)
    stdscr.refresh()
    stdscr.getch()



if __name__ == "__main__":
    wrapper(main)
    