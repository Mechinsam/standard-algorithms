# binary search
def BinarySearch(list_ : list, target : int) -> int: # doing 'list_' instead of 'list' because list is already defined in the standard library
	"""
	Searches ordered integer list and returns target position
	"""
	iMax = len(list_) - 1
	iMin, iMid = 0, 0 # this sets them both to 0 in one line

	while (iMax >= iMin):
		iMid = int((iMax + iMin)/2) # specified int because we dont want decimal places

		if list_[iMid] == target:
			return iMid
		elif list_[iMid] < target:
			iMin = iMid + 1
		else:
			iMax = iMid - 1


# main program
if __name__ == "__main__":
	# example
	searchArray = [1,3,5,7,8,9,11,34,45]
	target = 4

	print(f"array: {searchArray}\ntarget:4\n-------\n")
	
	variablePosition = BinarySearch(searchArray, target)

	if variablePosition == None: # we didnt get position returned
		print("Target not found")
	else:
		print(f"Target found in element {variablePosition} of the array")
