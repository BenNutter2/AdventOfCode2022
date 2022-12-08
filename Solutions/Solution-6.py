
    

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
                
            
print(day6_part1())
print(day6_part2())

