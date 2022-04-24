import spotipy
import json
import webbrowser
import requests

#NO NEED TO CHANGE
TRACK_URL = "https://api.spotify.com/v1/me/player"
#TODO, NO  NEED TO CHANGE YET
QUEUE_URL = "https://api.spotify.com/v1/me/player/queue"

#ENTER YOUR ACCESS TOKEN FOR QUEUE AND TRACK FROM:
#https://developer.spotify.com/console/post-queue/
#https://developer.spotify.com/console/get-user-player/?market=&additional_types=
ACCESS_TOKEN_QUEUE = "REPLACE WITH YOUR ACCESS TOKEN FOR QUEUE"
ACCESS_TOKEN_TRACK = "REPLACE WITH YOUR ACCESS TOKEN FOR TRACK"

#NOT IMPLEMENTED YET
def req_track(access_token):
    response = requests.get(
        QUEUE_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

#RETURNS CURRENT TRACK AND ARTIST
def get_current_track(access_token):
    response = requests.get(
        TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    resp_json = response.json()
    track_name = resp_json["item"]["name"]
    artists = resp_json["item"]["artists"]
    artist_name = ", ".join([artist["name"] for artist in artists])

    curr_track_info = {
        "name": track_name,
        "artists": artist_name
    }
    return curr_track_info

# DEFAULT WELCOME MESSAGE FOR USER
def welcome_message():
    print("Welcome ", user["display_name"], " to Play-a-Song!")
    curr_track_info = get_current_track(ACCESS_TOKEN_TRACK)
    print("Current song playing: ", curr_track_info["name"], "by", curr_track_info["artists"])
    print(f"-" * 55,"\n")
    print("Please enter from the following options:")
    print("0 - Exit")
    print("1 - Play-a-Song!")

def find_song():
    search = input("Enter Song Name: ")
    result = spotifyObject.search(search,1,0,"track")
    tracks = result["tracks"]
    tracks_items = tracks["items"]
    song = tracks_items[0]["external_urls"]["spotify"]
    webbrowser.open(song)
    print(f"[{search}] -", song, "- has opened in your browser!")

# ENTER YOUR PERSONAL USER INFO (FOUND ON SPOTIFY DEVELOPER)
username = "REPLACE WITH YOUR USERNAME"
clientID = "REPLACE WITH YOUR CLIENTID"
clientSecret = "REPLACE WITH YOUR CLIENTSECRET"

# YOU MAY KEEP THIS THE SAME, MAKE SURE TO ADD REDIRECTURI in YOUR DEVELOPER SETTINGS
redirectURI = "http://google.com/"

oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
token_dict = oauth_object.get_cached_token()
token = token_dict["access_token"]

spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

#YOU CAN LEAVE THE PRINT STATEMENT COMMENTED, UNLESS YOU WANT TO DISPLAY USER INFO
#print(json.dumps(user, sort_keys=True, indent=2))

welcome_message()

while True:
    selection = int(input())
    if selection == 0:
        print("Thanks for using Play-a-Song! See you next time!")
        break
    elif selection == 1:
        print(f"-" * 55,"\n")
        find_song()
        print("Thanks for using Play-a-Song! See you next time!")
        break
    else:
        print(f"-" * 55,"\n")
        print("Please enter from the following options:")
        print("0 - Exit")
        print("1 - Play-a-Song!")

