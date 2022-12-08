

def day5_part1():
    
    with open("Inputs/Input-5.txt") as f:
        
        stacks = [[], [], [], [], [], [], [], [], []]
        
        
        #----------------------failed attempt at solving problem generally for any input---------------------- 
        stacks = []
        
        max_pile_height = 0
        
        for line in f.readlines(): #Finds the height of the highest crate
            if line[0] == "[":
                max_pile_height += 1
            else:
                break
        
        for line in f.readlines():
            
            for char in range(1, len(line), 4):
                print(char)
                        
        stacks[0] = ['T', 'R', 'D', 'H', 'Q', 'N', 'P', 'B']
        stacks[1] = ['V', 'T', 'J', 'B', 'G', 'W']
        stacks[2] = ['Q', 'M', 'V', 'S', 'D', 'H', 'R', 'N']
        stacks[3] = ['C', 'M', 'N', 'Z', 'P']
        stacks[4] = ['B', 'Z', 'D']
        stacks[5] = ['Z', 'W', 'C', 'V']
        stacks[6] = ['S', 'L', 'Q', 'V', 'C', 'N', 'Z', 'G']
        stacks[7] = ['V', 'N', 'D', 'M', 'J', 'G', 'L']
        stacks[8] = ['G', 'C', 'Z', 'F', 'M', 'P', 'T']
        
    
        [x.reverse() for x in stacks]    
        
        instructions = []
        
        for line in f.readlines(): #Builds the stacks
            if line[0] == "m":
                
                instruction = line.strip()
                instruction = instruction.replace("move ", "")
                instruction = instruction.replace(" from", "")
                instruction = instruction.replace(" to", "")
                instruction = instruction.split(" ")
                
                instruction = [int(num) for num in instruction]

                instructions.append(instruction)
        
        for command in instructions:
            
            for i in range(command[0]): #repeats for number of crates specified
                
                popped_off = stacks[command[1]-1].pop() #takes the top crate off the stack
                stacks[command[2]-1].append(popped_off) #places the selected crate on the selected stack
        
        message1 = ""
        for element in stacks:
           message1 += element[-1]
        
        return message1

def day5_part2():
    
    with open("C:/Users/19870/OneDrive/Documents/AoC/Day5/Input-5.txt") as f:
        
        stacks = [[], [], [], [], [], [], [], [], []]
                      
        stacks[0] = ['T', 'R', 'D', 'H', 'Q', 'N', 'P', 'B']
        stacks[1] = ['V', 'T', 'J', 'B', 'G', 'W']
        stacks[2] = ['Q', 'M', 'V', 'S', 'D', 'H', 'R', 'N']
        stacks[3] = ['C', 'M', 'N', 'Z', 'P']
        stacks[4] = ['B', 'Z', 'D']
        stacks[5] = ['Z', 'W', 'C', 'V']
        stacks[6] = ['S', 'L', 'Q', 'V', 'C', 'N', 'Z', 'G']
        stacks[7] = ['V', 'N', 'D', 'M', 'J', 'G', 'L']
        stacks[8] = ['G', 'C', 'Z', 'F', 'M', 'P', 'T']
        
    
        [x.reverse() for x in stacks]    
        
        instructions = []
        for line in f.readlines(): #Builds the stacks
            if line[0] == "m":
                
                instruction = line.strip()
                instruction = instruction.replace("move ", "")
                instruction = instruction.replace(" from", "")
                instruction = instruction.replace(" to", "")
                instruction = instruction.split(" ")
                
                instruction = [int(num) for num in instruction]
                
                instructions.append(instruction)
                
        for command in instructions: 
            
            popped_off = stacks[command[1]-1][-command[0]:] #copies top crates off the specified stack
            stacks[command[1]-1] = stacks[command[1]-1][:-command[0]] #deletes the crates from the top of the pile
            stacks[command[2]-1] += (popped_off) #places the crates on the new stack
        
        message2 = ""
        
        for element in stacks:
            message2 += element[-1]
        return message2
    
def day5():
    
    return day5_part1(), day5_part2()
        
        
print(day5())