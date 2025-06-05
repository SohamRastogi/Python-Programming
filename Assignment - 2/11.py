def is_uniform(grid):
    first_value = grid[0][0]
    return all(cell == first_value for row in grid for cell in row)

def quadtree(grid):
    
    n = len(grid)  
    
   
    if is_uniform(grid):
        return grid[0][0]
    
    mid = n // 2  
    top_left = [row[:mid] for row in grid[:mid]]  
    top_right = [row[mid:] for row in grid[:mid]]  
    bottom_left = [row[:mid] for row in grid[mid:]]  
    bottom_right = [row[mid:] for row in grid[mid:]]  #

   
    return {
        "top_left": quadtree(top_left),
        "top_right": quadtree(top_right),
        "bottom_left": quadtree(bottom_left),
        "bottom_right": quadtree(bottom_right),
    }

# let 
image = [
    [1, 1, 2, 2],
    [1, 1, 2, 2],
    [3, 3, 4, 4],
    [3, 3, 4, 4]
]

quadtree_dict = quadtree(image)
print(quadtree_dict)