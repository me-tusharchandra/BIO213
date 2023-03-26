#Local Alignment

def matrix(arr, gap, match, mismatch, m, n):
    for i in range(1,n):
        arr[i][0] = 0

    for j in range(1,m):
        arr[0][j] = 0

    for i in range(1,n):
            for j in range(1,m):
                if seq1[j-1] == seq2[i-1]:
                    arr[i][j] = max(arr[i-1][j-1] + match, 0, arr[i-1][j] + gap, arr[i][j-1] + gap)
                else:
                    arr[i][j] = max(arr[i-1][j-1] + mismatch, 0, arr[i-1][j] + gap, arr[i][j-1] + gap)

def localAlignment(arr, seq1, seq2, i, j, str1, str2, score):
    if arr[i][j] == 0:
        print()
        print(str1)
        print(str2)
        print(score)
        return

    if i > 0 and j > 0 and seq1[j-1] == seq2[i-1]:
        if arr[i][j] == arr[i-1][j-1] + match:
            localAlignment(arr, seq1, seq2, i-1, j-1, seq1[j-1] + str1, seq2[i-1] + str2, score + match)

    if i > 0 and j > 0 and seq1[j-1] != seq2[i-1]:
        if arr[i][j] == arr[i-1][j-1] + mismatch:
            localAlignment(arr, seq1, seq2, i-1, j-1, str1, str2, score)

    if j > 0 and arr[i][j] == arr[i][j-1] + gap:
        localAlignment(arr, seq1, seq2, i, j-1, str1, str2, score)

    if i > 0 and arr[i][j] == arr[i-1][j] + gap:
        localAlignment(arr, seq1, seq2, i-1, j, str1, str2, score)


if __name__ == '__main__':
    print("********** Welcome to the Local Alignment Program **********\n")

    seq1 = 'GATGCGCAG'
    seq2 = 'GGCAGTA'

    match = int(input("Enter the Match score: "))
    mismatch = int(input("Enter the Mismatch score: "))
    gap = int(input("Enter the Map penalty: "))

    m = len(seq1) + 1
    n = len(seq2) + 1

    arr = [[0 for i in range(m)] for j in range(n)]

    matrix(arr, gap, match, mismatch, m, n)

    localAlignment(arr, seq1, seq2, n-1, m-1, '', '', 0)

    print()
    for line in arr:
            print(line)
    print()
