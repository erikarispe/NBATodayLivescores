from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template
from datetime import date

#http://127.0.0.1:5000/  flask url

app = Flask(__name__)

today = date.today()
formatted_date = today.strftime('%B %d, %Y')



url = 'https://www.cbssports.com/nba/scoreboard/'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

score_cards = soup.find_all('div', class_='single-score-card')

# Initialize variables
teams = []
scores = []
winners = []

# Iterate through each score card
for score_card in score_cards:
    # Extract team names
    teams_data = score_card.find_all('a', class_='team-name-link')
    team1 = teams_data[0].text.strip()
    team2 = teams_data[1].text.strip()

    # Extract scores if available, otherwise set to "TBD"
    scores_data = score_card.find_all('td', class_='total')
    score1 = int(scores_data[0].text.strip()) if scores_data else "TBD"
    score2 = int(scores_data[1].text.strip()) if scores_data else "TBD"

    if score1 > score2:
        winner_data = team1
    elif score2 > score1:
        winner_data = team2
    else:
        winner_data = "TBD"

    # Append data to lists
    teams.append({'team1': team1, 'team2': team2})
    scores.append({'score1': score1, 'score2': score2})
    winners.append(winner_data)

    

# Route to render the template
@app.route('/')
def index():
    return render_template('basketballscores.html', teams=teams, scores=scores, winners=winners, formatted_date=formatted_date)
if __name__ == '__main__':
    app.run(debug=True)
