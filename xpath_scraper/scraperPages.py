journals = {
    "laRepublica": {
        "XPATH_URL_TO_ARTICLE" : '//a[contains(@class, "kicker")]/@href',
        "XPATH_SUMMARY" : '//div[@class="lead"]/p/text()',
        "XPATH_BODY": '//div[@class="html-content"]/p[not(@class)]/text()',
        "HOME_URL": 'https://www.larepublica.co/',
    },
    "cnnEspanol": {
        "XPATH_URL_TO_ARTICLE": '//h2[@class="news__title"]/a/@href',
        "XPATH_SUMMARY": '//figcaption/text()',
        "XPATH_TITLE": '//header[@class="storyfull__header"]/h1[@class="storyfull__title"]/text()',
        "XPATH_BODY": '//div[@class="storyfull__body"]/p[not(@class)]/text()',
        "HOME_URL": 'https://cnnespanol.cnn.com/',
    },
    # "leFigaro": {
    #     "XPATH_URL_TO_ARTICLE": '//a[@class="fig-profile__link"]/@href',
    #     "XPATH_SUMMARY": '//p[@class="fig-standfirst"]/text()',
    #     "XPATH_BODY": '//div[@class="fig-body"]/p[@class="fig-paragraph"]/text()',
    #     "HOME_URL": 'https://www.lefigaro.fr/',
    # },
}