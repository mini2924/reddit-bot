import rlcompleter
import readline
import praw
import time
readline.parse_and_bind("tab: complete")

reddit = praw.Reddit(client_id='bS2mYttUbvze4w',
                     client_secret='7vFV5JAPk8RUZjlQs-2AiI6Hd68',
                     username='Mini_2924_Bot',
                     password='keelan29"',
                     user_agent='sub4sub')

subreddit = reddit.subreddit('Sub4Sub')

post_rate = 1.5
while True:
    for comment in subreddit.stream.comments():
        if 'sub' in comment.body:
            try:
                reply = 'hAvE YoU tRiEd sUbScrIbInG to Mini 2924 by clicking this link: https://www.youtube.com/channel/UCQK_6FsLU3m32z0GbFal6zg'
                comment.reply(reply)
                print('reply has been posted')
            except:
                print('too frequent')
                time.sleep(post_rate)
        time.sleep(post_rate)
