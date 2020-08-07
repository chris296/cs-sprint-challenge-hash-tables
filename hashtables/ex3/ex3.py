def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for i in arrays[0]:
        cache[i] = 1
    for x in arrays[1:]:
        for y in x:
            if y in cache:
                cache[y] += 1
    for k, v in cache.items():
        if v == len(arrays):
            result.append(k)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
