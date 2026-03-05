from algorithms.FIFO import FIFO
from algorithms.LRU import LRU
from algorithms.OPTFF import OPTFF

INPUT_DIR = "../tests/input/"
OUTPUT_DIR = "../tests/output/"

def runAlgorithms(inputFile, outputFile):
    
    with open(inputFile, 'r') as file:
        first_line = file.readline().strip()
        k, m = map(int, first_line.split())
        
        # Assuming the sequence is integers and not chars/strings
        second_line = file.readline().strip()
        idList = list(map(int, second_line.split()))
    
    fifo = FIFO(k, idList)
    lru = LRU(k, idList)
    optff = OPTFF(k, idList)

    with open(outputFile, 'w') as file:
        file.write("FIFO:   " + str(fifo) + "\n")
        file.write("LRU:    " + str(lru) + "\n")
        file.write("OPTFF:  " + str(optff) + "\n")


def main():
    print("Welcome to the cache eviction policies simulator!")

    inputFile = input("Enter the name of the input file: ")
    outputFile = input("Enter the name of the output file: ")

    runAlgorithms(INPUT_DIR + inputFile, OUTPUT_DIR + outputFile)


if __name__ == "__main__":
    main()