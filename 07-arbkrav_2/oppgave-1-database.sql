-- tabeller
CREATE TABLE customers (
	customer_id INT AUTO_INKREMENT NOT NULL,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL
	registered_date DATE NOT NULL,
	PRIMARY KEY (customer_id),
    UNIQUE(email)
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    PRIMARY KEY (product_id),
    UNIQUE(product_name)
);

CREATE TABLE orders (
	order_id INT AUTO_INKREMENT NOT NULL,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
	order_data DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
	PRIMARY KEY (order_id)
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

