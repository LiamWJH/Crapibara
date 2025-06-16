import re as regex

initcommand = input().split(" ")

file = ''
#init command stuff (inbrace, format, BOOM)
if initcommand[0] == "crapibara":
    with open(initcommand[1], "r") as f:
        file = f.read()

_loopidx = 0
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
                    try:
                        res = int(value[index - 1]) + int(value[index + 1])
                        del value[index - 1]
                        del value[index - 1]
                    except ValueError as ve:
                        errorlog("Type convertion error", _loopidx, "Dont try to convert INT to STR or LIST to INT or etc")
                
            value[index - 1] = str(res)
            index -= 2
        
        if value[index] == "-":
            if value[index - 1].isalpha():
                value[index - 1] = variables[value[index - 1]]
                
            try:
                res = int(value[index - 1]) - int(value[index + 1])
                del value[index - 1]
                del value[index - 1]
            except ValueError as ve:
                errorlog("Type convertion error", _loopidx, "Dont try to convert INT to STR or LIST to INT or etc")
            
            value[index - 1] = str(res)
            index -= 2
            
        if value[index] == "*":
            if value[index - 1].isalpha():
                value[index - 1] = variables[value[index - 1]]
                
            try:
                res = int(value[index - 1]) * int(value[index + 1])
                del value[index - 1]
                del value[index - 1]
            except ValueError as ve:
                errorlog("Type convertion error", _loopidx, "Dont try to convert INT to STR or LIST to INT or etc")
            
            value[index - 1] = str(res)
            index -= 2
            
        if value[index] == "/":
            if value[index - 1].isalpha():
                value[index - 1] = variables[value[index - 1]]
                
            try:
                res = int(value[index - 1]) - int(value[index + 1])
                del value[index - 1]
                del value[index - 1]
            except ZeroDivisionError as zde:
                errorlog("ZeroDivisionError", _loopidx, "Dont divide with 0")
            
            value[index - 1] = str(res)
            index -= 2
            
        if value[index] == "//":
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
        if "=" in value or ">" in value or "<" in value:
            index = 0
            value = value.split(" ")
            while index < len(value):
                if value[index].isalpha():
                    value[index] = variables[value[index]]
                index += 1
            value = " ".join(value)

        try:
            if eval(value):
                run_block(code)
            else:
                pass
        except NameError as ne:
            errorlog(f"'{ne}'", _loopidx, f"define '{ne}' or remove")
        
        except SyntaxError as se:
            errorlog(f"invalid syntax!",_loopidx, "Basic syntax error")

def printlnv(value):
    if regex.fullmatch(r'"[^"]*"', value):
        print(value[1:-1])  #removing '"' btw
    else:
        if "+" in value or "-" in value or "*" in value or "//" in value or "/" in value:
            print(math(value))
        else:
            try:
                print(variables[value])
            except KeyError as ke:
                errorlog(f"No variable named {str(ke)}", _loopidx, "Add variable or fix")

def printv(value):
    if regex.fullmatch(r'"[^"]*"', value):
        print(value[1:-1], end="")  #removing '"' btw
    else:
        if "+" in value or "-" in value or "*" in value or "//" in value or "/" in value:
            print(math(value))
        else:
            try:
                print(variables[value])
            except KeyError as ke:
                errorlog(f"No variable named {str(ke)}", _loopidx, "Add variable or fix")

def inputv(value):
    variables[value] = input()

variables = {"capibara":"its crapibara"}
def makevar(name, value):
    if "+" in value or "-" in value or "*" in value or "/" in value or "//" in value:
        variables[name] = math(value)
    else:
        variables[name] = value

#enterpreteur

#flatten list for code_lines
def errorlog(error, line, fix):
    print(f"Error on line: {line}\nProblem: {error} => possible fix: {fix}")

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


def run_block(code):
    _loopidx = 0
    while _loopidx < len(code):
        line = code[_loopidx]

        command = regex.sub(r'"[^"]*"', '', line)
        command = regex.sub(r"\([^)]*\)", "()", command)

        if command == "repeat()":
            #find code to run and index to skip to
            skipidx = find_end(_loopidx, code)
            inner_block = code[_loopidx + 1 : skipidx]
            
            #Runs code from value
            ntimes = int(regex.search(r"\d+", line).group())
            for _ in range(ntimes):
                run_block(inner_block)

            _loopidx = skipidx + 1
            continue

        if command == "if ()":
            #finds code to run and skip idx
            skipidx = find_end(_loopidx, code)
            inner_block = code[_loopidx + 1 : skipidx]

            #finds the condition to run and pass it into the conditionals function
            condition = regex.search(r"\((.*?)\)", line).group(1)
            conditionals("if", condition, inner_block)

            _loopidx = skipidx + 1
            continue

        match command:
            case "once()":
                #starter function nothing needed
                pass

            case "printv()":
                #find value and pass it to the function
                matchval = regex.search(r"\((.*?)\)", line)
                if matchval:
                    printv(matchval.group(1))

            case "printlnv()":
                #find value and pass it to the function
                matchval = regex.search(r"\((.*?)\)", line)
                if matchval:
                    printlnv(matchval.group(1))
            
            case "inputv()":
                #find value and pass it to the function
                matchval = regex.search(r"\((.*?)\)", line)
                if matchval:
                    inputv(matchval.group(1))
            
            case "///":
                #skips to where there is no comments
                _loopidx += 1
                while _loopidx < len(code) and code[_loopidx] != "///":
                    _loopidx += 1

                _loopidx += 1
                continue
            
            case "end":
                #j.i.c
                break
            
            case other:
                if not "=" in other:
                    errorlog(f"'{other}' is a non-existing function or command", _loopidx, "Fix it")
                else:
                    #declare variable if not there
                    other = other.split(" ")
                    makevar(other[0].strip(), other[2].strip())

        _loopidx += 1

def parse_braces(file):
    result = []
    for line in file.split("\n"):
        if "{" in line or "}" in line:
            if "{" in line:
                result.append(line[:-2])
            if "}" in line:
                pass
        else:
            result.append(line)
    
    return result

splitted = parse_braces(file)

for index in range(len(splitted)):
    splitted[index] = splitted[index].strip().split("\n")

code_lines = flattenlist(splitted)
code_lines = [line for line in code_lines if line] # '' removal

print("\n\n")
print("detected functions:")
print(code_lines)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("")


run_block(code_lines)