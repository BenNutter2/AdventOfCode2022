import numpy as np

def visible_from_edge(row):
    
    visible_list_pos = [] # positive direction
    visible_list_neg = [] # positive direction
    
    max_tree = -1
    
    for tree in row: 
        if tree > max_tree:
            visible_list_pos.append([tree, True])
            max_tree = tree
        else:
            visible_list_pos.append([tree, False])
    
    max_tree = -1
    
    for tree in reversed(row): 
        if tree > max_tree:
            visible_list_neg.append([tree, True])
            max_tree = tree
        else:
            visible_list_neg.append([tree, False])
    visible_list_neg = list(reversed(visible_list_neg))
    
    visible_list = []
    
    for i in range(len(visible_list_pos)):
        visible_list.append([visible_list_pos[i][0], visible_list_pos[i][1] or visible_list_neg[i][1] ])
    
    return visible_list

def findxpos(grid, column, row):
    tree_value = grid[row][column]
    
    current_score = 0
    
    if column == 0: 
        return current_score
    else:
        current_column = column - 1
        while current_column != -1:    
            if tree_value > grid[row][current_column]:
                current_score +=1
            else:
                current_score +=1 
                break
            current_column -= 1
            
    return current_score

def findxneg(grid, column, row):
    tree_value = grid[row][column]
    
    current_score = 0
    
    if column == len(grid[0]) - 1: 
        return current_score
    else:
        current_column = column + 1
        while current_column != len(grid[0]):    
            if tree_value > grid[row][current_column]:
                current_score += 1
            else:
                current_score +=1 
                break
            current_column += 1
                
    return current_score
    
def findypos(grid, column, row):
    tree_value = grid[row][column]
    
    current_score = 0
    
    if row == 0: 
        return current_score
    else:
        current_row = row - 1
        while current_row != -1:    
            if tree_value > grid[current_row][column]:
                current_score +=1
            else:
                current_score +=1 
                break
            current_row -= 1
            
    return current_score

def findyneg(grid, column, row):
    tree_value = grid[row][column]
    
    current_score = 0
    
    if row == len(grid) - 1: 
        return current_score
    else:
        current_row = row + 1
        while current_row != len(grid):    
            if tree_value > grid[current_row][column]:
                current_score +=1
            else:
                current_score +=1 
                break
            current_row += 1
            
    return current_score
    
def scenic_score(grid, column, row):
    
    total_score = findxneg(grid, column, row) * findxpos(grid, column, row) * findypos(grid, column, row) * findyneg(grid, column, row)
        
    return total_score




        
       
def day8_part1():
    
    with open("Inputs/Input-8.txt", "r") as file:
        
        input = file.readlines()

    input = [[*tree.strip()] for tree in input]
    
    input = [[int(tree) for tree in row] for row in input]
    
 
    rows_visible = []
    for index in range(len(input)):
        rows_visible.append(visible_from_edge(input[index]))
    
    columns_visible = []
    
    input_transposed = [[row[i] for row in input] for i in range(len(input[0]))]
    
    for index in range(len(input_transposed)):
        columns_visible.append(visible_from_edge(input_transposed[index]))
        
    columns_visible_transposed = [[row[i] for row in columns_visible] for i in range(len(columns_visible[0]))]
    
    
    trees_visible = []
    
    new_row = []
    for row_number in range(len(rows_visible)):
        new_row = []
        for column_number in range(len(rows_visible[0])):
            new_row.append([rows_visible[row_number][column_number][0], rows_visible[row_number][column_number][1] or columns_visible_transposed[row_number][column_number][1]])
        trees_visible.append(new_row)
    
    total = 0
    for z in trees_visible:
        for a in z:
            if a[1] == True:
                total+=1
    
    return total
day8_part1()
        
def day8_part2():
    
    with open("Inputs/Input-8.txt", "r") as file:
        
        input = file.readlines()

    input = [[*tree.strip()] for tree in input]
    
    input = [[int(tree) for tree in row] for row in input] #type: ignore

    scenic_scores = []
    for row in range(len(input)):
        
        for column in range(len(input[0])):
            
            scenic_scores.append(scenic_score(input, column, row))
    return max(scenic_scores)

def day8():
    return day8_part1(), day8_part2()

print(day8())