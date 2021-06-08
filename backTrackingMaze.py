# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:14:57 2021

@author: arber
"""

maze = [[".",".",".","."],
        [".","x","x","x"],
        [".",".",".","x"],
        ["x","x",".","."]]

print_maze(maze)


def print_maze(maze):
    for liste in maze:
        print_row = ""
        for row in liste : 
            print_row = print_row + " " + row
        print(print_row)


def solve_maze(maze):
    print("lala")
    
    return None


def solve_maze_helper(maze, sol = [], pos_row = 0, pos_col = 0):
    
    #Get size of the maze
    number_row = len(maze)
    number_col = len(maze[0])
    #print("number of rows : " + str(number_row) + '\n' + "number of columns : " + str(number_col))
    
    
    #Base case :
        
    # Robot is already home
    if(pos_row == number_row-1 and pos_col == number_col-1):
        return sol
    
    #Out of bounds
    if(pos_row >= number_row or pos_col >= number_col):
        return None
    
    # Is on a obstacle 
    if maze[pos_row][pos_col] == "x":
        return None
    
    # Try going right
    sol.append("r")
    sol_going_right = solve_maze_helper(maze, sol, pos_row, pos_col + 1)
    
    if sol_going_right is not None:
        return sol_going_right
    
    #If going right doesn't work we backtrack
    sol.pop()
    sol.append("d")
    sol_going_down = solve_maze_helper(maze, sol, pos_row + 1, pos_col)
    
    if sol_going_down is not None:
        return sol_going_down
    
    
    #No solution
    sol.pop()
    return None
    

        
    
print(solve_maze_helper(maze))












