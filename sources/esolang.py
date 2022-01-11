import os
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
print("Archiescript v1.0\n")

value = 0
cmd = input(">> ")
l = []
for i in cmd:
    l.append(i)

text = []
for c in l:
    if c == "+":
        value += 1
    elif c == "-":
        value -= 1
    elif c == ".":
        print(''.join(text))
    elif c == '#':
        if value == 1:
            text.append("a")
        elif value == 2:
            text.append("b")
        elif value == 3:
            text.append("c")
        elif value == 4:
            text.append("d")
        elif value == 5:
            text.append("e")
        elif value == 6:
            text.append("f")
        elif value == 7:
            text.append("g")
        elif value == 8:
            text.append("h")
        elif value == 9:
            text.append("i")
        elif value == 10:
            text.append("j")
        elif value == 11:
            text.append("k")
        elif value == 12:
            text.append("l")
        elif value == 13:
            text.append("m")
        elif value == 14:
            text.append("n")
        elif value == 15:
            text.append("o")
        elif value == 16:
            text.append("p")
        elif value == 17:
            text.append("q")
        elif value == 18:
            text.append("r")
        elif value == 19:
            text.append("s")
        elif value == 20:
            text.append("t")
        elif value == 21:
            text.append("u")
        elif value == 22:
            text.append("v")
        elif value == 23:
            text.append("w")
        elif value == 24:
            text.append("x")
        elif value == 25:
            text.append("y")
        elif value == 26:
            text.append("z")
        value = 0
    elif c == '@':
        if value == 1:
            text.append("A")
        elif value == 2:
            text.append("B")
        elif value == 3:
            text.append("C")
        elif value == 4:
            text.append("D")
        elif value == 5:
            text.append("E")
        elif value == 6:
            text.append("F")
        elif value == 7:
            text.append("G")
        elif value == 8:
            text.append("H")
        elif value == 9:
            text.append("I")
        elif value == 10:
            text.append("J")
        elif value == 11:
            text.append("K")
        elif value == 12:
            text.append("L")
        elif value == 13:
            text.append("M")
        elif value == 14:
            text.append("N")
        elif value == 15:
            text.append("O")
        elif value == 16:
            text.append("P")
        elif value == 17:
            text.append("Q")
        elif value == 18:
            text.append("R")
        elif value == 19:
            text.append("S")
        elif value == 20:
            text.append("T")
        elif value == 21:
            text.append("U")
        elif value == 22:
            text.append("V")
        elif value == 23:
            text.append("W")
        elif value == 24:
            text.append("X")
        elif value == 25:
            text.append("Y")
        elif value == 26:
            text.append("Z")
        value = 0
    elif c == ";":
        quit()
    elif c == "*":
        text.append(" ")
    elif c == "!":
        value = 0
    elif c == "&":
        text.append(str(value))
