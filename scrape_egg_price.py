import pandas as pd
from datetime import datetime

# Load the HTML table into a list of DataFrames
url = "https://e2necc.com/home/eggprice"
df_list = pd.read_html(url)

# Assuming the table of interest is the second one (index 1) in the list
table_data = df_list[1]

# Filter data for Namakkal
namakkal_data = table_data[table_data["Name Of Zone / Day"] == "Namakkal"]

# Get today's date in the format it appears in the DataFrame
today_date = datetime.today().strftime('%d')

# Extract today's price
today_price = namakkal_data.iloc[0][today_date]

# Check if the price is "-"
if today_price == "-":
    final = "The rate is same as the previous price!"
else:
    final = f"Today's egg price in Namakkal: {today_price} paise"

print(final)
