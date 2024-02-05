#this uses a url from CBS that shows the scoreboard of games for the present day.
#The output will show the matchup, along with the current scores, and show who is winning/won the game.
#if the game/games have not started, the scores will have a placeholder of TBD, once they have started the scores will be present.

from bs4 import BeautifulSoup
import requests

url = 'https://www.cbssports.com/nba/scoreboard/'
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
    score1 = scores[0].text.strip() if scores else "TBD"
    score2 = scores[1].text.strip() if scores else "TBD"

    if score1 or score2 == "TBD":
        winner = "TBD"
    elif score1 > score2:
        winner = team1
    else:
        winner = team2

    # Print the results
    print(f"{team1}: {score1}")
    print(f"{team2}: {score2}")
    print("Team in lead/Winner : ",winner)
    print("\n")
