
if __name__ == '__main__':
    data=[]
    data.append([int(input())])
    for i in range(1,data[0][0]+1):
        data.append([int(x) for x in input().split(' ')])
    for i in range(1, data[0][0] + 1):
        r = data[i][0]
        c = data[i][1]
        S1, S2 = min(r, c), max(r, c)
        res = (S1 * (S1 - 1) * (S1 + 1) * (2 * S2 - S1) // 12) % (10 ** 9 + 7)
        print('Case #'+str(i)+': '+str(res))





