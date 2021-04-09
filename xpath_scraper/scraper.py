import requests
import lxml.html as html
import os
import datetime


class Scraper:
    def __init__(self, home_url: str):
        self.home_url = home_url

    def make_request(self, url: str) -> html.Element:
        """Make the request to get the HTML of web page

        Args:
            url (str): Url of webpage to obtain the HTML

        Raises:
            ValueError: In case of HTTP error or any other error in the response

        Returns:
            html.Element: An object with the HTML of the Webpage 
        """
        try:
            response = requests.get(url)
            if response.status_code == 200:
                home = response.content.decode('utf-8')
                # Convert Home result in HTML to run XPATH script
                parsed = html.fromstring(home)
                return parsed

            else:
                raise ValueError(f'Error: {response.status_code}')
        except ValueError as ve:
            print(ve)
    

class JournalScraper(Scraper):

    def __init__(self, 
                xpath_title: str, 
                xpath_summary:str,
                xpath_body: str,
                xpath_url_to_article: str,
                folder_name: str,
                home_url:str
                ):
        super().__init__(home_url)
        self.xpath_title = xpath_title
        self.xpath_summary = xpath_summary
        self.xpath_body = xpath_body
        self.xpath_url_to_article = xpath_url_to_article
        self.folder_name = folder_name

        self.TODAY = datetime.date.today().strftime('%d-%m-%Y')
        self.DIR = "journal_articles"
        

    def get_title(self, url: str) -> str:
        """Get URL and extract title.

        Args:
            url (str): Article url

        Returns:
            str:  Title of the article 
        """
        spliter = url.split('/')[-1]
        spliter = spliter.split('-')[:-1]
        title = " ".join(spliter)
        return title
        
    def parse_article_file(self, url: str) -> str:
        """Scrap article content and create a file with the article.

        Args:
            url (str): Url of article to scrap content and make file
        
        Returns:
            str: Article route in local
        """
        try:
            # Get HTML.element from article page
            parsed = super().make_request(url)

            # Scraping info from URL
            if self.xpath_title: 
                title = parsed.xpath(self.xpath_title)[0]
            else:
                title = self.get_title(url)

            if self.xpath_summary:
                summary = parsed.xpath(self.xpath_summary)
            else:
                summary = []

            body = parsed.xpath(self.xpath_body)

            file_title = title.replace(' ', '_')
            route = f'{self.DIR}/{self.TODAY}/{self.folder_name}/{file_title}.txt'

            # Create the file
            with open(route, 'w', encoding='utf-8') as f:
                f.write(url)
                f.write('\n\n')
                f.write(title)
                f.write('\n\n')
                if len(summary) > 0:
                    f.write(summary[0])
                    f.write('\n\n')
                if len(body) > 0:
                    for paragraph in body:
                        f.write(paragraph)
                        f.write('\n')

            return route

        except ValueError as ve:
            print(ve)
        except FileExistsError as file_error:
            print(file_error)
        except IndexError as ie:
            print(ie, route)
        except Exception as e:
            print(f'Error: {e} trying parse each article url')


    def parse_home(self):
        """Call all functions for all process of journal "Larepublica"
        """
        try:
            url = self.home_url
            parsed = super().make_request(url=url)
            urls_to_notices = parsed.xpath(self.xpath_url_to_article)

            # Verify if DIR exist
            if not os.path.isdir(self.DIR):
                os.mkdir(self.DIR)
            if not os.path.isdir(f'{self.DIR}/{self.TODAY}'):
                os.mkdir(f'{self.DIR}/{self.TODAY}')
            if not os.path.isdir(f'{self.DIR}/{self.TODAY}/{self.folder_name}'):
                os.mkdir(f'{self.DIR}/{self.TODAY}/{self.folder_name}')
                
            results = list(map(lambda x: self.parse_article_file(x), urls_to_notices))

            print(results)

        except Exception as e:
            print(f'Error: {e} trying parse url in Home')

