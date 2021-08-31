import json
import os
import re




def one_line():
    inp = input("Your input: ")
    if os.path.exists("TEMP.txt"):
        os.remove("TEMP.txt")
    patt = input("Pattern: ")
    inp = inp.split(patt)

    write_json(f'splitted.json', inp)
    print("Saved to: " + os.getcwd() + "------->" + "splitted.json")


def read(file: str) -> str:
    return open(file, "r").read()


def write_json(file: str, data: dict):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def write(file: str, data: str):
    with open(file, "w", encoding="utf-8") as f:
        f.write(data)
        f.close()


def multiple_lines():
    write("TEMP.txt", "")
    input("I have just created a new file named TEMP.txt in "
          + os.getcwd() + "\nPlease paste what you want to split in, CLOSE the file before continuing\nPress Enter to continue")
    text = read("TEMP.txt")
    options = input('''OPTIONS:
    Type "num" to remove all numbers and newlines
    Press Enter to remove all newlines only
''')
    text = text.replace("\n", "|")
    if options == "num":
        text = re.sub(r"\d+", "", text)
    write('TEMP.txt', text)
    print('Now copy from the file above and paste it here, all new lines have been replaced with "|"')
    one_line()

i = input("""
    Select 1 if you're splitting a single line
           2 if you're splitting multiple lines
""")
if i == "1":
    one_line()
elif i == "2":
    multiple_lines()
else:
    print("No option, press Enter to exit")