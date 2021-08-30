from drive_get import create

def folder(folder):
    create(folder)
    mess = 'Here\'s the directory tree:'
    d = 0
    h = 1
    gap = 1
    for i in folder.split("/"):
        if "|" in i:
            for a in i.split("|"):
                if ">" in a:
                    for b in a.split(">"):
                        mess += "\n" + "\t" * (d + h) + "↳" + b
                        h += gap
                        if b == a.split(">")[-1]: h = 1
                else:
                    mess += "\n" + "\t" * d + "↳" + a
                
        else:
            mess += "\n" + "\t" * d + "↳" + i
        d += gap
    print(mess)
print("""
    USAGE:
    Use it as if you're accessing paths in Unix (with /),
    To indicate that the following is creating into the same folder aka have the same level,
    seperate those folders with |
    for child within child of the same folder, use >
    don't use / after using > please, that's enough for me
    eg: documents/child1/child2>child3>child4|child2>child3>child4
    eg2: documents/child1/child2/child 3/child 4
""")
folder(input("Your path is:\n"))
