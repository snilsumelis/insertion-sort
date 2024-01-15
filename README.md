# insertion-sort
## Description:
The provided Python code implements the insertion sort algorithm, which is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort is more efficient in practice than its quadratic time complexity would suggest and is suitable for small datasets or nearly sorted datasets.
## Time Complexity (Big-O Notation):
The time complexity of the insertion sort algorithm is O(n^2) in the worst case. This is because, in the worst-case scenario, each element in the unsorted part of the array needs to be compared and moved to its correct position.

- Best Case: O(n)
In the best-case scenario, when the input array is already sorted, the algorithm only needs to perform n-1 comparisons and 0 swaps.

- Average Case: O(n^2)
The average case occurs when each element in the array is equally likely to be in any position. On average, the algorithm performs n^2/4 comparisons and n^2/4 swaps.

- Worst Case: O(n^2)
The worst-case scenario happens when the input array is in reverse order. In this case, the algorithm performs the maximum number of comparisons and swaps, resulting in a time complexity of O(n^2).

## Here is an example first 4 steps of the Selection Sort algorithm for the array [7, 3, 5, 8, 2, 9, 4, 15, 6]:
### Step 1:
- Array: [7, 3, 5, 8, 2, 9, 4, 15, 6]
- Minimum element: 2 (index: 4)
- Swap: [2, 3, 5, 8, 7, 9, 4, 15, 6]
### Step 2:
- Array: [2, 3, 5, 8, 7, 9, 4, 15, 6]
- Minimum element: 3 (index: 1)
- Swap: [2, 3, 5, 8, 7, 9, 4, 15, 6]
### Step 3:
- Array: [2, 3, 5, 8, 7, 9, 4, 15, 6]
- Minimum element: 4 (index: 6)
- Swap: [2, 3, 4, 8, 7, 9, 5, 15, 6]
### Step 4:
- Array: [2, 3, 4, 8, 7, 9, 5, 15, 6]
- Minimum element: 5 (index: 2)
- Swap: [2, 3, 4, 8, 7, 9, 5, 15, 6]
