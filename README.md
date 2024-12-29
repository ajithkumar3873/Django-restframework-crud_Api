post
http://127.0.0.1:8000/inventory/products/all/

{
    "product_name": "Tab",
    "code": "a20",
    "price": 10000
}

get
http://127.0.0.1:8000/inventory/products/


getby id

http://127.0.0.1:8000/inventory/products/<id>/


update(patch)
http://127.0.0.1:8000/inventory/products/<id>/

{
    "product_name": "product 1",
    "code": "a200",
    "price": 10000
}


delete

http://127.0.0.1:8000/inventory/products/<id>/
