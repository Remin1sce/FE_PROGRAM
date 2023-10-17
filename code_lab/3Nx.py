n = int(input())
m = int(input())
maxScore = None
winTeam = None
for i in range(1,n+1):
  minScore = None
  for j in range(m):
    s = int(input())
    if minScore == None or s < minScore:
      minScore = s
  if maxScore == None or minScore > maxScore:
    maxScore = minScore
    winTeam = i
print("Team",winTeam)