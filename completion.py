import curses as cs

def input_autocomplete(commands: list, output: str = ""):
    def draw_menu(stdscr, search, suggestions):
        stdscr.clear()
        stdscr.addstr(0, 0, output)
        stdscr.addstr(1, 0, f"Search: {search}")
        if suggestions:
            suggestion_str = ' '.join(f'[{s}]' for s in suggestions)
            stdscr.addstr(2, 0, suggestion_str)
        stdscr.refresh()

    def main(stdscr):
        cs.curs_set(0)  # 隐藏光标
        stdscr.clear()
        stdscr.refresh()
        another = ""
        search = ""
        while True:
            suggestions = weighted_search(commands, search, another_search=another)
            draw_menu(stdscr, search, suggestions)
            
            key = stdscr.getkey()
            if key == '\n':
                break
            elif key.isdigit() and 1 <= int(key) <= 9:
                index = int(key) - 1
                if index < len(suggestions):
                    search = suggestions[index]
            elif key == '\b' or key == '\x7f':
                search = search[:-1]
            else:
                another = key.lower()
                search += key

        return search

    return cs.wrapper(main)

def weighted_search(commands, search, another_search=None):
    weights = {cmd: 0 for cmd in commands}
    
    for cmd in commands:
        if search.lower() in cmd.lower():
            weights[cmd] += 100
        if another_search and another_search.lower() in cmd.lower():
            weights[cmd] += 1
        for word in search.split():
            if word.lower() in cmd.lower():
                weights[cmd] += 1
    sorted_commands = sorted(commands, key=lambda x: weights.get(x, 0), reverse=True)
    
    result = sorted_commands[:9]
    
    return result

# Example is a shit code, you cann't understand it by example!
if __name__ == '__main__':
    print("what a fcking code, you cann't understand it by example!")