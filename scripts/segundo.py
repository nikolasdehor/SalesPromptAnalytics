# Function to summarize sales data
def summarize_sales(data, platform_name):
    summary = {
        "Platform": platform_name,
        "Total Quantity Sold": data["quantity"].sum(),
        "Total Revenue": data["total_price"].sum(),
        "Average Discount": data["discount_value"].mean()
    }
    return summary

# Summarize sales for each platform
aliexpress_summary = summarize_sales(aliexpress_data, "AliExpress")
etsy_summary = summarize_sales(etsy_data, "Etsy")
shopee_summary = summarize_sales(shopee_data, "Shopee")

# Combine summaries into a DataFrame for easier readability
summary_df = pd.DataFrame([aliexpress_summary, etsy_summary, shopee_summary])
summary_df
