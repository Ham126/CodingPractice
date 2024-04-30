numberArray = []
indexArray = []


def run():
    with open('AdventOfCode2023\Day3\data.txt', 'r') as file:
        array = file.readlines()
        for row in range(len(array)): 
            num = ''
            for column in range(len(array[row])):                        
                if array[row][column].isnumeric():
                    num += array[row][column]
                elif num == '':
                    continue
                else:
                    numberArray.append(int(num))
                    indexArray.append((row, column))
                    num = ''
                    
    print(numberArray)               


def isValidNumberPart():
    pass

run()