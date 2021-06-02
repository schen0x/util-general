import os
# import sys

def searchReplaceComplexStrInFolder(path: str, searchStr:str, replaceStr: str):
    '''
    Search and replace complex str recursively.

    pathNoTrailSysSep = '../volatile'

    searchStr = """
       a() {
           b
       }
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
        searchReplaceComplexStrInFolder(path, searchStr, replaceStr)
        return

    searchBytes = bytes(searchStr, 'utf-8')
    replaceBytes = bytes(replaceStr, 'utf-8')

    if os.path.isdir(path):
        for fileName in os.listdir(path):
            newPathStr = path + os.path.sep + fileName
            searchReplaceComplexStrInFolder(newPathStr, searchStr, replaceStr)
        return

    aFile = path
    with open(aFile, 'rb+') as f:
        content = f.read()
        if (searchBytes in content):
            f.seek(0)
            f.write(content.replace(searchBytes, replaceBytes))
    return
