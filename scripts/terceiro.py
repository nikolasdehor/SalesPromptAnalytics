# Function to find the most sold product
def most_sold_product(data, platform_name):
    most_sold = data.groupby("product_sold")["quantity"].sum().idxmax()
    total_quantity = data.groupby("product_sold")["quantity"].sum().max()
    return {"Platform": platform_name, "Most Sold Product": most_sold, "Total Quantity": total_quantity}

# Determine the most sold product for each platform
most_sold_aliexpress = most_sold_product(aliexpress_data, "AliExpress")
most_sold_etsy = most_sold_product(etsy_data, "Etsy")
most_sold_shopee = most_sold_product(shopee_data, "Shopee")

# Combine results into a DataFrame for easier readability
most_sold_df = pd.DataFrame([most_sold_aliexpress, most_sold_etsy, most_sold_shopee])
most_sold_df
