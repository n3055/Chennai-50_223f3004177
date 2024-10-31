import requests
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()
token = os.getenv('API_KEY')
##First we gather all the logins of user from chennai with over 50 followers
#for i in range(5):
#    r = requests.get("https://api.github.com/search/users?q=location%3AChennai+followers%3A>50&page="+str(i+1)+"&per_page=100")
#    res = r.json()
#    for it in res['items']:
#        with open("Users.txt","a") as f1:
#            f1.write(it['login']+"\n")
##Now we have all the user-names saved in a txt file
#Scrape info users one by one
#users = {
#    "login":[],
#    "name":[],
#    "company":[],
#    "location":[],
#    "email":[],
#    "hireable":[],
#    "bio":[],
#    "public_repos":[],
#    "followers":[],
#    "following":[],
#    "created_at":[]
#}
headers = {'Authorization': 'token ' + token}
#with open("Users.txt","r") as f:
#    for i in range(419):
#        r = requests.get("https://api.github.com/users/"+str(f.readline().strip()),headers=headers).json()
#        for k in users:
#            users[k].append(r[k])
#df = pd.DataFrame(users)
#df.to_csv("users.csv",index=False)
###Cleaning Companies name
#df = pd.read_csv("users.csv")
#for i in range(419):
#    df.loc[i,'company']=
#df.to_csv("users2.csv",index=False)
#####TIME TO GET THOSE REPOS
repo = {
"login": [],
"full_name": [],
"created_at": [], 
"stargazers_count": [],
"watchers_count": [],
"language": [],
"has_projects": [],
"has_wiki": [],
"license_name": [] 
}
with open("Users.txt","r") as f:
    for i in range(123):
        log = f.readline().strip()
        pg = 1
        rep_c = 0
        flag = False
        while True:
            r = requests.get("https://api.github.com/users/"+log+"/repos?sort=pushed_at&page="+str(pg)+"&per_page=200",headers=headers).json()
            if str(r)=="[]":
                break
            for rep in r:
                repo['login'].append(log)
                repo['full_name'].append(rep['full_name'])
                repo['created_at'].append(rep['created_at'])
                repo['stargazers_count'].append(rep['stargazers_count'])
                repo['watchers_count'].append(rep['watchers_count'])
                repo['language'].append(rep['language'])
                repo['has_projects'].append(rep['has_projects'])
                repo['has_wiki'].append(rep['has_wiki'])
                if rep['license']== None:
                    repo['license_name'].append("null")
                else:
                    repo['license_name'].append(rep['license']['name'])
                df = pd.DataFrame(repo)
                df.to_csv("repositories3.csv",index=False)
                rep_c+=1
                if rep_c==500:
                    flag = True
                    break
            if flag:
                break
            pg+=1
