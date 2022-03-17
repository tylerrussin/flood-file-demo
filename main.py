import os
import sys
import time
import random
import keyboard
import curses

from Command_Line_Font import command_line_font


def flood_fill(screen, sr, sc, new_color, old_color, view):
    '''Conversts values in a matrix in a flood fill
       pattern using depth first search'''

    # Quit simulation
    if keyboard.is_pressed('Q'):
        curses.endwin()                                 # End curses instance
        os.system(f"mode con: cols={120} lines={40}")   # Reset screen buffer
        command_line_font(16)                           # Reset default font size
        sys.exit()                                      # Exit Program

    # Transfrom value
    if screen[sr][sc] == old_color:

        screen[sr][sc] = new_color  # Set to new color

        # Display current screen
        screen[nScreenHeight - 1][nScreenWidth - 1] = ''
        view.addstr(0, 0, ''.join(str(ele) for sub in screen for ele in sub), curses.color_pair(1))

        for p1, row in enumerate(screen):
            for p2, value in enumerate(row):
                if value == 2:
                    view.addstr(p1, p2, ' ', curses.color_pair(2))

        view.addstr(nScreenHeight - 1, nScreenWidth - 1, '')
        view.refresh()

        time.sleep(.0001)   # Slow down traversal

        # North
        if sr >= 1: 
            flood_fill(screen, sr-1, sc, new_color, old_color, view)

        # South
        if sr+1 < len(screen): 
            flood_fill(screen, sr+1, sc, new_color, old_color, view)

        # West
        if sc >= 1: 
            flood_fill(screen, sr, sc-1, new_color, old_color, view)

        # East
        if sc+1 < len(screen[0]): 
            flood_fill(screen, sr, sc+1, new_color, old_color, view)


if __name__ == '__main__':

    command_line_font(16)       # Console ASCII font size
    nScreenWidth = 120          # Console Screen Size X (columns)
    nScreenHeight = 40          # Console Screen Size Y (rows)
    sr = 20                      # Color change starting coords
    sc = 60
    new_color = 2               # Color to be changed to

    # Create Screen Buffer
    screen = [[random.choice([' ',' ', u'\u2588']) for x in range(nScreenWidth)] for y in range(nScreenHeight)]
    os.system(f"mode con: cols={nScreenWidth} lines={nScreenHeight}")
    view = curses.initscr()
    curses.start_color()                                            # Enables color
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)     # Setting color pairs
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)

    # Set old color
    old_color = screen[sr][sc]

    # Preform transformation
    if new_color != old_color:
        flood_fill(screen, sr, sc, new_color, old_color, view)

        while 1:

            # Quit simulation
            if keyboard.is_pressed('Q'):
                curses.endwin()                                 # End curses instance
                os.system(f"mode con: cols={120} lines={40}")   # Reset screen buffer
                command_line_font(16)                           # Reset default font size
                sys.exit()  

            # Display current screen
            screen[nScreenHeight - 1][nScreenWidth - 1] = ''
            view.addstr(0, 0, ''.join(str(ele) for sub in screen for ele in sub), curses.color_pair(1))

            for p1, row in enumerate(screen):
                for p2, value in enumerate(row):
                    if value == 2:
                        view.addstr(p1, p2, ' ', curses.color_pair(2))

            view.addstr(nScreenHeight - 1, nScreenWidth - 1, '')
            view.refresh()