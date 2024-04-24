# Value found from each line of data.txt file
sumArray = []


with open('AdventofCode/Day1/data.txt', 'r') as file:
    for line in file:
        charArray = []
        # Separate line of file in array of characters
        for character in line:
            if character.isnumeric():
                charArray.append(character)
        solution = int(charArray[0] + charArray[-1])
        sumArray.append(solution)


# Takes sum of all number 
print(sum(sumArray))

