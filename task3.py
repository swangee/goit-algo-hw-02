from collections import deque
import sys


def is_closing(c):
    return c in "}])"


def is_bracket(c):
    return c in "{}[]()"

def matches_closing(open, close):
    match open:
        case "(":
            return close == ")"
        case "{":
            return close == "}"
        case "[":
            return close == "]"
        case _:
            return False

def is_valid_syntax(string):
    stack = deque()

    for c in string:
        if not is_bracket(c):
            continue

        if not is_closing(c):
            stack.append(c)
            continue

        if len(stack) == 0:
            return False

        if not matches_closing(stack.pop(), c):
            return False

    return len(stack) == 0


def cleanup_line(line):
    return line.replace(" ", "").casefold()


def main():
    while True:
        for line in sys.stdin:
            line = line.strip()
            clean_line = cleanup_line(line)

            if 'exit' == clean_line:
                print("good bye")
                return

            print(f'Line "{line}" is {"symmetric " if is_valid_syntax(clean_line) else "asymmetric"}')


if __name__ == '__main__':
    main()