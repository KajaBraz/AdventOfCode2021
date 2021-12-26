from functools import reduce


def read_input(path):
    with open(path) as f:
        input = f.read()
    return input


def get_binary(s):
    conversion_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                       '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
                       'E': '1110', 'F': '1111'}
    binary = ''.join(conversion_dict[n] for n in s)
    return binary


def literal(binary):
    new_binary = binary
    nums = []
    pref, num = new_binary[0], new_binary[1:5]
    nums.append((pref, num, int(num, 2)))
    new_binary = new_binary[5:]
    while pref == '1':
        pref, num = new_binary[0], new_binary[1:5]
        nums.append((pref, num, int(num, 2)))
        new_binary = new_binary[5:]
    nums = join_more_bits(nums)
    return nums[1], new_binary


def operator(binary, V_VAL):
    I = binary[0]

    if I == '0':
        L = binary[1:16]
        L_dec = int(L, 2)
        R = binary[16:]
        new_R = R
        exp_val = []
        while len(R)-len(new_R)<L_dec:
            new_R, V_VAL, new_exp_val = packet_decoder(new_R, V_VAL)
            exp_val.append(new_exp_val)
        return V_VAL, new_R, exp_val

    else:
        L = binary[1:12]
        L_dec = int(L, 2)
        R = binary[12:]
        exp_val = []
        for sub_packet in range(L_dec):
            R, V_VAL, new_exp_val = packet_decoder(R, V_VAL)
            exp_val.append(new_exp_val)
        return V_VAL, R, exp_val


def packet_decoder(binary, V_VAL):
    V = int(binary[:3], 2)
    T = int(binary[3:6], 2)
    R = binary[6:]

    V_VAL += V
    new_exp_val = 0

    if T == 4:
        new_exp_val, R = literal(R)
    else:
        if T == 0:
            V_VAL, R, exp_val = operator(R, V_VAL)
            new_exp_val = sum(exp_val)
        elif T == 1:
            V_VAL, R, exp_val = operator(R, V_VAL)
            new_exp_val = reduce(lambda acc, val: acc * val, exp_val, 1)
        elif T == 2:
            V_VAL, R, exp_val = operator(R, V_VAL)
            new_exp_val = min(exp_val)
        elif T == 3:
            V_VAL, R, exp_val = operator(R, V_VAL)
            new_exp_val = max(exp_val)
        elif T == 5:
            V_VAL, R, exp_val = operator(R, V_VAL)
            new_exp_val = 1 if exp_val[0] > exp_val[1] else 0
        elif T == 6:
            V_VAL, R, exp_val = operator(R, V_VAL)
            new_exp_val = 1 if exp_val[0] < exp_val[1] else 0
        elif T == 7:
            V_VAL, R, exp_val = operator(R, V_VAL)
            new_exp_val = 1 if exp_val[0] == exp_val[1] else 0
    return R, V_VAL, new_exp_val


def join_more_bits(nums):
    b = ''.join(num[1] for num in nums)
    return [b, int(b, 2)]


if __name__ == '__main__':
    data = read_input('input16.txt')
    bin_num = get_binary(data)
    remaining, final_v, expression_val = packet_decoder(bin_num, 0)
    print(final_v, expression_val, )
