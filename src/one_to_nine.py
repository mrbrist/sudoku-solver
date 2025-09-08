def one_to_nine(arr):
        # Checks if the passed array contains all the numbers 1 to 9
        tmp = []
        tmp.extend(arr)
        tmp.sort()
        return tmp == [1,2,3,4,5,6,7,8,9]