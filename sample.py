def get_score(player_scores):
    min_score = float('inf')
    for score in player_scores:
        if score < min_score:
            min_score = score
    return min_score

def main():
    n = int(input())  # Number of teams
    m = int(input())  # Number of players per team
    
    # Initialize variables for tracking the winning team and highest score
    winning_team = 0
    highest_score = 0
    
    # Iterate through each team
    for i in range(n):
        for j in range(m):
            player_scores = list(map(int, input()))
            team_score = get_score(player_scores)
            if team_score > highest_score:
             highest_score = team_score
            winning_team = i + 1
    
    print(f"The winning team is Team {winning_team} with a score of {highest_score}")

if __name__ == "__main__":
    main()