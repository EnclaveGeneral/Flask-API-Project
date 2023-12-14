import time
import requests, json
from pprint import pprint

Application_ID = "64d0eef050264d0d12f4752bd2989997"

def getUserID(username):
  baseURL = "https://api.worldofwarships.com/wows/account/list/"
  params = {"application_id": Application_ID,
            "search": username}
  try:
     print("Establishing Connection......")
     res = requests.get(baseURL, params=params)
     res = res.json()
     if (res["status"] != "ok"):
        return "Invalid User Input"
     else:
        account_ID = res["data"][0]["account_id"]
        return account_ID
  except:
     return None

def getPlayerData(username):
    res = getUserID(username)
    if res is None:
       print("Server Connection Failure!")
    elif res == "Invalid User Input":
       print("Invalid User Input")
    else:
       playerID = res
       baseURL = "https://api.worldofwarships.com/wows/account/info/"
       try:
          print("Establishing Connection......")
          params = {"application_id": Application_ID,
                    "account_id": playerID,
                    "extra": "statistics.pvp_solo"}
          res = requests.get(baseURL, params=params)
          res = res.json()
          if res["status"] != "ok":
             print("Invalid Input")
          else:
             statistics = res["data"][str(playerID)]["statistics"]
             print("Total Number of Battles: " + str(statistics["battles"]))
             time.sleep(2)
             print("Total distance sailed (Nautical Miles): " + str(statistics["distance"]))
             time.sleep(2)
             losses = float(statistics["pvp"]["losses"])
             battles = float(statistics["pvp"]["battles"])
             winrate = 100 - (losses/battles * 100)
             print("Current PVP Winrate: " + str(winrate) + "%")
             time.sleep(2)
             pprint(statistics)
       except:
          return "Server Connection Failure!"



def main():
  print("Welcome to WOWs Stats Simulator!")
  user = input("Enter Username Here: ")
  user.strip()
  getPlayerData(user)
  # Induced and paused time interval to eliminate the possibility of API Overload.
  time.sleep(1)
  again = input("Do you want to search another user? ")
  again.lower()
  again.strip()
  if (again == "yes"):
     main()
  else:
     print("Thank you for using this product! We will be implementing front end in the near future!")

  #Call The Api Function Here

if __name__ == "__main__":
    try:
        main()
    except (NameError, SyntaxError):
        # pass does "nothing" - it is useful if you are trying to nothing in your code,
        # but still need a line to avoid a syntax error
        pass