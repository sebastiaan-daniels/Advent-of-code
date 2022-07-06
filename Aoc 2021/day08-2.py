class segment():
    def __init__(self,parameter) -> None:
        #split the parameter
        foo = parameter.split(' | ')
        #set parameters as lists
        self.in_val = foo[0].split()
        self.out_val = foo[1].split()

    def __str__(self) -> str:
        return f'Current value contains: {self.in_val} and output {self.out_val}'
    def decipher(self):
        #we'll add data we cannot instantly read to this list
        incomplete = []
        #check for numbers we can decipher instantly
        for item in self.in_val:
            if len(item) == 2: #1
                self.one = {_ for _ in item}
            elif len(item) == 3: #7
                self.seven = {_ for _ in item}
            elif len(item) == 4: #4
                self.four = {_ for _ in item}
            elif len(item) == 7: #8
                self.eight = {_ for _ in item}
            else:  incomplete.append(item)
        
        #deduct 6, 9 and 0

        #find all with len = 6
        six_segment =  []
        for a in incomplete:
            if len(a) == 6:
                six_segment.append(a)
        for a in six_segment: 
            incomplete.remove(a)
        #only 9 has all elements of 4, 0 and 6 don't
        for a in six_segment:
            a_split = {_ for _ in a}
            dif = self.four.difference(a_split)
            if len(dif) == 0:
                self.nine = a_split
                six_segment.remove(a)
                break
        #only 0 has all elements of 7, 6 does not
        for a in six_segment:
            a_split = {_ for _ in a}
            dif = self.seven.difference(a_split)
            if len(dif) == 0: #0
                self.zero = a_split
            elif len(dif) == 1: #6
                self.six = a_split
        
        #decipher 2,3,5 (5 segments)

        #5 is part of 6, 2 and 3 are not
        for a in incomplete:
            a_split = {_ for _ in a}
            dif = a_split.difference(self.six)
            if len(dif) == 0: #5
                self.five = a_split
                incomplete.remove(a)
                break
        
        #3 is part of 9, 2 is not
        for a in incomplete:
            a_split = {_ for _ in a}
            dif = a_split.difference(self.nine)
            if len(dif) == 0:
                self.three = a_split
            elif len(dif) == 1:
                self.two = a_split
        del incomplete
    

    def summation(self):
        #loop through out
        total = []
        for item in self.out_val:
            #make set
            item = {_ for _ in item}
            #long if else statement
            if item == self.zero: val = 0
            elif item == self.one: val = 1
            elif item == self.two: val = 2
            elif item == self.three: val = 3
            elif item == self.four: val = 4
            elif item == self.five: val = 5
            elif item == self.six: val = 6
            elif item == self.seven: val = 7
            elif item == self.eight: val = 8
            elif item == self.nine: val = 9
            total.append(str(val))
        self.value = int(''.join(total))
        

def main():
    #read all inputs
    with open('inday08-1.txt','r') as f: data = [a.rstrip('\n') for a in f.readlines()]
    #make a total
    total = 0
    #loop through each line
    for line in data:
        #make the line a segment object
        line_segment = segment(line)
        #decipher the line
        line_segment.decipher()
        #get the total of this line
        line_segment.summation()
        #append the total 
        total += line_segment.value

    #print the running total
    print(total)

    
if __name__ == "__main__":
    main()