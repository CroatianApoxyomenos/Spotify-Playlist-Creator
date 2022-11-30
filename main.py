from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os

print("""
 #####  ######  ####### ####### ### ####### #     # 
#     # #     # #     #    #     #  #        #   #  
#       #     # #     #    #     #  #         # #   
 #####  ######  #     #    #     #  #####      #    
      # #       #     #    #     #  #          #    
#     # #       #     #    #     #  #          #    
 #####  #       #######    #    ### #          #    
 -------------------------------------------------
           PLAYLIST CREATOR - © HERMESX
\n""")

CLIENT_ID = ""
CLIENT_SECRET = ""


def initializeConfig():
    global CLIENT_ID, CLIENT_SECRET
    if os.path.exists("./config.json"):
        with open("./config.json", "r") as config:
            config_dict = json.load(config)
            CLIENT_ID = config_dict["client_id"]
            CLIENT_SECRET = config_dict["client_secret"]

    else:
        print("You will be asked this only once! If there are changes, "
              "you have to delete config.json and token.txt files and redo the steps!")
        new_client_id = input("Please insert CLIENT ID from SPOTIFY DEVELOPER DASHBOARD: ")
        new_client_secret = input("Please insert CLIENT SECRET from SPOTIFY DEVELOPER DASHBOARD: ")
        with open("./config.json", "w") as config:
            config.write(
                '{'
                f'"client_id": "{new_client_id}",'
                f'"client_secret": "{new_client_secret}"'
                '}'
            )
        initializeConfig()


initializeConfig()

date = input("\nWhich year do you want to travel to? Type the date in this specific format: YYYY-MM-DD: ")
year = date.split("-")[0]
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL).text

soup = BeautifulSoup(response, "html.parser")
print("\nScraping tracks from Billboard top 100 ...")
titles_list = [title.getText().split("\t")[9] for title in soup.select(selector="li ul li h3")]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="https://example.com/",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))
user = sp.current_user()
user_id = user["id"]

tracks_uris = []
print("Scraping tracks URIs from Spotify ...")
for track in titles_list:
    result = sp.search(q=f"track:{track} year:{year}", type="track")
    try:
        track_uri = result["tracks"]["items"][0]["uri"]
        tracks_uris.append(track_uri)
    except IndexError:
        print(f"{track} doesn't exist in Spotify. Skipped")

playlist = sp.user_playlist_create(user=f"{user_id}", name=f"Top 100 from year {year}", public=False)

playlist_id = playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=tracks_uris)

print(f"\nPlaylist for year {year} was created!\n"
      f"You can access it here: https://open.spotify.com/playlist/{playlist_id}")
