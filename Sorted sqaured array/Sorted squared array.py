"""You are given an array of Integers in which each subsequent value is not less than the previous value. Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order."""

# Step 1: Clarify the questions
# Eg: Are all integers distinct? Positive? Can have negatives? Empty Array?

# Step 2: Write multiple test cases
	# Eg: [1, 3, 5] => [1, 9, 25]
	# Eg: [1, 2, 3, 4, 5] => [1, 4, 9, 16, 25]

	# Eg: [-4, -2, 0, 1, 3] => [0, 1, 4, 9, 16]

def sortedSqauredArray(arr):
	"""Return a Sorted and Sqaured array."""

	if len(arr):
		for i in range(len(arr)):
			arr[i] = arr[i] * arr[i]

		arr.sort()
		return arr
	else:
		return []


print(sortedSqauredArray([1, 3, 5])) # [1, 9, 25]

# My solution takes O(nlogn) and O(1) space.
# O(nlogn) because of use of sorting algorithm.

