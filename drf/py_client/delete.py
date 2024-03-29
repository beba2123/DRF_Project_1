import requests

product_id = input("Enter the product id you want to remove: ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not a valid id')

if product_id:
        endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"

get_response = requests.delete(endpoint)
print(get_response.status_code)
if get_response.status_code == 204:
    print(f'Product with id {product_id} has been deleted')
else:
    print('Failed to delete the product, please try again later')