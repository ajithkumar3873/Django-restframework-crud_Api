post request-http://localhost:8000/inventory/products/all/
{
    "product_name": "Tab",
    "code": "a20",
    "price": 10000
}
<br>

get request- http://localhost:8000/inventory/products/
<br
    
getby id request - http://localhost:8000/inventory/products/<id>/
<br>

update(patch) request - http://localhost:8000/inventory/products/<id>/
{
    "product_name": "product 1",
    "code": "a200",
    "price": 10000
}
<br>

delete request - http://localhost:8000/inventory/products/<id>/
