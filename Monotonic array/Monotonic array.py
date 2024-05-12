"""An array is monotonic if it is either monotone increasing or monotone decreasing. An array is monotone increasing if all its elements from left to right are non-decreasing. An array is monotone decreasing if all its elements from left to right are non-increasing. Given an integer array return true if the given array is monotonic, or false otherwise."""

# Step 1: Clarify the questions

def monotonic_array(array):
	"""Returns True if any given array is monotonic, False otherwise."""

	n = len(array)

	if n == 0: return True

	first = array[0]
	last = array[-1]

	if first > last:
		# Monotonic decreasing or False
		for k in range(n-1):
			if array[k] < array[k+1]:
				return False
	elif first == last:
		# Monotonic if all elements are same or False
		for k in range(n-1):
			if array[k] != array[k+1]:
				return False
	else:
		# Monotonic increasing or False
		for k in range(n-1):
			if array[k] > array[k+1]:
				return False
			
	return True


print(monotonic_array([])) # True
print(monotonic_array([1, 2, 3])) # True
print(monotonic_array([3, 2, 1])) # True
print(monotonic_array([1, 1, 1])) # True
print(monotonic_array([1, 2, -3])) # False