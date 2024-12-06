class Instructions():
    def __init__(self, instructions: list[str]) -> None:
        self.instructions = {}
        for i in range(11,100):
            self.instructions[i] = []
        for item in instructions:
            data = (lambda x: (int(x[0]),int(x[1])) )(item.split("|"))
            self.instructions[data[0]].append(data[1])

    def getInstruction(self,page:int) -> list:
        return self.instructions[page]


class Pages():
    def __init__(self, pages: list[str]) -> None:
        self.pages = [self.lstcnvrt(x) for x in pages]
        self.good_instructions = []

    def lstcnvrt(self, instr:str) ->list:
        return [int(x) for x in instr.split(",")]
    
    def isGood(self, instr: Instructions, page:list[int]) -> bool:
        rect = []
        for i, item in enumerate(page):
            items_before = page[:i]
            cur_instr = instr.getInstruction(item)
            rect.extend([x in items_before for x in cur_instr])
        return not any(rect)
    
    def listGood(self, instr: Instructions) -> None:
        for page in self.pages:
            is_good = self.isGood(instr, page)
            if is_good: self.good_instructions.append(page)


def main():
    total = 0
    # data filtering
    data = [x.strip() for x in open("in05.txt", 'r').readlines()]
    # Instruction filtering
    instructions = []
    pages = []
    for item in data:
        if "|" in item:
            instructions.append(item)
        elif "," in item:
            pages.append(item)

    instr = Instructions(instructions)
    page = Pages(pages)

    page.listGood(instr)

    for item in page.good_instructions:
        total+= item[len(item) // 2]
    
    print(total)
    

if __name__ == "__main__":
    main()
