def OPTFF(k, IDs):

    cache = []
    misses = 0

    for i in range(len(IDs)):
        idx = IDs[i]
        
        if idx not in cache:
            misses += 1

            # Cache not full
            if len(cache) < k:
                cache.append(idx) 

            # Cache full
            else:
                # Searches furthest ID
                futureUses = []

                for j in cache:
                    futureUses.append(float('inf'))

                for c in range(len(cache)):
                    for x in range(i + 1, len(IDs)):
                        if IDs[x] == cache[c]:
                            futureUses[c] = x
                            break

                # Looks for the furthest ID
                maxIndex = 0
                for c in range(1, len(futureUses)):
                    if futureUses[c] > futureUses[maxIndex]:
                        maxIndex = c

                # Replace that ID
                cache.pop(maxIndex)
                cache.append(idx)

    return misses