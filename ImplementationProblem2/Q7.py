n=7755

s=str(n)
length=len(s)
left_sum=0
right_sum=0
for i in range(length//2):
    left_sum+=int(s[i])
for i in range(length//2,length):
    right_sum+=int(s[i])

if left_sum==right_sum:
    print("LUCKY")
else:
    print("READY")