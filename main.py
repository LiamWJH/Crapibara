import re as regex

initcommand = input()
initcommand = initcommand.split(" ")

file = ''
#init command stuff (inbrace, format, BOOM)
if initcommand[0] == "inbrace":
    with open(initcommand[1], "r") as f:
        file = f.read()

#built in BS
def math(value):

    #finish the function idiot you were implementing changing the values of numbers and expression into a single result Think Think Think! use del btw
    value = value.split(" ")
    index = 0
    for thing in value:
        if thing == "+":
            int(value[index - 1]) + int(value[index + 1])
            value[index - 1]

            index += 2
        if thing == "-":
            int(value[index - 1]) - int(value[index + 1])
            index += 2
        if thing == "*"
            int(value[index - 1]) * int(value[index + 1])
            index += 2
        if thing == "//":
            int(value[index - 1]) // int(value[index + 1])
            index += 2
        if thing == "/":
            int(value[index - 1]) / int(value[index + 1])
            index += 2
    
def printlnv(value):
    if regex.fullmatch(r'"[^"]*"', value):
        print(value[1:-1])  #removing '"' btw
    else:
        if "+" in value or "-" in value or "*" in value or "//" in value or "/" in value:
            print(math(value))
        else:
            print(variables[value])

def printv(value):
    if regex.fullmatch(r'"[^"]*"', value):
        print(value[1:-1], end="")  #removing '"' btw
    else:
        print(variables[value], end="")

def inputv(value):
    variables[value] = input()

variables = {"Hello_World":"Easy"}
def makevar(name, value):
    variables[name] = value
#enterpreteur

#flatten list for code_lines
def flattenlist(vallist):
    flattened_ver = []
    for thing in vallist:
        if isinstance(thing, list):
            flattened_ver.extend(flattenlist(thing))
        else:
            flattened_ver.append(thing)
    return flattened_ver

#repeat loop BS
#helper for NESTEDqrqrqrqrqrqr
def run_block(code):
    _loopidx = 0
    while _loopidx < len(code):
        line = code[_loopidx]
        command = regex.sub(r'"[^"]*"', '', line)
        command = regex.sub(r"\([^)]*\)", "()", command)

        if command == "repeat()":
            skipidx = _loopidx
            while skipidx < len(code) and code[skipidx].strip() != "end":
                skipidx += 1

            ntimes = regex.search(r"\d+", line)
            if ntimes:
                inner_block = code[_loopidx + 1 : skipidx]
                for _ in range(int(ntimes.group())):
                    run_block(inner_block)

            _loopidx = skipidx + 1
            continue

        match command:  
            case "once()":
                pass

            case "printv()":
                matchval = regex.search(r"\((.*?)\)", line)
                if matchval:
                    printv(matchval.group(1))

            case "printlnv()":
                matchval = regex.search(r"\((.*?)\)", line)
                if matchval:
                    printlnv(matchval.group(1))
            
            case "inputv()":
                matchval = regex.search(r"\((.*?)\)", line)
                if matchval:
                    inputv(matchval.group(1))
            case "///":
                _loopidx += 1
                while _loopidx < len(code) and code[_loopidx] != "///":
                    _loopidx += 1

                _loopidx += 1
                continue

            

            case "end":
                break

            case other:
                other = other.split(" ")
                makevar(other[0].strip(), other[2].strip())

        _loopidx += 1


splitted = []

for thing in file.split("\n"):
    if "{" in thing or "}" in thing:
        if "{" in thing:
            splitted.append(thing[:-2])
        if "}" in thing:
            pass
    else:
        splitted.append(thing)

for thing in range(len(splitted)):
    splitted[thing] = splitted[thing].strip()
    splitted[thing] = splitted[thing].split("\n")

code_lines = flattenlist(splitted)
code_lines = [line for line in code_lines if line] # '' removal

print("\n\n")
print("detected functions:")
print(code_lines)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("")


run_block(code_lines)