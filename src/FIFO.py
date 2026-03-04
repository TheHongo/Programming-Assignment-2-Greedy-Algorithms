def FIFO(k, IDs):

    cache = []
    hits = 0
    misses = 0

    for request in IDs:
        if request in cache:
            hits += 1
        else:
            misses += 1
            if len(cache) < k:
                cache.append(request)
            else:
                cache.pop(0)
                cache.append(request)

    return hits, misses