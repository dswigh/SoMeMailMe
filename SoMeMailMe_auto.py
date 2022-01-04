#This script takes the email password as an argument, 
# which is required for automation
#imports
import sys
import csv
import datetime
import pandas as pd
import smtplib, ssl
from SocialMediaScraper.src.scraper import IH_scraper
from getpass import getpass


# get data
class SoMeMailMe():
    def __init__(self, tt_id, ig_id, token):
        self.tt_id = tt_id
        self.ig_id = ig_id
        self.token = token
        # Get a free token at www.influencerhunters.com
    
    def scraper(self):
        api_scraper = IH_scraper(token_IH_API=self.token)
        tt_data, tt_success = api_scraper.tt.get_user_info(self.tt_id)
        tt_followers = tt_data['stats']['followerCount']
        tt_likes = tt_data['stats']['heartCount']
        tt_posts = tt_data['stats']['videoCount']
        
        ig_data, ig_success= api_scraper.ig.get_user_detailed_info(self.ig_id)
        ig_followers = ig_data['followers']['count']
        
        return tt_followers, tt_likes, tt_posts, ig_followers
    
    def update_csv(self, csv_file):
        #updates csv file by adding new row data
        f = open(csv_file, 'a', newline='')
        date = datetime.datetime.today().strftime('%d/%m/%Y')
        time = datetime.datetime.today().strftime('%H:%M:%S')
        tt_followers, tt_likes, tt_posts, ig_followers = self.scraper()
        new_row = [date, time, tt_followers, tt_likes, tt_posts, ig_followers]
        writer = csv.writer(f)
        writer.writerow(new_row)
        f.close()
    
    def extract_csv_data(self, csv_file):
        df = pd.read_csv(csv_file)
        
        #check that today row is actually today
        today_data = df.iloc[-1]
        today_date = datetime.datetime.today()
        today_date_str = today_date.strftime('%d/%m/%Y')
        if today_data['date'] != today_date_str:
            raise Exception('No data about today')
        
                # find data from 7 days ago
        last_week_date = today_date - datetime.timedelta(days=7)
        last_week_str = last_week_date.strftime('%d/%m/%Y')
        found_last_week_data = False
        for i in range(len(df['date'])):
            last_week_data = df.iloc[-i]
            if last_week_data['date'] == last_week_str:
                found_last_week_data = True
                break
        
        if found_last_week_data:
        
            #create dict with relevant data
            # 'date','tt_followers', 'new_tt_followers', 'tt_likes', 'tt_posts', 'ig_followers'
            # new refers to new in the last 7 days
            new_tt_followers = int(today_data['tt_followers']) - int(last_week_data['tt_followers'])
            new_tt_likes = int(today_data['tt_likes']) - int(last_week_data['tt_likes'])
            new_tt_posts = int(today_data['tt_posts']) - int(last_week_data['tt_posts'])
            new_ig_followers = int(today_data['ig_followers']) - int(last_week_data['ig_followers'])

            SoMeDict = {'date': today_data['date'], 'tt_followers': int(today_data['tt_followers']), 
                        'new_tt_followers': new_tt_followers, 'tt_likes': int(today_data['tt_likes']),
                        'new_tt_likes': new_tt_likes , 'tt_posts': int(today_data['tt_posts']),
                        'new_tt_posts': new_tt_posts, 'ig_followers': int(today_data['ig_followers']),
                        'new_ig_followers': new_ig_followers}
        
        
        else:
            SoMeDict = {'date': today_data['date'], 'tt_followers': int(today_data['tt_followers']), 
                        'tt_likes': int(today_data['tt_likes']), 'tt_posts': today_data['tt_posts'],
                        'ig_followers': int(today_data['ig_followers'])}
            
        return SoMeDict
    
    def write_email(self, SoMeDict):
        try:
            tt_new_follower_ratio = int(SoMeDict['new_tt_followers'])/(int(SoMeDict['tt_followers'])-int(SoMeDict['new_tt_followers']))
            tt_new_like_ratio = int(SoMeDict['new_tt_likes'])/(int(SoMeDict['tt_likes'])-int(SoMeDict['new_tt_likes']))
            ig_new_follower_ratio = int(SoMeDict['new_ig_followers'])/(int(SoMeDict['ig_followers'])-int(SoMeDict['new_ig_followers']))

            message = (f"Subject: Social media weekly recap {SoMeDict['date']}\n\n"

f"Hi {self.tt_id},\n\n"

f"You now have {SoMeDict['tt_followers']} followers on TikTok, \
that's {SoMeDict['new_tt_followers']} ({round(tt_new_follower_ratio*100)}%) more than last week with {SoMeDict['new_tt_posts']} new posts!\n\n"

f"You now have {SoMeDict['tt_likes']} likes on TikTok, \
that's {SoMeDict['new_tt_likes']} ({round(tt_new_like_ratio*100)}%) more than last week with {SoMeDict['new_tt_posts']} new posts!\n\n"

f"You now have {SoMeDict['ig_followers']} followers on Instagram, \
that's {SoMeDict['new_ig_followers']} ({round(ig_new_follower_ratio*100)}%) more than last week!\n\n"

"Kinds regards,\n"
"The Curious Chemist\n\n\n"


"This is an automated message, please do not reply. Instead email thecuriouchemist1@gmail.com.")
        
        except KeyError:
            message = (f"Subject: Social media weekly recap {SoMeDict['date']}\n\n"

f"Hi {self.tt_id},\n\n"

f"You now have {SoMeDict['tt_followers']} followers on TikTok.\n\n"

f"You now have {SoMeDict['tt_likes']} likes on TikTok.\n\n"

f"You now have {SoMeDict['ig_followers']} followers on Instagram.\n\n"

"Kinds regards,\n"
"The Curious Chemist\n\n\n"


"This is an automated message, please do not reply. Instead email thecuriouchemist1@gmail.com.")
        
        return message
    
    def send_email(self, sender_email, receiver_email, sender_email_password):
        SoMeDict = self.extract_csv_data('../SoMe_data.csv')
        message = self.write_email(SoMeDict)
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        password = sender_email_password

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

def main():
    #take in arguments for main
    args = sys.argv[1:]
    #args should be in this order, see also  readme.md
    
    tt_id, ig_id, token, sender_email, receiver_email, sender_email_password = args

    #initiate SoMeMailMe:
    SoMe_user = SoMeMailMe(tt_id, ig_id, token)
    # Get a free token at www.influencerhunters.com
    
    #update csv file
    SoMe_user.update_csv('../SoMe_data.csv')
    print('Successfully updated csv file')

    # if sunday send out email
    if datetime.datetime.today().weekday() == 6:
        SoMe_user.send_email(sender_email, receiver_email, sender_email_password)
        print('Successfully sent you a Sunday weekly recap!')

if __name__ == "__main__":
    main()

# # create csv

# # open the file in the write mode
# f = open('SoMe_data.csv', 'w')

# # create the csv writer
# writer = csv.writer(f)

# # write a row to the csv file
# row = ['date','time','tt_followers', 'tt_likes', 'tt_posts', 'ig_followers']
# writer.writerow(row)

# # close the file
# f.close()
# print('SoMe_data.csv created successfully')

