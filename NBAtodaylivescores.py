from bs4 import BeautifulSoup
import requests

url = 'https://www.cbssports.com/nba/scoreboard/20240204/'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# Find all elements with the class "single-score-card"
score_cards = soup.find_all('div', class_='single-score-card')

# Iterate through each score card
for score_card in score_cards:
    # Extract team names
    teams = score_card.find_all('a', class_='team-name-link')
    team1 = teams[0].text.strip()
    team2 = teams[1].text.strip()
    
    

    # Extract scores if available, otherwise set to "TBD"
    scores = score_card.find_all('td', class_='total')
    score1text = scores[0].text.strip() if scores else "TBD"
    score2text = scores[1].text.strip() if scores else "TBD"

    score1 = int(score1text)
    score2 = int(score2text)

    if score1 > score2:
        winner = team1
    elif score2 > score1:
        winner = team2
    else:
        winner = "TBD"

    # Print the results
    print(f"{team1}: {score1}")
    print(f"{team2}: {score2}")
    print("Team in lead/Winner : ",winner)
    print("\n")
