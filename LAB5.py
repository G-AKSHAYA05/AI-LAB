#minmax algorithm
def minimax(depth, nodeindex, ismax, scores, height):
    if ismax:
        return max(
            minimax(depth+1, nodeindex * 2,
                    True, scores, height),
            minimax(depth+ 1, nodeindex *2+1,
                    True, scores, height)
        )
#Main Program
scores = list(map(int, input("Enter 8 leaf node value: ").split()))
height = 3
result = minimax(0, 0, True, scores, height)
print(" \n The optimal value is:", result)

