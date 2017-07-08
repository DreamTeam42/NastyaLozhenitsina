import scrapy
import json


class BashSpider(scrapy.Spider):
    # имя парсера(поискового робота)
    name = 'BashSpider'
    # ссылока на начальную страницу для парсинга
    str1 =  'https://investmoscow.ru/tenders?Page=1&PerPage=10&'
    str2 = 'TenderListType=0&HasAdvancedFilter=True&PostedTenderKinds=2&IsHectare=false'
    start_urls = [str1 + str2]
    print (start_urls)

    # функция парсинга
    def parse(self, responce):
        # итерируем
        for page in responce.css('div.list-card__name-block'):
            #urls = page.css('div.col-sm-4.list-card__col1 div.list-card__name-block div.list-card__name-block')
            print (255555555)
            yield {
                'Str': page.xpath('./a[@class="list-card__name"]/@href').extract_first(),
            }

        # итерируемся по url страницы

        for next_page in responce.css('ul.pagination__page-list a::attr(href)'):
            yield responce.follow(next_page, self.parse)
