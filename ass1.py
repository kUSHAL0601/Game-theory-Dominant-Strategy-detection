import math

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
n_players=min(n_players,len(n_actions))
n_actions=[0]+n_actions
input()
payoffs=list(map(float,input().split()))

# payoffs_2d=[]
# for i in range(len(payoffs)//n_players):
#     payoffs_2d.append([])
#     for j in range(n_players):
        # payoffs_2d[i]/.append(payoffs[n_players*i+j])
# print(payoffs_2d)

step_size=[0]*(n_players+1)
step_size[1]=n_players
for i in range(2,n_players+1):
        step_size[i]=step_size[i-1]*n_actions[i-1]
max_len=len(payoffs)
payoffs=[0]+payoffs
# print(step_size)
# print(max_len)

def get_dominant_strategy(player_idx):
    idx_flag={}
    action_count={}
    dominant_strats=[]
    for j in range(player_idx,max_len+1,n_players):
        ans=-math.inf
        if j not in idx_flag:
            x=j
            action=1
            while action<=n_actions[player_idx] and x<=max_len:
                idx_flag[x]=1
                ans=max(ans,payoffs[x])
                action+=1
                x+=step_size[player_idx]
            x=j
            action=1
            while action<=n_actions[player_idx] and x<=max_len:
                if payoffs[x]==ans:
                        try:
                            action_count[action]+=1
                        except:
                            action_count[action]=1
                action+=1
                x+=step_size[player_idx]
    for action in range(1,n_actions[player_idx]+1):
        try:
            if action_count[action]==max_len/(n_players*n_actions[player_idx]):
                dominant_strats.append(action)
        except:
            pass
    if not len(dominant_strats):
        print("No dominant strategies for Player",player_idx)
    else:
        print("Dominant strategies for Player",player_idx,*dominant_strats)
    return dominant_strats,action_count

dominant_strategies={}
action_counts={}
flag=False
for p in range(1,n_players+1):
    dominant_strategies[p],action_counts[p]=get_dominant_strategy(p)
    print(dominant_strategies[p],action_counts[p])
    if not len(dominant_strategies[p]):
        flag=True