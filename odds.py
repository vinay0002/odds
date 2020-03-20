import pandas as pd
import requests
from bs4 import BeautifulSoup
page=requests.get("https://www.oddschecker.com/horse-racing/townsville/race-6/winner")
soup=BeautifulSoup(page.content,"html.parser")
data=soup.find(id="t1")
diff_row=data.find(class_="diff-row evTabRow bc")
name_wrap=diff_row.find(class_="sel nm has-silks")

temp= [diff_row.find(class_="bottom-row jockey").get_text() for diff_row in data]

# top_row=name_wrap.find(class_="top-row").get_text()
# bottom_row=name_wrap.find(class_="bottom-row jockey").get_text()

# print(top_row)
# print(bottom_row)
# print(diff_row)
print(temp)

odds= pd.DataFrame(
    {
        'temp':temp
    }
)

print(odds)
odds.to_csv("odds_player_list.csv")