# tscjhair-attack
Shaina Peters: Project manager, database professional, spotify editor
Terry Guan: Machine learning algorithm, generating data and images
Caleb Smith-salzberg: Getty Images and Clarifai API master, app.py routing technician
Jennifer Zhang: Front end developer, AJAX (not Achilles) and JS user


## What it is

This project is a site that gives the user a list of five art mediums, and the user can select which ones they like and don't like. Based on the user's selections, more art pieces are chosen with machine learning, and the more the user says what they like and dislike, the more accurate the options given to the user get.

## How to run

Enter a virtualenv if you wish, and run `python app.py`
Go to the main page, create an account, and select the art medium you like (music, visual art/images)
Start selecting images/music you like/dislike! Submit your results and repeat. Based on your inputed likes/dislikes, we return images/music we think you might like.

If you would like to see an account where machine learning has processed some data, use the following sample account:
Username: sample
Password: sample

### API keys

API keys should be in a file called credentials.txt inputed as such:

```
Spotify:<KEY>
Clarifai:<KEY>
GettyImages:<KEY>
***NOTE: no space between name of API and <KEY>
```

## Dependancies

  * flask
  * requests
  * clarifai
  * spotipy

`pip install -r requirements.txt`
if this fails, run `pip install <package name>` where package name is the individual package names listed above
