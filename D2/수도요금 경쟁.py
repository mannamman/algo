#수도요금 경쟁
T = int(input())
for i in range(1,T+1):
    A_fee,B_basic_fee,B_boundary,B_extra_fee,usage = map(int,input().split())
    over_L = usage-B_boundary
    if(over_L<0):
        over_L=0
    A = A_fee * usage
    B = B_basic_fee + (over_L) * B_extra_fee
    if(A>B):
        print("#{} {}".format(i,B))
    print("#{} {}".format(i,A))