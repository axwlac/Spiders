import scrapy

class CSpider(scrapy.Spider):
    def __init__(self):
        self.i = 2

    name = 'Gomita'
    start_urls=['https://www.azucardulcerias.com/collections/los-mas-buscados?page=1']
    
    def parse(self, response):
        for p in response.css('div.desc'): 
            if(p.css('a::text').get() != None): 
                yield {
                    'Nombre': p.css('a::text').get(),
                    'Precio': p.css('span.money::text').get().replace('$','')
                }
        
        next_page = f'https://www.azucardulcerias.com/collections/los-mas-buscados?page={self.i}'
        self.i = self.i+1
        if(self.i<=20): 
            yield response.follow(next_page, callback=self.parse)