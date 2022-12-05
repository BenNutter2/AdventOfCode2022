

def day5_part1():
    
    with open("C:/Users/19870/OneDrive/Documents/AoC/Day5/Input-5.txt") as f:
        
        stacks = [[], [], [], [], [], [], [], [], []]
        
        # stack_label = ""
        
        # for line in f.readlines(): #Finds the labels
        #     if line[0] != "[":
        #         stack_label = line.strip()
        #         break
        #     pass
        
        # stack_label = stack_label.replace(" ", "")
        
        # for label in stack_label: # Creates stacks
        #     stacks["stack" + label] = []
        # print(stacks)
        
        # for line in f.readlines(): #Builds the stacks
        #     if line[0] == "[":
        #         next_stack = line.strip()
        #         for i in range(1, len(line), 4):
        #             if next_stack[i] != 0:
        #                 stack_number = 
                        
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
            for i in range(command[0]):
                popped_off = stacks[command[1]-1].pop()
                stacks[command[2]-1].append(popped_off)
        
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
            
            popped_off = stacks[command[1]-1][-command[0]:]
            stacks[command[1]-1] = stacks[command[1]-1][:-command[0]]
            stacks[command[2]-1] += (popped_off)
        
        message2 = ""
        for element in stacks:
            message2 += element[-1]
        return message2
    
def day5():
    
    return day5_part1(), day5_part2()
        
        
print(day5())