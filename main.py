import requests
import json
import csv
import os

# Flipkart Affiliate Keys
fkAffiliateId = 'ankitjain21'
fkAffiliateToken = 'd349526c4d45448aa11af14cdd7224aa'

# Folder Name
directory = 'Products'

# Set Headers
headers = {
    'content-type': 'application/json',
    'Fk-Affiliate-Token': fkAffiliateToken,
    'Fk-Affiliate-Id': fkAffiliateId
}

# Create Dir if not exits
if not os.path.exists(directory):
    os.makedirs(directory)

# For fetching all the products categories
r_categories = requests.get(
    'https://affiliate-api.flipkart.net/affiliate/api/'
    + fkAffiliateId + '.json'
)
# Get Categories from the data
categories = json.loads(r_categories.text)
categories = categories['apiGroups']['affiliate']['apiListings']
try:
    # Traverse all the Categories
    for i in categories:
        # Get API URL of each Product V1.1.0
        url = categories[i]['availableVariants']['v1.1.0']['get']

        # Fetch products data
        r_data = requests.get(url, headers=headers)
        data = json.loads(r_data.text)
        products = data['products']
        # Create CSV file
        f = open(directory + "/" + i + ".csv", "w+")
        writer = csv.writer(f)
        # CSV Header,
        writer.writerow([
            "title", "productId", "productDescription", "imageUrls",
            "productFamily", "maximumRetailPrice", "flipkartSellingPrice",
            "flipkartSpecialPrice", "productUrl", "productBrand", "inStock",
            "codAvailable", "discountPercentage", "offers", "categoryPath",
            "size", "color", "storage", "sizeUnit", "displaySize",
            "shippingCharges", "estimatedDeliveryTime", "sellerName",
            "sellerAverageRating", "sellerNoOfRatings", "sellerNoOfReviews",
        ])
        # Traverse each product
        for j in products:
            # Exception Handling
            try:
                # Write each product data in CSV file
                writer.writerow([
                    j['productBaseInfoV1']['title'],
                    j['productBaseInfoV1']['productId'],
                    j['productBaseInfoV1']['productDescription'],
                    j['productBaseInfoV1']['imageUrls']['400x400'],
                    ','.join(j['productBaseInfoV1']['productFamily']),
                    j['productBaseInfoV1']['maximumRetailPrice']['currency'] +
                    " " + str(
                        j['productBaseInfoV1']['maximumRetailPrice']['amount']
                    ),
                    j['productBaseInfoV1']['flipkartSellingPrice']['currency'] +
                    " " + str(
                        j['productBaseInfoV1']['flipkartSellingPrice']['amount']
                    ),
                    j['productBaseInfoV1']['flipkartSpecialPrice']['currency'] +
                    " " + str(
                        j['productBaseInfoV1']['flipkartSpecialPrice']['amount']
                    ),
                    j['productBaseInfoV1']['productUrl'],
                    j['productBaseInfoV1']['productBrand'],
                    j['productBaseInfoV1']['inStock'],
                    j['productBaseInfoV1']['codAvailable'],
                    j['productBaseInfoV1']['discountPercentage'],
                    ','.join(j['productBaseInfoV1']['offers']),
                    j['productBaseInfoV1']['categoryPath'],
                    j['productBaseInfoV1']['attributes']['size'],
                    j['productBaseInfoV1']['attributes']['color'],
                    j['productBaseInfoV1']['attributes']['storage'],
                    j['productBaseInfoV1']['attributes']['sizeUnit'],
                    j['productBaseInfoV1']['attributes']['displaySize'],
                    j['productShippingInfoV1']['shippingCharges']['currency'] + " " + str(j['productShippingInfoV1']['shippingCharges']['amount']),
                    j['productShippingInfoV1']['estimatedDeliveryTime'],
                    j['productShippingInfoV1']['sellerName'],
                    j['productShippingInfoV1']['sellerAverageRating'],
                    j['productShippingInfoV1']['sellerNoOfRatings'],
                    j['productShippingInfoV1']['sellerNoOfReviews'],
                ])
            except:
                # Pass if any exceptions occurs so that script continues to
                # fetch other products data
                pass
        # Close the file object
        f.close()
except Exception as e:
    print(e)
    pass
