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
    
    file = open("Inputs/Input-3.txt", "r")
    input = file.readlines()

    priorities  = []
   
    for rucksack in input:
        compartment1 = rucksack[len(rucksack)//2:]
        compartment2 = rucksack[:len(rucksack)//2]
        
        common_element = common_member2(compartment1, compartment2)
        priorities.append(common_element)
    
    priorities_total = 0
    
    for letter in priorities:
        if (letter.isupper()):
            priorities_total += ord(letter) - 38
        else:
            priorities_total += ord(letter) - 96
            
    file.close()
    
    return priorities_total
    
def day3_part2():
    
    file = open("Inputs/Input-3.txt", "r")
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
    import time, tracemalloc
    
    tracemalloc.start()     # Start memory allocation trace
    start = time.time()
    
    print(day3_part1(), day3_part2())
    
    print("\t\tTotal elapsed time:", time.time()-start)
    print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
day3()

