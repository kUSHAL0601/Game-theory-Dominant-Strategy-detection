l1=input()
l2=input()
l2=l2.split('{')
l3=l2[1]
l3=l3.split('"')
n_players=(len(l3)-1)//2
players=[]
for i in range(2*n_players+1):
    if(i%2==1):
        players.append(l3[i])
n_actions=l2[2].split(' ')
n_actions.pop(0)
n_actions.pop(len(n_actions)-1)
n_actions=list(map(int,n_actions))
input()
payoffs=list(map(float,input().split()))
payoffs_2d=[]
for i in range(len(payoffs)//n_players):
    payoffs_2d.append([])
    for j in range(n_players):
        payoffs_2d[i].append(payoffs[n_players*i+j])
print(payoffs_2d)
