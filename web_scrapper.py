# http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup/
from bs4 import BeautifulSoup
import requests

def get_games_from_wikipedia():
    url = 'https://en.wikipedia.org/wiki/2018_in_video_gaming'
    r = requests.get(url)
    data = r.text

    soup = BeautifulSoup(data)
    tables = soup.find_all("table", class_="wikitable")[4]
    rows = tables.find_all("tr")

    del rows[0]
    processed_count, not_processed_count = 0, 0
    for data in rows:
        try:
            name_cell = data.find_all("i")
            name = name_cell[0].find("a")
            if not name:
                name = name_cell[0].contents[0]
            else:
                name = name.contents[0]
            print(name)
            processed_count += 1
        except Exception as err:
            print('WAS NOT PROCESSED')
            not_processed_count += 1

    print("{} titles were successfully processed, {} titles failed to be processed".format(processed_count, not_processed_count))

def get_movie_urls():
    scraped_urls = ['https://scannain.com/upcoming-irish-cinema-release-dates/']
    found_links, links_parsed = 0, 0
    while links_parsed < len(scraped_urls):
        r = requests.get(scraped_urls[links_parsed])
        data = r.text
        soup = BeautifulSoup(data)

        def _search_for_urls():
            found_links = 0
            button_container = soup.find_all("div", class_="cb-post-pagination clearfix")[0]
            links = button_container.find_all('a', href=True)
            for page in links:
                if(page['href'] not in scraped_urls):
                    scraped_urls.append(page['href'])
                    found_links += 1
            return found_links
        found_links += _search_for_urls()
        links_parsed += 1
    print('Parsed {} links and found {} while scrapping'.format(links_parsed, found_links))
    return scraped_urls

get_movie_urls()

def get_films_from_scannain():
    url = 'https://scannain.com/upcoming-irish-cinema-release-dates/'
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)

    table = soup.find_all("tr")
    processed_count, not_processed_count = 0, 0
    for row in table:
        try:
            meta = row.find_all('h2')
            date = meta[0].contents[0]
            name = meta[1].contents[1]
            h3 = row.find('h3')
            genre = h3.contents[0]
            print('{}, Date: {}, Genre: {}'.format(name.encode('utf-8'), date.encode('utf-8'), genre.encode('utf-8')))
            processed_count += 1
        except Exception as err:
            print(err)
            not_processed_count += 1
    print("{} titles were successfully processed, {} titles failed to be processed".format(processed_count, not_processed_count))