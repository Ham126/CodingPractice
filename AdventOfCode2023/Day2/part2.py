sum = 0

with open('AdventofCode/Day2/data.txt', 'r') as file:
    ID = 0
    for line in file:
        ID += 1   
        maxRed = 0
        maxGreen = 0
        maxBlue = 0
        getRidOfGameText = line.split(':')
        rounds = getRidOfGameText[1].split(';')
        for i in range(len(rounds)):
            set = rounds[i].split(',')          
            for pull in range(len(set)):
                if 'red' in set[pull]:
                    num = ''
                    for character in set[pull]:
                        if character.isnumeric():
                            num += character
                    if int(num) > maxRed:
                        maxRed = int(num)
                elif 'green' in set[pull]:
                    num = ''
                    for character in set[pull]:
                        if character.isnumeric():
                            num += character
                    if int(num) > maxGreen:
                         maxGreen = int(num)
                elif 'blue' in set[pull]:
                    num = ''
                    for character in set[pull]:
                        if character.isnumeric():
                            num += character
                    if int(num) > maxBlue:
                         maxBlue = int(num)
        sum += maxRed * maxGreen * maxBlue
print(sum)