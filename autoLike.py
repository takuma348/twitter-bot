# coding: utf-8
import tweepy
import time
import sys
from datetime import datetime

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

# 関数群
def searchTweets(query):
 tweets = api.search(q=query, count=100)
 return tweets

def likeTweets(tweets):
    like_count = 0
    created_at = datetime.now().strftime("%Y%m%d%H%M%S")
    for tweet in tweets:
        user_id = tweet.user._json['screen_name']
        tweet_id = tweet.id
    try:
        api.create_favorite(tweet_id) #フォロワーでなければいいねする
        print("{}:[INFO]以下のユーザーをいいねしました。user_id:{}".format(created_at, user_id))
        like_count += 1
        print("[INFO]いいね数: {}".format(like_count))
    except Exception as e:
        print("[EEROR]いいねに失敗しました: {}".format(e))
        if e.response and e.response.status == 429:
           print("[INFO] rate limit の上限値を超えたので、15分待機後に実行します")
           time.sleep(60 * 15)
        if e.response and e.response.status == 139:
           print("[ERROR] すでにいいねをしているツイートです。")
    return like_count

if __name__ == '__main__':
   #Tweepy
   auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
   auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
   #APIインスタンスを作成
   api = tweepy.API(auth)
   #引数を受け取る
   args = sys.argv
   query = args[1] #中身がhoge
   #いいねする
   tweets =  searchTweets(query)
   likeTweets(tweets)
