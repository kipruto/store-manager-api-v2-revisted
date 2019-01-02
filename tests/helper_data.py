import json

test_admin_user = json.dumps(dict(
    email='admin@test.com',
    is_admin=True,
    password="test123"
))


test_attendant_user = json.dumps(dict(
    email='attendant@test.com',
    is_admin=False,
    password="test123"
))

admin_user_login = json.dumps(dict(
    email='admin@test.com',
    password="test123"
))

attendant_user_login = json.dumps(dict(
    email='attendant@test.com',
    password="test123"
))

wrong_user_login = json.dumps(dict(
    email='admin@test.com',
    password="test"
))

test_blank_email_value_user = json.dumps(dict(
    email='',
    is_admin=True,
    password="test123"
))

test_invalid_email_user = json.dumps(dict(
    email='test',
    is_admin=True,
    password="test123"
))

test_non_boolean_is_admin_value_user = json.dumps(dict(
    email='tests@test.com',
    is_admin="true",
    password="test123"
))

test_short_password = json.dumps(dict(
    email='testy@test.com',
    is_admin=True,
    password="test"
))



product = json.dumps(dict(
    category='beverages',
    product_name='coffee',
    quantity=100,
    unit_price=50.00
))

another_product = json.dumps(dict(
    category='candies',
    product_name='mint',
    quantity=80,
    unit_price=35.00
))

product_with_an_empty_value = json.dumps(dict(
    category='',
    product_name='coffee',
    quantity=100,
    unit_price=50.00
))

product_with_non_string_product_name = json.dumps(dict(
    category='beverages',
    product_name=8,
    quantity=100,
    unit_price=50.00
))

product_with_non_string_category = json.dumps(dict(
    category=8,
    product_name='coffee',
    quantity=100,
    unit_price=50.00
))

product_with_non_integer_quantity = json.dumps(dict(
    category='beverages',
    product_name='coffee',
    quantity='hundred',
    unit_price=50.00
))

product_with_non_positive_integer_quantity = json.dumps(dict(
    category='beverages',
    product_name='coffee',
    quantity=-100,
    unit_price=50.00
))

product_with_non_float_price = json.dumps(dict(
    category='beverages',
    product_name='coffee',
    quantity=100,
    unit_price=50
))

product_with_non_positive_float_price = json.dumps(dict(
    category='beverages',
    product_name='coffee',
    quantity=100,
    unit_price=-50.00
))

update_product = json.dumps(dict(
    product_id=1,
    product_name='tea',
    category='beverages',
    quantity=100,
    unit_price=50.00
))

update_non_existent_product = json.dumps(dict(
    product_id=10,
    product_name='tea',
    category='beverages',
    quantity=100,
    unit_price=50.00
))

sale = json.dumps(dict(
    product_id=2,
    quantity=1
))

sale_non_existent = json.dumps(dict(
    product_id=5,
    quantity=10
))

insufficient_product_sale = json.dumps(dict(
    product_id=2,
    quantity=101
))

sale_with_blank_value = json.dumps(dict(
    product_id=2,
    quantity=""
))

sale_with_non_int_product_id_value = json.dumps(dict(
    product_id="one",
    quantity=10
))

sale_with_non_int_quantity_value = json.dumps(dict(
    product_id=2,
    quantity="ten"
))

sale_with_non_positive_quantity_value = json.dumps(dict(
    product_id=2,
    quantity=-1
))


# key errors
user_without_password_key = json.dumps(dict(
    email='admin@test.com',
    is_admin=True
))

user_without_is_admin_key = json.dumps(dict(
    email='admin@test.com',
    password="test123"
))

user_without_email_key = json.dumps(dict(
    is_admin=True,
    password="test123"
))

product_without_price_key = json.dumps(dict(
    category='beverages',
    product_name='coffee',
    quantity=100
))

product_without_quantity_key = json.dumps(dict(
    category='beverages',
    product_name='coffee',
    unit_price=50.00
))

product_without_category_key = json.dumps(dict(
    product_name='coffee',
    quantity=100,
    unit_price=50.00
))

product_without_product_name_key = json.dumps(dict(
    category='beverages',
    quantity=100,
    unit_price=50.00
))

user_login_without_password_key = json.dumps(dict(
    email='admin@test.com'
))

update_product_without_product_name_key = json.dumps(dict(
    product_id=1,
    category='beverages',
    quantity=100,
    unit_price=50.00
))

update_product_without_category_key = json.dumps(dict(
    product_id=1,
    product_name='coffee',
    quantity=100,
    unit_price=50.00
))

update_product_without_quantity_key = json.dumps(dict(
    product_id=1,
    category='beverages',
    product_name='coffee',
    unit_price=50.00
))

update_product_without_price_key = json.dumps(dict(
    product_id=1,
    category='beverages',
    product_name='coffee',
    quantity=100,
))

sale_product_without_quantity_key = json.dumps(dict(
    product_id=1
))

sale_product_without_product_id_key = json.dumps(dict(
    quantity=10
))