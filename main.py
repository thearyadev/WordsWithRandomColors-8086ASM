code = """
ORG 100h
MOV AX,0xB800 
MOV DS,AX      	
MOV CH,00001111b
MOV BX,0x0000
ADD CH, 100
"""
words = ['abnormal', 'absurd', 'adorable', 'advice', 'blind', 'deaf', 'brash', 'brave', 'day', 'poker', 'smile',
         'pineapple', 'microphone', 'keyboard', 'frown', 'editor', 'unicorn', 'parent', 'jesus', 'stand', 'sit',
         'sleep', 'death', 'concussion', 'mercy', 'trial', 'judge', 'browse', 'disk', 'remote', 'speaker', 'president',
         'chime', 'sail', 'boat', 'resist', 'click', 'press', 'choke', 'fly', 'crash', 'burn', 'break', 'explode',
         'escape', 'purge', 'crack', 'pencil', 'doubt']

for i in words:
    code += "ADD CH, 100\n"
    for c in i:
        code += f"""MOV CL, '{c}'
MOV [BX], CX
ADD BX, 2
"""
    code += f"""MOV CL, ' '
MOV [BX], CX
ADD BX, 2
"""

code += "\nret\n"

print(code)
