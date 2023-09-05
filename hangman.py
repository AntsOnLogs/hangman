import string, os, requests, sys, random, platform

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() in ["Linux", "Darwin"]:
        os.system("clear")

def get_word():
    try:
        words = requests.get("https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt").text
    except requests.RequestException:
        try:
            with open("words.txt","r") as f:
                words = f.read()
        except FileNotFoundError:
            print("Could not get word!")
            sys.exit()

    return random.choice(words.splitlines())

def print_stage(stage: int):
    match stage:
        case 1:
            print(hmstage1)
        case 2:
            print(hmstage2)
        case 3:
            print(hmstage3)
        case 4:
            print(hmstage4)
        case 5:
            print(hmstage5)
        case 6:
            print(hmstage6)
        case 7:
            print(hmstage7)

hmstage1 = """
   ┌────────┐
   │        │
   │        │
            │
            │
            │
            │
            │
            │
            │
            │
            │
            │
            │
            │
   ─────────┴─────────"""

hmstage2 = """
   ┌────────┐
   │        │
   │        │
  xxx       │
 xxxxx      │
  xxx       │
            │
            │
            │
            │
            │
            │
            │
            │
            │
   ─────────┴─────────
"""

hmstage3 = """
   ┌────────┐
   │        │
   │        │
  xxx       │
 xxxxx      │
  xxx       │
   x        │
   x        │
   x        │
   x        │
   x        │
            │
            │
            │
            │
   ─────────┴─────────
"""

hmstage4 = """
   ┌────────┐
   │        │
   │        │
  xxx       │
 xxxxx      │
  xxx       │
   x        │
xxxx        │
   x        │
   x        │
   x        │
            │
            │
            │
            │
   ─────────┴─────────
"""

hmstage5 = """
   ┌────────┐
   │        │
   │        │
  xxx       │
 xxxxx      │
  xxx       │
   x        │
xxxxxxx     │
   x        │
   x        │
   x        │
            │
            │
            │
            │
   ─────────┴─────────
"""

hmstage6 = """
   ┌────────┐
   │        │
   │        │
  xxx       │
 xxxxx      │
  xxx       │
   x        │
xxxxxxx     │
   x        │
   x        │
   x        │
  x         │
 x          │
x           │
            │
   ─────────┴─────────
"""

hmstage7 = """
   ┌────────┐
   │        │
   │        │
  xxx       │
 xxxxx      │
  xxx       │
   x        │
xxxxxxx     │
   x        │
   x        │
   x        │
  x x       │
 x   x      │
x     x     │
            │
   ─────────┴─────────
"""

word = get_word()

out = []

s = string.ascii_letters

out = ["_" if i in s else i for i in word]

inval = []

stage = 1

while True:
    print_stage(stage)

    print("".join(out))

    print(f"\nIncorrect guesses: \n{' '.join(inval)}\n" if len(inval) > 0 else "")

    if stage >= 7:
        print(f"You lose! The word was '{word}'")
        break
    elif "".join(out) == word:
        print("\nYou win!")
        break

    guess = input("What's your guess? ").lower()

    if not guess or guess[0] in inval:
        continue

    indexes = [i for i, letter in enumerate(word) if letter.lower() == guess[0]]

    if not indexes:
        stage+=1
        inval.append(guess[0])
    else:
        for i in indexes:
            out[i] = word[i]

    clear()
