data = {'?': 0, 'a': 0, 'b': 0, 
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
        data["o"]=49
    elif num==2: 
        data["t"]=50
    elif num==3: 
        data["h"]=51
    elif num==4: 
        data["n"]=ord(input('>'))
    elif num==5: 
        print(chr(data["n"]), end='')
    elif num==6: 
        print(chr(39), end='')
    elif num==7: 
        data["?"]=13 if data["n"]==data["o"] else data["?"]
    elif num==8: 
        data["?"]=16 if data["n"]==data["t"] else data["?"]
    elif num==9: 
        data["?"]=19 if data["n"]==data["h"] else data["?"]
    elif num==10: 
        print(chr(data["T"]), end='')
    elif num==11: 
        print(chr(data["H"]), end='')
    elif num==12: 
        data["?"]=21
    elif num==13: 
        print(chr(data["S"]), end='')
    elif num==14: 
        print(chr(data["T"]), end='')
    elif num==15: 
        data["?"]=21
    elif num==16: 
        print(chr(data["N"]), end='')
    elif num==17: 
        print(chr(data["D"]), end='')
    elif num==18: 
        data["?"]=12
    elif num==19: 
        print(chr(data["R"]), end='')
    elif num==20: 
        print(chr(data["D"]), end='')
    elif num==21: 
        pass

endline=21
while data["?"]!=endline:
    hold=data["?"]
    execute(data["?"])
    if data["?"]==hold:
        data["?"]+=1