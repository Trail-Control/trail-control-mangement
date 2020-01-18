import requests
from requests_oauthlib import OAuth1
import json

consumer_key = 'Ommit'
consumer_secret='Omit'

token='Omit'
token_secret='Omit'

twitter_user ='KcTrailsStatus'

URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count=100'.format(twitter_user)
auth = OAuth1(consumer_key, consumer_secret, token, token_secret)


def submit_tweets(trail_org, tweets):
    jdump = {
        trail_org: tweets
    }
    print(jdump)


if __name__ == '__main__':
    res =requests.get(URL, auth=auth)

    results = []
    if res.status_code == 200:

        try:
            deserialized = json.loads(res.content)
            for status in deserialized:
                try:
                    id = status['id']
                    trail = status['entities']['hashtags'][0]['text']

                    posted = status['created_at']
                    results.append({
                        "tweet_id": id,
                        "trail_name": trail,
                        "posted_date": posted
                    })
                except Exception as deserialize_fail:
                    print('Failed to get data from tweet')
                    print(status)
                    print(deserialize_fail)

        except Exception as e:
            print('Response from twitter was not json object')
            print(e)
    else:
        print('Request for trail statuses was not successful')
        print(res.status_code)
        print(res.content)

    submit_tweets(twitter_user, results)



