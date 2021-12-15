from ..functions import read_lines

def main():

    input = read_lines("./inputs/201902.txt")

    intcode = input[0].split(",")

    intcode = list(map(int, intcode))

    # intcode[1] = 12
    # intcode[2] = 2

    print(f"Starting intcode: {intcode}")

    location_counter = 0
    loop_counter = 0

    while True:
    #ERROR IS OCCURING ON LOOP 3 WHEN THE FIRST MULTIPLICATION OCCURS, THE #19 STORED IN SLOT 19 SHOULD BE REPLACED WITH A 10, BUT IT'S NOT
        loop_counter += 1

        opcode = intcode[location_counter]

        if opcode == 1:
            intcode[intcode[location_counter + 3]] = intcode[location_counter + 1] + intcode[location_counter + 2]

        elif opcode == 2:
            intcode[intcode[location_counter + 3]] = intcode[location_counter + 1] * intcode[location_counter + 2]

        elif opcode == 99:
            break

        else:
            print("opcode alingment error")

        print(f"On loop #{loop_counter} the updated intcode is: {intcode}")
        location_counter += 4

    print(f"Ending intcode: {intcode}")

main()