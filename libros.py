# -*- coding: utf-8 -*-
import scrapy


class LibrosSpider(scrapy.Spider):
    name = 'libros'
    page_number = 2
    allowed_domains = ['tienda.fciencias.unam.mx/en/4-mathematics']
    start_urls = ['http://tienda.fciencias.unam.mx/en/4-mathematics/']

    def parse(self, response):
    	productos = response.xpath('.//*[@class="thumbnail-container"]')
    	for libro in productos:
        	titulos = libro.xpath('.//*[@class="h3 product-title"]/a/text()').extract()
        	precios = libro.xpath('.//*[@class="price"]/text()').extract()
        
        	#yield{'titulo':titulos,
              	#      'precio':precios}
        
   	next_page = 'https://tienda.fciencias.unam.mx/en/4-mathematics?page=2'+str(LibrosSpider.page_number)
        page_number = page_number + 1
        if page_number <= 4:
        	yield response.follow(next_page, callback = self.parse)

        
        #i += 1
	#url = 'https://tienda.fciencias.unam.mx/en/4-mathematics/page=2'
	
	#nexturl = ''
	#for k in range(len(url)-1):
		#nexturl += url[k]
	#url[len(url)-1] = str(i)
	#nexturl += str(i)
	#print(url)
	
	#yield scrapy.Request()   
	
	
