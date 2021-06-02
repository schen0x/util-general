import os
import re
import fileinput

def countLinesRecursive(path: str, ignorePathRegex: list):
    '''
    Search and count total line number.

    path = '../volatile'

    ignorePathRegex = """
    node_module
    """

    replaceStr = """
       b() {
           c
       }
    """
    '''

    s = path[-1]
    if (s == os.path.sep) or (s == '/') or (s == '\\'):
        path = path[0:-1]
        return countLinesRecursive(path, ignorePathRegex)


    for i in ignorePathRegex:
        if re.search(i, path):
            return 0

    if os.path.isdir(path):
        dir_line_counter = 0
        for fileName in os.listdir(path):
            newPathStr = path + os.path.sep + fileName
            dir_line_counter += countLinesRecursive(newPathStr, ignorePathRegex)
        return dir_line_counter

    return count_lines(path)

def count_lines(filePath: str):
    lines_count = 0
    with open(filePath, 'rb') as f:
        content = f.read()
        lines = content.split(b'\n')
        for line in lines:
            lines_count += 1

    print(filePath + ": non-empty-lines " + str(lines_count))
    return lines_count

if __name__ == "__main__":
    res = countLinesRecursive("./", ["LICENSE", ".git"])
    print("sum: " + str(res))