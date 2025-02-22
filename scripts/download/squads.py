import requests
import os
import json

with open("data/tournaments.json", "r") as tournaments_file:
    for line in tournaments_file.readlines():
        document = json.loads(line)
        short_name = document["shortName"]
        year = document["year"]
        print(short_name)
        if short_name == "france2019":
            for team in document["teams"]:
                print(team)
                tournament_dir = f"data/raw/tournaments/{short_name}/squads/"
                if not os.path.isdir(tournament_dir):
                    os.makedirs(tournament_dir, exist_ok=True)
                location = f"{tournament_dir}/{team['id']}.html"
                if not os.path.exists(location):
                    response = requests.get(f"https://www.fifa.com/womensworldcup/teams/team/{team['id']}/")
                    with open(location, "w") as squad_file:
                        squad_file.write(response.text)
        else:
            for team in document["teams"]:
                print(team)
                tournament_dir = f"data/raw/tournaments/{short_name}/squads/"
                if not os.path.isdir(tournament_dir):
                    os.mkdir(tournament_dir)
                location = f"{tournament_dir}/{team['id']}.html"
                if not os.path.exists(location):
                    response = requests.get(f"https://www.fifa.com/womensworldcup/archive/edition={year}/library/teams/team={team['id']}/_players/_players_list.html")
                    with open(location, "w") as squad_file:
                        squad_file.write(response.text)
