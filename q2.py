import itertools
import random

def random_permutation(iterable, r):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))

    # Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key




# This code is contributed by Mohit Kumra


#permut = itertools.permutations(random_permutation(range(1,101), 5))
#permut = itertools.permutations.random_permutation(range(100),3)
#permut = itertools.permutations([1,2,3,4,5,6],3)

#count_permut = []
#for i in permut:
    #count_permut.append(i)
    #print all permutations
    #print  count_permut.index(i)+1, i
#print the total number of permutations
#print'number of permutations', len(count_permut)



permut = itertools.permutations(random_permutation(range(1,101), 100))

# Driver code to test above

#count_permut = []
count_permut = []
insertionSort(count_permut)
print ("Sorted array is:")
for i in range(len(count_permut)):
	print ("%d" %count_permut[i])
#for i in range(len(arr)):
	#print ("%d" %arr[i])
