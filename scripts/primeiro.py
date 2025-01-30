import pandas as pd

# File paths
aliexpress_path = '/mnt/data/Meganium_Sales_Data_-_AliExpress.csv'
etsy_path = '/mnt/data/Meganium_Sales_Data_-_Etsy.csv'
shopee_path = '/mnt/data/Meganium_Sales_Data_-_Shopee.csv'

# Load data from CSV files
aliexpress_data = pd.read_csv(aliexpress_path)
etsy_data = pd.read_csv(etsy_path)
shopee_data = pd.read_csv(shopee_path)

# Check the first few rows and structure of the data
aliexpress_summary = aliexpress_data.head(), aliexpress_data.info()
etsy_summary = etsy_data.head(), etsy_data.info()
shopee_summary = shopee_data.head(), shopee_data.info()

aliexpress_data_shape = aliexpress_data.shape
etsy_data_shape = etsy_data.shape
shopee_data_shape = shopee_data.shape

aliexpress_summary, etsy_summary, shopee_summary, aliexpress_data_shape, etsy_data_shape, shopee_data_shape
