from bs4 import BeautifulSoup
import requests


def get_page():
    result = requests.get(
        'https://uisnetpr01.njit.edu/courseschedule/?term=202095#/crs_100')

    if(result.status_code == 200):
        print("Request returned status 200. Good to go!")
        return result.content
    else:
        print("Status err: ", result.status_code)


def soupify():
    src = get_page()
    soup = BeautifulSoup(src, 'lxml')
    print("links:", soup.find_all("a"))


soupify()
