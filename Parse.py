import scrapy
import json

#tendersListWraper

class BashSpider(scrapy.Spider):
    # имя парсера(поискового робота)
    name = 'BashSpider'
    # ссылока на начальную страницу для парсинга
    start_urls = ['https://investmoscow.ru/tenders/tendercard/?tenderId=16992527']

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
            infa = block_1.css('div.tender-card__description div::text').extract_first()
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

            if len(infa) > 0:
                infa.replace('\r\n', '')
                infa_object = ' '.join(infa.split())
            else:
                infa_object = 'None'

            if len(contact) > 0:
                contact[0].replace('\r\n', '')
                contact[1].replace('\r\n', '')
                contact_m = ' '.join(contact[0].split())
                telephone_n = ' '.join(contact[1].split())
            else:
                contact_m = 'None'
                telephone_n = 'None'

            if len(rnumber) > 0:
                rnumber[0].replace('\r\n', '')
                rnumber_n = ' '.join(rnumber[0].split())
            else:
                rnumber_n = 'None'

            if len(use) > 0:
                use[0].replace('\r\n', '')
                use_n =  ' '.join(use[0].split())
            else:
                use_n = 'None'

            if len(type) > 0:
                type[0].replace('\r\n', '')
                type_n =  ' '.join(type[0].split())
            else:
                type_n = 'None'

            if len(area) > 0:
                area[0].replace('\r\n', '')
                area_n = ' '.join(area[0].split())
            else:
                area_n = 'None'

            if len(space_cars) > 0:
                space_cars[0].replace('\r\n', '')
                space_cars_n = ' '.join(space_cars[0].split())
            else:
                space_cars_n = 'None'

            if len(land_plot_rea) > 0:
                land_plot_rea[0].replace('\r\n', '')
                land_plot_rea_n = ' '.join(land_plot_rea[0].split())
            else:
                land_plot_rea_n = 'None'

            if len(metro) > 0:
                metro[0].replace('\r\n', '')
                metro_n = ' '.join(metro[0].split())
            else:
                metro_n = 'None'

            if len(area_garage) > 0:
                area_garage[0].replace('\r\n', '')
                area_garage_n = ' '.join(area_garage[0].split())
            else:
                area_garage_n = 'None'

            if len(distance) > 0:
                distance[0].replace('\r\n', '')
                distance_n = ' '.join(distance[0].split())
            else:
                distance_n = 'None'

            if len(l_area) > 0:
                l_area[0].replace('\r\n', '')
                l_area_n = ' '.join(l_area[0].split())
            else:
                l_area_n = 'None'

            if len(n_area) > 0:
                n_area[0].replace('\r\n', '')
                n_area_n = ' '.join(n_area[0].split())
            else:
                n_area_n = 'None'

            if len(area_o) > 0:
                area_o[0].replace('\r\n', '')
                area_o_n = ' '.join(area_o[0].split())
            else:
                area_o_n = 'None'

            if len(price) > 0:
                price[0].replace('\r\n', '')
                price_n = ' '.join(price[0].split())
            else:
                price_n = 'None'

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

            if len(elevator) > 0:
                elevator[0].replace('\r\n', '')
                elevator_n = ' '.join(elevator[0].split())
            else:
                elevator_n = 'None'

            if len(f_elevator) > 0:
                f_elevator[0].replace('\r\n', '')
                f_elevator_n = ' '.join(f_elevator[0].split())
            else:
                f_elevator_n = 'None'

            if len(parck_place) > 0:
                parck_place[0].replace('\r\n', '')
                parck_place_n = ' '.join(parck_place[0].split())
            else:
                parck_place_n = 'None'

            if len(telephone) > 0:
                telephone[0].replace('\r\n', '')
                telephone_n = ' '.join(telephone[0].split())
            else:
                telephone_n = 'None'

            if len(security) > 0:
                security[0].replace('\r\n', '')
                security_n = ' '.join(security[0].split())
            else:
                security_n = 'None'

            if len(type_entrance) > 0:
                type_entrance[0].replace('\r\n', '')
                type_entrance_n = ' '.join(type_entrance[0].split())
            else:
                type_entrance_n = 'None'

            if len(buld_type) > 0:
                buld_type[0].replace('\r\n', '')
                buld_type_n = ' '.join(buld_type[0].split())
            else:
                buld_type_n = 'None'

            if len(wall_material) > 0:
                wall_material[0].replace('\r\n', '')
                wall_material_n = ' '.join(wall_material[0].split())
            else:
                wall_material_n = 'None'

            if len(storey) > 0:
                storey[0].replace('\r\n', '')
                storey_n = ' '.join(storey[0].split())
            else:
                storey_n = 'None'

            if len(line_house) > 0:
                line_house[0].replace('\r\n', '')
                line_house_n = ' '.join(line_house[0].split())
            else:
                line_house_n = 'None'

            if len(number_room) > 0:
                number_room[0].replace('\r\n', '')
                number_room_n = ' '.join(number_room[0].split())
            else:
                number_room_n = 'None'

            if len(floor) > 0:
                floor[0].replace('\r\n', '')
                floor_n = ' '.join(floor[0].split())
            else:
                floor_n = 'None'


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

            if len(type_b) > 0:
                type_b[0].replace('\r\n', '')
                type_b_n = ' '.join(type_b[0].split())
            else:
                type_b_n = 'None'

            if len(form_b) > 0:
                form_b[0].replace('\r\n', '')
                form_b_n = ' '.join(form_b[0].split())
            else:
                form_b_n = 'None'

            if len(subject) > 0:
                subject[0].replace('\r\n', '')
                subject_n = ' '.join(subject[0].split())
            else:
                subject_n = 'None'

            if len(t_floor) > 0:
                t_floor[0].replace('\r\n', '')
                t_floor_n = ' '.join(t_floor[0].split())
            else:
                t_floor_n = 'None'

            if len(t_floor_2) > 0:
                t_floor_2[0].replace('\r\n', '')
                t_floor_2_n = ' '.join(t_floor_2[0].split())
            else:
                t_floor_2_n = 'None'

            if len(link) > 0:
                link[0].replace('\r\n', '')
                link_n = ' '.join(link[0].split())
            else:
                link_n = 'None'

            if len(link_2) > 0:
                link_2[0].replace('\r\n', '')
                link_2_n = ' '.join(link_2[0].split())
            else:
                link_2_n = 'None'

            if len(type_p) > 0:
                type_p[0].replace('\r\n', '')
                type_p_n = ' '.join(type_p[0].split())
            else:
                type_p_n = 'None'

            if len(size_deposit) > 0:
                size_deposit[0].replace('\r\n', '')
                size_deposit_n = ' '.join(size_deposit[0].split())
            else:
                size_deposit_n = 'None'

            if len(lease_term) > 0:
                lease_term[0].replace('\r\n', '')
                lease_term_n = ' '.join(lease_term[0].split())
            else:
                lease_term_n = 'None'

            if len(status) > 0:
                status[0].replace('\r\n', '')
                status_n = ' '.join(status[0].split())
            else:
                status_n = 'None'

            if len(victor) > 0:
                victor[0].replace('\r\n', '')
                victor_n = ' '.join(victor[0].split())
            else:
                victor_n = 'None'

            if len(total_price) > 0:
                total_price[0].replace('\r\n', '')
                total_price_n = ' '.join(total_price[0].split())
            else:
                total_price_n = 'None'

            if len(list_documents) > 0:
                list_documents[0].replace('\r\n', '')
                list_documents_n = ' '.join(list_documents[0].split())
            else:
                list_documents_n = 'None'

            if len(inspection) > 0:
                inspection[0].replace('\r\n', '')
                inspection_n = ' '.join(inspection[0].split())
            else:
                inspection_n = 'None'

            #Строки в четвертом блоке
            acceptance_ap = table_4.xpath('//tr[th/text()="\r\n                    Прием заявок:\r\n                "]/td/text()').extract()
            selection = table_4.xpath('//tr[th/text()="\r\n                    Отбор участников:\r\n                "]/td/text()').extract()
            bidding = table_4.xpath('//tr[th/text()="\r\n                    Проведение торгов:\r\n                "]/td/text()').extract()
            summarizing = table_4.xpath('//tr[th/text()="\r\n                    Подведение итогов:\r\n                "]/td/text()').extract()

            if len(acceptance_ap) > 0:
                acceptance_ap[0].replace('\r\n', '')
                acceptance_ap_n = ' '.join(acceptance_ap[0].split())
            else:
                acceptance_ap_n = 'None'

            if len(selection) > 0:
                selection[0].replace('\r\n', '')
                selection_n = ' '.join(selection[0].split())
            else:
                selection_n = 'None'

            if len(bidding) > 0:
                bidding[0].replace('\r\n', '')
                bidding_n = ' '.join(bidding[0].split())
            else:
                bidding_n = 'None'

            if len(summarizing) > 0:
                summarizing[0].replace('\r\n', '')
                summarizing_n = ' '.join(summarizing[0].split())
            else:
                summarizing_n = 'None'

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

            if len(lot_documentation) > 0:
                lot_documentation_m = []
                for i in range(len(lot_documentation)):
                    lot_documentation[i].replace('\r\n', '')
                    lot_documentation_n = ' '.join(lot_documentation[i].split())
                    lot_documentation_m.append(lot_documentation_n)
            else:
                lot_documentation_m = 'None'

            if len(lot_documentation_2) > 0:
                lot_documentation_2_m = []
                for i in range(len(lot_documentation_2)):
                    lot_documentation_2[i].replace('\r\n', '')
                    lot_documentation_2_n = ' '.join(lot_documentation_2[i].split())
                    lot_documentation_2_m.append(lot_documentation_2_n)
            else:
                lot_documentation_2_m = 'None'

            if len(other) > 0:
                other_m = []
                for i in range(len(other)):
                    other[i].replace('\r\n', '')
                    other_n = ' '.join(other[i].split())
                    other_m.append(other_n)
            else:
                other_m = 'None'

            if len(other_2) > 0:
                other_2_m = []
                for i in range(len(other_2)):
                    other_2[i].replace('\r\n', '')
                    other_2_n = ' '.join(other_2[i].split())
                    other_2_m.append(other_2_n)
            else:
                other_2_m = 'None'

            if len(passport_object) > 0:
                passport_object_m = []
                for i in range(len(passport_object)):
                    passport_object[i].replace('\r\n', '')
                    passport_object_n = ' '.join(passport_object[i].split())
                    passport_object_m.append(passport_object_n)
            else:
                passport_object_m = 'None'

            if len(passport_object_2) > 0:
                passport_object_2_m = []
                for i in range(len(passport_object_2)):
                    passport_object_2[i].replace('\r\n', '')
                    passport_object_2_n = ' '.join(passport_object_2[i].split())
                    passport_object_2_m.append(passport_object_2_n)
            else:
                passport_object_2_m = 'None'

            if len(application_review) > 0:
                application_review_m = []
                for i in range(len(application_review)):
                    application_review[i].replace('\r\n', '')
                    application_review_n = ' '.join(application_review[i].split())
                    application_review_m.append(application_review_n)
            else:
                application_review_m = 'None'

            if len(application_review_2) > 0:
                application_review_2_m = []
                for i in range(len(application_review_2)):
                    application_review_2[i].replace('\r\n', '')
                    application_review_2_n = ' '.join(application_review_2[i].split())
                    application_review_2_m.append(application_review_2_n)
            else:
                application_review_2_m = 'None'

            if len(bidding_protocol) > 0:
                bidding_protocol_m = []
                for i in range(len(bidding_protocol)):
                    bidding_protocol[i].replace('\r\n', '')
                    bidding_protocol_n = ' '.join(bidding_protocol[i].split())
                    bidding_protocol_m.append(bidding_protocol_n)
            else:
                bidding_protocol_m = 'None'

            if len(bidding_protocol_2) > 0:
                bidding_protocol_2_m = []
                for i in range(len(bidding_protocol_2)):
                    bidding_protocol_2[i].replace('\r\n', '')
                    bidding_protocol_2_n = ' '.join(bidding_protocol_2[i].split())
                    bidding_protocol_2_m.append(bidding_protocol_2_n)
            else:
                bidding_protocol_2_m = 'None'

            if len(changes) > 0:
                changes_m = []
                for i in range(len(changes)):
                    changes[i].replace('\r\n', '')
                    changes_n = ' '.join(changes[i].split())
                    changes_m.append(changes_n)
            else:
                changes_m = 'None'

            if len(changes_2) > 0:
                changes_2_m = []
                for i in range(len(changes_2)):
                    changes_2[i].replace('\r\n', '')
                    changes_2_n = ' '.join(changes_2[i].split())
                    changes_2_m.append(changes_2_n)
            else:
                changes_2_m = 'None'

            if len(tender) > 0:
                tender_m = []
                for i in range(len(tender)):
                    tender[i].replace('\r\n', '')
                    tender_n = ' '.join(tender[i].split())
                    tender_m.append(tender_n)
            else:
                tender_m = 'None'

            if len(tender_2) > 0:
                tender_2_m = []
                for i in range(len(tender_2)):
                    tender_2[i].replace('\r\n', '')
                    tender_2_n = ' '.join(tender_2[i].split())
                    tender_2_m.append(tender_2_n)
            else:
                tender_2_m = 'None'

            if len(campaign_extension) > 0:
                campaign_extension_m = []
                for i in range(len(campaign_extension)):
                    campaign_extension[i].replace('\r\n', '')
                    campaign_extension_n = ' '.join(campaign_extension[i].split())
                    campaign_extension_m.append(campaign_extension_n)
            else:
                campaign_extension_m = 'None'

            if len(campaign_extension_2) > 0:
                campaign_extension_2_m = []
                for i in range(len(campaign_extension_2)):
                    campaign_extension_2[i].replace('\r\n', '')
                    campaign_extension_2_n = ' '.join(campaign_extension_2[i].split())
                    campaign_extension_2_m.append(campaign_extension_2_n)
            else:
                campaign_extension_2_m = 'None'

            #Координаты с карты
            coord = item.xpath('//*[@id="content"]/script/text()').extract() # текст js
            coords = coord[0]
            start = coords.find('[') + 1 # (первое вхождение "[") + 1
            end = coords.rfind(']') # последнее вхождение "]"
            string = coords[start:end] # Строка с необходимыми нам данными
            parsed_coord =  json.loads(string) #Преобразование в словарь

            coords_p = parsed_coord["Coords"][1:-1].split(',') # взятие координат по ключу
            id = parsed_coord["Id"] # взятие id по ключу

            # словарь
            yield {
                #primaryInfo
                'Infa_about_object': infa_object,
                'Contacts_managers': contact_m,
                'Telephone': telephone_n,
                'Registry number': rnumber_n,
                'Appointment': use_n,
                'Object_type': type_n,
                'Area': area_n,
                'Space_cars, sq.m': space_cars_n,
                'Land_plot_rea': land_plot_rea_n,
                'Nearest_metro_station': metro_n,
                'Area_garage, sq.m.': area_garage_n,
                'Distance_to_metro, km': distance_n,
                'Living_area, sq.m': l_area_n,
                'Non-residential_area, sq.m.': n_area_n,
                'Area_object, sq.m.': area_o_n,
                'Initial_price, rub': price_n,
                #secondaryInfo
                'Elevator': elevator_n,
                'Freight_elevator': f_elevator_n,
                'Parking_place': parck_place_n,
                'Telephone_lines': telephone_n,
                'Security_site': security_n,
                'Type_entrance_building': type_entrance_n,
                'Building_type': buld_type_n,
                'Wall_Material': wall_material_n,
                'Storey_house': storey_n,
                'Line_houses': line_house_n,
                'Number_room': number_room_n,
                'floor': floor_n,
                # auctionInfo
                'Type_bidding': type_b_n,
                'Bidding_form': form_b_n,
                'Tender_subject': subject_n,
                'Trading_floor': t_floor_n,
                'Trading_floor_2': t_floor_2_n,
                'Link to torgi.gov.ru': link_n,
                'Link_2_to torgi.gov.ru': link_2_n,
                'Type_initial_price': type_p_n,
                'Size_deposit, rub.': size_deposit_n,
                'Lease_term': lease_term_n,
                'Status_trades': status_n,
                'Victor': victor_n,
                'Total_price': total_price_n,
                'List_provided_documents': list_documents_n,
                'Object_inspection': inspection_n,
                # procedureInfo
                'Acceptance_applications': acceptance_ap_n,
                'Selection_participants': selection_n,
                'Bidding': bidding_n,
                'Summarizing': summarizing_n,
                # attachedFiles
                'Lot_documentation': lot_documentation_m,
                'Lot_documentation_2': lot_documentation_2_m,
                'Other':other_m,
                'Other_2': other_2_m,
                'Passport_object': passport_object_m,
                'Passport_object_2': passport_object_2_m,
                'Application_review_protocol': application_review_m,
                'Application_review_protocol_2': application_review_2_m,
                'Bidding_protocol': bidding_protocol_m,
                'Bidding_protocol_2': bidding_protocol_2_m,
                'Notice_changes': changes_m,
                'Notice_changes_2':changes_2_m,
                'Notice_tender': tender_m,
                'Notice_tender_2': tender_2_m,
                'Extension_application_campaign': campaign_extension_m,
                'Extension_application_campaign_2': campaign_extension_2_m,
                #Photo
                'Photo_main': big_img,
                'Photo': small_img,
                #Coordinates on the map and Id
                'Coordinates': coords_p,
                'Id': id,

            }
        # итерируемся по url страниц
        for next_page in responce.css('ul.pagination__page-list a::attr(href)'):
            yield responce.follow(next_page, self.parse)

