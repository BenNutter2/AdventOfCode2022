def day2_part1():
    
    file = open("C:/Users/19870/OneDrive/Documents/AoC/Input-2.txt", "r")
    input = file.readlines()
    strategy_total = 0 
    round_score = 0
    
    for round in input:
        
        round_score = 0
        
        opponent_choice = round[0]
        strategy_choice = round[2]
        
        if (opponent_choice == "A" and strategy_choice == "Y")  or (opponent_choice == "B" and strategy_choice == "Z") or (opponent_choice == "C" and strategy_choice == "X"): #For Wins
            round_score+=6
            
        elif (opponent_choice == "A" and strategy_choice == "X")  or (opponent_choice == "B" and strategy_choice == "Y") or (opponent_choice == "C" and strategy_choice == "Z"): #For Draws
            round_score+=3
            
        round_score += ord(strategy_choice) - 87 
        strategy_total += round_score
        
    file.close()
    
    return strategy_total


def day2_part2():
    
    file = open("C:/Users/19870/OneDrive/Documents/AoC/Input-2.txt", "r")
    input = file.readlines()
    strategy_total = 0 
    round_score = 0
    
    for round in input:
        
        round_score = 0
        
        opponent_choice = round[0]
        strategy_result = round[2]
        
        if strategy_result == "Y":
            round_score += 3
            round_score += ord(opponent_choice) - 64 #To find choice score e.g A = 1, B = 2, C = 3
            
        elif strategy_result == "Z":
            round_score += 6
            
            if opponent_choice == "A":
                round_score += 2
                
            elif opponent_choice == "B":
                round_score += 3
            
            elif opponent_choice == "C":
                round_score += 1
                
    
        elif strategy_result == "X":
            
            if opponent_choice == "A":
                round_score += 3
                
            elif opponent_choice == "B":
                round_score += 1
            
            elif opponent_choice == "C":
                round_score += 2
                
        strategy_total += round_score
        
    file.close()    
    return strategy_total


def day2():
    return day2_part1(), day2_part2()

print(day2())