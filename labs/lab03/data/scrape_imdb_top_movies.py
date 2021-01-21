# This is a python script that gets the data from IMDb. :)

from bs4 import BeautifulSoup
import requests
import re
import csv
import json


def scrapeTopIMDB():
    allMovieData = []

    imdb_top = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
    imdb_response = requests.get(imdb_top, timeout=5)

    imdb_table = (
        BeautifulSoup(imdb_response.content, "html.parser")
        .find("tbody", {"class": "lister-list"})
        .findChildren("tr")
    )

    for imdb_tr in imdb_table:
        imdb_titleColumn = (
            imdb_tr
            .findChildren("td", {"class": "titleColumn"})[-1]
        )

        imdb_ratingColumn = (
            imdb_tr
            .findChildren("strong")[-1]
            .attrs["title"]
            .split(" ")
        )

        title = imdb_titleColumn.findChildren("a")[-1].text

        year = int(
            re.sub(r'[()]', '', imdb_titleColumn
                   .findChildren("span")[-1].text)
        )

        decade = 10*(year//10)

        rank = int(
            imdb_titleColumn.contents[0]
            .strip()
            .replace(".", "")
        )

        rating = float(imdb_ratingColumn[0])

        votes = int(
            imdb_ratingColumn[3]
            .replace(",", "")
        )

        allMovieData.append({"Rank": rank, "Rating": rating, "Votes": votes, "Title": title,
                             "Year": year, "Decade": decade})
    return allMovieData


def saveToCsv(movieData):
    with open('imdb.csv', 'w') as f:
        fieldnames = ['Rank', 'Rating', 'Votes', 'Title', 'Year', 'Decade']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(movieData)


def saveToTsv(movieData):
    with open('imdb.tsv', 'w') as f:
        fieldnames = ['Rank', 'Rating', 'Votes', 'Title', 'Year', 'Decade']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows(movieData)


def saveToJson(movieData):
    with open("imdb.json", "w") as j:
        json.dump(movieData, j)


def runScrape():
    print("Starting to scrape imdb...")
    movies = scrapeTopIMDB()
    print("imdb data collected!")

    print("Saving to CSV")
    saveToCsv(movies)
    print("Saving to TSV")
    saveToTsv(movies)
    print("Saving to JSON")
    saveToJson(movies)

runScrape()
