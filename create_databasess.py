import sqlite3
import random
import datetime

# define sql commnds for creating the tables
create_sales_table = """create Table sales(
                        sale_id INTEGER PRIMARY KEY,
                        sale_date Date,
                        customer_id INTEGER,
                        product_id INTEGER,
                        quantity INTEGER,
                        unit_price DECIMAL(10, 2),
                        total_price DECIMAL(10,2),
                        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                        FOREIGN KEY (product_id) REFERENCES customers(product_id)
                        )"""

create_product_table = """create table products(
                        product_id INTEGER PRIMARY KEY,
                        product_name TEXT,
                        unit_cost DECIMAL(10,2)
                        )"""

create_customer_table = """create table customers(
                        customer_id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        email TEXT,
                        phone TEXT
                    )"""

# Define sql commands for inserting smaple data into the tables
insert_products_data = '''INSERT INTO products (product_name, unit_cost) VALUES (?, ?)'''

insert_sales_data = '''INSERT INTO sales (sale_date, customer_id, product_id, quantity, unit_price, total_price) VALUES (?, ?, ?, ?, ?, ?)'''

insert_customers_data = '''INSERT INTO customers (first_name, last_name, email, phone) VALUES (?, ?, ?, ?)'''

# define sample dat for the product and customer tables
products = [('Product A', 50.00), ('Product B', 25.00), ('Product C', 75.00), ('Product D', 40.00), ('Product E', 6)]

customers = [
    ('John', 'Doe', 'johndoe@example.com', '555-1234'),
    ('Jane', 'Doe', 'janedoe@example.com', '555-5678'),
    ('Bob', 'Smith', 'bobsmith@example.com', '555-9012'),
    ('Alice', 'Jones', 'alicejones@example.com', '555-3456'),
    ('David', 'Brown', 'davidbrown@example.com', '555-7890'),
    ('Emily', 'Davis', 'emilydavis@example.com', '555-2345'),
    ('Frank', 'Wilson', 'frankwilson@example.com', '555-6789'),
    ('Grace', 'Lee', 'gracelee@example.com', '555-1234'),
    ('Henry', 'Chen', 'henrychen@example.com', '555-5678'),
    ('Isabel', 'Garcia', 'isabelgarcia@example.com', '555-9012')
]

# define the start and end dates for generating sales data
start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2022, 12, 31)

# connect to the datbase and create the tables
with sqlite3.connect("sales.db") as conn:
    conn.execute(create_sales_table)

    conn.execute(create_product_table)

    conn.execute(create_customer_table)

# inserrt sample data into the product table
for product in products:
    conn.execute(insert_products_data, product)

# inserrt sample data into the customer table
for customer in customers:
    conn.execute(insert_customers_data, customer)

for i in range(1000):
    sale_date = start_date + datetime.timedelta(days=random.randint(0, 364))
    customer_id = random.randint(1, len(customers))
    product_id = random.randint(1, len(products))
    quantity = random.randint(1, 10)
    unit_price = products[product_id-1][1]
    total_price = quantity * unit_price
    conn.execute(insert_sales_data, (sale_date, customer_id, product_id, quantity, unit_price, total_price))

# commit the changes
conn.commit()

print('Database Successfully created!')


