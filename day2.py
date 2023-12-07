def calculate_wrapping_paper(dimensions):
    total_paper = 0

    for dimension in dimensions:
        l, w, h = dimension
        surface_area = 2 * (l * w + w * h + h * l)
        extra_paper = min(l*w, w*h, h*l)
        total_paper += surface_area + extra_paper

    return total_paper


def format_data(file_path):
    formatted_data = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                formatted_line = tuple(map(int, line.strip().replace('x', ',').split(',')))
                formatted_data.append(formatted_line)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return formatted_data


def calc_total_ribbon(dimensions):
    total_ribbon = 0

    for dimension in dimensions:
        l, w, h = dimension

        smallest_perimeter = 2 * (l + w + h - max(l, w, h))
        ribbon_bow = l * w * h
        present_ribbon = smallest_perimeter + ribbon_bow
        total_ribbon += present_ribbon

    return total_ribbon


data = format_data("/Users/prakharpratap/codes/python/adventofcode/day2.txt")
paper = calculate_wrapping_paper(data)
print(paper)
ribbon = calc_total_ribbon(data)
print(ribbon)
