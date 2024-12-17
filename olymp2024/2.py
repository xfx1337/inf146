def max_chain_length(A, B, C, D):
    pairs = min(B, C)

    length = 2 * pairs

    B -= pairs
    C -= pairs

    if B > 0 or C > 0:
        length += 1
    length += 2 * A
    length += 2 * D

    return length


A = int(input()) # right white, left white
B = int(input()) # right white, left black
C = int(input()) # right black, left white
D = int(input()) # right black, left black
print(max_chain_length(A, B, C, D))