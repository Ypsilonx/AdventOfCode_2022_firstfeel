# --- Part Two ---
# As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

# Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

# The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

# Again considering the example above, the crates begin in the same configuration:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# Moving a single crate from stack 2 to stack 1 behaves the same as before:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

#         [D]
#         [N]
#     [C] [Z]
#     [M] [P]
#  1   2   3
# Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

#         [D]
#         [N]
# [C]     [Z]
# [M]     [P]
#  1   2   3
# Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

#         [D]
#         [N]
#         [Z]
# [M] [C] [P]
#  1   2   3
# In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

# Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

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

    presouvane_bedny = []
    for i in range(0,pohyb):
        x = stacks[odkud-1].pop()
        presouvane_bedny.append(x)
    presouvane_bedny.reverse()
    
    for bedna in presouvane_bedny:
        stacks[kam-1].append(bedna)

print(stack_1[len(stack_1)-1] + stack_2[len(stack_2)-1] + stack_3[len(stack_3)-1] + stack_4[len(stack_4)-1] + stack_5[len(stack_5)-1] + stack_6[len(stack_6)-1] + stack_7[len(stack_7)-1] + stack_8[len(stack_8)-1] + stack_9[len(stack_9)-1])