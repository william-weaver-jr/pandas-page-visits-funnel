import codecademylib3
import pandas as pd

# Import all of the CSV files
visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])

visits_cart = pd.merge(visits, cart, how='left')
print(visits_cart.head())
print(len(visits_cart))
print(visits_cart['cart_time'].isnull().sum())

percent_visited = (empty_cart / visits_cart_len) * 100
print(f"{percent_visited}% of user only visited without placing a t-shirt in the cart.")

# What percentage placed a t-shirt in their cart but did not checkout?
cart_checkout = pd.merge(cart, checkout, how='left')
empty_checkout = cart_checkout['checkout_time'].isnull().sum()
percent_no_checkout = round((empty_checkout / len(cart_checkout['checkout_time'])) * 100, 2)
print(f"{percent_no_checkout}% of visitors placed a t-shirt in their cart but did not checkout.")

# Merge all the datasets and preview the first couple of rows
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
all_data.head()

# What percentage of users proceeded to checkout, but did not purchase a t-shirt?
non_purchase = all_data['purchase_time'].isnull().sum()
percent_no_purchase = round((non_purchase / len(all_data)) * 100, 2)
print(f"{percent_no_purchase}% of users got to checkout but did not purchase.")

# Check each part of the funnel for the weakest step
print(f"{percent_visited}% of user only visited without placing a t-shirt in the cart.")
print(f"{percent_no_checkout}% of visitors placed a t-shirt in their cart but did not checkout.")
print(f"{percent_no_purchase}% of users got to checkout but did not purchase.")

# Calculate the average time from initial visit to final purchase.
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase)
mean_time_to_purchase = all_data['time_to_purchase'].mean()
print(mean_time_to_purchase)
