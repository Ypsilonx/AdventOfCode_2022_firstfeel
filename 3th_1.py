# --- Day 3: Rucksack Reorganization ---
# One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

# Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

# The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

# The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

# For example, suppose you have the following list of contents from six rucksacks:

# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
# The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
# The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
# The fourth rucksack's compartments only share item type v.
# The fifth rucksack's compartments only share item type t.
# The sixth rucksack's compartments only share item type s.
# To help prioritize item rearrangement, every item type can be converted to a priority:

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
# In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

import pandas as pd

def Batoh(list):
    batoh = list
    for x in batoh:
        delka = len(x)//2
        #print(delka)
        i = 0
        prihradka1 = []
        for item in range(0, delka):
            #print(item)
            prihradka1.append(x[i])
            i += 1
            #print(prihradka1)
        prihradka2 = []
        for item in range(delka, len(x)):
            #print(item)
            prihradka2.append(x[i])
            i += 1
            #print(prihradka2)

    ele = []
    for element in prihradka1:
        if element in prihradka2:
            ele.append(element)
            #print(ele[0])
    return ele[0]

with open('input3.txt', encoding='utf-8') as batoh:
    prihradky = batoh.readlines()

batoh_1 = [item.split('\n')[0] for item in prihradky]
#print(batoh_1)

priority = {
'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,
'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,
'x':24,'y':25,'z':26,'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,
'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,
'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52
}
batoh_2 = [batoh_1[x:x+1] for x in range(0, len(batoh_1))]
#print(batoh_2)

i = 0
shoda = []
for bagl in batoh_2:
    shoda.append(Batoh(bagl))
    i += 1

print(shoda)

vysledek = (pd.Series(shoda)).map(priority)
print(sum(vysledek))