from bs4 import BeautifulSoup
import requests
import urllib.request
from PIL import Image
from instagramy import InstagramUser

  

URL = "http://www.instagram.com/{}/"




def get_user_img(username):
    user = InstagramUser(username)
    picture = user.profile_picture_url

    private = user.is_private
    
    r = requests.get(URL.format(username))
    i = BeautifulSoup(r.text,"html.parser")
    meta = i.find("meta",property="og:image")
    return picture

def get_user_data(username):
    user = InstagramUser(username)
    follower = user.followed_by_viewer
    private = user.is_private
    return user

if __name__ == "__main__":
    print('Please enter Username:')
    username =  input()
    img1 = get_user_img(username)

    
    urllib.request.urlretrieve(img1,"gfg.jpg")
    img = Image.open("gfg.jpg")
    img.show()
    
    
    print("User is private? " + str(get_user_data(username).is_private))
    print("User has " + str(get_user_data(username).number_of_followers) + " Follower")

    
  
    

