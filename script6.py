#!/usr/bin/python3.9

def parse_input(input: str) -> list[int]:
    return [int(lantern) for lantern in input.strip().split(",")]

def main():
    with open("input6") as input_file:
        lanterns = parse_input(input_file.readline())

    total = 0
    for l in lanterns:
        day = 0
        step = [l]
        while day < 256:
            for i in range(len(step)):
                if step[i]==0:
                    step[i] = 6
                    step.append(8)
                else:
                    step[i] -= 1
            day += 1
        length = len(step)
        total += length
        print(length)
    print(total)

if __name__ == "__main__":
    main()