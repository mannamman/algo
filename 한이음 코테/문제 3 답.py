#3
voters = ["01","10","01","01","10"]
def fun(voters):
    out = list()
    length = len(voters[0])
    while(1):
        hash_map = dict()
        for i in range(length):
            if(str(i) in out):
                continue
            hash_map[str(i)] = 0
        if(len(hash_map)<1):
            return -1
        for i in voters:
            hash_map[i[0]] = hash_map[i[0]] + 1
        result = 0
        for i in hash_map:
            result = hash_map[i] + result

        big = 0
        big_index = 0
        small = 100
        small_index = list()
        for i in hash_map:
            if(big<hash_map[i]):
                big = hash_map[i]
                big_index = i
        for i in hash_map:
            if(small>=hash_map[i]):
                small = hash_map[i]
        if(big>result/2):
            return int(big_index)
        else:
            temp=list()
            for i in hash_map:
                if(hash_map[i]==small):
                    temp.append(i)
                    small_index.append(i)
            for i in small_index:
                out.append(i)
            for i in temp:
                del(hash_map[i])
            for i in range(len(voters)):
                for j in small_index:
                    if(j in voters[i]):
                        index = voters[i].index(j)
                        voters[i] = voters[i][:index] + voters[i][index+1:]
fun(voters)