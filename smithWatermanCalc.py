import numpy as np

dna1 = "A"   #top squence
dna2 = "A"   #side sequence

gapPenalty = -2
matchScore = 1
mismatchScore = -1
totalScore = 0

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





matrixSW = np.matrix([0])
rowLen = len(dna1)
columnLen = len(dna2)

matrixSW = createMatrix(matrixSW, rowLen, columnLen)

matrixSW = calcMatrix(dna1, dna2, matrixSW, columnLen, rowLen)



