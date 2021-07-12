#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Execute main and secondary menu"""

__version__ = "0.1.6"

import os
import re
import curses


import subprocess

import menu as menu_list

from config import HOME, EDITOR
from alice_in_shell import Alice_in_shell as wonderland


alice = wonderland(HOME)
ALIASES = alice.get_aliases()
MAIN_MENU = ["Edit alias list", "Choose alias", "Exit"]


def main(stdscr):
    alice.source_aliases()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)

    # A UNINTENDED LOL-ZONE: SORRY FOR THIS
    # ------------+----------+-------------
    #      /\O    |    _O    |      O
    #       /\/   |   //|_   |     /_
    #      /\     |    |     |     |\
    #     /  \    |   /|     |    / |
    #   LOL  LOL  |   LLOL   |  LOLLOL
    # ------------+----------+-------------
    # BLACK MAGIC FULL FEATURED ENABLED
    def display_rows(
        menu, row_id: int, page_counter: int, menu_mode: str, height, width
    ):
        current_row_id = row_id
        current_page = page_counter
        display_menu = menu_list.Menu(menu, height, width)
        display_menu.get_menu_list(stdscr, current_row_id, menu_mode)

        # Main menu mode
        if menu_mode == "main":
            while True:
                key = stdscr.getch()
                stdscr.clear()
                # TODO: Use switch, Luke!
                if key == curses.KEY_UP and current_row_id > 0:
                    current_row_id -= 1
                    stdscr.refresh()
                elif key == curses.KEY_UP and current_row_id == 0:
                    current_row_id = 2
                    stdscr.refresh()
                elif (
                    key == curses.KEY_DOWN
                    and current_row_id < len(display_menu.menu) - 1
                ):
                    current_row_id += 1
                    stdscr.refresh()
                elif key == curses.KEY_DOWN and current_row_id == 2:
                    current_row_id = 0
                    stdscr.refresh()
                # editor mode
                elif (
                    key == curses.KEY_ENTER
                    or key in [10, 13]
                    and current_row_id == len(display_menu.menu) - 3
                ):
                    alice.edit_aleases(EDITOR)
                    stdscr.refresh()
                    display_rows(MAIN_MENU, 0, 1, "main", height, width)

                # load first page of aliases
                elif (
                    key == curses.KEY_ENTER
                    or key in [10, 13]
                    and current_row_id == len(display_menu.menu) - 2
                ):
                    if ALIASES:
                        stdscr.refresh()
                        chunk = alice.alias_paginate(ALIASES, current_page)
                        if chunk:
                            display_rows(
                                chunk, 0, current_page, "aliases", height, width
                            )
                        else:
                            break
                    else:
                        stdscr.addstr(1, 0, "Sory, there are no aleases")
                        stdscr.getch()
                elif (
                    key == curses.KEY_ENTER
                    or key in [10, 13]
                    and current_row_id == len(display_menu.menu) - 1
                ):
                    stdscr.clear()
                    break
                # Some adaptive, if we want to resize window update the func with the new h, w
                elif key == curses.KEY_RESIZE:
                    stdscr.refresh()
                    height, width = stdscr.getmaxyx()
                    display_rows(
                        menu, current_row_id, current_page, menu_mode, height, width
                    )
                    break
                elif key == curses.KEY_EXIT or ord("q"):
                    break

                display_menu.get_menu_list(stdscr, current_row_id, "main")

        # Aliases menu navmode
        elif menu_mode == "aliases":
            while True:
                key = stdscr.getch()
                stdscr.clear()
                # UP condition
                if key == curses.KEY_UP and current_row_id > 0:
                    current_row_id -= 1
                    stdscr.refresh()
                elif key == curses.KEY_UP and current_row_id <= 0 and current_page == 1:
                    current_row_id = 0
                    stdscr.refresh()
                # paginate to the previuos page of aleases
                elif key == curses.KEY_UP and current_row_id <= 0:
                    stdscr.refresh()
                    current_page -= 1
                    prev_chunk = alice.alias_paginate(ALIASES, current_page)
                    if prev_chunk:
                        display_rows(
                            prev_chunk, 0, current_page, "aliases", height, width
                        )
                    else:
                        break
                # DOWN condition
                elif (
                    key == curses.KEY_DOWN
                    and current_row_id < len(display_menu.menu) - 1
                ):
                    current_row_id += 1
                    stdscr.refresh()
                # paginate to the next page of aleases
                elif key == curses.KEY_DOWN and current_row_id >= 9:
                    stdscr.refresh()
                    current_page += 1
                    next_chunk = alice.alias_paginate(ALIASES, current_page)
                    if next_chunk:
                        display_rows(
                            next_chunk, 0, current_page, "aliases", height, width
                        )
                    else:
                        break
                elif key == curses.KEY_ENTER or key in [10, 13]:
                    stdscr.refresh()
                    for _id, row in enumerate(menu):
                        if _id == current_row_id:
                            cmdr = str(
                                re.sub(r"[^\w\s]+|[\d]+", r"", f"{str(row)}").strip()
                            )
                            stdscr.addstr(0, 0, cmdr)
                            stdscr.addstr(3, 0, "Press Enter to exec")
                            stdscr.getch()
                            curses.endwin()
                            # getting os enviroment for source aliases
                            subprocess.call([os.environ["SHELL"], "-ic", cmdr])

                # RESIZE condition
                elif key == curses.KEY_RESIZE:
                    stdscr.refresh()
                    height, width = stdscr.getmaxyx()
                    display_rows(
                        menu, current_row_id, current_page, menu_mode, height, width
                    )
                    break
                elif key == ord("q"):
                    break
                display_menu.get_menu_list(stdscr, current_row_id, "aliases")

    # Getting initial terminal window size
    height, width = stdscr.getmaxyx()

    display_rows(MAIN_MENU, 0, 1, "main", height, width)


if __name__ == "__main__":
    curses.wrapper(main)
