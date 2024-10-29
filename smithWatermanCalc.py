import numpy as np

dna1 = "TGTTACGGAGTCTCTGCTCGC"   #top squence
dna2 = "GGTTGACTACGCTCTGAGAGATC"   #side sequence

gapPenalty = -2
matchScore = 3
mismatchScore = -3
totalScore = 0
matrixSW = np.matrix([0])
rowLen = len(dna1)
columnLen = len(dna2)

def createMatrix(matrixSW, rowLen, columnLen):

    matrixSW = np.zeros((columnLen + 1, rowLen + 1), dtype = int)
    return matrixSW

def findMatchValue(column, row ,matrixSW):
    cellScore = matchScore
    cellScore += matrixSW[row - 1, column - 1]

    return cellScore

def findMismatchValue(column, row, matrixSW):
    cellScore = mismatchScore
    cellScore += matrixSW[row - 1, column - 1]

    return cellScore

def findTopScore(column, row, matrixSW):
    cellScore = gapPenalty + matrixSW[row, column - 1 ]

    return cellScore

def findLeftScore(column, row, matrixSW):
    cellScore = gapPenalty + matrixSW[row - 1, column ]
    return cellScore

def calcCell(column, row, dna1, dna2, matrixSW):
    #if the same nucleotide
    if dna1[column - 1] == dna2[row - 1]:
        diagonalScore = findMatchValue(column, row, matrixSW)

    #if mismatch
    else:
        diagonalScore = findMismatchValue(column, row, matrixSW)

    scoreLeft = findLeftScore(column, row, matrixSW)    #find the left and top score for a gap
    scoreTop = findTopScore(column, row, matrixSW)

    maxScore = max(scoreLeft, scoreTop, diagonalScore)

    if maxScore < 0:                      #if score is negative, set to 0
        maxScore = 0

    return maxScore

def calcRow(row, dna1, dna2, matrixSW, rowLen):
    rowIndex = 1
    while rowIndex <= rowLen:
        
        score = calcCell(rowIndex, row, dna1, dna2, matrixSW)
        matrixSW[row, rowIndex] = score

        rowIndex += 1

    return matrixSW

def calcMatrix(dna1, dna2, matrixSW, columnLen, rowLen):
    index = 1
    while index <= columnLen:
        matrixSW = calcRow(index, dna1, dna2, matrixSW, rowLen)
        index += 1
    return matrixSW

def calcSequence(matrixSW, dna1, dna2):
    local1 = ""
    local2 = ""
    maxValue = np.max(matrixSW)
    if maxValue > 0:
        maxLocation = np.unravel_index(matrixSW.argmax(), matrixSW.shape)
        
        row = maxLocation[0] - 1 
        column = maxLocation[1] - 1

        while matrixSW[row , column] != 0: #while not at a 0

            diagonal = matrixSW[row - 1, column - 1]
            left = matrixSW[row, column - 1]
            up = matrixSW[row - 1, column]

            topScore = max(left, up, diagonal)


            if topScore == diagonal: #if DNA matches or mismatches
                local1 += dna1[column]
                local2 += dna2[row]
                row -= 1
                column -= 1
            elif topScore == up: #if highest score is above current cell
                local1 += "-" #gap in dna1
                local2 += dna2[row]
                row -= 1
            elif topScore == left: #if highest score is to the left of current cell
                local2 += "-" #gap in dna2
                local1 += dna1[column]
                column -= 1
    #run condition one more time after reaches 0 to evaluate last cell.
    if dna1[column] == dna2[row]: 
        local1 += dna1[column]
        local2 += dna2[row]
        row -= 1
        column -= 1
    elif topScore == up: 
        local1 += "-"
        local2 += dna2[row]
        row -= 1
    elif topScore == left: 
        local2 += "-" 
        local1 += dna1[column]
        column -= 1

    return (local1[::-1], local2[::-1])
        



matrixSW = createMatrix(matrixSW, rowLen, columnLen)
matrixSW = calcMatrix(dna1, dna2, matrixSW, columnLen, rowLen)

print(matrixSW)

results = calcSequence(matrixSW, dna1, dna2)

print(results[0])
print(results[1])