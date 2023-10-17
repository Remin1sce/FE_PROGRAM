def find_winning_team(scores):
    winning_team = None
    min_scores = [min(team_scores) for team_scores in scores]
    max_min_score = max(min_scores)
    winning_team_index = min_scores.index(max_min_score)
    winning_team = f"Team {winning_team_index + 1}"
    return winning_team

# Read input
N = int(input())
M = int(input())

scores = []
for _ in range(N):
    team_scores = list(map(int, input()))
    scores.append(team_scores)

# Find and print the winning team
winning_team = find_winning_team(scores)
print(winning_team)