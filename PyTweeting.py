
import tweepy
auth = tweepy.OAuthHandler('DJ3yOjQhddvAMkhDffs85kmfR','yIw8OWpdoAOL167xpRBgpRtkBgHA7CuQQlI3M5DD2CFBNBnkuk')

auth.set_access_token('1166597179135471621-CtRH6kHoxYecyKlI0xOI7PeGV9lHAR','XaCGjngj88Ed6AZEnYh22mZLrFGCAI1RSaBV6XftO3rQG')

api = tweepy.API(auth)

api.update_status("Tweepy automated Tweet.")
