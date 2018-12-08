import db
import datetime
# Add more calculations and create a seperate file for them for part 2
def get_average(hits, at_bats):
    try:
        return hits / at_bats
    except ZeroDivisionError:
        #although there are checks to make sure the user enters valid at bats value
        #if the file contains the error at read time an error would occur
        print("At bats can't be 0. Division by zero error.")
        return None

player_position = ("P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF")
double_dash_line = "=" * 64
dash_line = "-" * 64


def display_menu():
    print(double_dash_line)
    print("{:^64}".format("Chicago Cubs Baseball Team Manager"))
    print()

    game_date()

    print("MENU OPTIONS")
    print("1 - Display Lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")

def menu_selection():
    while True:
        try:
            selection = int(input("Menu Option: "))
            return selection
        except ValueError:
            print("You entered an invalid integer. Please try again")


def display_lineup(lineup):
    header = ("{:<6}{:<20s}{:^10s}{:^10s}{:^10s}{:^10s}".format(" ", "Player", "POS", "AB", "H", "AVG"))
    player = 0
    print(header)
    print(dash_line)
    for i in lineup:
        player += 1
        if int(i["at_bats"]) == 0:
            average = 0.000
        else:
            average = get_average(float(i['hits']), float(i['at_bats']))

        print('{:<6}{:<20s}{:^10s}{:^10}{:^10s}{:^10.3f}'.format(player, i["name"], i["position"], i["at_bats"],
                                                                  i["hits"], average))


def add_player(lineup):
    player_name = input("Player Name:\t")

    position = input("Position:\t")
    while position not in player_position:
        print("Please choose a valid position")
        position = input("Position:\t")

    at_bats = int(input("At bats:\t"))
    while at_bats < 0:
        print("Can't have negative at bats.")
        at_bats = int(input("At bats:\t"))

    hits = int(input("Hits:\t"))
    while hits > at_bats or hits < 0:
        print("Can't have more hits than at bats.")
        hits = int(input("Hits:\t"))

    player = {}
    player["name"] = player_name
    player["position"] = position
    player["at_bats"] = str(at_bats)
    player["hits"] = str(hits)
    lineup.append(player)
    db.write_players(lineup)
    print(player_name + " was added.")


def remove_player(lineup):
    player_number = int(input("What player (by number) would you like to delete:\t"))
    while player_number > len(lineup) or player_number < 1:
        print("Select a player number from the lineup.")
        player_number = int(input("What player (by number) would you like to delete:\t"))
    removed_player = lineup.pop(player_number - 1)
    print(removed_player["name"] + " was removed from the lineup")
    db.write_players(lineup)


def move_player(lineup):
    player_number1 = int(input("Which player (by number) would you like to move:\t"))
    while player_number1 > len(lineup) or player_number1 < 1:
        print("Select a player number from the lineup.")
        player_number1 = int(input("Which player (by number) would you like to move:\t"))

    new_position = int(input("What position would you like to move the player to:\t"))
    while new_position == player_number1 or new_position > len(lineup) or new_position < 1:
        print("Select a player number from the lineup.")
        new_position = int(input("What position would you like to move the player to:\t"))

    player = lineup.pop(player_number1 - 1)
    lineup.insert(new_position - 1, player)
    print(lineup[new_position - 1]["name"] + " was moved")
    db.write_players(lineup)


def edit_position(lineup):
    player = int(input("Which players position is changing:\t"))
    while player > len(lineup) or player < 1:
        print("Select a player number from the lineup.")
        player = int(input("Which players position is changing:\t"))

    position = input("What is the new position:\t")
    while position not in player_position:
        print("Please choose a valid position")
        position = input("Position:\t")

    lineup[player - 1]["position"] = position
    print(lineup[player - 1]["name"] + " position was changed to " + position)
    db.write_players(lineup)


# finish last two menu options
def edit_stats(lineup):
    player = int(input("Select a player to update stats:\t"))
    print("You selected " + lineup[player - 1]["name"])

    at_bats = int(input("What is the new number of at bats:\t"))
    while at_bats < 0:
        print("Please enter a non negative number of at bats")
        at_bats = int(input("What is the new number of at bats:\t"))

    hits = int(input("What is the new number of hits:\t"))
    while hits > at_bats or hits < 0:
        print("Please enter a number equal to or less than the number of at bats")
        hits = int(input("What is the new number of hits:\t"))

    lineup[player - 1]["at_bats"] = str(at_bats)
    lineup[player - 1]["hits"] = str(hits)

    print("New stats for " + lineup[player - 1]["name"] + ":\tAB - " + lineup[player - 1]["at_bats"] +
          "\t H - " + lineup[player - 1]["hits"])
    db.write_players(lineup)

def game_date():
    valid_date = False
    todays_date = datetime.date.today()
    print("Current Date:\t\t", todays_date)
    user_date = (input("Game Date:\t\t"))
    if user_date == '':
        return

    while not valid_date:
        try:
            game_day = datetime.date(int(user_date[0:4]), int(user_date[5:7]), int(user_date[8:]))
            valid_date = True
        except ValueError:
            print("Enter a valid date.")
            user_date = (input("Game Date:\t\t"))
            if user_date == '':
                return

    days_until = int((game_day - todays_date).days)
    if days_until > 0:
        print("Days until game:\t" + str(days_until))

