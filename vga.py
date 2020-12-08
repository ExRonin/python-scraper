import bs4
import requests


url = requests.get('https://www.newegg.com/p/pl?d=vga')
soup = bs4.BeautifulSoup(url.text,'html.parser')

containers = soup.select('.item-container')


for container in containers:
	rate = container.select('.item-branding')
	rating = rate[0].text.strip()

	spek = container.select('.item-title')
	speks = spek[0].text.strip()

	ship = container.select('.price-ship')
	shiping = ship[0].text.strip()

	print("Rating: " + rating)
	print("Product: " + speks)
	print("Shiping: " + shiping)

