def monthly_sales_trend(data, platform_name):
    data['date'] = pd.to_datetime(data['date'])  # Assume coluna 'date' nos CSVs
    data['month_year'] = data['date'].dt.to_period('M')
    monthly = data.groupby('month_year').agg(
        Total_Quantity=('quantity', 'sum'),
        Total_Revenue=('total_price', 'sum')
    ).reset_index()
    monthly['Platform'] = platform_name
    return monthly

# Aplicar função
monthly_aliexpress = monthly_sales_trend(aliexpress_data, "AliExpress")
monthly_etsy = monthly_sales_trend(etsy_data, "Etsy")
monthly_shopee = monthly_sales_trend(shopee_data, "Shopee")

# Combinar resultados
monthly_trends = pd.concat([monthly_aliexpress, monthly_etsy, monthly_shopee], ignore_index=True)
monthly_trends