#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests
import pandas as pd

# Define our "base" API
generalAPI = "https://fantasy.premierleague.com/api/bootstrap-static/" # this will never change regardless of the lookup we perform

def main():
    """Run time code"""

    # create resp, which is our request object
    genResp = requests.get(f"{generalAPI}")   # this "f" string reads: API + "total_players"
                                                # OR, https://api.magicthegathering.io/v1/sets

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    #print( dir(resp) )
    #print( resp.json().get("teams") )
    teamsData = genResp.json().get("teams")
    print("FPL Teams:\n")
    for team in teamsData:
        print(team.get("name"))

    print("\n")

    ###########################
    playerData = genResp.json().get("elements")
    #print("FPL Players:\n")

    df = pd.DataFrame([])
    ind = 1
    for player in playerData:
        if player.get("in_dreamteam"):
            #print( player.get("first_name") + " " + player.get("second_name") )
            #print( "In Dreamteam: True"  )
            #print( "Form: " + str(player.get("form")) )
            #print("\n")
            df = df.append(pd.DataFrame(
                {"Firstname" : [player.get("first_name")],
                "Surname" : [player.get("second_name")],
                "Form" : [player.get("form")]},
                index=[ind]), ignore_index=True)
            
            ind = ind + 1

    print("\n\n")
    print(df)

if __name__ == "__main__":
    main()

