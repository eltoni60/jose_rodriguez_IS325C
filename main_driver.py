import menu_options #function for each menu selection
import db   #Functions to read and write to files
import datetime

def main():
    #read the file into a list of list and check for file not found
    lineup = db.read_players()
    if lineup == None:
        print("The file was not found.")
        return 0


   #Display the menu selection to the user
    menu_options.display_menu()
    print()
    print("POSITIONS\n" + str(menu_options.player_position))
    print(menu_options.double_dash_line)
    #Ask user for initial menu selection to enter the loop
    menu_selection = menu_options.menu_selection()
    #Loop that goes through the user's menu selection until exit is selected
    while menu_selection != 7:

        if menu_selection == 1:
            menu_options.display_lineup(lineup)
        elif menu_selection == 2:
            menu_options.add_player(lineup)
        elif menu_selection == 3:
            menu_options.remove_player(lineup)
        elif menu_selection == 4:
            menu_options.move_player(lineup)
        elif menu_selection == 5:
            menu_options.edit_position(lineup)
        elif menu_selection == 6:
            menu_options.edit_stats(lineup)
        else:
            print("Please select a valid menu options")
        #ask the user to select another option from the menu
        print()
        menu_selection = int(input("Menu Option: "))




if  __name__ == "__main__":
    main()