import scrapy


class HawkspiderSpider(scrapy.Spider):
    name = "hawkspider"
    allowed_domains = ["aviation-safety.net"]
    start_urls = ["https://aviscation-safety.net/wikibase/type/H60/4"]

    def parse(self, response):
        crashes = response.css('tr.list')

        for crash in crashes:
            yield {
                'date': response.css('td.list a::text').get(),
                'type': response.css('td.list::text').get(),
                # 'operator' :
                # 'fat':
                # 'loc' :

            }
