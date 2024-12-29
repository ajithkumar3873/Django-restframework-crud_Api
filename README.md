post -http://localhost:8000/inventory/products/all/

{
    "product_name": "Tab",
    "code": "a20",
    "price": 10000
}
<br>
get - http://localhost:8000/inventory/products/

<br>
getby id

http://localhost:8000/inventory/products/<id>/

<br>
update(patch)
http://localhost:8000/inventory/products/<id>/

{
    "product_name": "product 1",
    "code": "a200",
    "price": 10000
}

<br>

delete

http://127.0.0.1:8000/inventory/products/<id>/
