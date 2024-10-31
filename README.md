# Chennai-50_223f3004177
Data Analysis of Github users from chennai with over 50 followers
# Scraping the data
"The first step is to filter people from Chennai who have over 50 followers. To do this, I used GitHub's advanced search tool, where I set the parameters and found 419 such users. This also gave me a URL with the required query (i.e., location: Chennai and followers > 50). I appended that query to api.github.com/search to create the URL for our API requests. I used the requests module in Python to make an API request to the URL. Initially, I could only make a limited number of requests, so I included a header with an API key to allow my program to make more requests per minute. I then stored only the required fields in a dictionary, and using pandas, I created a DataFrame, which was saved as a CSV file using to_csv().

Scraping Users.csv was straightforward, but scraping repositories.csv required making individual API calls for all 419 users to get the necessary fields. To handle this, I divided my user data into four chunks and made API calls for each chunk, ensuring that the request process wasn't interrupted and I didn't have to start over. After 20–30 minutes, my repositories.csv file was ready. You can check the program in the scraper.py file in this repository
# Most interesting and Surprising fact
* People with more followers didn't necessarily have more repositories.
* The percentage of people who used Markdown had more stars on their repositories.
* People with fewer followers tend to write lengthy bios to attract followers.
# An actionable recommendation for developers 
* Creating a few quality projects is more important than making many average projects.
* Using Markdown to improve the appearance of repositories can help earn more stars."

