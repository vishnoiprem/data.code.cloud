import scrapy


class QuestionsSpider(scrapy.Spider):
    name = "questions"
    start_urls = [
        'https://datascience.stackexchange.com/'
    ]

    def parse(self, response):
        counter = 0

        for question in response.css('div.s-post-summary'):

            counter = counter + 1

            summary = question.css("div.s-post-summary--content h3 a.s-link::text").get()
            votes = question.css(
                "div.s-post-summary--stats div.s-post-summary--stats-item__emphasized span.s-post-summary--stats-item-number::text").get()
            number_of_answers = question.css(
                "div.s-post-summary--stats div.has-answers span.s-post-summary--stats-item-number::text").get()
            views = question.css(
                "div.s-post-summary--stats div:last-child span.s-post-summary--stats-item-number::text").get()

            print(dict(summary=summary, votes=votes, number_of_answers=number_of_answers, views=views))

            if counter == 10:
                break


from scrapy.crawler import CrawlerProcess

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(QuestionsSpider)
process.start()  # the script will block here until the crawling is finished