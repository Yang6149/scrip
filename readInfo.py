cacheInfo = []
def read(src):
    with open('./ad.style.factory_cal.log', 'r') as f:
    for line in f.readlines():
        if "CacheHit" in line:
            cacheInfo.append(line)
def b(begin,end){
    out = []
    n = begin
    while(n<=end){
        if n<10:
            out.append('0'+str(n))
        else:
            out.append(str(n))
    }
}
prefix = './ad.style.factory_cal.log.2020-12-09_'

for i in b(16,17):
    src = prefix+i
    read(src)
num = 0
for i in cacheInfo:
    if num%100==0:
        print(i)
    num +=1