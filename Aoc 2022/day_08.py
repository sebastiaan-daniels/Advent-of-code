# part one
with open('input08.txt','r') as f:
    data = f.read().split('\n')[:-1]

# step one, create 2D array
data = [[int(y) for y in x] for x in data]

count = 0
# coordinate (0, 0) is equal to the top left corner
edges = [0, len(data) - 1] # if either x or y is one of these, tree is on edge
visible = 0
for cor_y, row in enumerate(data):
    for cor_x, value in enumerate(row):
        trees_left = []
        trees_right = []
        trees_above = []
        trees_below = []
        if cor_x in edges or cor_y in edges:
            visible += 1
            continue
        # gather x coordinates
        for row_index, item in enumerate(data[cor_y]):
            if row_index < cor_x:
                trees_left.append(item)
            elif row_index > cor_x:
                trees_right.append(item)
        # gather y coordinates
        for row_index, item in enumerate(data):
            if row_index < cor_y:
                trees_above.append(item[cor_x])
            elif row_index > cor_y:
                trees_below.append(item[cor_x])
        
        if all([value > tree for tree in trees_left]):
            visible += 1
        elif all([value > tree for tree in trees_right]):
            visible += 1
        elif all([value > tree for tree in trees_above]):
            visible += 1
        elif all([value > tree for tree in trees_below]):
            visible += 1
        
print(visible)


# part two
with open('input08.txt','r') as f:
    data = f.read().split('\n')[:-1]

# step one, create 2D array
data = [[int(y) for y in x] for x in data]

# coordinate (0, 0) is equal to the top left corner
edges = [0, len(data) - 1] # if either x or y is one of these, tree is on edge
scores = []
for cor_y, row in enumerate(data):
    for cor_x, value in enumerate(row):
        view_distances = []
        trees_left = []
        trees_right = []
        trees_above = []
        trees_below = []
        if cor_x in edges or cor_y in edges:
            # Stupid assumption, but I'm going to assume trees on the edge will not have a high scenic score so I'll be skipping them
            continue
        # gather x coordinates
        for row_index, item in enumerate(data[cor_y]):
            if row_index < cor_x:
                trees_left.append(item)
            elif row_index > cor_x:
                trees_right.append(item)
        # gather y coordinates
        for row_index, item in enumerate(data):
            if row_index < cor_y:
                trees_above.append(item[cor_x])
            elif row_index > cor_y:
                trees_below.append(item[cor_x])
        
        # for counting scores trees on the left, and trees above need to be reversed. (since we look left and up)
        trees_left, trees_above = trees_left[::-1], trees_above[::-1]
           
        # very redundant but copy pasting is quicker and it's a challenge not a beauty contest
        c_vd = 0
        for item in trees_left:
            
            if item < value: c_vd += 1
            elif item >= value:
                c_vd += 1
                break
        view_distances.append(c_vd)

        c_vd = 0
        for item in trees_right:
            
            if item < value: c_vd += 1
            elif item >= value:
                c_vd += 1
                break
        view_distances.append(c_vd)

        c_vd = 0
        for item in trees_above:
            
            if item < value: c_vd += 1
            elif item >= value:
                c_vd += 1
                break
        view_distances.append(c_vd)

        c_vd = 0
        for item in trees_below:
            
            if item < value: c_vd += 1
            elif item >= value:
                c_vd += 1
                break
        view_distances.append(c_vd)
        scenic_score = 1
        for n in view_distances:
            scenic_score *= n
        scores.append(scenic_score)

print(max(scores))