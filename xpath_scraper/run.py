from scraperPages import journals
from scraper import JournalScraper


def run():
    # parse_home()
    for key, value in journals.items():
        folder_name = key
        xpath_summary = value.get('XPATH_SUMMARY')
        xpath_body = value.get('XPATH_BODY')
        home_url = value.get('HOME_URL')
        xpath_url_to_article = value.get('XPATH_URL_TO_ARTICLE')
        xpath_title = value.get("XPATH_TITLE", None)

        scraper = JournalScraper(
            xpath_summary=xpath_summary, xpath_body=xpath_body, 
            xpath_title=xpath_title, xpath_url_to_article=xpath_url_to_article,
            home_url=home_url, folder_name=folder_name)

        scraper.parse_home()


if __name__ == '__main__':
    run()
