#!/usr/bin/python3
filename = input("Filename: ")
realext = input("Real extension: ")
hiddenext = input("Hidden extension: ")

file = 'rlo\u202Egpj.bat'
file = filename + '\u202E' + hiddenext[::-1] + '.' + realext
with open(file, 'w') as f:
    f.write('#!/usr/bin/bash\necho "rlo"\npause')
