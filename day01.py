def get_input(path: str):
    data = open(path, 'r').read()
    measurements = [int(number) for number in data.split()]
    return measurements


def count_increases(measurements: [int]):
    return sum([True for i in range(1, len(measurements)) if measurements[i] > measurements[i - 1]])


def count_three_window_increases(measures: [int]):
    three_windows_incr = [measures[x] + measures[x + 1] + measures[x + 2] for x in range(len(measures) - 2)]
    return sum([True for i in range(1, len(three_windows_incr)) if three_windows_incr[i] > three_windows_incr[i - 1]])


if __name__ == '__main__':
    input_data = get_input('input01.txt')
    increments_num = count_increases(input_data)
    three_window_increments_num = count_three_window_increases(input_data)
    print(increments_num)
    print(three_window_increments_num)
