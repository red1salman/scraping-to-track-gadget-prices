In this project, we web scrap graphics cards products for sale off newegg.com. We tabularize and turn it into a data set. Running the python script anytime will create a csv file and update the webpage's data on it with each graphics card's brand, product name, and shipping. 

We grab the URL of the product page of [newegg.com](httpnewegg.com) and paste it into the script.

The script uses two packages, Beautiful Soup and URL lib 

The Beautiful Soup package is a good way to parse HTML text through Python. In the other package URL lib, there is a module called request and inside of that module, we will use a function called URL open. This will use web client to grab something from the Internet. 

In this project, Beautiful soup is going to parse HTML text from the URL and URL lib (uClient variable) is going to grab the webpage itself and download [it.](httpit.to)
