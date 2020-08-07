def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    results = []
    j = None
    for idx, val in enumerate(weights):
        if val in cache:
            j = cache[val]
            cache[val] = [j, idx]
        else:
            cache[val] = idx
    print("cache:", cache)
    for idx, val in enumerate(weights):
        if (limit - val) in cache and (limit - val) != idx:
            results.append(idx)
    if results == []:
        return None
    results.sort(reverse=True)
    print(results)
    return results
