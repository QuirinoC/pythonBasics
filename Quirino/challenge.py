words = ['Not_a_flamethrower_by_elon_musk','renato', 'perro', 'washington', 'python', 'jose', 'azul', 'spaguetti', 'raviolli', 'Super_Smash_Bros_Ultimate']
k = 3
max = 0
for i in range(len(words) - k + 1):
    if len(''.join(words[i:i+k])) > len(''.join(words[max:max+k])):
        max = i

print(words[max:max+k])