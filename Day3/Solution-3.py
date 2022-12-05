def common_member2(a, b):
    a_set = set(a)
    b_set = set(b)
    a=list((a_set)&(b_set))
    for i in a:
        return i
    
def common_member3(a, b, c):
    a_set = set(a)
    b_set = set(b)
    c_set = set(c)
    a=list((a_set)&(b_set)&(c_set))
    for i in a:
        return i

def day3_part1():
    
    file = open("C:/Users/19870/OneDrive/Documents/AoC/Day3/Input-3.txt", "r")
    input = file.readlines()

    pritorities  = []
   
    for rucksack in input:
        compartment1 = rucksack[len(rucksack)//2:]
        compartment2 = rucksack[:len(rucksack)//2]
        
        common_element = common_member2(compartment1, compartment2)
        pritorities.append(common_element)
    
    pritorities_total = 0
    
    for letter in pritorities:
        if (letter.isupper()):
            pritorities_total += ord(letter) - 38
        else:
            pritorities_total += ord(letter) - 96
            
    file.close()
    
    return pritorities_total
    
def day3_part2():
    file = open("C:/Users/19870/OneDrive/Documents/AoC/Day3/Input-3.txt", "r")
    input = file.readlines()
    
    pritorities  = []
    
    for i in range(0,len(input), 3):
        pritorities.append(common_member3(input[i].strip(), input[i+1].strip(), input[i+2].strip()))
      # type: ignore
    pritorities_total = 0
    
    for letter in pritorities:
        if (letter.isupper()):
            pritorities_total += ord(letter) - 38
        else:
            pritorities_total += ord(letter) - 96
            
    file.close()
    
    return pritorities_total

def day3():
    print(day3_part1(), day3_part2())
day3()

