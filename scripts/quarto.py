# Function to find the most popular product by country for a platform
def most_popular_by_country(data, platform_name):
    grouped = data.groupby(["delivery_country", "product_sold"])["quantity"].sum().reset_index()
    most_popular = grouped.loc[grouped.groupby("delivery_country")["quantity"].idxmax()]
    most_popular["Platform"] = platform_name
    return most_popular

# Get the most popular products by country for each platform
popular_aliexpress = most_popular_by_country(aliexpress_data, "AliExpress")
popular_etsy = most_popular_by_country(etsy_data, "Etsy")
popular_shopee = most_popular_by_country(shopee_data, "Shopee")

# Combine results into a single DataFrame
popular_products = pd.concat([popular_aliexpress, popular_etsy, popular_shopee], ignore_index=True)
popular_products.rename(columns={"delivery_country": "Country", "product_sold": "Most Popular Product", "quantity": "Total Quantity"}, inplace=True)
popular_products

