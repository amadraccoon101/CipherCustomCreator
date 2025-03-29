from skillCreator import createSkills
import sys, threading

fname = "AM02"
f = open("inputAM02Revised.txt", "r", encoding="utf-8")
fntsize = 7

nextline = f.readline()
while nextline:
    fntsize = 8
    cardName = nextline.strip()
    bordertxt = f.readline().strip()
    #bordertxt = bordertxt.strip()
    border = True
    if "false" in bordertxt:
        border = False
    if "7" in bordertxt:
        fntsize = 7
    rwln = 290
    if "rlnch" in bordertxt:
        nextline = f.readline()
        rwln = int(nextline.strip())
    skills = []
    nextline = f.readline()
    while nextline and nextline.strip() != "---------------":
        skills.append(nextline)
        nextline = f.readline()
        print(nextline)
    print(border)
    print(cardName)
    print(skills)
    createSkills(skills, cardName, border, fname, fntsize, rwln)
    nextline = f.readline()

limit = sys.getrecursionlimit()
print(limit)
size = threading.stack_size()
print(size)