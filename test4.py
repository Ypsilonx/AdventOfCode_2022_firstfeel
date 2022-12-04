def PracovniDvojka(x):
    prvni_elf = x[0]
    print(prvni_elf)
    druhy_elf = x[1]

    prvni_elf_prace = [prace.split('-') for prace in prvni_elf]
    print(prvni_elf_prace)
    druhy_elf_prace = [prace.split('-') for prace in druhy_elf]
    print(druhy_elf_prace)

    porovnani_1 = set(prvni_elf_prace)
    verdikt_1 = set(druhy_elf_prace).issubset(porovnani_1)
    porovnani_2 = set(druhy_elf_prace)
    verdikt_2 = set(prvni_elf_prace).issubset(porovnani_2)
    print(verdikt_1)
    print(verdikt_2)


with open('input4.txt', encoding='utf-8') as elfs:
    dvojice = elfs.readlines()

dvojice = [item.split('\n')[0] for item in dvojice]
dvojice = [dvojice[x:x+1] for x in range(0,len(dvojice))]
pocet_dvojic = len(dvojice)
#print(pocet_dvojic)
#print(dvojice)
dvojka = [item[0].split(',') for item in dvojice]
#print(dvojka)
#list = ['1-2','1-8']

verdikt = []
i = 0
for x in dvojka:
    print(x)
    ano_ne = PracovniDvojka(x)
    verdikt.append(ano_ne)
    if i == 1000:
        break
    i += 1