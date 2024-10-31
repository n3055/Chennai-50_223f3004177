import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from datetime import datetime
df = pd.read_csv("users.csv")
df["leader_strength"] = df["followers"]/(df["following"]+1)
st.header("Chennai:blue[50] :bar_chart:")
st.divider()
st.header("Users Analysis :computer:")
st.dataframe(df)
st.subheader("Top-5 users:trophy:")
users = st.columns(3)
with users[0]:
    st.text("Most-followed")
    st.dataframe(df.loc[[0,1,2,3,4],["login","followers"]])
with users[1]:
    st.text("Earliest_users")
    st.dataframe(df.loc[[351,215,100,300,316],["login","created_at"]])
with users[2]:
    st.text("Leader_strength")
    st.dataframe(df.loc[[2,0,12,13,10],["login","leader_strength"]])
st.subheader("Major Companies :cityscape:")
cmpy = {}
surname = {}
t_hireable = 0
email_hireable = 0
t_Nhire = 0
email_Nhire = 0
avg_hireable_following = 0
avg_Nhire_following = 0
bio_length = []
followers = []
for i in range(419):
    c = str(df.loc[i,"company"])
    n = str(df.loc[i,"name"])
    if c != "nan":
        if c in cmpy.keys():
            cmpy[c]+=1
        else:
            cmpy[c]=1
    name = list(n.strip().split(" "))
    if name[-1] in surname.keys():
        surname[name[-1]]+=1
    else:
        surname[name[-1]]=1
    ht = str(df.loc[i,"hireable"])
    if ht=="nan":
        t_Nhire+=1
        avg_Nhire_following+=int(df.loc[i,"following"])
        if str(df.loc[i,"email"])!="nan":
            email_Nhire+=1
    else:
        t_hireable+=1
        avg_hireable_following+=int(df.loc[i,"following"])
        if str(df.loc[i,"email"])!="nan":
            email_hireable+=1
    bio = str(df.loc[i,"bio"])
    if bio=="nan":
        continue
    bio_list = bio.strip().split()
    bio_length.append(len(bio_list))
    followers.append(int(df.loc[i,"followers"]))
cmpy["ZOHO CORPORATION"]+=cmpy["ZOHO"]
del cmpy["ZOHO"]
cmpy_filter = {}
for k in cmpy.keys():
    if cmpy[k]!=1:
        cmpy_filter[k]=cmpy[k]
st.bar_chart(cmpy_filter,color="#ffaa00")
st.write("\"Majority of Developers work at :red[ZOHO CORPORATION]\"")
st.subheader("Most Common surname :pencil:")
surname_filter = {}
for n1 in surname.keys():
    if surname[n1]!=1:
        surname_filter[n1]=surname[n1]
st.bar_chart(surname_filter)
st.write("\"Most Common surname is :red[S] followed by :red[KUMAR], given that last word is the surname\"")
st.subheader("Do people who are hireable share their email adresses more often?:thinking_face:")

avg_hireable_following/=t_hireable
avg_Nhire_following/=t_Nhire
st.latex(r'''\frac{Email Hireable }{Total hireable}-\frac{Email NotHireable}{Total NotHireable}''')
st.latex((email_hireable/t_hireable)-(email_Nhire/t_Nhire))
st.write(":red[YES], people who are hireable share their email ids more often")
st.subheader("Does writing long bio help gain more followers?:thinking_face:")


