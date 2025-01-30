def average_order_value(data, platform_name):
    aov = data['total_price'].sum() / data['order_id'].nunique()  # Assume coluna 'order_id'
    return {"Platform": platform_name, "Average Order Value": round(aov, 2)}

# Calcular para cada plataforma
aov_aliexpress = average_order_value(aliexpress_data, "AliExpress")
aov_etsy = average_order_value(etsy_data, "Etsy")
aov_shopee = average_order_value(shopee_data, "Shopee")

# Criar DataFrame
aov_df = pd.DataFrame([aov_aliexpress, aov_etsy, aov_shopee])
aov_df