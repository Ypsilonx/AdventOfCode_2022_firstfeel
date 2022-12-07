

with open('input.txt', encoding='utf-8') as signal:
    marker = signal.readlines()
    
marks = list(marker[0])
print(marks)

a_1 = 0
a_2 = 1
a_3 = 2
a_4 = 3
a_5 = 4
a_6 = 5
a_7 = 6
a_8 = 7
a_9 = 8
a_10 = 9
a_11 = 10
a_12 = 11
a_13 = 12
a_14 = 13

port = 14
for i in marks:
    set = [marks[a_1], marks[a_2], marks[a_3], marks[a_4], marks[a_5], marks[a_6], marks[a_7], marks[a_8], marks[a_9], marks[a_10], marks[a_11], marks[a_12], marks[a_13], marks[a_14]]
    b_1 = set.count(marks[a_1])
    b_2 = set.count(marks[a_2])
    b_3 = set.count(marks[a_3])
    b_4 = set.count(marks[a_4])
    b_5 = set.count(marks[a_5])
    b_6 = set.count(marks[a_6])
    b_7 = set.count(marks[a_7])
    b_8 = set.count(marks[a_8])
    b_9 = set.count(marks[a_9])
    b_10 = set.count(marks[a_10])
    b_11 = set.count(marks[a_11])
    b_12 = set.count(marks[a_12])
    b_13 = set.count(marks[a_13])
    b_14 = set.count(marks[a_14])
    if b_1 == 1:
        if b_2 == 1:
            if b_3 == 1:
                if b_4 == 1:
                    if b_5 == 1:
                        if b_6 == 1:
                            if b_7 == 1:
                                if b_8 == 1:
                                    if b_9 == 1:
                                        if b_10 == 1:
                                            if b_11 == 1:
                                                if b_12 == 1:
                                                    if b_13 == 1:
                                                        if b_14 == 1:
                                                            break
    a_1 += 1
    a_2 += 1
    a_3 += 1
    a_4 += 1
    a_5 += 1
    a_6 += 1
    a_7 += 1
    a_8 += 1
    a_9 += 1
    a_10 += 1
    a_11 += 1
    a_12 += 1
    a_13 += 1
    a_14 += 1
    port +=1

print(port)
