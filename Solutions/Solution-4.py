def doesEncompass(string1, string2):
    
    string1 = string1.split("-")
    string2 = string2.split("-")
    
    start1 = int(string1[0])
    start2 = int(string2[0])
    
    end1 = int(string1[1])
    end2 = int(string2[1])

    if (start1 <= start2) and (end1 >= end2):
        return True
    return False


def doesOverlap(string1, string2):
    
    string1 = string1.split("-")
    string2 = string2.split("-")

    start1 = int(string1[0])
    start2 = int(string2[0])
    end1 = int(string1[1])
    end2 = int(string2[1])

    if (start1 <= start2) and (end1 >= start2):
        return True
    return False

def day4_part1():
    
    with open("Inputs/Input-4.txt", "r") as f:
        input=[]
        for line in f:
            strip_lines=line.strip()
            input.append(strip_lines)
 
    split_input = [pair.split(",") for pair in input]
    
    encompass_total = 0
    
    for pair in split_input:
        if (doesEncompass(pair[0], pair[1]) or doesEncompass(pair[1], pair[0])):
            encompass_total+=1
    return encompass_total        
    
def day4_part2():
    
    with open("Inputs/Input-4.txt", "r") as f:
        input=[]
        for line in f:
            strip_lines=line.strip()
            input.append(strip_lines)
 
    split_input = [pair.split(",") for pair in input]
    
    encompass_total = 0
    
    for pair in split_input:
        if (doesOverlap(pair[0], pair[1]) or  doesOverlap(pair[1], pair[0])):
            encompass_total += 1  
    return encompass_total

def day4():
    import time, tracemalloc
    
    tracemalloc.start()     # Start memory allocation trace
    start = time.time()
    
    print("Answer 1: ", day4_part1(), "\nAnswer 2: ", day4_part2(), "\n")  # type: ignore
    
    print("\t\tTotal elapsed time:", time.time()-start)
    print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
day4()