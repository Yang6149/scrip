cacheInfo = []
def read():
    with open('./ad.style.factory_cal.log', 'r') as f:
    for line in f.readlines():
        if "map full ,Size" in line:
            cacheInfo.append(line)
        if "Cache change Size" in line:
            cacheInfo.append(line)
        if "error happen there" in line:
            cacheInfo.append(line)
        if "CacheHit" in line:
            cacheInfo.append(line)
