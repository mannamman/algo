def countGroups(related):
    # Write your code here
    pole = 0
    length = len(related)
    result = [0 for _ in range(length-1)]
    answer = 0
    for i in range(len(related)):
        if(pole>=length-1):
            break
        if(related[pole][pole + 1]=='1' and related[pole + 1][pole]=='1'):
            result[i] = True
        else:
            result[i] = False
        pole = pole + 1
    for i in result:
        if(i==False):
            answer = answer + 1
    
    count = 0
    for i in range(length):
        for j in range(i):
            if(related[j][i]=='1' and related[i][j]=='1'):
                count = count + 1
    answer = answer + 1 - count
    
    return(answer)
