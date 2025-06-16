import re as regex

initcommand = input()
initcommand = initcommand.split(" ")

file = ''
#init command stuff (inbrace, format, BOOM)
if initcommand[0] == "crapibara":
    with open(initcommand[1], "r") as f:
        file = f.read()

#built in BS


def math(value):
    value = value.split(" ")
    index = 0
    while index != len(value) - 1:
        if value[index] == "+":
            if value[index - 1].isalpha():
                
                varname = value[index - 1]
                value[index - 1] = variables[varname]
                
                if type(value[index - 1]).__name__ == 'str':
                    res = variables[varname] + variables[value[index + 1]]
                    del value[index - 1]
                    del value[index - 1]
                    
                    
                else:
                    res = int(value[index - 1]) + int(value[index + 1])
                    del value[index - 1]
                    del value[index - 1]
            
            value[index - 1] = str(res)
            index -= 2
        if value[index] == "-":
            if value[index - 1].isalpha():
                value[index - 1] = variables[value[index - 1]]
                
            res = int(value[index - 1]) - int(value[index + 1])
            del value[index - 1]
            del value[index - 1]
            
            value[index - 1] = str(res)
            index -= 2
        if value[index] == "*":
            if value[index - 1].isalpha():
                value[index - 1] = variables[value[index - 1]]
                
            res = int(value[index - 1]) * int(value[index + 1])
            del value[index - 1]
            del value[index - 1]
            
            value[index - 1] = str(res)
            index -= 2
        if value[index] == "//":
            if value[index - 1].isalpha():
                value[index - 1] = variables[value[index - 1]]
                
            res = int(value[index - 1]) // int(value[index + 1])
            del value[index - 1]
            del value[index - 1]
            
            value[index - 1] = str(res)
            index -= 2
        if value[index] == "/":
            if value[index - 1].isalpha():
                value[index - 1] = variables[value[index - 1]]
                
            res = int(int(value[index - 1]) / int(value[index + 1]))
            del value[index - 1]
            del value[index - 1]
            
            value[index - 1] = str(res)
            index -= 2
        index += 1
    return value[0]
        
def conditionals(types, value, code):
    if types == "if":
        #value parsing: SHIT
        if "=" in value or ">" in value or "<" in value:
            index = 0
            value = value.split(" ")
            while index < len(value):
                if value[index].isalpha():
                    value[index] = variables[value[index]]
                index += 1
            value = " ".join(value)

        if eval(value):
            run_block(code)
        else:
            pass
    
    #maybe implement later
    #elif type == "else_if":
    #    if value
    
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
        if "+" in value or "-" in value or "*" in value or "//" in value or "/" in value:
            print(math(value))
        else:
            print(variables[value])

def inputv(value):
    variables[value] = input()

variables = {"Hello_World":"Easy"}
def makevar(name, value):
    if "m:" in value:
        variables[name] = math(value)
    else:
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


def find_end(cmdindex, code):
    depth = 0
    for idx in range(cmdindex, len(code)):
        cmd = regex.sub(r'"[^"]*"', '', code[idx])
        cmd = regex.sub(r"\([^)]*\)", "()", cmd) 

        if cmd in ("if ()", "repeat()"):
            depth += 1
        elif cmd == "end":
            depth -= 1
            if depth == 0:
                return idx


#repeat loop BS
#helper for NESTEDqrqrqrqrqrqr
def run_block(code):
    _loopidx = 0
    while _loopidx < len(code):
        line = code[_loopidx]
        #print("line: ", line, _loopidx)
        command = regex.sub(r'"[^"]*"', '', line)
        command = regex.sub(r"\([^)]*\)", "()", command)

        if command == "repeat()":
            skipidx = find_end(_loopidx, code)
            inner_block = code[_loopidx + 1 : skipidx]
            ntimes = int(regex.search(r"\d+", line).group())

            for _ in range(ntimes):
                run_block(inner_block)

            _loopidx = skipidx + 1
            continue

        
        if command == "if ()":
            skipidx = find_end(_loopidx, code)
            inner_block = code[_loopidx + 1 : skipidx]

            condition = regex.search(r"\((.*?)\)", line).group(1)
            conditionals("if", condition, inner_block)

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
                if other.strip() == "once ()":
                    pass
                else:
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
#print(variables)
