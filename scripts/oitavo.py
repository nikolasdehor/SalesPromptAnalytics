def top_countries(data, platform_name, n=5):
    country_revenue = data.groupby('delivery_country')['total_price'].sum().nlargest(n).reset_index()
    country_revenue['Platform'] = platform_name
    return country_revenue

# Gerar rankings
top_aliexpress = top_countries(aliexpress_data, "AliExpress")
top_etsy = top_countries(etsy_data, "Etsy")
top_shopee = top_countries(shopee_data, "Shopee")

# Unir resultados
top_countries_df = pd.concat([top_aliexpress, top_etsy, top_shopee], ignore_index=True)
top_countries_df.rename(columns={'delivery_country': 'Country', 'total_price': 'Total Revenue'}, inplace=True)
top_countries_df