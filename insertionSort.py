A = [5, 2, -3, 4, 6, -7, 1, 9, 12, 5, -6]
for k in range(1, len(A)):       # Insert all elements 2 to n
    item = A[k]             # The k'th element to be inserted
    i = k             # i will hold the position of insertion
    while i > 0 and A[i-1] > item:
        A[i] = A[i-1]                        # Shift to right
        i -= 1
    A[i] = item                                   # Insertion
    print(A)                              # Comment this line
print(A)