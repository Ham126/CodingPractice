sum = 0
nums = ["zero", "one","two","three","four", "five", "six", "seven", "eight", "nine"]

def replaceLine(t):
    for i in range(0, 2):
        for j  in range(0, len(nums)):
            t = t.replace(nums[j], str(j) + nums[j][-1])
    return t

with open('AdventOfCode\Day1\data.txt', 'r') as file:

    i=0
    for line in file:
        i = i+1
        convStr = replaceLine(line)
        charArray = []
        for character in convStr:
            if character.isnumeric():
                charArray.append(character)
        solution = int(charArray[0] + charArray[-1])
        print(f'{i} : {line} : {solution}')
        sum = sum + solution

print(sum)