# Takes a Set program names source.txt.
# Creates an equivalent Python program named output.py

from linecache import getline

key = True
line = 1

def resolve(p,line,s=0):
    if p.isnumeric():
        return p
    elif p.isalpha() or p == "?":
        return 'data["%s"]' %(p)
    elif p=="!":
        return "0"
    else:
        print("Line: %i" %(line))
        if s == 1:
            raise Exception("Invaild condition value.")
        else: 
            raise Exception("Invaild source value.")


with open("output.py","w") as target:
    target.write("""data = {'?': 0, 'a': 0, 'b': 0, 
'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 
'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 
'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 
'x': 0, 'y': 0, 'z': 0, 'A': 65, 'B': 66, 'C': 67, 
'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 
'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79,
'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 
'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90}

def execute(num):
    global data
    if num==1:
        """)
    while key == True:
        setline = ""
        condition = ""
        currentline = getline("source.txt", line)
        if currentline == "":
            break
        currentline = currentline[:-1]
        currentline = currentline.split()
        if currentline[0][0]=="[":
            trigger = currentline[0][1:4]
            currentline.pop(0)
            condition=" if "
            condition+= resolve(trigger[0],line,1)
            if trigger[1] == "=":
                condition+="=="
            elif trigger[1] == "/":
                condition+="!="
            else:
                print("Line: %i" %(line))
                raise Exception("Invaild condition.")
            condition+= resolve(trigger[2],line,1)
            condition+=" else "

        if currentline[0] == "Set" or currentline[0] == "set":
            if currentline[1] == "!":
                setline = "print(chr("
            elif currentline[1].isnumeric():
                print("Line: %i" %(line))
                raise Exception("Can't set a constant.")
            else:
                setline = 'data["%s"]=' %(currentline[1])
        
            if currentline[2]=="!":
                setline+="ord(input('>'))"
            elif currentline[2][0]!="(":
                setline+=resolve(currentline[2],line)
            else:
                currentline[2]=currentline[2][1:-1]
                setline+=resolve(currentline[2][0],line)
                if currentline[2][1]=="+" or currentline[2][1]=="-":
                    setline+=currentline[2][1]
                else:
                    print("Line: %i" %(line))
                    raise Exception("Invalid combiner.")
                setline+=resolve(currentline[2][2],line)
            if currentline[1] == "!":
                setline += "), end='')"
            if condition != "":
                condition+=resolve(currentline[1],line)
                setline += condition
            target.write(setline)
        else:
            target.write("pass")
        line+=1
        target.write("\n    elif num==%i: " %(line))
        target.write("\n        ")
    target.write("""pass

endline="""+str(line)+"\n")
    target.write("""while data["?"]!=endline:
    hold=data["?"]
    execute(data["?"])
    if data["?"]==hold:
        data["?"]+=1""")
print("Translation Successful!")