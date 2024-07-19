# Lecture 7.4 - Greedy Algorithms-Huffman Coding.pdf (PDF file)
**Summary**
Huffman Coding:

Huffman coding is a lossless data compression algorithm, which reduces the size of text files by replacing frequently used characters with shorter codes and less frequently used characters with longer codes. It allows efficient transmission and storage of data.

**Efficient communication:**

- Data is often sent in binary strings of length 5, but some letters may occur more frequently than others, leading to inefficient data transfer.
- Huffman coding assigns shorter strings to more frequent letters, optimizing data transfer.

**Prefix codes:**

- Prefix codes are used to represent each character, where no code is a prefix of another code.
- This ensures unique decoding of the message.

**Optimal prefix codes:**

- The measure of efficiency of a prefix code is the Average Bits per Letter (ABL).
- Huffman coding aims to find the most efficient prefix code for a given set of characters and their frequencies.

**Recursive algorithm:**

- Huffman's algorithm is a recursive algorithm that finds the optimal prefix code:
  - Step 1: Choose the two characters with the lowest frequencies, and combine them into a new character with the combined frequency.
  - Step 2: Repeat step 1 until only one character remains.
  - Step 3: Assign codes to the characters from the tree representation of the optimal prefix code.

**Optimality of Huffman's algorithm:**

- By induction, Huffman's algorithm is proven to create optimal prefix codes.
- Suppose there is a better optimal tree, then shuffling the labels and merging the lowest frequency characters will create a better tree, which is a contradiction.

**Implementation and complexity:**

- Implementation involves maintaining frequencies in an array and finding minimum values with a linear scan, leading to a complexity of O(k²).
- Using a heap to maintain frequencies reduces the complexity to O(k log k).

**Why is Huffman coding greedy?**

- It recursively combines characters with the lowest frequencies.
- It makes locally optimal choices without considering other pairings of characters.

**Historical notes:**

- Claude Shannon invented information theory, but his work did not provide a practical method for constructing optimal codes.
- Shannon and Robert Fano developed recursive solutions, but they were not optimal.
- David A. Huffman, a graduate student of Fano, discovered the optimal prefix code algorithm during his course.
