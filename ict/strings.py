def commonSubstring(a, b):
    # Write your code here
    result = list()
    status = False
    for i,j in zip(a,b):
        for x in i:
            status = False
            if x in j:
                status = True
                result.append("YES")
                break
        if(status == False):
            result.append("NO")
    for i in result:
        print(i)
