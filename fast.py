import requests
import random

#Token: https://open.spotify.com/get_access_token?reason=transport&productType=web_player

x = 0
def follow():
  global x
  Bearer = "Bearer"
  username = input("[\x1B[32m>\x1B[0m] Username to Follow: ")
  with open("tokens.txt") as file:
      while (token := file.readline().rstrip()):
          headers = {'authorization': f"{Bearer} {token}"}
          r = requests.put(f"https://api.spotify.com/v1/me/following?type=user&ids={username}", headers=headers)
          x = x + 1
          if r.status_code == 204:
              print("Folowers: ", x)
          else:
            print("Error: ", r.status_code)
follow()
print("End")