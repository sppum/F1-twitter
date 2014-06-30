"""
We need to be able, to start with at least, to:

    * Read timeline
    * Know the season (parse F1 website)
    * Know who is playing
    * Prompt for quali / win ahead of first practice
    * Accept responses, not allow responses after first practice has started (allow admin override)
    * Parse the F1 website for winners / poles etc, maintain list in db?
    * Work out the score after quali / race
    * Update people after the result? Accept questions about scores etc
    * Tell the winner / loser / all people the result at the end of the season

"""

try:
    from twitter import *

except Exception, e:
    print "Could not import the twitter module %s", e

# Some classes

class Tweet(object):
    def __init__(self, twitterHandle, tweetType, tweetContent):
        self.handle = twitterHandle
        self.tweetType = tweetType
        self.tweetContent = tweetContent

class User(object):
    def __init__(self, name, twitterHandle, ladderScore, ladderPosition):
        self.name = name
        self.twitterHandle = twitterHandle
        self.ladderScore = ladderScore
        self.ladderPosition = ladderPosition

