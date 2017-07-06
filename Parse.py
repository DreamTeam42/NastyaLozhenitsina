import scrapy
import json



class BashSpider(scrapy.Spider):
    # имя парсера(поискового робота)
    name = 'BashSpider'
    # список ссылок для парсинга
    start_urls = ['https://investmoscow.ru/tenders/tendercard/?tenderId=16990037']

    # функция парсинга
    def parse(self, responce):
        # итерируем
        for item in responce.css('#content'):
            # выдёргиваем нужные блоки
            block_1 = item.css('#content div.tender-card div.col-md-6 div#primaryInfo div.col-md-12')
            block_2 = item.css('#content div.tender-card div.col-md-6 div#secondaryInfo div.col-lg-12')
            block_3 = item.css('#content div.tender-card div.col-md-6 div#auctionInfo div.col-md-12')
            block_4 = item.css('#content div.tender-card div.col-md-6 div#procedureInfo ')
            block_5 = item.css('#content div.tender-card div.col-md-6 div#attachedFiles ')
            photo = item.css('#content div.tender-card div.col-md-6 div.col-md-12.tender-card-image-container div.image-container.pull-right')

            table_1 = block_1.css(' table')
            table_2 = block_2.css(' table')
            table_3 = block_3.css(' table')
            table_4 = block_4.css(' table')
            table_5 = block_5.xpath('./div[1]/div/table')



            big_img = photo.xpath('//ul[@class="big_img"]//a/@href').extract()
            small_img = photo.xpath('//ul[@class="small_img"]//a/@href').extract()

            #Строки в первом блоке
            contact = table_1.xpath('//tr[th/text()="\r\n                    Контакты менеджеров:\r\n                "]/td/text()').extract()
            rnumber = table_1.xpath('//tr[th/text()="\r\n                    Реестровый номер:\r\n                "]/td/text()').extract()
            use =   table_1.xpath('//tr[th/text()="\r\n                    Назначение:\r\n                "]/td/text()').extract()
            type = table_1.xpath('//tr[th/text()="\r\n                    Тип объекта:\r\n                "]/td/text()').extract()
            area = table_1.xpath('//tr[th/text()="\r\n                    Район:\r\n                "]/td/text()').extract()
            space_cars = table_1.xpath('//tr[th/text()="\r\n                    Площадь машиноместа, кв.м:\r\n                "]/td/text()').extract()
            land_plot_rea = table_1.xpath('//tr[th/text()="\r\n                    Площадь земельного участка:\r\n                "]/td/text()').extract()
            metro = table_1.xpath('//tr[th/text()="\r\n                    Ближайшая станция метро:\r\n                "]/td/text()').extract()
            area_garage = table_1.xpath('//tr[th/text()="\r\n                    Площадь гаража, кв.м:\r\n                "]/td/text()').extract()
            distance = table_1.xpath('//tr[th/text()="\r\n                    Расстояние до метро, км:\r\n                "]/td/text()').extract()
            l_area = table_1.xpath('//tr[th/text()="\r\n                    Жилая площадь, кв.м:\r\n                "]/td/text()').extract()
            n_area = table_1.xpath('//tr[th/text()="\r\n                    Нежилая площадь, кв.м:\r\n                "]/td/text()').extract()
            area_o = table_1.xpath('//tr[th/text()="\r\n                    Площадь объекта, кв.м:\r\n                "]/td/text()').extract()
            price = table_1.xpath('//tr[th/text()="\r\n                    Начальная цена, руб.:\r\n                "]/td/text()').extract()

            #Строки во втором блоке
            elevator = table_2.xpath('//tr[th/text()="\r\n                                        Наличие лифта\r\n                                    "]/td/text()').extract()
            f_elevator = table_2.xpath('//tr[th/text()="\r\n                                        Наличие грузового лифта\r\n                                    "]/td/text()').extract()
            parck_place = table_2.xpath('//tr[th/text()="\r\n                                        Наличие парковки\r\n                                    "]/td/text()').extract()
            telephone = table_2.xpath('//tr[th/text()="\r\n                                        Наличие телефонных линий\r\n                                    "]/td/text()').extract()
            security = table_2.xpath('//tr[th/text()="\r\n                                        Наличие охраны на объекте\r\n                                    "]/td/text()').extract()
            type_entrance = table_2.xpath('//tr[th/text()="\r\n                                        Тип входа в здание\r\n                                    "]/td/text()').extract()
            buld_type = table_2.xpath('//tr[th/text()="\r\n                                        Тип здания\r\n                                    "]/td/text()').extract()
            wall_material = table_2.xpath('//tr[th/text()="\r\n                                        Материал стен\r\n                                    "]/td/text()').extract()
            storey = table_2.xpath('//tr[th/text()="\r\n                                        Этажность дома\r\n                                    "]/td/text()').extract()
            line_house = table_2.xpath('//tr[th/text()="\r\n                                        Линия домов\r\n                                    "]/td/text()').extract()
            number_room = table_2.xpath('//tr[th/text()="\r\n                                            Номер помещения\r\n                                        "]/td/text()').extract()
            floor = table_2.xpath('//tr[th/text()="\r\n                                            этаж\r\n                                        "]/td/text()').extract()


            #Строки в третьем блоке
            type_b = table_3.xpath('//tr[th/text()="\r\n                    Вид торгов:\r\n                "]/td/text()').extract()
            form_b = table_3.xpath('//tr[th/text()="\r\n                    Форма торгов:\r\n                "]/td/text()').extract()
            subject = table_3.xpath('//tr[th/text()="\r\n                    Предмет торгов:\r\n                "]/td/text()').extract()
            t_floor = table_3.xpath('//tr[th/text()="\r\n                    Площадка торгов:\r\n                "]/td/a/text()').extract()
            t_floor_2 = table_3.xpath('//tr[th/text()="\r\n                    Площадка торгов:\r\n                "]/td/a/@href').extract()
            link = table_3.xpath('//tr[th/text()="\r\n                    Ссылка на torgi.gov.ru:\r\n                "]/td/a/text()').extract()
            link_2 = table_3.xpath('//tr[th/text()="\r\n                    Ссылка на torgi.gov.ru:\r\n                "]/td/a/@href').extract()
            type_p = table_3.xpath('//tr[th/text()="\r\n                    Вид начальной цены:\r\n                "]/td/text()').extract()
            size_deposit = table_3.xpath('//tr[th/text()="\r\n                    Размер задатка, руб.:\r\n                "]/td/text()').extract()
            lease_term = table_3.xpath('//tr[th/text()="\r\n                    Срок аренды:\r\n                "]/td/text()').extract()
            status = table_3.xpath('//tr[th/text()="\r\n                    Статус торгов:\r\n                "]/td/text()').extract()
            victor = table_3.xpath('//tr[th/text()="\r\n                    Победитель:\r\n                "]/td/text()').extract()
            total_price = table_3.xpath('//tr[th/text()="\r\n                    Итоговая цена:\r\n                "]/td/text()').extract()
            list_documents = table_3.xpath('//tr[th/text()="\r\n                    Перечень предоставляемых документов:\r\n                "]/td/text()').extract()
            inspection = table_3.xpath('//tr[th/text()="\r\n                    Осмотр объекта:\r\n                "]/td/text()').extract()

            #Строки в четвертом блоке
            acceptance_ap = table_4.xpath('//tr[th/text()="\r\n                    Прием заявок:\r\n                "]/td/text()').extract()
            selection = table_4.xpath('//tr[th/text()="\r\n                    Отбор участников:\r\n                "]/td/text()').extract()
            bidding = table_4.xpath('//tr[th/text()="\r\n                    Проведение торгов:\r\n                "]/td/text()').extract()
            summarizing = table_4.xpath('//tr[th/text()="\r\n                    Подведение итогов:\r\n                "]/td/text()').extract()

            #Строки в пятом блоке
            lot_documentation = table_5.xpath('//tr[th/a/text()="\r\n                                Лотовая документация\r\n                            "]/td/a/@href').extract()
            lot_documentation_2 = table_5.xpath('//tr[th/a/text()="\r\n                                Лотовая документация\r\n                            "]/td[2]/text()').extract()
            other = table_5.xpath('//tr[th/a/text()="\r\n                                Иное\r\n                            "]/td/a/@href').extract()
            other_2 = table_5.xpath('//tr[th/a/text()="\r\n                                Иное\r\n                            "]/td[2]/text()').extract()
            passport_object = table_5.xpath('//tr[th/a/text()="\r\n                                Паспорт объекта\r\n                            "]/td/a/@href').extract()
            passport_object_2 = table_5.xpath('//tr[th/a/text()="\r\n                                Паспорт объекта\r\n                            "]/td[2]/text()').extract()
            application_review = table_5.xpath('//tr[th/a/text()="\r\n                                Протокол рассмотрения заявок\r\n                            "]/td/a/@href').extract()
            application_review_2 = table_5.xpath('//tr[th/a/text()="\r\n                                Протокол рассмотрения заявок\r\n                            "]/td[2]/text()').extract()
            bidding_protocol = table_5.xpath('//tr[th/a/text()="\r\n                                Протокол торгов\r\n                            "]/td/a/@href').extract()
            bidding_protocol_2 = table_5.xpath('//tr[th/a/text()="\r\n                                Протокол торгов\r\n                            "]/td[2]/text()').extract()
            changes = table_5.xpath('//tr[th/a/text()="\r\n                                Сообщение о внесении изменений\r\n                            "]/td/a/@href').extract()
            changes_2 = table_5.xpath('//tr[th/a/text()="\r\n                                Сообщение о внесении изменений\r\n                            "]/td[2]/text()').extract()
            tender = table_5.xpath('//tr[th/a/text()="\r\n                                Извещение о торгах\r\n                            "]/td/a/@href').extract()
            tender_2 = table_5.xpath('//tr[th/a/text()="\r\n                                Извещение о торгах\r\n                            "]/td[2]/text()').extract()
            campaign_extension = table_5.xpath('//tr[th/a/text()="\r\n                                Сообщение о продлении заявочной кампании\r\n                            "]/td/a/@href').extract()
            campaign_extension_2 = table_5.xpath('//tr[th/a/text()="\r\n                                Сообщение о продлении заявочной кампании\r\n                            "]/td[2]/text()').extract()

            #Координаты с карты
            coord = item.xpath('//*[@id="content"]/script/text()').extract() # текст js
            coords = coord[0]
            start = coords.find('[') + 1 # (первое вхождение "[") + 1
            end = coords.rfind(']') # последнее вхождение "]"
            string = coords[start:end] # Строка с необходимыми нам данными
            parsed_coord =  json.loads(string) #Преобразование в словарь

            coords_p = parsed_coord["Coords"] # взятие координат по ключу
            id = parsed_coord["Id"] # взятие id по ключу

            # словарь
            yield {
                #primaryInfo
                'Infa_about_object': block_1.css('div.tender-card__description div::text').extract_first(),
                'Contacts_managers': contact,
                'Registry number': rnumber,
                'Appointment': use,
                'Object_type': type,
                'Area': area,
                'Space_cars, sq.m': space_cars,
                'Land_plot_rea': land_plot_rea,
                'Nearest_metro_station': metro,
                'Area_garage, sq.m.': area_garage,
                'Distance_to_metro, km': distance,
                'Living_area, sq.m': l_area,
                'Non-residential_area, sq.m.': n_area,
                'Area_object, sq.m.': area_o,
                'Initial_price, rub': price,
                #secondaryInfo
                'Elevator': elevator,
                'Freight_elevator': f_elevator,
                'Parking_place': parck_place,
                'Telephone_lines': telephone,
                'Security_site': security,
                'Type_entrance_building': type_entrance,
                'Building_type': buld_type,
                'Wall_Material': wall_material,
                'Storey_house': storey,
                'Line_houses': line_house,
                'Number_room': number_room,
                'floor': floor,
                # auctionInfo
                'Type_bidding': type_b,
                'Bidding_form': form_b,
                'Tender_subject': subject,
                'Trading_floor': t_floor,
                'Trading_floor_2': t_floor_2,
                'Link to torgi.gov.ru': link,
                'Link_2_to torgi.gov.ru': link_2,
                'Type_initial_price': type_p,
                'Size_deposit, rub.': size_deposit,
                'Lease_term': lease_term,
                'Status_trades': status,
                'Victor': victor,
                'Total_price': total_price,
                'List_provided_documents': list_documents,
                'Object_inspection': inspection,
                # procedureInfo
                'Acceptance_applications': acceptance_ap,
                'Selection_participants': selection,
                'Bidding': bidding,
                'Summarizing': summarizing,
                # attachedFiles
                'Lot_documentation': lot_documentation,
                'Lot_documentation_2': lot_documentation_2,
                'Other':other,
                'Other_2': other_2,
                'Passport_object': passport_object,
                'Passport_object_2': passport_object_2,
                'Application_review_protocol': application_review,
                'Application_review_protocol_2': application_review_2,
                'Bidding_protocol': bidding_protocol,
                'Bidding_protocol_2': bidding_protocol_2,
                'Notice_changes': changes,
                'Notice_changes_2':changes_2 ,
                'Notice_tender': tender,
                'Notice_tender_2': tender_2,
                'Extension_application_campaign': campaign_extension,
                'Extension_application_campaign_2': campaign_extension_2,
                #Photo
                'Photo_main': big_img,
                'Photo': small_img,
                #Coordinates on the map and Id
                'Coordinates': coords_p,
                'Id': id,

            }
        # итерируемся по url страниц
        for next_page in responce.css('div.pager a::attr(href)'):
            yield responce.follow(next_page, self.parse)



