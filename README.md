# Smith-Waterman Calculator
Smith-Waterman local sequence alignment calculator for DNA sequences.

# Description
Uses the Smith-Waterman algorithm to create a scoring matrix and local alignment of a sequence. Traceback starts at the highest score and aligns until a 0 score is reached. The resulting score matrix and local alignment are printed on the screen.

This calculator was designed so I could get a better understanding of implementing bioinformatics algorithms in Python. I learned how to manipulate numpy arrays, which allowed me to create a dynamic data structre for this problem. In future implementations, I hope to include a feature that prints out multiple aligmnents in the case that there are multiple occurances of the maximum score.

# Usage
Input the DNA sequence as a string and change the scoring as desired. 
