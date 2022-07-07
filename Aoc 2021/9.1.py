#step 1, read input
with open('in9.txt','r') as f:
    data = [_.rstrip('\n') for _ in f.readlines()]

#create a totals list of low_points
low_points = []

#loop through everything and find low points
for row_index,row in enumerate(data):
    for column_index,column in enumerate(row):
        is_low = []
        #check left
        try:
            if int(column) < int(row[column_index - 1]):
                is_low.append(True)
        except IndexError:
            is_low.append(True)
        #check right
        try:
            if int(column) < int(row[column_index + 1]):
                is_low.append(True)
        except IndexError:
            is_low.append(True)
        #check up
        try:
            if int(column) < int(data[row_index-1][column_index]):
                is_low.append(True)
        except IndexError:
            is_low.append(True)
        #check down
        try:
            if int(column) < int(data[row_index+1][column_index]):
                is_low.append(True)
        except IndexError:
            is_low.append(True)
        
        #length of is_low must be 4 to have a low point
        if len(is_low) == 4:
            low_points.append(int(column))

#calculate the risk level
risk = sum(low_points) + len(low_points)

#print the risk
print(f'The risk is: {risk}')
