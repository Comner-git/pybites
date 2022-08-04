from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    feed_parse = feedparser.parse(FEED_URL)
    feed_entries = feed_parse.entries
    games = []
    for x in range(len(feed_entries)):
        games.append(Game(feed_entries[x].title,
                    feed_entries[x].link))
    return games
    pass
