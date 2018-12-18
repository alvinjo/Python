#!/usr/bin/python3
filename = input("Filename: ")
hiddenext = input("Hidden extension: ")

file = filename + '\u202E' + hiddenext[::-1] + '.' + 'bat'
with open(file, 'w') as f:
    f.write('#!/usr/bin/bash\necho "rlo"\npause')
