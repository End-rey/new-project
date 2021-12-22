def command():
    # пишем сначала количество комманд, потом сами комманды из списка
    n = int(input())
    l = []
    for _ in range(n):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd != "print":
            cmd += "(" + ",".join(args) + ")"
            eval("l."+cmd)
        else:
            print(l)


def main():
    command()


if __name__ == '__main__':
    main()
