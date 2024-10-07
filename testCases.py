import numpy as np
from smithWatermanCalc import createMatrix, calcMatrix

def testCase1(): #matching sequence

    dna1 = "AAGC"
    dna2 = "AAGC"

    expectedMatrix = np.array([[0,0,0,0,0],
                              [0,1,1,0,0],
                              [0,1,2,0,0],
                              [0,0,0,3,1],
                              [0,0,0,1,4]])

    matrixSW = np.matrix([0])
    rowLen = len(dna1)
    columnLen = len(dna2)


    matrixSW = createMatrix(matrixSW, rowLen, columnLen)
    matrixSW = calcMatrix(dna1, dna2, matrixSW, columnLen, rowLen)

    assert np.array_equal(matrixSW, expectedMatrix), "Test Case 1 failed"


def testCase2(): #shortest sequence
    
    dna1 = "A"
    dna2 = "T"

    expectedMatrix = np.array([[0,0], 
                               [0,0]])

    matrixSW = np.matrix([0])
    rowLen = len(dna1)
    columnLen = len(dna2)


    matrixSW = createMatrix(matrixSW, rowLen, columnLen)
    matrixSW = calcMatrix(dna1, dna2, matrixSW, columnLen, rowLen)

    assert np.array_equal(matrixSW, expectedMatrix), "Test Case 2 failed"


def testCase3(): #non-matching sequence

    dna1 = "AG"
    dna2 = "TC"

    expectedMatrix = np.array([[0,0,0],
                              [0,0,0],
                              [0,0,0]])

    matrixSW = np.matrix([0])
    rowLen = len(dna1)
    columnLen = len(dna2)


    matrixSW = createMatrix(matrixSW, rowLen, columnLen)
    matrixSW = calcMatrix(dna1, dna2, matrixSW, columnLen, rowLen)

    assert np.array_equal(matrixSW, expectedMatrix), "Test Case 3 failed"











testCase1()
testCase2()
testCase3()