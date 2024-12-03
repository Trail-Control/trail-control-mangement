import requests
from requests_oauthlib import OAuth1
import json
import os
from dateutil.parser import parse
from datetime import datetime

consumer_key = ''
consumer_secret=''

token='316884809-'
token_secret=''

twitter_user ='KcTrailsStatus'

URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count=100'.format(twitter_user)
auth = OAuth1(consumer_key, consumer_secret, token, token_secret)

os.environ['NO_PROXY'] = '127.0.0.1'

def submit_tweets(trail_org, tweets):
    jdump = {
        trail_org: tweets
    }
    print(jdump)
    r = requests.post('http://localhost:5000/api/v1/tweets/', json=jdump)
    if r.status_code == 201:
        print('Completed')
    else:
        print('Some sort of failure, code: ' + str(r.status_code) )


if __name__ == '__main__':
    res =requests.get(URL, auth=auth)


    results = []
    if res.status_code == 200:

        try:
            deserialized = json.loads(res.content)
            for status in deserialized:
                try:
                    id = status['id']
                    if len(status['entities']['hashtags']) > 0:
                        trail = status['entities']['hashtags'][0]['text']
                        trail_status = ''
                        if 'closed' in status['text'].lower():
                            trail_status = 'closed'
                        elif 'delayed' in status['text'].lower():
                            trail_status = 'delayed'
                        else:
                            trail_status = 'open'

                        posted = status['created_at']
                        date = datetime.strftime(parse(posted), '%Y-%m-%d %H:%M:%S')
                        results.append({
                            #"tweet_id": id,
                            "trail_name": trail,
                            "updated_date": date,
                            "status": trail_status
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



