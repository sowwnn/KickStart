from itertools import combinations
# def Solution(p,line):
#     res = -1
#     for C in combinations(line, p):
#         C = list(C)
#         _max = max(C)
#         count = 0
#         for item in C:
#             if item != _max:
#                 count += _max - item
#         if res == -1 or count < res:
#             res = count
#     return res
# def Solution(p,line):
#     line.sort()
#     res = -1
#     for i in range(len(line)-p+1):
#         c = line[i:i+p]
#         _max = max(c)
#         count = 0
#         for item in c:
#             if item != _max:
#                 count += _max - item
#         if res == -1 or count < res:
#             res = count
#     return res
#
# def Solution(p,line):
#     line.sort()
#     pre = [0]
#     res = 1000000000000
#     for i in range(len(line)):
#         pre.append(sum(line[:i+1]))
#     for i in range(len(line)):
#         if i >= p-1:
#             hour = p*line[i] - (pre[i + 1] - pre[i -p +1 ])
#             if hour < res: res= hour
#     return res

def Solution(p,line):
    line.sort()
    pre = [0]
    sum = 0
    res = 1000000000000
    for i in range(0,len(line)):
        sum+= line[i]
        pre.append(sum)
    for i in range(p-1,len(line)):
        res = min(res,p*line[i] - (pre[i + 1] - pre[i -p +1 ]))
    return res
if __name__ == '__main__':
    testcase = int(input())
    for i in range(testcase):
        temp = input().split()
        n = (int(temp[0]))
        p = (int(temp[1]))
        line = ([int(x) for x in input().split()])
        print('Case #' + str(i + 1) + ': ' + str(Solution(p, line)))






