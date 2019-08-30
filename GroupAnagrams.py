# 把字符串排好序的结果作为key，同一个key的字符串组成的队列作为value
    hashmap = {}
    for n in strs:
        key = ''.join(sorted(n))
        if key not in hashmap:
            hashmap[key] = [n]
        else:
            hashmap[key] += [n]
    return hashmap.values()
