# UFID and Student Names
Name: Hong Ouyang | UFID: 54798985
<br/>
Name: Jack Stone | UFID: 22490590

# Instructions for Running the Algorithms
1. Clone the repo into an IDE that runs Python.
2. If applicable, add your input file into `/tests/input/`.
3. In the terminal, cd to the `src` file.
4. Run the program either by typing in `python main.py` or pressing the Run button in the main file of your IDE.
5. When the file is running, it prompts you to input a file from `/tests/input/`, type the file you want to test for misses.
    - When inputting in the file ensure:
        - You do not input any folders such as `/tests/input/` unless if your input file is in a folder in input.
        - Your input file has its extention name, which would be `.in`.
        - The file is formatted correctly.
    - An example would be typing in `example1.in`.

6. After inputting the input file you will be prompted to provide a output file.
    - You do not input any folders such as `/tests/output/` unless if you wish for your output file to be in a folder in `/tests/output/`.
    - Your output file has its extention name, which would be `.out`.
    - The output file does not have to be an existing one.
    - Naming the output to have the same name as an existing file will replace that existing file.
    - An example would be typing in `example1.out`.

7. Following these steps, your output file will appear in `tests/output/`.

# Assumptions
The code assumes that the input file has a viable .in file name that will follow the format layed out in the assignment, being:
```
k m
r1 r2 r3 ... rm
```
Where:
- ( k ) = cache capacity ( ( k >= 1 ) ).
- ( m ) = number of requests.
- ( r_1, .., r_m ) = sequence of integer IDs (Not characters/strings/floats/etc).

</br>
We also assume that the inputted output file has a viable .out file name that follows the format:

```
FIFO    : <number_of_misses>
LRU     : <number_of_misses>
OPTFF   : <number_of_misses>
```
