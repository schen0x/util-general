# usage: python rename_files_n_dir_recursive.py [searchRoot] [oldName] [newStr]
# python .\rename_files_n_dir_recursive.py E:\temp OOOOO NNNNN
# rename all file && dir in the [searchRoot]
# cautious! do not use with simple pattern:
#   e.g. 'p' -> 'b'; result: 'apple' -> 'abble'
#   e.g. 'CCC' -> 'DDD'; result: 'CCCC' -> 'DDDC'

import sys,os

def rename(searchRootABS, oldName, newStr):
    # print('processing dir/file: ' + searchRootABS)

    # os.listdir() return dir and files as an array.
    for childBase in os.listdir(searchRootABS):
        # print(child)
        meta = 'unknown'
        if os.path.isdir(childBase):
            meta = 'dir'
        elif os.path.isfile(childBase):
            meta = 'file'
        elif os.path.islink(childBase):
            meta = 'link'
        # if a child(basename) contains oldStr, replace it.
        if (oldStr in childBase):
            childOldABS = searchRootABS + os.sep + childBase
            newBase = childBase.replace(oldStr, newStr)
            childNewABS = searchRootABS + os.sep + newBase
            os.rename(childOldABS, childNewABS)
            print('renamed ' + meta + ': '  + childOldABS + ' -> ' + childNewABS)
    
    for newChildBase in os.listdir(searchRootABS):
        newChildABS = searchRootABS + os.sep + newChildBase
        if os.path.isdir(newChildABS):
            rename(newChildABS, oldName, newStr)

if __name__ == "__main__":
    searchRootABS = sys.argv[1]
    oldStr = sys.argv[2]
    newStr = sys.argv[3]
    os.chdir(searchRootABS)
    rename(searchRootABS, oldStr, newStr)

