def discount_effectiveness(data, platform_name):
    discounted = data[data['discount_value'] > 0]
    regular = data[data['discount_value'] == 0]
    
    effectiveness = {
        "Platform": platform_name,
        "Discounted_Sales": discounted['quantity'].sum(),
        "Regular_Sales": regular['quantity'].sum(),
        "Discount_Impact_Ratio": round(len(discounted) / len(data), 2)
    }
    return effectiveness

# Aplicar análise
discount_aliexpress = discount_effectiveness(aliexpress_data, "AliExpress")
discount_etsy = discount_effectiveness(etsy_data, "Etsy")
discount_shopee = discount_effectiveness(shopee_data, "Shopee")

# Consolidar
discount_df = pd.DataFrame([discount_aliexpress, discount_etsy, discount_shopee])
discount_df