def split_seq(seq, sep):
    start = 0
    while start < len(seq):
        try:
           stop = start + seq[start:].index(sep)
           yield seq[start:stop]
           start = stop + 1
        except ValueError:
           yield seq[start:]
           break

with open('input.txt', encoding='utf-8') as elfs:
    calories = elfs.readlines()
    
calories_1 = [item.split('\n')[0] for item in calories]
print(calories_1)
calories_2 = [i for i in split_seq(calories_1,"")]
print(calories_2)
calories_elf = []
for elf in calories_2:
    elf = [int(item) for item in elf]
    elf1 = sum(elf)
    calories_elf.append(elf1)
    print(calories_elf)
    
print(max(calories_elf))
