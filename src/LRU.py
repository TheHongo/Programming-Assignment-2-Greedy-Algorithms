def LRU(k, IDs):
    cache = []
    hits = 0
    misses = 0

    if k == 0:
        return 0, len(IDs) #k = 0 -> all misses

    #most recent -> end of list
    #least recent -> begining of list
    for rid in IDs:

        if rid in cache:
            hits += 1
            cache.remove(rid)
            cache.append(rid)

        else:
            misses += 1

            if len(cache) == k:
                cache.pop(0)

            cache.append(rid)
    
    return hits, misses

        

