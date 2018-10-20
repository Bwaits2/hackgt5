# comments
# all posts
# hot?
import praw
import re
from .subreddits import NEUTRAL_SUBREDDIT_NAMES, DEMOCRAT_SUBREDDIT_NAMES, REPUBLICAN_SUBREDDIT_NAMES


reddit = praw.Reddit(client_id='U-vZKYv1CT1-jQ',
                     client_secret='olft-yTuAsOKO4Pm0cuXndsLX4I',
                     user_agent='sexywalrus123v1',)


def callAPI(party_name):
    final_string = ""

    for x in get_subreddits(party_name):
        subreddit = reddit.subreddit(x)
        hot = subreddit.hot(limit=3)

        for s in hot:
            if not s.stickied:
                cs = s.title
                cs = re.sub(r'^https?:\/\/.*[\r\n]*', ' ', cs, flags=re.MULTILINE)
                cs = re.sub('[^a-zA-z]+', ' ', cs)
                final_string += str(cs.encode("utf-8", errors='ignore'))
                final_string += " "
                comments = s.comments
                for c in comments:
                    if not c.stickied:
                        cs = c.body
                        cs = re.sub(r'^https?:\/\/.*[\r\n]*', ' ', cs, flags=re.MULTILINE)
                        cs = re.sub('[^a-zA-z]+', ' ', cs)
                        final_string += str(cs.encode("utf-8", errors='ignore'))

    return final_string.lower()


def get_subreddits(party_name):
    if party_name is "neutral":
        return NEUTRAL_SUBREDDIT_NAMES
    elif party_name is "democrat":
        return DEMOCRAT_SUBREDDIT_NAMES
    elif party_name is "republican":
        return REPUBLICAN_SUBREDDIT_NAMES
    else:
        return None


