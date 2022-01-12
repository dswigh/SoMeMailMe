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

from SoMeMailMe import SoMeMailMe

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
    #print('Successfully updated csv file')

    # if sunday send out email
    if datetime.datetime.today().weekday() == 6:
        SoMe_user.send_email(sender_email, receiver_email, sender_email_password)
        #print('Successfully sent you a Sunday weekly recap!')

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

