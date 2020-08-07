#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = []
    for i in tickets:
        cache[i.source] = i.destination
    print(cache)
    route.append(cache['NONE'])
    i = 0
    while i < len(cache)-1:
        currentdestination = route[i]
        route.append(cache[currentdestination])
        i += 1
    print(route)

    return route
