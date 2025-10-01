'''
Fill in the blanks so the 
function returns all permutations of the input list:
'''


def get_permutations(arr):
    if len(arr) == __________:
        return [arr[:]]
    
    result = []
    for i in range(len(arr)):
        first = arr[__________]
        rest = arr[:i] + arr[__________]
        for perm in get_permutations(__________):
            result.append([first] + __________)
    return result

print(get_permutations([1, 2, 3]))

'''
Expected Output:
[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
'''