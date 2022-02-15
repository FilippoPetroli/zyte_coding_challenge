import scrapy

class BooksSpider(scrapy.Spider):
	name = 'books'

	start_urls = [
		'https://books.toscrape.com/',
	]
	
	def parse(self, response):
		for category in response.css('ul.nav li ul li a'):
			yield response.follow(category, callback = self.parse_book)

		

		
	
	def parse_book(self, response):
		for book in response.css('.product_pod'):
			yield {
				'title': book.css('h3 a::attr(title)').get(),
				'price': book.css('.product_price p::text').get(),
				'image_url': response.urljoin(book.css('.image_container img::attr(src)').get()),
				'details_url': response.urljoin(book.css('h3 a::attr(href)').get())
			}

		next_page = response.css('ul.pager li.next a::attr(href)').get()
		if next_page is not None:
			yield response.follow(next_page, callback = self.parse_book)