# Chennai-50_223f3004177
Data Analysis of Github users from chennai with over 50 followers
# Scraping the data
First step is to filter people from chennai who have over 50 followers.
To do this I used github's advanced search tool where I passed the parameters and I got 419 such users.This also gave me a url with required query(i.e. location:chennai and followers>50). I appended that query to api.github.com/search and we got our URL to which we will be making our api requests.
I Used requests module in python to make a api request to the URL we have. But I could only make limited requests at start, to tackle this I used header which included api_key which allowed my program to make more requests per minute.
Then I stored only the required fields in a dictionary and using pandas I created a Dataframe which was saved as csv using to_csv().
Scraping Users.csv was easy but to scrape repositories.csv I had to traverse through all the users and make individual api call to all 419 users and get the required fields. To Tackle this I divided my users data into 4 chunks and made api cal for each chunk,this made sure that the api request was not interrepted and I didn't have to start all over again. And finally after 20-30 mins my repositories.csv was ready. You can check the program in scraper.py file in this repository
