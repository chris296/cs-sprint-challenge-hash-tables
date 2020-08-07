def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    x = 0
    y = 0
    for idx, val in enumerate(weights):
        cache[val] = idx
    print("cache:", cache)
    for idx, val in enumerate(weights):
        if (limit - val) in cache and (limit - val) != idx:
            x = max(cache[limit - val], idx)
            y = min(cache[limit - val], idx)
    if x == 0 and y == 0:
        return None
    print(x, y)
    return (x, y)
