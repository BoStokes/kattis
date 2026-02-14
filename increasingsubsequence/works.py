while True:
    n, *A = map(int, input().split())
    if n == 0:
        break
    A.append(10**8+1)
    n+=1

    prev = [[] for _ in range(n)]

    length = [1] * n
    max_len = 1
    max_idx = 0
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and length[j]+1 >= length[i]:
                if length[j] + 1 > length[i]:
                    prev[i] = []
                length[i] = length[j]+1
                prev[i].append(j)
                if length[i] > max_len:
                    max_len = length[i]
                    max_idx = i
    def print_LIS(i):
        if not prev[i]:
            print(f'{max_len} {A[i]}', end='')
            return
        print_LIS(min(prev[i], key=lambda j:A[j]))
        print(f' {A[i]}', end='')

    print_LIS(max_idx)
    print()

    

