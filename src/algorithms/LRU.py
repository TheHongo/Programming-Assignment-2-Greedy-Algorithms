def LRU(k, IDs):
    cache = []
    misses = 0

    if k == 0:
        return 0, len(IDs) #k = 0 -> all misses

    # most recent -> end of list
    # least recent -> begining of list
    for rid in IDs:

        # Hit
        if rid in cache:
            # Update cache order
            cache.remove(rid)
            cache.append(rid)

        # Misses
        else:
            misses += 1

            # If cache full, remove LRU ID
            if len(cache) == k:
                cache.pop(0)

            cache.append(rid)
    
    return misses

        

