from typing import List

class BinarySearch:
    def __init__(self, ara: List[int]):
        ara.sort()  # Sorts in place
        self.ara = ara

    def binary_search(self, target: int):
        low = 0
        high = len(self.ara) - 1

        while low<=high:
            # mid = int((low + high)/2)
            # *** MOST important "//" Nah dile Python ee "Type Cast" hobe Nah... Mane, Number ta "float" hoye jabe... eijonno "//" dile "int" ee Convert hoye jabe ***
            mid = (low + high) // 2

            if self.ara[mid] == target:
                return mid
            elif self.ara[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

if __name__ == "__main__":
    bs_obj = BinarySearch([1,3,4,5])
    idx = bs_obj.binary_search(5)
    print(idx)