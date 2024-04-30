sumID = 0
maxRed = 12
maxGreen = 13
maxBlue = 14
with open('AdventofCode/Day2/data.txt', 'r') as file:
    ID = 0
    for line in file:
        ID += 1   
        getRidOfGameText = line.split(':')
        rounds = getRidOfGameText[1].split(';')
        gameValid = True      
        for i in range(len(rounds)):
            set = rounds[i].split(',')          
            for pull in range(len(set)):
                if 'red' in set[pull]:
                    num = ''
                    for character in set[pull]:
                        if character.isnumeric():
                            num += character
                    if int(num) > maxRed:
                        gameValid = False
                elif 'green' in set[pull]:
                    num = ''
                    for character in set[pull]:
                        if character.isnumeric():
                            num += character
                    if int(num) > maxGreen:
                        gameValid = False
                elif 'blue' in set[pull]:
                    num = ''
                    for character in set[pull]:
                        if character.isnumeric():
                            num += character
                    if int(num) > maxBlue:
                        gameValid = False
        if gameValid:
            sumID += ID
            
print(sumID)