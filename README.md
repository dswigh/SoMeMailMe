# Mail Me My Social Media follower count (SoMeMailMe)

TikTok only show data 60 days back in time. With this repo you can easily scrape your follower count, likes count, and posts count from TikTok; it also scrapes your instagram follower count, and automatically adds all this data to a csv file. If the code is run on a Sunday, it will also send you a weekly recap showing how these numbers have changed over the past week.

# How to use:
1. Clone this repository and create an environment containing the appropriate packages
2. Create new email to send yourself emails from, and set 'Allow less secure apps' to ON
    * https://realpython.com/python-send-email/
3. Import IH_scraper:
    1. Clone the Social-Media-Scraper repo, which can be found here: https://github.com/InfluencerHunters/Social-Media-Scraper 
    2. Place the folder in the root directory of this project and rename it as 'SocialMediaScraper'
    3. Put the following two lines at the top of scraper.py:
        * import sys
        * sys.path.append('SocialMediaScraper/src')
4. Get a free token for Social-Media-Scraper at www.influencerhunters.com
5. Place SoMe_data.csv in the parent folder
6. To run the main function copy the following into the terminal:
    * python SoMeMailMe.py <tt_id>, <ig_id>, <token> <sender_email> <receiver_email>
    * e.g. python SoMeMailMe.py 'thecuriouschemist' 'the_curious_chemist' 'XXXXXXXXXXXXXXXX' 'sender@gmail.com' 'reciever@gmail.com'
7. The terminal will then ask you to input the password to your (sender) email
8. If you wish, you can automatically run this script every day using CRON: 
    * https://www.jcchouinard.com/python-automation-with-cron-on-mac/

