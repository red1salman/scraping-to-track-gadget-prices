import requests
from bs4 import BeautifulSoup as soup

# URl to web scrap from.
# web scrap graphics cards from Newegg.com
my_url = "https://www.newegg.com/p/pl?d=graphics+cards"
page_soup = soup(requests.get(my_url).text, "html.parser")

# name the output file to write to local disk
out_filename = "graphics_cards.csv"
# header of csv file to be written
headers = "brand, product_name, shipping\n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)

# loops over each product and grabs attributes about
# each product

# exclude the recommendedItems as it does not have shipping info
for container in page_soup.select(':not(#recommendItems).items-view .item-container'):

    brand = container.select_one('a.item-brand img[alt]')['alt']
    product_name = container.select_one('a.item-title').get_text(strip=True)
    shipping = container.select_one('li.price-ship').get_text(strip=True).replace("$", "").replace(" Shipping", "")

    print("brand: ", brand + "\n")
    print("product_name: ", product_name + "\n")
    print("shipping: ", shipping + "\n")

    # writes the dataset to file

    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()  # Close the file

