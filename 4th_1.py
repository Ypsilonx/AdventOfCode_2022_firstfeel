# --- Day 4: Camp Cleanup ---
# Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.

# However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

# For example, consider the following list of section assignment pairs:

# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8
# For the first few pairs, this list means:

# Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
# The Elves in the second pair were each assigned two sections.
# The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
# This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

# .234.....  2-4
# .....678.  6-8

# .23......  2-3
# ...45....  4-5

# ....567..  5-7
# ......789  7-9

# .2345678.  2-8
# ..34567..  3-7

# .....6...  6-6
# ...456...  4-6

# .23456...  2-6
# ...45678.  4-8
# Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

# In how many assignment pairs does one range fully contain the other?

def PracovniDvojka(x):
    prvni_elf = x[0]
    druhy_elf = x[1]

    prvni_elf_prace = prvni_elf.split('-')
    prvni_elf_prace = range(int(prvni_elf_prace[0]),(int(prvni_elf_prace[1])+1))
    #print(prvni_elf_prace)
    druhy_elf_prace = druhy_elf.split('-')
    druhy_elf_prace = range(int(druhy_elf_prace[0]),(int(druhy_elf_prace[1])+1))
    #print(druhy_elf_prace)

    porovnani_1 = set(prvni_elf_prace)
    verdikt_1 = set(druhy_elf_prace).issubset(porovnani_1)
    porovnani_2 = set(druhy_elf_prace)
    verdikt_2 = set(prvni_elf_prace).issubset(porovnani_2)
    return f'{verdikt_1+verdikt_2}'

with open('input4.txt', encoding='utf-8') as elfs:
    dvojice = elfs.readlines()

dvojice = [item.split('\n')[0] for item in dvojice]
dvojice = [dvojice[x:x+1] for x in range(0,len(dvojice))]
pocet_dvojic = len(dvojice)
#print(pocet_dvojic)
#print(dvojice)
dvojka = [item[0].split(',') for item in dvojice]
#print(dvojka[0])
#list = ['1-2','1-8']

verdikt = []
i = 0
for x in dvojka:
    ano_ne = PracovniDvojka(x)
    verdikt.append(ano_ne)
    if i == 1000:
        break
    i += 1
print(verdikt)
nula = verdikt.count('0')
print(nula)
jedna = verdikt.count('1')
print(jedna)
dva = verdikt.count('2')
print(dva)
print(f'Výsledek: {jedna + dva}')