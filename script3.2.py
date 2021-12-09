#!/usr/bin/python3

def binary_to_desc(bits: str) -> int:
    length = len(bits)
    result = 0
    for i, bit in enumerate(bits):
        if bit == "1":
            result += 2**(length-i-1)
    return result

def recursive(input: list[str], column: int, revert=False) -> int:
    amount_of_ones = sum([ int(line[column]) for line in input])
    bit = int(amount_of_ones/len(input)*2)
    if revert:
        bit = 1-bit 
    output = []
    for line in input:
        if int(line[column]) == bit:
            output.append(line.strip())
    if len(output) > 1:
        return recursive(output, column+1, revert=revert)
    else:
        print(output[0])
        return binary_to_desc(output[0])

def main():
    with open("input3") as input_file:
        input = input_file.readlines()
        a = recursive(input, 0)
        b = recursive(input, 0, True)
        print(a, b, a*b)


if __name__ == "__main__":
    main()