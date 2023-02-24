#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Execute main menu"""

__version__ = "0.1.4"

import curses

from menu import Menu
from config import MENU_LANG


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)

    # Getting initial terminal window size
    height, width = stdscr.getmaxyx()

    Menu.display_rows(stdscr, MENU_LANG, 0, 1, "main", height, width)


if __name__ == "__main__":
    curses.wrapper(main)