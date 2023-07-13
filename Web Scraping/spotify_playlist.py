
# from bs4 import BeautifulSoup
# # import lxml

# with open(r"bs4-start\website.html", "r", encoding="utf8") as file:
#     contents = file.read()



# soup = BeautifulSoup(contents, "html.parser")

# # print(soup.title)
# # print(soup.title.string)

# # print(soup.prettify())

# # print(soup.p)

# all_anchor_tags = soup.find_all(name = "a") 
# # .find_all() method return the list of all the  elements which are specified by us.(Here <a>)

# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())

# # .getText allow us to get the text part of all the anchor tags here

# for tag in all_anchor_tags:
#     print(tag.get("href"))

# # .get allows us to get the link part of the anchor tag.

# heading = soup.find(name= "h1", id="name")
# print(heading)
# #

# section_heading = soup.find(name= "h3", class_= "heading")

# print(section_heading.get("class"))


# #.find() method returns the elements with name and id specified


# company_url = soup.select_one(selector="p a")

# # .select_one method will allow us to get the element with values of selector parameter.
# # here we have only one  anchor tag which is within a , p tag.

# print(company_url)

# heading = soup.select(".heading")
# print(heading)
# # This will give a list of items with the class (here heading).

# from bs4 import BeautifulSoup
# import requests

# response = requests.get(url="https://news.ycombinator.com/news")

# yc_webpage = (response.text)

# soup = BeautifulSoup(yc_webpage, "html.parser")

# print(soup.title)


# articles = soup.find_all(name="a", class_="titlelink")
# article_text = []
# article_link = []

# for article_tag in articles:
#     text = article_tag.getText()
#     article_text.append(text)
#     link = article_tag.get("href")
#     article_link.append(link)

# article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name= "span", class_ = "score")]


# print(article_text)
# print(article_link)
# print(article_upvote)


# print(max(article_upvote))
# print(article_upvote.index(max(article_upvote)))
# print(article_text[(article_upvote.index(max(article_upvote)))])
# print(article_link[(article_upvote.index(max(article_upvote)))])



################################################# TOP 100 Movies ########################################################

# from bs4 import BeautifulSoup
# import requests

# response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
# empire_webpage = response.text
# # print(empire_webpage)

# soup = BeautifulSoup(empire_webpage, "html.parser")

# movie_heading = soup.find_all(name = "h3", class_ = "title")

# movie_list = [movie.getText() for movie in movie_heading]

# # for movie in movie_heading:
# #         text = movie.text
# #         movie_list.append(text) 
# # print(movie_list[::-1])


# try:
#     with open(r"bs4-start\movies.txt", "w", encoding="utf8") as file:
#         for movie_name in movie_list[::-1]:
#             file.write(f"{movie_name}\n")
        
# except FileNotFoundError:
#     with open(r"bs4-start\movies.txt", "a") as file:
#         for movie_name in movie_list[::-1]:
#             file.write(f"{movie_name}\n")


######################################################### SPOTIFY PLAYLIST ####################################################################

from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify
# from pprint import PrettyPrinter
# pp = PrettyPrinter(indent=4)

SPOTIPY_CLIENT_ID = "88a3eb4ca3f04d64aa00811e9865da27"
SPOTIPY_CLIENT_SECRET = "78978a0cf0d94013ade7153e19c8f51f"
REDIRECT_URI = "http://example.com"

# ID = # 1CxTenLHnYmwLEUpyysnWt
# USERID = # 31x44ytlq6h3z5fiw7gqxo2mopw4


date = input("Which year do you want to travel to? Type the date in this forat YYYY-MM-DD:")

response = requests.get(url= f"https://www.billboard.com/charts/hot-100/{date}/")

bb_webpage = response.text
soup = BeautifulSoup(bb_webpage, "html.parser")


song_heading = soup.select(" ul li h3", id= "title-of-a-story" )
list_= [song.getText() for song in song_heading][0:100]
song_list = [song.strip("\t\n") for song in list_]
# print(song_list)




sp = Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri= REDIRECT_URI,
        client_secret=SPOTIPY_CLIENT_SECRET,
        client_id=SPOTIPY_CLIENT_ID,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user = sp.current_user()["id"]
# print(user)
# playlist_list = []

# a = sp.current_user_playlists()["items"]
# for i in range(len(a)):
#     playlist_list.append(a[i]["name"])
# print(playlist_list)

song_uris = []

year = date.split("-")[0]

for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    
    except IndexError:
        print(f"{song} doesn't exist in spotify. Skipped")


# print((song_uris))



a = sp.user_playlist_create(user ="31x44ytlq6h3z5fiw7gqxo2mopw4",name=f"{date} Billboard 100" , public=False)

# print(a["id"])

sp.playlist_add_items(playlist_id=a["id"], items=song_uris)

############################################################################################## XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ###############################################

############################################################################################## AMAZON PRICE TRACKING #################################################################


# from bs4 import BeautifulSoup
# import requests
# import smtplib

# MY_EMAIL = "nokiatv2001@gmail.com"
# MY_PASSWORD = "r2ohit2000"


# headers = {

#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"    ,
#     "Accept-Language": "en-US,en;q=0.9"

# }


# response = requests.get(url= "https://www.amazon.in/dp/B08VB57558/ref=s9_acsd_al_bw_c2_x_0_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-6&pf_rd_r=R77E5PH8JFP8NXVDFJZS&pf_rd_t=101&pf_rd_p=2dc88236-5060-4676-a057-3fc053ff6948&pf_rd_i=20656599031", headers= headers)
# amazon_webpage = response.text
# response.status_code

# # print(amazon_webpage)

# soup = BeautifulSoup(amazon_webpage, "html.parser")

# price = soup.find(name="span", class_= "a-offscreen")

# item_price = (price.text.split("₹"))
# item_price = (item_price[1])
# price_string = ""
# for i in item_price.split(","):
#     price_string+=i

# if float(price_string) < 32000.00:

#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs="epicslayer2021@gmail.com",
#             msg=f"Subject:Amazon Price Alert!\n\n BUY kR lo Samsung Mobile")
    
