import argparse
import time


def followfile(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def readfile(filename, num, follow):
    lines = []
    with open(filename, "r") as file:
        if not follow:
            for line in file:
                lines.append(line)
                if len(lines) > num:
                    lines.remove(lines[0])
            print(*lines, end="")
        else:
            for line in file:
                lines.append(line)
                if len(lines) > num:
                    lines.remove(lines[0])
            print(*lines, sep="", end="")
            loglines = followfile(file)
            for line in loglines:
                print(line, end="")


def main():
    parser = argparse.ArgumentParser(description='instructions...')
    parser.add_argument('filename', type=str)
    parser.add_argument('-n', dest="num", type=int, default=10)
    parser.add_argument('-f', dest="follow", action='store_true')
    args = parser.parse_args()
    readfile(args.filename, args.num, args.follow)


if __name__ == "__main__":
    main()
