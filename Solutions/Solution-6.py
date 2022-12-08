def day6_part1():
    
    with open("Inputs/Input-6.txt") as f:
        
        input = list(f.readline())
        
        buffer = ""
        
        for index in range(len(input) -3):
            buffer = input[index:index+4]
            
            if len(set(buffer)) == 4:
                return index + 4
def day6_part2():
    with open("Inputs/Input-6.txt") as f:
        input = list(f.readline())
        
        buffer = ""
        for index in range(len(input) - 14):
            buffer = input[index:index+14]
            
            if len(set(buffer)) == 14:
                return index + 14
                
def day6():       
    import time, tracemalloc
    
    tracemalloc.start()     # Start memory allocation trace
    start = time.time()
    
    print("Answer 1: ", day6_part1(), "\nAnswer 2: ", day6_part2(), "\n")  # type: ignore
    
    print("\t\tTotal elapsed time:", time.time()-start)
    print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
day6()
