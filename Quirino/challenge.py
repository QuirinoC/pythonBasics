words = ['juan','renato', 'perro', 'washington', 'python', 'jose', 'azul']
k = 3
concats = []
for i in range(len(words) - 3):
    concats.append("".join(words[i:i+3]))

print(concats)
max = 0
for i, string in enumerate(concats):
    if len(string) > len(concats[max]):
        max = i
    
print(concats[max])
