import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }

    r = requests.get(url=url, headers=headers)

    with open("index.html", "w") as file:
        file.write(r.text)

    r = requests.get("https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most", headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    hotels_cards = soup.find_all("div", class_="hotel_card_dv")

    for hotel_url in hotels_cards:
        hotel_url = hotel_url.find("a").get("href")
        print(hotel_url)


def get_data_with_selenium(url):
    options = webdriver.ChromeOptions()
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36")

    # try:
    #     driver = webdriver.Firefox(
    #         executable_path="/home/cain/PycharmProjects/scrap_tutorial/lesson6/geckodriver",
    #         options=options
    #     )
    #     driver.get(url=url)
    #     time.sleep(5)
    #
    #     with open("index_selenium.html", "w") as file:
    #         file.write(driver.page_source)
    #
    # except Exception as ex:
    #     print(ex)
    # finally:
    #     driver.close()
    #     driver.quit()

    with open("index_selenium.html") as file:
        src = file.read()


    soup = BeautifulSoup(src, "lxml")

    hotels_cards = soup.find_all("div", class_="hotel_card_dv")

    for hotel_url in hotels_cards:
        hotel_url = "https://www.tury.ru" + hotel_url.find("a").get("href")
        print(hotel_url)


def main():
    # get_data("https://www.tury.ru/hotel/most_luxe.php")
    get_data_with_selenium("https://www.tury.ru/hotel/most_luxe.php")


if __name__ == "__main__":
    main()
