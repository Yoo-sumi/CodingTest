n=1260
count=0

coin_types=[500,100,50,10]

for coin in coin_types:
    count += n//coin
    #a=n//coin
    #count+=a
    n%=coin

print(count) #동전의 개수는 6