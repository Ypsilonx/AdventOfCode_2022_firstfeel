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
    verdikt_3 = bool(list(porovnani_1 & porovnani_2))
    return f'{verdikt_1+verdikt_2+verdikt_3}'

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
tri = verdikt.count('3')
print(tri)
print(f'Výsledek: {jedna + dva + tri}')