# create csv

# open the file in the write mode
f = open('SoMe_data.csv', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
row = ['date','time','tt_followers', 'tt_likes', 'tt_posts', 'ig_followers']
writer.writerow(row)

# close the file
f.close()
print('SoMe_data.csv created successfully')