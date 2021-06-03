# python3 only
import os
import re

def countLinesRecursive(pathRaw: str, ignore: str):
    '''
    Print total none-empty line counts for all and each file in the path.

    Example: countLinesRecursive("./", ignore)
    Params:
        path = '../volatile'
        ignore = """
            .git
            node_module
        """
    '''
    path = pathRaw
    if (os.sep != "/"):
        path = pathRaw.replace(os.sep, '/')
        path = re.sub("/+", "/", path)

    # dir
    if os.path.isdir(path):
        dir_line_counter = 0
        s = path[-1]
        if (s == os.path.sep) or (s == '/') or (s == '\\'):
            path = path[0:-1]
        path += os.sep

        if _shouldIgnore(path, ignore):
            return 0

        for fileName in os.listdir(path):
            newPathStr = path + fileName
            dir_line_counter += countLinesRecursive(newPathStr, ignore)
        return dir_line_counter

    # file
    if _shouldIgnore(path, ignore):
        return 0

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

def _shouldIgnore(pathRaw: str, ignoreRaw: str):
    '''
        return: True if should be ignored
    '''
    ignore = ignoreRaw
    path = pathRaw

    if (os.sep != "/"):
        ignore = ignore.replace(os.sep, '/')
        path = path.replace(os.sep, '/')

    ignore = re.sub("/+", "/", ignore)
    path = re.sub("/+", "/", path)

    ignorePathRegex = ignore.split("\n")
    for i in ignorePathRegex:
        pattern = i.strip()
        if (len(pattern) < 1):
            continue
        if re.search(pattern, path):
            # if match, ignore
            return True
    return False
    

if __name__ == "__main__":
    ignore = """
        \.git/
        node_module/
        LICENSE
    """
    res = countLinesRecursive("./", ignore)
    print("sum: " + str(res))