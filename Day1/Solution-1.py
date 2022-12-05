
def day1():
    
    file = open("C:/Users/19870/OneDrive/Documents/AoC/Day1/Input-1.txt", "r")
    calories = []
    total = 0

    for number in file.readlines():
        if number == "\n":
            calories.append(total)
            total = 0
        else:
            total+=int(number)
    
    answer1 = max(calories)
    answer2 = sum(sorted(calories)[-3:])
    
    return "Answer 1: " + str(answer1) + "\n" + "Answer 2: " + str(answer2)
    
print(day1())