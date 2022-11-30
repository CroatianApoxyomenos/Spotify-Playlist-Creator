# Spotify Playlist Creator
using Billboard Top 100 web scraping
## Installation
First run in your console `pip install -r requirements.txt`
## First use
If you don't already have a Spotify account, you can sign up at: http://spotify.com/signup/ and create a new Spotify App at: https://developer.spotify.com/dashboard/. 

Here you will find your CLIENT ID and CLIENT SECRET codes which you will need further. At this step, go to edit settings and set the _redirect URI_ to http://example.com.

When you run the script, you will be prompted to input the CLIENT codes and afterwards you will be redirected to an URL where you will be asked to agree to Spotify's terms of service. Copy this URL and enter in the console.
## Enjoy
You will only be asked once to enter the CLIENT codes and to agree to Spotify's TOS. If you change the Spotify account, you have to delete the newly created `config.json` and `token.txt` files and redo the steps for the first use of this script.

![test_pic](https://user-images.githubusercontent.com/107721907/204844141-345287f4-5ca6-47f8-9ed3-d3884855ed9b.jpg)
