from bs4 import BeautifulSoup
import requests

query = "footballers of African descent who played in the FIFA 2018 final and the Euro 2016 final?"

# query google and save all those top 'K' results
# eg:
results = [
    "https://en.wikipedia.org/wiki/Michy_Batshuayi",
    "https://en.wikipedia.org/wiki/Marcus_Rashford",
    "https://www.theguardian.com/football/ng-interactive/2018/jun/05/world-cup-2018-complete-guide-players-ratings-goals-caps",
    "https://bleacherreport.com/articles/2785862-why-france-are-carrying-africas-hopes-in-the-world-cup-final",
    "https://www.indiatoday.in/sports/fifa-world-cup-2018/story/world-cup-2018-final-french-players-proud-to-represent-africa-1286287-2018-07-15",
    "http://www.espn.com/espn/feature/story/_/id/23402874/world-cup-rank-espn-fc",
    "https://www.fifa.com/fifa-world-ranking/",
    "https://www.vox.com/2018/6/12/17356780/world-cup-2018-russia-teams-schedule-tickets",
    "https://www.sportskeeda.com/slideshow/10-active-footballers-who-changed-nationality-played-international-football"
    "https://www.quora.com/How-many-Muslim-players-does-the-French-national-football-team-have"]

for index, result in enumerate(results):
    with open('file_' + str(index) + '.txt', 'w+') as file:
        resp = requests.get(result)
        soup = BeautifulSoup(resp.text, 'html.parser')
        for ptag in soup.find_all('p'):
            para = ptag.get_text().strip()
            if para:
                file.write(para)
                file.write('\n')
