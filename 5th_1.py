# --- Day 5: Supply Stacks ---
# The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

# The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

# The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

#         [Z]
#         [N]
#     [C] [D]
#     [M] [P]
#  1   2   3
# Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

#         [Z]
#         [N]
# [M]     [D]
# [C]     [P]
#  1   2   3
# Finally, one crate is moved from stack 1 to stack 2:

#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3
# The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

# After the rearrangement procedure completes, what crate ends up on top of each stack?

with open('input5.txt', encoding='utf-8') as sklad:
    hromady = sklad.readlines()

hromady = [item.split('\n')[0] for item in hromady]

n = 0
mapa_hromady = []
for y in hromady:
    mapa_hromady.append(hromady[n])
    if n == 7:
        break
    n += 1
    
#print('Výchozí klíč ke skladu: ', mapa_hromady)

i = 0
for j in hromady:
    hromady.pop(0)
    if i == 9:
        break
    i += 1

#print('Seznam instrukcí: ', hromady)

stack_1 = ['R', 'P', 'C', 'D', 'B', 'G']
stack_2 = ['H', 'V', 'G']
stack_3 = ['N', 'S', 'Q', 'D', 'J', 'P', 'M']
stack_4 = ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M']
stack_5 = ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S']
stack_6 = ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S']
stack_7 = ['B', 'Z', 'M', 'H', 'F', 'T', 'Q']
stack_8 = ['C', 'M', 'D', 'B', 'F']
stack_9 = ['F', 'C', 'Q', 'G']

stacks = [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]
#print(stacks)

pocet_instrukci = len(hromady)
#print(pocet_instrukci)

for n in range(0,pocet_instrukci):
    instrukce = hromady[n]
    instrukce_1 = instrukce.split(' ')
    pohyb = int(instrukce_1[1])
    odkud = int(instrukce_1[3])
    kam = int(instrukce_1[5])
    #print(f'Pohyb {pohyb} beden z {odkud} hromady do {kam} hromady.')

    for i in range(0,pohyb):
        if (stacks[odkud-1]) != []:
            x = stacks[odkud-1].pop()
            #print(x)
            stacks[kam-1].append(x)
        else:
            break

print(stack_1[len(stack_1)-1] + stack_2[len(stack_2)-1] + stack_3[len(stack_3)-1] + stack_4[len(stack_4)-1] + stack_5[len(stack_5)-1] + stack_6[len(stack_6)-1] + stack_7[len(stack_7)-1] + stack_8[len(stack_8)-1] + stack_9[len(stack_9)-1])