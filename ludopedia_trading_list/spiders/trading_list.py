# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


import scrapy


class TradingList(scrapy.Spider):
    name = "trading_list"
    start_urls = [
        'https://www.ludopedia.com.br/lista/10998/troca-de-jogos-ludopedia-setembro',
    ]

    def parse(self, response):
        for game in response.css('div.lista-item'):
            yield {
                'game_name': game.css('h3.mar-no::text').extract_first(),
                'item_id': game.css('div[data-bloco]').xpath('@id').extract_first(),
            }

        next_page = response.css('a[title="Próxima Página"]::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
