from collections import deque
import sys

def is_palindrome(line):
    if len(line) < 2:
        return False

    dq = deque()

    for c in line:
        dq.append(c)

    while len(dq) > 0:
        c = dq.popleft()

        if len(dq) == 0:
            return True

        if c != dq.pop():
            return False

    return True


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

            print(f'Line "{line}" is {"not a " if not is_palindrome(clean_line) else ""}palindrome')

if __name__ == '__main__':
    main()