n = 4

S = [0] * n
D = [[0] * n for _ in range(n)]

sum = 0
Dtemp = 0
flag = 0

i = 1
S[0] = 0
D[0][1] = 2
D[0][2] = 6
D[0][3] = 5
D[1][0] = 2
D[1][2] = 4
D[1][3] = 4
D[2][0] = 6
D[2][1] = 4
D[2][3] = 2
D[3][0] = 5
D[3][1] = 4
D[3][2] = 2

while i < n:
    k = 1
    Dtemp = 10000
    while k < n:
        l = 0
        flag = 0
        while l < i:
            if S[l] == k:
                flag = 1
                break
            else:
                l += 1
        if flag == 0 and D[k][S[i - 1]] < Dtemp:
            j = k
            Dtemp = D[k][S[i - 1]]
        k += 1
    S[i] = j
    i += 1
    sum += Dtemp

sum += D[0][j]

for j in range(n):
    print(j, end=' ')
print("\n" + str(sum))
