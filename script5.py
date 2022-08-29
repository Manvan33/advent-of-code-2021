#!/usr/bin/python3.9

def parse_input(input: list[str]) -> list[tuple[tuple[int, int], tuple[int, int]]]:   
    segments = []
    for line in input:
        points = []
        for point in line.split("->"):
            x,y = point.strip().split(",")
            points.append((x,y))
        segments.append((points[0], points[1]))
    return segments

def keep_only_vert_and_horiz(segments):
    output = []
    for seg in segments:
        if seg[0][0] == seg[1][0] or seg[0][1] == seg[1][1]:
            output.append(seg)
    return output

def draw_points(segments):
    points = []
    for seg in segments:
        x1, y1, x2, y2 = map(int, [seg[0][0], seg[0][1], seg[1][0], seg[1][1]])
        if x1 == x2:
            for y in range(y1, y2+1):
                points.append((x1, y))
        elif y1 != y2:
            print("PROBLEM")
        else:
            for x in range(x1, x2+1):
                points.append((x, y1))
    return points
    
def main():
    with open("input5") as input_file:
        segments = parse_input(input_file.readlines())
    filtered = keep_only_vert_and_horiz(segments)
    points = draw_points(filtered)
    uniq_points = set(points)
    for point in uniq_points:
        points.pop(points.index(point))
    print(len(set(points)))

if __name__ == "__main__":
    main()