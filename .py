# Created by: Roman Beya and Gillian Gonzales
# Created for: Digitera Interactive, Web Scraping Assignment: Link 2
# Created on: Tuesday, July10th, 2018
# This script scrapes all of the data off of this DJ website using Beautiful Soup to parse the data

from bs4 import BeautifulSoup
import requests
import csv

# Create a csv file object that will open up a new csv file and write to it
csv_file = open("Web_Scraping_Link_3.csv", "w")

# Create a csv writer object that will write to the new csv file created above
csv_writer = csv.writer(csv_file)

# Define names of headers to properly identify the sorted data
csv_writer.writerow(['Post_Created_By', 'Post_Last_Viewed_By', 'Date_of_Last_View'])

url = requests.get("https://www.babycenter.ca/g25003393/moms-in-ottawa").text

soup = BeautifulSoup(url, "lxml")

title = soup.title.string

containers = soup.findAll("div", class_="activePostsItem row ")

for container in containers:
    date_of_view = container.find("span", class_="latestDate")
    split_front = date_of_view.string.split("\">")[0]
    split_back = split_front.split("</div>")[0]

    latest_comment = container.find("div", class_="thrLatest hide-for-small medium-3 columns")
    #print(str(latest_comment))
    split_latest_comment_front = str(latest_comment).split("<br/>")[1]
    #print(split_latest_comment_front)

    split_latest_comment_back = split_latest_comment_front.split("</div>")[0]

    #print(split_latest_comment_back)

    poster = container.find("div", class_="postInfo clearfix")
    split_poster_front = str(poster).split("</a>")[1]
    split_poster_back = split_poster_front.split("<!")[0]

    if split_poster_back.__contains__("/>"):
        print(split_poster_back.split("/>")[1])
        csv_writer.writerow([split_poster_back.split("/>")[1], split_latest_comment_back, split_back])
    else:
        print(split_poster_back)
        csv_writer.writerow([split_poster_back, split_latest_comment_back, split_back])

csv_file.close()