fig, ax = plt.subplots()
plt.axis([0,40,0,300])
X = np.array(bio_length).reshape(-1,1)
y = np.array(followers).reshape(-1,1)
reg = LinearRegression().fit(X, y)
ax.scatter(bio_length,followers)
x = np.arange(0,40,0.5).reshape(-1,1)
y_pred = reg.predict(x)
ax.plot(x,y_pred,color='r')
st.pyplot(fig)
st.write(":red[Regression Slope]")
st.write(reg.coef_[0])
st.write("\"There is a negative correlation between :red[length of the bio] and :blue[followers]\"")
st.write("But This doesn't mean wrting lengthy bio will repel followers XD.One possibility could be people with less followers write lengthy bio to attract new followers.")
st.write(":red[Conclusion]: Writing lengthy bio doesn't help with followers")
st.subheader("Do hireables follow more people than those who are not hireable?:thinking_face:")
st.latex("(Average following for hireable=True)-(Average of follwing for hireable=False)")
st.latex(avg_hireable_following-avg_Nhire_following)
st.write("\":red[YES],hireable users follow more people than those who are not hireable\"")
st.subheader("Correlation between the number of followers and number of public repositories:chart_with_upwards_trend:")
fig2,ax2 = plt.subplots()
ax2.scatter(df["public_repos"],df["followers"])
reg2 = LinearRegression().fit(np.array(df["public_repos"]).reshape(-1,1), np.array(df["followers"]).reshape(-1,1))
ax2.plot(df["public_repos"],reg2.predict(np.array(df["public_repos"]).reshape(-1,1)),color='r')
st.pyplot(fig2)
st.latex("Correlation Coefficient=")
st.latex(df["followers"].corr(df["public_repos"]))
st.latex("Regression slope=")
st.latex(reg2.coef_[0])
st.write("\"To get one additional followers you need to create approximately :red[4 repositories] according to regression model\".But some users have more followers with less repositories which means quality of projects matter more than quantity to gain followers.")
st.write("So we can say,:blue[Number of followers] and :blue[number of public_repos] are weakly correlated:red[!!!!!!!]")
repo = pd.read_csv("repositories.csv")
st.header("Repositories Analysis :male-technologist:")
st.dataframe(repo)
st.subheader("Most popular license used :scroll:")
lic = {}
lang = {}
lang_star = {}
lang_2020 = {}
weekend_repos = {}
for i in range(26326):
    date_object = datetime.strptime(repo.loc[i,"created_at"][:10], '%Y-%m-%d').date()
    if date_object.weekday()==5 or date_object.weekday()==6:
        if repo.loc[i,"login"] not in weekend_repos.keys():
            weekend_repos[repo.loc[i,"login"]]=1
        else:
            weekend_repos[repo.loc[i,"login"]]+=1 
    repo.loc[i,"has_wiki"]=int(repo.loc[i,"has_wiki"])
    repo.loc[i,"has_projects"]=int(repo.loc[i,"has_projects"])
    if str(repo.loc[i,"license_name"])!="nan":
        if repo.loc[i,"license_name"] not in lic.keys():
            lic[repo.loc[i,"license_name"]]=1
        else:
            lic[repo.loc[i,"license_name"]]+=1
    if str(repo.loc[i,"language"])!="nan":
        if repo.loc[i,"language"] not in lang.keys():
            lang[repo.loc[i,"language"]]=1
            lang_star[repo.loc[i,"language"]]=repo.loc[i,"stargazers_count"]
        else:
            lang[repo.loc[i,"language"]]+=1
            lang_star[repo.loc[i,"language"]]+=repo.loc[i,"stargazers_count"]
        if int(str(df.loc[df.index[df["login"]==repo.loc[i,"login"]],"created_at"]).split()[1].split('-')[0])>2020:
            if repo.loc[i,"language"] not in lang_2020.keys():
                lang_2020[repo.loc[i,"language"]]=1
            else:
                lang_2020[repo.loc[i,"language"]]+=1
            
st.bar_chart(lic,color="#ffaa00")
st.write("Top 3 Most popular License Names are :blue[MIT License], :blue[Apache License 2.0], :blue[GNU General Public License v3.0]")
st.subheader("Most popular language	:coffee:")
st.bar_chart(lang)
st.write(":blue[JavaScript] is the most popular language among these users")
st.subheader("Languages popular among users who joined after :two::zero::two::zero:")
st.bar_chart(lang_2020,color="#ffaa00")
st.write(":blue[JavaScript] is still the most popular language followed by :red[HTML]")

st.subheader("Languages with highest average number of stars per repository	:star2:")
for s in lang_star.keys():
    lang_star[s]/=lang[s]
st.bar_chart(lang_star)
st.write(":blue[Markdown] has the highest average number of stars per repository:red[!!!!!!!!]")
st.write("Use Markdown to stand out and gain more stars :)")
st.subheader("Correlation Between wikis and projects enabled:chart_with_upwards_trend:")
st.latex(repo["has_projects"].corr(repo["has_wiki"]))
st.write(":red[Projects] and :blue[wiki] are :red[weakly] correlated")
st.subheader("Top 5 users who created most repositories on weekend:trophy:")
wr = {k: v for k, v in sorted(weekend_repos.items(), key=lambda item: item[1], reverse=True)}
wr = dict(list(wr.items())[0: 5])
st.dataframe(wr)
footer = """<style>.footer {position: fixed;left: 0;bottom: 0;width: 100%;background-color: #000;color: #5f6061;text-align: center;}</style><div class='footer'><p>Made with ❤️ by RISHI ANAND</p></div>"""
st.markdown(footer, unsafe_allow_html=True)
