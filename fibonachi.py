FIBONACHI_START = []


def fibonachi():
    count = int(input('Enter count for Fibonachi cycle: '))
    for i in range(count):
        if i == 0:
            FIBONACHI_START.append(0)
            continue
        if i == 1:
            FIBONACHI_START.append(1)
            continue
        else:
            FIBONACHI_START.append(FIBONACHI_START[i-2] + FIBONACHI_START[i-1])

if __name__ == '__main__':
    fibonachi()
    for num in FIBONACHI_START:
        print (num)