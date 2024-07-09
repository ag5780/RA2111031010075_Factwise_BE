def maxS(arr,k):
    t=sum(arr)
    n=len(arr)
    window=sum(arr[:k])
    max_sum=window
    for i in range(k):
        window+=arr[n-1-i]-arr[k-1-i]
        max_sum=max(max_sum,window)
    return max_sum
print("Card pointers array:")
Card=list(map(int,input("Points: ").strip().split()))
k=int(input("K:"))
print("Output;",maxS(Card,k))