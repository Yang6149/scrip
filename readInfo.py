cacheInfo = []
def read(src):
    with open(src, 'r') as f:
        for line in f.readlines():
            if "CacheHit" in line:
                cacheInfo.append(line)

    

prefix = '../ad.style.factory_cal.log.2020-12-09_'

for i in [18,19,20]:
    src = prefix+str(i)
    read(src)
num = 0
for i in cacheInfo:
    if num%100==0:
        print(i)
    num +=1
