from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
from nba_api.stats.static import teams
import json
##############################
##############################
##############################


def build_lists(player_ID):
    player_info = commonplayerinfo.CommonPlayerInfo(player_ID)
    # Dictionary with three keys(CommonPlayerInfo, PlayerHeadlineStats, AvailableSeasons)
    D = player_info.get_normalized_dict()
    return (D)
##############################
##############################
##############################


def get_player_stats(D):
    stats_list = D["PlayerHeadlineStats"]
    return (stats_list)
##############################
##############################
##############################


def get_player_info(D):
    info_list = D["CommonPlayerInfo"]
    return (info_list)
##############################
##############################
##############################


def get_league_leaders():
    # Open the json file
    with open("/Users/aryanverma/Documents/Projects/NBAstats/playerinfo.json") as f:
        data = json.load(f)
    # Establish the lists
    ppg_list = []
    rpg_list = []
    apg_list = []
    x = 0
    # Player Stats Dictionaries
    for D1 in data:
        ID = D1["id"]
        is_active = D1["is_active"]
        player_info = commonplayerinfo.CommonPlayerInfo(ID)
        D = player_info.get_normalized_dict()
        stats_list = D["PlayerHeadlineStats"]
        print("STATS LIST: ", stats_list)
        if is_active == True:
            for player in stats_list:
                print("CAME HERE")
                player_points = player["PLAYER_NAME"], player["PTS"]
                player_rebounds = player["PLAYER_NAME"], player["REB"]
                player_assists = player["PLAYER_NAME"], player["AST"]
                ppg_list.append(player_points)
                rpg_list.append(player_rebounds)
                apg_list.append(player_assists)
                x += 1
            if x == 10:
                break
    ppg_list = sorted(ppg_list, key=lambda x: x[1], reverse=True)
    rpg_list = sorted(rpg_list, key=lambda x: x[1], reverse=True)
    apg_list = sorted(apg_list, key=lambda x: x[1], reverse=True)
    # return (ppg_list, rpg_list, apg_list)
    return ppg_list
##############################
##############################
##############################


def main():
    # Menu options for the program
    MENU = '''Menu options
    
    1) Look up specific player's stats
    2) Look up specific player's information
    3) Look up league leaders
    4) Quit
    
    Enter choice: '''
    print()
    choice = input(MENU)
    # As long as the user doesn't quit
    while choice != '4':
        # PlayerHeadlineStats
        if choice == '1':
            full_name = input("Enter a NBA player's full name: ")
            full_name_new = full_name.strip().lower().split()
            print()
            with open("/Users/aryanverma/Documents/Projects/NBAstats/playerinfo.json") as f:
                data = json.load(f)
            for D in data:
                D_ID = D["id"]
                D_name = D["full_name"]
                D_name_new = D_name.strip().lower().split()
                if full_name_new == D_name_new:
                    # Player Stats
                    player_info = commonplayerinfo.CommonPlayerInfo(D_ID)
                    stats_list = player_info.get_normalized_dict()[
                        "PlayerHeadlineStats"]
                    for L in stats_list:
                        for key, value in L.items():
                            key = str(key).strip()
                            value = str(value).strip()
                            print(key, ":", value)
            print()
        # CommonPlayerInfo
        elif choice == '2':
            full_name = input("Enter a NBA player's full name: ")
            full_name_new = full_name.strip().lower().split()
            print()
            with open("/Users/aryanverma/Documents/Projects/NBAstats/playerinfo.json") as f:
                data = json.load(f)
            for D in data:
                D_ID = D["id"]
                D_name = D["full_name"]
                D_name_new = D_name.strip().lower().split()
                if full_name_new == D_name_new:
                    # Player Stats
                    player_info = commonplayerinfo.CommonPlayerInfo(D_ID)
                    info_list = player_info.get_normalized_dict()[
                        "CommonPlayerInfo"]
                    for L in info_list:
                        for key, value in L.items():
                            key = str(key).strip()
                            value = str(value).strip()
                            print(key, ":", value)
            print()
        # League leaders
        elif choice == '3':
            top_five = 0
            ppg_leader, rpg_leader, apg_leader = get_league_leaders()
            # PPG Leaders
            print("{:>15s}".format("POINTS"))
            print("{:>23s}".format("--------------------"))
            for T1 in ppg_leader:
                print(T1)
                top_five += 1
                if top_five == 5:
                    break
            print()
            # # RPG Leaders
            # print("{:>15s}".format("REBOUNDS"))
            # print("{:>23s}".format("--------------------"))
            # for T2 in rpg_leader:
            #     print(T2)
            #     top_five += 1
            #     if top_five == 5:
            #         break
            # print()
            # # APG Leaders
            # print("{:>15s}".format("ASSISTS"))
            # print("{:>23s}".format("--------------------"))
            # for T3 in apg_leader:
            #     print(T3)
            #     top_five += 1
            #     if top_five == 5:
            #         break
            # print()
        # If user enters a option that doesn't exist
        else:
            print("Invalid option. Please try again! ")
        # Re-promt the user
        choice = input(MENU)
    # Closing message
    print("Thanks for using this program, have a nice day.")


if __name__ == "__main__":
    main()
