import re
def main():
    data =open("in03.txt", 'r').read()

    r = re.findall(r"(mul\(\d+,\d+\)){1}", data)
    print(r)

def get_mult(mult:str) -> int:
    return (lambda a,b: int(a)*int(b))( *mult[4:-1].split(','))
    

def one_line():
    print(sum([(lambda a,b: int(a)*int(b))( *mult[4:-1].split(',')) for mult in re.findall(r"(mul\(\d+,\d+\)){1}", open("in03.txt", 'r').read())]))

if __name__ == "__main__":
    one_line()
