# Global Alignment - Q1

# matrix formation
def matrix(arr, gap, match, mismatch, m, n):
    for i in range(1,n):
        arr[i][0] = arr[i-1][0] + int(gap)

    for j in range(1,m):
        arr[0][j] = arr[0][j-1] + int(gap)

    for i in range(1,n):
            for j in range(1,m):
                if seq1[j-1] == seq2[i-1]:
                    arr[i][j] = max(arr[i-1][j-1] + match, arr[i-1][j] + int(gap), arr[i][j-1] + int(gap))
                else:
                    arr[i][j] = max(arr[i-1][j-1] + mismatch, arr[i-1][j] + int(gap), arr[i][j-1] + int(gap))


def optimalAlignment(arr, seq1, seq2, i, j, str1, str2, score):
    if i == 0 and j == 0:
        print()
        print(str1)
        print(str2)
        print(score)
        return

    if i > 0 and j > 0 and seq1[j-1] == seq2[i-1]:
        optimalAlignment(arr, seq1, seq2, i-1, j-1, seq1[j-1] + str1, seq2[i-1] + str2, score + match)

    if i > 0 and j > 0 and seq1[j-1] != seq2[i-1]:
        if arr[i-1][j-1] + mismatch == arr[i][j]:
            optimalAlignment(arr, seq1, seq2, i-1, j-1, seq1[j-1] + str1, seq2[i-1] + str2, score + mismatch)

    if j > 0 and arr[i][j-1] + gap == arr[i][j]:
        optimalAlignment(arr, seq1, seq2, i, j-1, seq1[j-1] + str1, '_' + str2, score + gap)

    if i > 0 and arr[i-1][j] + gap == arr[i][j]:
        optimalAlignment(arr, seq1, seq2, i-1, j, '_' + str1, seq2[i-1] + str2, score + gap)

if __name__ == '__main__':
    print()
    print("********** Welcome to the Global Alignment Program **********")

    seq1 = 'GATGCGCAG' 
    seq2 = 'GGCAGTA'

    print()
    match = int(input("Enter the Match score: "))
    mismatch = int(input("Enter the Mismatch score: "))
    gap = int(input("Enter the Gap score: "))
    
    m = len(seq1) + 1
    n = len(seq2) + 1

    arr = [[0 for i in range(m)] for j in range(n)]

    matrix(arr, gap, match, mismatch, m, n)

    optimalAlignment(arr, seq1, seq2, n-1, m-1, '', '', 0)

    print()
    for line in arr:
            print(line)
    print()




