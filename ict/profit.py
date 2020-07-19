def stockPairs(stocksProfit, target):
    # Write your code here
    stocksProfit.sort()
    result = dict()
    for i in range(len(stocksProfit)-1,-1,-1):
        temp = stocksProfit[i] 
        if(temp>=target):
            continue 
        for j in range(0,i,1):
            data =stocksProfit[i]+stocksProfit[j] 
            if(data>target):
                break
            elif(data==target):
                result[temp] = 1
    return(len(result))

stocksProfit = [5, 7, 9, 13, 11, 6, 6, 3, 3]
target = 12 profit's target
타겟에 맞게끔 값찾기 7,5 5,7은 같은값이여서 ㄴㄴ
