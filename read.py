#「20 min time: %v CacheSize change final Cache hit : %f,hit:%d,sum:%d,size:%d
# logs.Noticef("Cache change Size")
# logs.Info("^cid:%d^filterHash:%v^tupleHash:%v", m.CreativeId, hash, tupleHash)
# logs.Noticef("map full ,Size:%d", len)
# logs.Noticef("now map size is %d", len)
mapp = {}
cacheInfo = []
def read():
    with open('./ad.style.factory_cal.log', 'r') as f:
    for line in f.readlines():
        if "^" in line:
            spp = line.split("^")
            cid = spp[1]
            filterHash = spp[2]
            tupleHash = spp[3]
            if filterHash not in mapp:
                mapp[filterHash] = []
            mapp[filterHash].append((cid,tupleHash))
        if "「" in line:
            cacheInfo.append(line.split("「")[1])
        if "map full ,Size" in line:
            cacheInfo.append(line)
        if "Cache change Size" in line:
            cacheInfo.append(line)
        if "error happen there" in line:
            cacheInfo.append(line)


def Info():
    first = 0
    mz = 0
    for key in mapp:
        first = first + 1
        mz = mz + len(mapp[key])
        #print(len(mapp[key]))
        cidlist = [ i[0] for i in mapp[key]]
        tupleHashlist = [ i[1] for i in mapp[key]]
        dif = []
        if len(set(tupleHashlist))>1:
            print("problem !,there is different tuplesId in same filterHash")
            s = set()
            for i in range(len(tupleHashlist)):
                if tupleHashlist[i] not in s:
                    dif.append(cidlist[i])
        print(cidlist)
        print(tupleHashlist)
    print("first",first)
    print("mz",mz)
def Read20Min():
    for i in cacheInfo:
        print(i)
read()
Read20Min()
#Info()
#123
