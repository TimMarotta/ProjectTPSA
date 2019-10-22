# @Author   Timothy Marotta
# @Date     October 21, 2019
# NOTE: Twython documentation is provided here: https://twython.readthedocs.io/en/latest/

from twython import Twython

# TODO hide API keys to allow public Git repository
APP_KEY = 'nVVvc5Ip48FRXmX1zd0fjyE9p'
APP_SECRET = 'Ya0EJufgblAgeYan1wiB91UEHaL0fQGracAxT17LORnN47Iruy'

set_twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = set_twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

results = twitter.cursor(twitter.search, q='python', lang='en', count=100)
for result in results:
    print(result)
