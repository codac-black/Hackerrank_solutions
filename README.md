# A Very Big Sum

This repository contains a Python implementation of the "A Very Big Sum" problem from HackerRank.

## Problem Description

In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

## Function Description

The `aVeryBigSum` function calculates the sum of all elements in an array of integers.

### Parameters

- `ar`: An array of integers.

### Returns

- The sum of all array elements as a long integer.

## Usage

```python
from aVeryBigSum import aVeryBigSum

ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
result = aVeryBigSum(ar)
print(f"The sum is: {result}")
```

## Testing

To run the tests, use the following command:

```
python -m unittest test_aVeryBigSum.py
```

## GitHub Actions

This repository uses GitHub Actions to automatically run tests on every push and pull request to the main branch.