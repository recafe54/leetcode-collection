def fn(arr):
    left = ans = 0
    right = len(arr) - 1
    CONDITION = ''

    while left < right:
        if CONDITION:
            left += 1
        else:
            right -= 1
    
    return ans