cacheInfo = []
def read():
    with open('./ad.style.factory_cal.log', 'r') as f:
    for line in f.readlines():
        if "CacheHit" in line:
            cacheInfo.append(line)
num = 0
for i in cacheInfo:
    if num%100==0:
        print(i)
    num +=1