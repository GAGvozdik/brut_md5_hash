import hashlib

list_hash = []
c = '83427085f24ab6e0bb83f6a8a2136379'

ll = []
sault = '.145291728310085349'
rul = '673635968.'

i = 17
lenn = 1000

k = 0

for j in range(lenn):

    ll.append(hashlib.md5())

    ll[j].update(bytes(rul + str(j) + sault, "ascii"))
    list_hash.append(ll[j].hexdigest())

    if list_hash[j][:3] == c[:3]:
        print('есть совпадение')
        print(list_hash[j])
        print("искомое число - ", j)
