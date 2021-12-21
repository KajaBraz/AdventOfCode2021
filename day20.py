from day05 import read_input


def create_dict(image):
    image_dict = {}
    for i in range(len(image)):
        image_dict[i] = image[i]
    return image_dict


def cut_pixels(image_dict, pixel_coordinates, sign):
    x, y = pixel_coordinates

    add_bgn = ''
    add_end = ''
    if y == 0:
        add_bgn = sign
    elif y == len(image_dict[x]) - 1:
        add_end = sign

    for i in range(x - 1, x + 2):
        if i not in image_dict:
            image_dict[i] = sign * len(image_dict[0])

    considered_pixels = [add_bgn + image_dict[row][y - 1:y + 2] + add_end for row in range(x - 1, x + 2)]

    return considered_pixels, image_dict


def get_value(cut_rows):
    s = ''.join([rows for rows in cut_rows])
    s = s.replace('.', '0')
    s = s.replace('#', '1')
    s = s.replace('-', '1')
    return int(s, 2)


def enlarge_rows(image_dict, sign):
    for k, v in image_dict.items():
        image_dict[k] = sign * 2 + v + sign * 2
    return image_dict


def enhance_image(algorithm, image, n_cycle):
    image_dict = create_dict(image)

    for i in range(n_cycle):
        if i % 2 == 0:
            sign = '.'
        else:
            sign = '-'
        image_dict[sorted(image_dict.keys())[0] - 1] = sign * len(image_dict[0])
        image_dict[sorted(image_dict.keys())[-1] + 1] = sign * len(image_dict[0])
        image_dict = enlarge_rows(image_dict, sign)
        upd_image_dict = {}

        for x in sorted(image_dict.keys()):
            upd_image_dict[x] = ''
            for y in range(len(image_dict[x])):
                current, image_dict = cut_pixels(image_dict, (x, y), sign)
                val = get_value(current)
                upd_image_dict[x] += algorithm[val]
        image_dict = upd_image_dict
    return image_dict


def count_lit(img_dict):
    cnt = sum([row.count('#') for row in img_dict.values()])
    return cnt


if __name__ == '__main__':
    input_data = read_input('input20.txt')
    alg = input_data[0]
    initial_image = create_dict(input_data[2:])
    img_part_1 = enhance_image(alg, initial_image, 2)
    img_part_2 = enhance_image(alg, initial_image, 50)
    print(count_lit(img_part_1))
    print(count_lit(img_part_2))
