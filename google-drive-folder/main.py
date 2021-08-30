from drive_get import create

def folder(folder):
    create(folder)
    mess = 'Created in Juvenile Project folder: \n Juvenile Project'
    d = 0
    for i in folder.split("/"):
        if i[0] == "&":
            for a in i[1:].split("|"):
                mess += "\n" + "\t" * d + "↳" + a
        else:
            mess += "\n" + "\t" * d + "↳" + i
        d += 2
    print(mess)

folder("hello/&why|22|11")