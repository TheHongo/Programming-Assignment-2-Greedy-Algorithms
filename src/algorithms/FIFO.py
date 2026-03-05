def FIFO(k, IDs):

    cache = []
    misses = 0

    for i in IDs:
        if i not in cache:
            misses += 1

            # Cache full
            if len(cache) == k:
                cache.pop(0)
            
            # Add ID to cache
            cache.append(i)

    return misses