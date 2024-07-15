def binarysearchlist(arr: list[int], target: int) -> bool:
    h = len(arr) - 1
    l = 0

    while l <= h:
        mid = (l + h) // 2
        n = arr[mid]

        if n == target:
            return True
        
        elif n > target:
            h = mid - 1
        else:
            l = mid + 1

    return False
  
