import pandas as pd
import time

def measure_runtime(func, *args, **kwargs):
    """
    Measures the runtime of a given function.

    Parameters:
    func (callable): The function to be timed.
    *args: Arguments to pass to the function.
    **kwargs: Keyword arguments to pass to the function.

    Returns:
    result: The result of the function execution.
    elapsed_time: The time the function took to execute (in seconds).
    """
    start_time = time.time()  # Start the timer
    result = func(*args, **kwargs)  # Execute the function
    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time  # Calculate elapsed time
    return result, elapsed_time

def analyze_data():
    # Load the data
    df = pd.read_excel('project_data.xlsx')
    print(df.head())

    # Number of unique shops
    un_shops = df.shopid.unique()
    print(f"num of shops {un_shops}")
    print(f"num of shops {len(un_shops)}")


    shops = df['shopid'].nunique() #returns the number of unique values for each column.
    print(f"Number of unique shops: {shops}") 

    # Number of unique shops that are both cross-border and preferred
    shops_pref_cb = df[(df['cb_option'] == 1) & (df['is_preferred'] == 1)]['shopid'].nunique()
    print(f"Number of unique shops cross border and preferred: {shops_pref_cb}")

    # Number of products with zero sold count
    products_zero_sold_count = df[df['sold_count'] == 0]['itemid'].nunique()
    print(f"Number of products with zero sold count: {products_zero_sold_count}")

    # Extract year from 'item_creation_date' and count products created in 2018
    df['item_creation_date'] = pd.to_datetime(df['item_creation_date'])  # Ensure it's in datetime format
    df['year'] = df['item_creation_date'].dt.year
    products_year_2018 = df[df['year'] == 2018]['itemid'].nunique()
    print(f"Number of products created in 2018: {products_year_2018}")

    # Group by 'shopid' and count unique 'item_id' for each shop
    shop_unique_products = df.groupby('shopid')['itemid'].nunique()
    # df[df['is_preferred']=='1'].groupby(['shopid'])['itemid'].count().sort_values(ascending = False)[0:3]

    # Sort the result in descending order and get the top 3 shop IDs
    top_3_shops = shop_unique_products.sort_values(ascending=False).head(3)

    print(f"Top 3 Preferred Shops with the largest number of unique products:\n {top_3_shops}")

    # Filter for cross-border products
    cross_border_products = df[df['cb_option'] == True]

    # Group by 'category' and count unique 'product_id' for each category
    category_unique_products = cross_border_products.groupby('category')['itemid'].nunique()

    # Sort the result in descending order and get the top 3 categories
    top_3_categories = category_unique_products.sort_values(ascending=False).head(3)

    print("Top 3 Categories with the largest number of unique cross-border products:")
    print(top_3_categories)

    # Add a new column for revenue calculation
    df['revenue'] = df['price'] * df['sold_count']

    # Group by 'shopid' and calculate the total revenue for each shop
    shop_revenue = df.groupby('shopid')['revenue'].sum()

    # Sort by revenue in descending order and select the top 3
    top_3_shops_by_revenue = shop_revenue.sort_values(ascending=False).head(3)

    print("Top 3 shopid with the highest revenue:")
    print(top_3_shops_by_revenue)


    # Count the number of variations for each product
    product_variation_counts = df.groupby('itemid').size()

    # Filter for products with more than 3 variations
    products_with_more_variations = product_variation_counts[product_variation_counts > 3]

    # Get the total number of products
    num_products_with_more_variations = len(products_with_more_variations)

    print(f"Number of products with more than 3 variations: {num_products_with_more_variations}")

    # Identify duplicated listings within each shop
    df['is_duplicated'] = df.duplicated(subset=['shopid', 'item_name', 'item_description', 'price'], keep=False)

    print("Duplicated listings have been marked in the 'is_duplicated' column.")

    # Filter for duplicated listings with sold_count < 2
    duplicated_listings = df[(df['is_duplicated'] == True) & (df['sold_count'] < 2)]

    # Save the result to an Excel file
    duplicated_listings.to_excel("duplicated_listings.xlsx", index=False)

    print("Duplicated listings with sold_count < 2 have been saved to 'duplicated_listings.xlsx'.")

    # Count duplicated listings for each shop
    shop_duplicated_counts = df[df['is_duplicated'] == True].groupby('shopid').size()

    # Find the shopid with the most duplicated listings
    preferred_shop_with_most_duplicates = shop_duplicated_counts.idxmax()

    print(f"The preferred shop with the most duplicated listings is: {preferred_shop_with_most_duplicates}")





# Measure the runtime of the analysis
_, elapsed_time = measure_runtime(analyze_data)
print(f"Script executed in {elapsed_time:.2f} seconds")
