
--NOTE TABLES IN DATABASE WERE CREATED BY BUILTIN FEATURE OF IN OBJECT EXPLORER HOWEVER DATA WAS INSERTED THORUGH FOLLOWING
--COMMANDS


select * from cart
select * from customers
select* from brands
select* from shippers
select* from [selected item]
select* from products
select* from product_brand
select* from orders
select* from [delivery areas]
select* from categories


/*(1, 'Shirts',
(2, 'Pants', 
(3, 'Dresses', 
(4, 'Shoes',
(5, 'Accessories', */

INSERT INTO products (name, category, description, size, color, price, discount, [quantity_in_stock,] )
VALUES 
('Kids T-Shirt', 1, 'Cute cotton t-shirt for kids', 'M', 'Blue', 12.99, 0, 50),
('Girls Dress', 3, 'Beautiful dress for little girls', 'L', 'Pink', 24.99, 5, 30),
('Boys Jeans', 2, 'Stylish jeans for boys', 'S', 'Denim Blue', 19.99, 10, 40),
('Minor shoes', 4,  'Stylish shoes for children','S', 'Red', 20, 0, 20),
('Toddler Onesie', 5, 'Soft onesie for toddlers', 'ExS', 'Yellow', 9.99, 0, 20);

select * from products

INSERT INTO brands (brand_name, email)
VALUES 
('KidsFashionCo', 'info@kidsfashionco.com'),
('LittlePrincess', 'contact@littleprincess.com'),
('CoolKidsWear', 'hello@coolkidswear.com'),
('TinyTrendz', 'info@tinytrendz.com');
select * from brands

INSERT INTO product_brand(product_id, brand_id)
VALUES 
(28, 1), -- Assuming the product with ID 1 belongs to the brand with ID 1
(25, 2), -- Assuming the product with ID 2 belongs to the brand with ID 2
(26, 3), -- Assuming the product with ID 3 belongs to the brand with ID 3
(27, 4); -- Assuming the product with ID 4 belongs to the brand with ID 4
select* from product_brand

INSERT INTO categories (name, description)
VALUES 
(1, 'Tops', 'Upper garments for kids'),
(3, 'Dresses', 'Various styles of dresses for children'),
(2, 'Bottoms', 'Pants, shorts, and skirts for kids'),
(4, 'shoes', 'One-store shoes for babies,  toddlers and kids'),
(5, 'accessories', 'All other garment accessories');
select* from categories

INSERT INTO [delivery areas] (city, area, country, postal_code, charges, isPossible)
VALUES 
('New York', 'Manhattan', 'USA', '10001', 5.99, 1),
('London', 'Westminster', 'UK', 'SW1A 0AA', 4.50, 1),
('Sydney', 'CBD', 'Australia', '2000', 7.25, 1),
('Paris', 'Le Marais', 'France', '75003', 6.75, 1);
select* from [delivery areas]

INSERT INTO shippers (id, name, contact_number, email)
VALUES 
(1, 'SpeedyShip', '+1234567890', 'info@speedyship.com'),
(2, 'ExpressDelivery', '+1987654321', 'contact@expressdelivery.com'),
(3, 'SwiftCarriers', '+1122334455', 'hello@swiftcarriers.com'),
(4, 'FastFreight', '+1555098765', 'support@fastfreight.com');

select * from shippers


INSERT INTO orders (cart_id, customer_id, order_date, total_amount, payment_method, status, ShipCity, ShipDate, ShipVia, ShipperID)
VALUES 
(31, 1, '2023-12-08', 120.50, 'Credit Card', 'Shipped', 'New York', '2023-12-10', 'Post', 1),
(21, 2, '2023-12-09', 95.25, 'PayPal', 'Processing', 'London', '2023-12-12', 'Leopards', 2),
(23, 3, '2023-12-10', 200.00, 'Debit Card', 'Delivered', 'Sydney', '2023-12-14', 'Leopards', 2),
(30, 8, '2023-12-11', 150.75, 'Cash on Delivery', 'Pending', 'Paris', '2023-12-16', 'TCS', 4);

select* from orders


INSERT INTO cart (	customer_id,	product_id,	total,	discount,	gross_total)
VALUES 
(2, 28, 15.75,0, 15.75),
(18, 28, 15.75,0, 15.75),
(19, 28, 15.75,0, 15.75),
(2, 24, 25.99, 1, 24.99),
(2, 24, 10.50,0.5, 10),
(2, 25, 5.00,0, 5.00),
(2, 27, 15.75,0, 15.75);

