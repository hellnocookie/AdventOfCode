
class SortAlgo:

    @staticmethod
    def quick_sort(arr: list) -> list:
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return SortAlgo.quick_sort(left) + middle + SortAlgo.quick_sort(right)