import bs4
import requests
import csv

url = requests.get('https://www.newegg.com/Laptops-Notebooks/Category/ID-223?Tpk=laptop')
soup = bs4.BeautifulSoup(url.text,'html.parser')

containers = soup.select('.item-container')

csv_file = open('laptop.csv', 'w')
csv_writer = csv.writer(csv_file)


csv_writer.writerow(['Brand' ,'Product','Price','Shiping'])

for container in containers:
	brands = container.select('.item-branding')
	brand = brands[0].img['title'].strip()

	spek = container.select('.item-title')
	speks = spek[0].text.strip()

	prices = container.select('.price-current')
	price = prices[0].text.strip()

	ship = container.select('.price-ship')
	shiping = ship[0].text.strip()

	print("Brand: " + brand)
	print("Product: " + speks)
	print("Price: " + price)
	print("Shiping: " + shiping)
	csv_writer.writerow([brand ,speks,price,shiping])

csv_file.close()

