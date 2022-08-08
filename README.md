# carrefour-classifier
Product url classifier based on Carrefour categories

# Deliver:

• **The code used to scrape Carrefour's website:** 

Scrapping.ipynb

• **The raw data scraped from Carrefour:**

**I)pages_category.txt**

_Manually selected pages, with product listings for certain categories. In case you need to add products from a new category, just add the homepage link of this category in this file and run notebook Scrapping.ipynb_


**II)output_scrapping/**

_After scrapping the links present in pages_category.txt, all links to the pages of each product in the categories are extracted. On the Carrefour website, each category page features approximately 60 products on each category homepage._

Thus, 1729 product links were collected (~60 * 31 categories).

• **The cleaned data scraped from Carrefour.**

**I) all_products.csv**

_Columns in the file:Product Title, Link to Product, Processed Title Text, Category._

• **The code used to build, train and evaluate your model.**

Classification.ipynb

• **A document explaining how you tackled the problem.**
