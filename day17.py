import re


def is_in_target(xt, yt, current):
    if current[0] in range(xt[0], xt[1] + 1) and current[1] in range(yt[0], yt[1] + 1):
        return True
    return False


def exceeded_target(current, yt, vy):
    if current[1] < 0 and current[1] < yt[0] and vy < 0:
        return True
    return False


def simulate(vx, vy, xt, yt):
    x, y = 0, 0
    while not exceeded_target((x, y), yt, vy):
        x += vx
        y += vy
        if vx > 0:
            vx = vx - 1
        elif vx < 0:
            vx = vx + 1
        vy = vy - 1

        if is_in_target(xt, yt, (x, y)):
            return True


def find_vel(xt, yt):
    max_x = max(xt) if max(xt) >= 0 else -min(xt)
    max_y = max(yt) if max(yt) >= 0 else -min(yt)
    found_velocities = []
    for vx in range(max_x + 1):
        for vy in range(min(yt), max_y + 1):
            found = simulate(vx, vy, xt, yt)
            if found:
                found_velocities.append((vx, vy))
    return found_velocities


def found_highest_y(velocities_list):
    max_vy = max(velocities_list, key=lambda v: v[1])
    highest_point = (2 + (max_vy[1] - 1)) * max_vy[1] // 2

    return highest_point


if __name__ == '__main__':
    data = 'target area: x=240..292, y=-90..-57'
    area_coordinates = re.findall(r'-?\d+', data)
    x_target = [int(coord) for coord in area_coordinates[0:2]]
    y_target = [int(coord) for coord in area_coordinates[2:]]
    velocities = find_vel(x_target, y_target)
    print(len(velocities))
    highest_y = found_highest_y(velocities)
    print(highest_y)
