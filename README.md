# insta-scraper

The **instagram.py** file displays the code for the scraping of Instagram accounts and specifically their profile picture and follower count.
After moving on from scraping through the metadata provided by the source code of an Instagram account, I decided to use the Instagramy package to scrape username, profile picture, follower count and if the user is private.
This code was implemented in a google cloud function, which can only be accessed by the website, that it was designed for, due to HTTP restrictions. 
The source code in the cloud functions is developed a bit differently, to prevent access denied exceptions. Furthermore the **details.html** file displays a login form for the designed website, so that the provider can scrape the users informations for further business interactions.
