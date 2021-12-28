# Mail Me My Social Media follower count (SoMeMailMe)
To run the main function copy the following into the terminal after cloning the repository

python SoMeMailMe.py <tt_id>, <ig_id>, <token> <sender_email> <receiver_email>

e.g.
python SoMeMailMe.py 'thecuriouschemist' 'the_curious_chemist' 'XXXXXXXXXXXXXXXX' 'sender@gmail.com' 'reciever@gmail.com'

The terminal will then ask you to input the password to your (sender) email
You can get a free token at www.influencerhunters.com

## IMPORTANT: Do not use your main email as the sender, create a new email
You need to set 'Allow less secure apps' to ON, and also enter your email password into the terminal, so you may accidentally push your password to the wrong place.
See also this tutorial: https://realpython.com/python-send-email/

To import IH_scraper please do the following:
1. Clone the Social-Media-Scraper repo, which can be found here: https://github.com/InfluencerHunters/Social-Media-Scraper 
2. Place the folder in the root directory of this project and rename it as 'SocialMediaScraper'
3. Put the following two lines at the top of scraper.py:
import sys
sys.path.append('SocialMediaScraper/src')

