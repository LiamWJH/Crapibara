code_lines = ["once()", "printv()", "repeat()", "a = 8", "if ()", "endloop","endif","end"]

endindexcount = 0
def find_end(cmdindex):
    endindex = (cmdindex + 1) * -1
    return endindex

print(code_lines[find_end(0)], find_end(0))