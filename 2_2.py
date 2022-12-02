#The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
#
#The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:
#
#In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
#In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
#In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
#Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.
#
#Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

with open('input2.txt', encoding='utf-8') as elfs:
    hra = elfs.readlines()

hra_1 = [item.split('\n')[0] for item in hra]
#hra_2 = [item.split(' ') for item in hra_1]


for i in range(len(hra_1)):
    if hra_1[i] == 'A X':
        hra_1[i] = 'A Z'
    elif hra_1[i] == 'B X':
        hra_1[i] = 1
    elif hra_1[i] == 'C X':
        hra_1[i] = 'C Y'
    elif hra_1[i] == 'A Y':
        hra_1[i] = 'A X'
    elif hra_1[i] == 'B Y':
        hra_1[i] = 5
    elif hra_1[i] == 'C Y':
        hra_1[i] = 'C Z'
    elif hra_1[i] == 'A Z':
        hra_1[i] = 'A Y'
    elif hra_1[i] == 'B Z':
        hra_1[i] = 9
    elif hra_1[i] == 'C Z':
        hra_1[i] = 'C X'

for i in range(len(hra_1)):
    if hra_1[i] == 'A Z':
        hra_1[i] = 3
    elif hra_1[i] == 'C Y':
        hra_1[i] = 2
    elif hra_1[i] == 'A X':
        hra_1[i] = 4
    elif hra_1[i] == 'C Z':
        hra_1[i] = 6
    elif hra_1[i] == 'A Y':
        hra_1[i] = 8
    elif hra_1[i] == 'C X':
        hra_1[i] = 7

hra_sum = sum(hra_1)
print(hra_sum)
