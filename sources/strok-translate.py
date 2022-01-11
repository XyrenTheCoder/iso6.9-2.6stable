### DO NOT MODIFY
import os
import json
import time
import random
import sys as sus

cwd = os.getcwd()

def run():
    while True:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("Stroke translator\nMade by thatOneArchUser :)\n\n")
        inp = input("- Type your stroke here (ctrl + c to exit): ")
        for i in range(5):
            print("Translating" + "."*i)
            sus.stdout.write("\033[F")
            time.sleep(0.25)
        with open(f"E:/VSC/words.json", "r") as f:
            words = json.load(f)
        var = str()
        s = inp.lower()
        for i, c in enumerate(s):
            var += random.choice(words[c])
        print(var)
        input("Press enter to continue...")

try:
    run()
except KeyboardInterrupt:
    print("\nExiting...")
    time.sleep(0.5)
    sus.exit()
except Exception as e:
    print(e)
