import scrapy



class BashSpider(scrapy.Spider):
    # имя парсера(поискового робота)
    name = 'BashSpider'
    # список ссылок для парсинга
    start_urls = ['https://investmoscow.ru/tenders/tendercard/?TenderID=17037958']

    # функция парсинга
    def parse(self, responce):
        # итерируем
        for item in responce.css('div.col-md-6'):
            # выдёргиваем нужные блоки
            block_1 = item.css('div.col-md-6 div#primaryInfo div.col-md-12')
            table_1 = block_1.css(' table')
            tbody_1 = table_1.css('tbody')

            # словарь
            yield {
                #primaryInfo
                'Infa_about_object': block_1.css('div.tender-card__description div::text').extract_first(), #Работает  корректно
                'Contacts_managers': tbody_1.xpath('//tr[th/text()="\n                     Контакты менеджеров:\n                 "]/td/text()').extract_first(),#Не работает! Необходимо из td получить текст.
                                                                                                                                                                 #Важно: т.к. данные в таблице могут меняться,
                                                                                                                                                                 #взятие по индексу(следующий вариант) не подходит.
                                                                                                                                                                 #Необходимо сравнение с продыдущим блоком
                'Registry number': tbody_1.xpath('//tr[2]/td/text()').extract_first(), # Не работает!
                #'Appointment': item.xpath('//*[@id="primaryInfo"]/div/div/table/tbody/tr[1]/td/text()').extract_first(),
                #'Object_type': tbody_1.css('tr:nth-child(4) td ::text').extract_first(),
                #'Area': tbody_1.css('tr:nth-child(5) td ::text').extract_first(),
                #'Nearest_metro_station': tbody_1.css('tr:nth-child(6) td ::text').extract_first(),
                #'Distance_to_metro, km': tbody_1.css('tr:nth-child(7) td ::text').extract_first(),
                #'Living_area, sq.m': tbody_1.css('tr:nth-child(8) td ::text').extract_first(),
                #'Non-residential_area, sq.m.': tbody_1.css('tr:nth-child(9) td ::text').extract_first(),
                #'Area_object, sq.m.': tbody_1.css('tr:nth-child(9) td ::text').extract_first(),
                #'Initial_price, rub': tbody_1.css('tr:nth-child(9) td ::text').extract_first(),
                # secondaryInfo
                #'Elevator': tbody_1.css('tr:nth-child(9) td ::text').extract_first(),
                #'Freight_elevator': tbody_1.css('tr:nth-child(9) td ::text').extract_first(),
                #'Parking_place': tbody_1.css('tr:nth-child(9) td ::text').extract_first(),
                #'Telephone_lines': tbody_1.css('tr:nth-child(9) td ::text').extract_first(),
                #'Security_site': tbody_1.css('tr:nth-child(9) td ::text').extract_first(),
                #'Building_type': tbody_1.css('tr:nth-child(9) td ::text').extract_first(),
                #'Storey_house': tbody_1.css('tr:nth-child(9) td ::text').extract_first(),
                #'Line_houses': tbody_1.css('tr:nth-child(9) td ::text').extract_first(),
                #'floor': tbody_1.css('tr:nth-child(9) td ::text').extract_first(),

                #\n                    \u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440\u043e\u0432:\n
            # auctionInfo
                # procedureInfo
                # attachedFiles
            }
        # итерируемся по url страниц
        for next_page in responce.css('div.pager a::attr(href)'):
            yield responce.follow(next_page, self.parse)

            # primaryInfo > div > div > table > tbody > tr:nth-child(2) > td

