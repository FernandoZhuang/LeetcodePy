# def tribonacci(n):
#     q0, q1, q2 = 0, 1, 1
#
#     if (n < 3): return 1 if n == 2 else n
#     for flag in range(2, n):
#         tmp = q0 + q1 + q2
#         q0, q1, q2 = q1, q2, tmp
#
#     return q2

def tribonacci(n):
    num = [0, 1, 1]

    if (n < 3): return num[n]
    # for i in range(2, n): num.append(sum(num[-3:]))
    i = 3
    while i <= n:
        num.append(sum(num[-3:]))
        i += 1

    return num[-1]


if __name__ == '__main__':
    tribonacci(25)
