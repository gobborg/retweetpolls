# retweetpolls
A script to retweet your polls at a set time- great for visibility across timezones.
---

Do you live in not North America? Are you disappointed that your banger polls get low engagement because the Americans and Canadians are sleeping?
Do you live in the Americas, but you're disappointed by east/west coast time differences (let's face it- no one lives in the middle)?
I have a solution for you: a retweet polls script.
Simply set a cronjob to run this script at whatever time the North Americans are awake and on Twitter with relation to the local time of the machine on which you're hosting the cronjob and python script. 9PM EDT seems like a good time to post to Twitter.

You need:
* a cronjob
* Python 3 (I wrote the script in Python3.9.6)
* to figure out the time difference between your timezone and whatever time of day you want the Americans to see your polls
* Twitter API access keys from developer.twitter.com

I host my cronjobs for Twitter in a virtual machine so that it is constantly running.

Gratitudes and acknowledgements:
* Big thanks to Igor Brigadir's documentation https://github.com/igorbrigadir/twitter-advanced-search
* The for loop basis was taken from https://github.com/0xGrimnir/Simple-Retweet-Bot/blob/master/retweet.py

Limitations:
* This will not work for media polls. As of now, you have to pay for those anyway at ads.twitter.com

Instructions:
* You can copy/paste your API keys directly into the retweetpolls.py file, or you can import them like I do. I have my import file set up as keys.py, and it contains:
    Consumer_API_key = 'REDACTED'  
    Consumer_API_secret_key = 'REDACTED'  
    Bearer_token = 'REDACTED'  
    Access_token = 'REDACTED'  
    Access_secret = 'REDACTED'  
* Change the Advanced Search operators to whatever you want them to be.
* Set up your cronjob.
