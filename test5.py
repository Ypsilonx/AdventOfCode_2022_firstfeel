with open('test.txt', encoding='utf-8') as sklad:
    hromady = sklad.readlines()

hromady = [item.split('\n')[0] for item in hromady]

n = 0
mapa_hromady = []
for y in hromady:
    mapa_hromady.append(hromady[n])
    if n == 3:
        break
    n += 1
    
print('Výchozí klíč ke skladu: ', mapa_hromady)

i = 0
for x in hromady:
    hromady.pop(0)
    if i == 4:
        break
    i += 1

print('Seznam instrukcí: ', hromady)

stack_1 = ['Z', 'N']
stack_2 = ['M', 'C', 'D']
stack_3 = ['P']



stacks = [stack_1, stack_2, stack_3]

#print(stacks)

pocet_instrukci = len(hromady)
#print(pocet_instrukci)

for n in range(0,pocet_instrukci):
    instrukce = hromady[n]
    instrukce_1 = instrukce.split(' ')
    pohyb = int(instrukce_1[1])
    odkud = int(instrukce_1[3])
    kam = int(instrukce_1[5])
    print(f'Pohyb {pohyb} beden z {odkud} hromady do {kam} hromady.')

    for i in range(0,pohyb):
        if (stacks[odkud-1]) != []:
            x = stacks[odkud-1].pop()
            #print(x)
            stacks[kam-1].append(x)
        else:
            break
        
print(stack_1)
print(stack_2)
print(stack_3)