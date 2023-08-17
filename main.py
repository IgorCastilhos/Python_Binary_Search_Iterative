class BinarySearch():
    # low and high keep track of which part of the list you'll search in
    # low               high
    # [ ] , [ ] , [ ] . [ ]
    @staticmethod
    def search_iterative(list, item):
        # low and high keep track of which part of the list you'll search in.
        low = 0
        high = len(list) - 1  # Last element of the array

        # While you haven't narrowed it down to one element ...
        while low <= high:
            # ... check the middle element
            mid = (low + high) // 2
            guess = list[mid]
            # Found the item.
            if guess == item:
                return mid
            # The guess was too high.
            if guess > item:
                high = mid - 1
            # The guess was too low.
            else:
                low = mid + 1

        # Item doesn't exist
        return None


if __name__ == "__main__":
    # We must initialize the class to use the methods of this class
    bs = BinarySearch()
    my_list = [1, 3, 5, 7, 9]

    print(bs.search_iterative(my_list, 44))  # => 1
