@bot.command()
async def encode(ctx, *, text:str):
    value = 0
    arr = []
    for i in text:
        if i == "a":
            arr.append("+#")
        elif i == "b":
            arr.append("++#")
        elif i == "c":
            arr.append("+++#")
        elif i == "d":
            arr.append("++++#")
        elif i == "e":
            arr.append("+++++#")
        elif i == "f":
            arr.append("++++++#")
        elif i == "g":
            arr.append("+++++++#")
        elif i == "h":
            arr.append("++++++++#")
        elif i == "i":
            arr.append("+++++++++#")
        elif i == "j":
            arr.append("++++++++++#")
        elif i == "k":
            arr.append("+++++++++++#")
        elif i == "l":
            arr.append("++++++++++++#")
        elif i == "m":
            arr.append("+++++++++++++#")
        elif i == "n":
            arr.append("++++++++++++++#")
        elif i == "o":
            arr.append("+++++++++++++++#")
        elif i == "p":
            arr.append("++++++++++++++++#")
        elif i == "q":
            arr.append("+++++++++++++++++#")
        elif i == "r":
            arr.append("++++++++++++++++++#")
        elif i == "s":
            arr.append("+++++++++++++++++++#")
        elif i == "t":
            arr.append("++++++++++++++++++++#")
        elif i == "u":
            arr.append("+++++++++++++++++++++#")
        elif i == "v":
            arr.append("++++++++++++++++++++++#")
        elif i == "w":
            arr.append("+++++++++++++++++++++++#")
        elif i == "x":
            arr.append("++++++++++++++++++++++++#")
        elif i == "y":
            arr.append("+++++++++++++++++++++++++#")
        elif i == "z":
            arr.append("++++++++++++++++++++++++++#")
        elif i == "A":
            arr.append("+@")
        elif i == "B":
            arr.append("++@")
        elif i == "C":
            arr.append("+++@")
        elif i == "D":
            arr.append("++++@")
        elif i == "E":
            arr.append("+++++@")
        elif i == "F":
            arr.append("++++++@")
        elif i == "G":
            arr.append("+++++++@")
        elif i == "H":
            arr.append("++++++++@")
        elif i == "I":
            arr.append("+++++++++@")
        elif i == "J":
            arr.append("++++++++++@")
        elif i == "K":
            arr.append("+++++++++++@")
        elif i == "L":
            arr.append("++++++++++++@")
        elif i == "M":
            arr.append("+++++++++++++@")
        elif i == "N":
            arr.append("++++++++++++++@")
        elif i == "O":
            arr.append("+++++++++++++++@")
        elif i == "P":
            arr.append("++++++++++++++++@")
        elif i == "Q":
            arr.append("+++++++++++++++++@")
        elif i == "R":
            arr.append("++++++++++++++++++@")
        elif i == "S":
            arr.append("+++++++++++++++++++@")
        elif i == "T":
            arr.append("++++++++++++++++++++@")
        elif i == "U":
            arr.append("+++++++++++++++++++++@")
        elif i == "V":
            arr.append("++++++++++++++++++++++@")
        elif i == "W":
            arr.append("+++++++++++++++++++++++@")
        elif i == "X":
            arr.append("++++++++++++++++++++++++@")
        elif i == "Y":
            arr.append("+++++++++++++++++++++++++@")
        elif i == "Z":
            arr.append("++++++++++++++++++++++++++@")
        elif i == " ":
            arr.append("*")
        elif i.isdigit:
            if i == 0:
                arr.append("!&")
            else:
                var = "+"*int(i) + "&!"
                arr.append(var)

    arr.append(".;")
    var = ''.join(arr)
    await ctx.reply(f"`{var}`")
