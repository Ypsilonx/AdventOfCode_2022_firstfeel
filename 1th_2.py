#--- Part Two ---
#By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.
#
#To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.
#
#In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.
#
#Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

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

with open('input1.txt', encoding='utf-8') as elfs:
    calories = elfs.readlines()
    
calories_1 = [item.split('\n')[0] for item in calories]
#print(calories_1)
calories_2 = [i for i in split_seq(calories_1,"")]
#print(calories_2)
calories_elf = []
for elf in calories_2:
    elf = [int(item) for item in elf]
    elf1 = sum(elf)
    calories_elf.append(elf1)
    #print(calories_elf)
    
first_elf = max(calories_elf)
print(first_elf)
calories_elf.sort(reverse=True)
#print(calories_elf)
three_elf = calories_elf[0] + calories_elf[1] + calories_elf[2]
print(three_elf)
