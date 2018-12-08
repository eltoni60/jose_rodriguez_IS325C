import csv

FILENAME = "players.txt"

def read_players():
    try:
        players = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                player = {}
                player["name"] = row[0]
                player["position"] = row[1]
                player["at_bats"] = row[2]
                player["hits"] = row[3]
                players.append(player)
        return players
    except FileNotFoundError:
        return None

def write_players(players):
    with open(FILENAME, "w") as file:
        for player in players:
            file.write(player["name"] + ",")
            file.write(player["position"] + ",")
            file.write(player["at_bats"] + ",")
            file.write(player["hits"] + "\n")

