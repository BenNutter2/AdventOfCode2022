from anytree import Node, NodeMixin, RenderTree, findall

from functools import lru_cache

def find_directory_size(directory):
    total = 0
    if len(directory.children) == 0:
       total += int(directory.file_size)
    for children in directory.children:
        total += find_directory_size(children)
    return total

def find_sizes_less_than_100k(directory):
    
    sizes = []
    
    directories = findall(directory, lambda node: node.file_type == "dir")
    for folder in directories:
        size = find_directory_size(folder)
        if size <= 100000:
            sizes.append(size)
    return sizes

def find_sizes(directory):
    sizes = []
    
    directories = findall(directory, lambda node: node.file_type == "dir")
    for folder in directories:
        size = find_directory_size(folder)
        sizes.append(size)
    return sizes




#def cd_in(directory):
    
def day7_part1():
    with open("Inputs/Input-7.txt") as f:
        input = f.readlines()
        
    input = [line.strip() for line in input]
    
    root = Node("root", parent=None, file_type = "dir")
    current_directory = root
    collect_lines = False
    
    
    for line in input:
        if line == "$ cd /": #Outermost
            collect_lines = False
            current_directory = root
            
        elif line == "$ cd ..": #Go out 1
            collect_lines = False
            current_directory = current_directory.parent
            
        elif line[:4] == "$ cd": #Go in 1
            collect_lines = False
            possible_directories = current_directory.children
            
            for child in possible_directories:
                if child.name == line[5:]:
                    current_directory = child
                    break
                    
        elif line == "$ ls":
            collect_lines = True
            
        elif collect_lines == True:
            contents = line.split(" ")
            if contents[0] == "dir":
                directory = Node(contents[1], parent=current_directory, file_type = "dir")
            else:
                directory = Node(contents[1], parent=current_directory, file_type = "file", file_size = contents[0])
    
    #print(RenderTree(root))

    answer1 = find_sizes_less_than_100k(root)
    
    total_disk_used = find_directory_size(root)
    
    content = find_sizes(root)
    content = sorted(content)
    
    total_disk_space = 70000000
    
    free_space = total_disk_space - total_disk_used
    
    answer2 = 0
    for size in content:
        if size + free_space > 30000000:
            answer2 = size
            break
    print(answer2)
        
print(day7_part1())



