
USE [POSHAAK]
GO
/****** Object:  Table [dbo].[brands]    Script Date: 09/12/2023 05:38:24 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[brands](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[brand_name] [varchar](250) NOT NULL,
	[email] [varchar](250) NULL,
 CONSTRAINT [PK_brands] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[cart]    Script Date: 09/12/2023 05:38:24 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cart](
	[entry_id] [int] IDENTITY(1,1) NOT NULL,
	[customer_id] [int] NOT NULL,
	[product_id] [int] NOT NULL,
	[total] [float] NOT NULL,
	[discount] [float] NULL,
	[gross_total] [float] NOT NULL,
 CONSTRAINT [PK_cart] PRIMARY KEY CLUSTERED 
(
	[entry_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[categories]    Script Date: 09/12/2023 05:38:24 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[categories](
	[id] [int] NOT NULL,
	[name] [nvarchar](255) NOT NULL,
	[description] [text] NOT NULL,
 CONSTRAINT [PK_categories] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[customers]    Script Date: 09/12/2023 05:38:24 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[customers](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[last_name] [nvarchar](250) NOT NULL,
	[email] [nvarchar](255) NULL,
	[password] [nvarchar](255) NOT NULL,
	[account_type] [nvarchar](100) NOT NULL,
 CONSTRAINT [PK_customers] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[delivery areas]    Script Date: 09/12/2023 05:38:24 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[delivery areas](
	[city] [nvarchar](100) NOT NULL,
	[area] [nvarchar](150) NOT NULL,
	[country] [nvarchar](255) NULL,
	[postal_code] [nvarchar](255) NULL,
	[charges] [float] NULL,
	[isPossible] [bit] NOT NULL,
 CONSTRAINT [PK_delivery areas] PRIMARY KEY CLUSTERED 
(
	[city] ASC,
	[area] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[orders]    Script Date: 09/12/2023 05:38:24 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[orders](
	[order_id] [int] IDENTITY(1,1) NOT NULL,
	[customer_id] [int] NOT NULL,
	[order_date] [date] NOT NULL,
	[total_amount] [decimal](10, 2) NOT NULL,
	[payment_method] [nchar](50) NOT NULL,
	[status] [nchar](50) NOT NULL,
	[shipDate] [date] NULL,
	[shipVia] [nvarchar](100) NULL,
	[shipperID] [int] NULL,
 CONSTRAINT [PK__orders__46596229CB5D5EC2] PRIMARY KEY CLUSTERED 
(
	[order_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[product_brand]    Script Date: 09/12/2023 05:38:24 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[product_brand](
	[product_id] [int] NOT NULL,
	[brand_id] [int] NOT NULL,
 CONSTRAINT [PK_product_brand] PRIMARY KEY CLUSTERED 
(
	[product_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[products]    Script Date: 09/12/2023 05:38:24 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[products](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](255) NOT NULL,
	[category] [int] NOT NULL,
	[description] [text] NULL,
	[size] [char](3) NOT NULL,
	[color] [nvarchar](250) NOT NULL,
	[price] [float] NOT NULL,
	[discount] [float] NULL,
	[quantity_in_stock,] [int] NOT NULL,
 CONSTRAINT [PK_products] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[selected item]    Script Date: 09/12/2023 05:38:24 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[selected item](
	[item_id] [int] NOT NULL,
	[description] [text] NOT NULL,
	[quantity] [int] NULL,
	[price] [float] NULL,
 CONSTRAINT [PK_selected item] PRIMARY KEY CLUSTERED 
(
	[item_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[shippers]    Script Date: 09/12/2023 05:38:24 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[shippers](
	[id] [int] NOT NULL,
	[name] [nvarchar](255) NULL,
	[contact_number] [nvarchar](20) NULL,
	[email] [nvarchar](50) NULL,
 CONSTRAINT [PK_shippers] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[brands] ON 

INSERT [dbo].[brands] ([id], [brand_name], [email]) VALUES (1, N'Adidas', N'adidas@example.com')
INSERT [dbo].[brands] ([id], [brand_name], [email]) VALUES (2, N'Nike', N'nike@example.com')
INSERT [dbo].[brands] ([id], [brand_name], [email]) VALUES (3, N'Puma', N'puma@example.com')
INSERT [dbo].[brands] ([id], [brand_name], [email]) VALUES (4, N'Reebok', N'reebok@example.com')
INSERT [dbo].[brands] ([id], [brand_name], [email]) VALUES (5, N'Under Armour', N'underarmour@example.com')
INSERT [dbo].[brands] ([id], [brand_name], [email]) VALUES (6, N'KidsFashionCo', N'info@kidsfashionco.com')
INSERT [dbo].[brands] ([id], [brand_name], [email]) VALUES (7, N'LittlePrincess', N'contact@littleprincess.com')
INSERT [dbo].[brands] ([id], [brand_name], [email]) VALUES (8, N'CoolKidsWear', N'hello@coolkidswear.com')
INSERT [dbo].[brands] ([id], [brand_name], [email]) VALUES (9, N'TinyTrendz', N'info@tinytrendz.com')
SET IDENTITY_INSERT [dbo].[brands] OFF
GO
INSERT [dbo].[categories] ([id], [name], [description]) VALUES (1, N'Shirts', N'Variety of shirts for children')
INSERT [dbo].[categories] ([id], [name], [description]) VALUES (2, N'Pants', N'Comfortable pants for children')
INSERT [dbo].[categories] ([id], [name], [description]) VALUES (3, N'Dresses', N'Beautiful dresses for children')
INSERT [dbo].[categories] ([id], [name], [description]) VALUES (4, N'Shoes', N'Stylish shoes for children')
INSERT [dbo].[categories] ([id], [name], [description]) VALUES (5, N'Accessories', N'Cute accessories for children')
GO
SET IDENTITY_INSERT [dbo].[customers] ON 

INSERT [dbo].[customers] ([id], [last_name], [email], [password], [account_type]) VALUES (1, N'Anas', N'1234@gmaill.com', N'123456', N'star')
INSERT [dbo].[customers] ([id], [last_name], [email], [password], [account_type]) VALUES (2, N'sherali', N'abc@gmaill.com', N'123456', N'star')
INSERT [dbo].[customers] ([id], [last_name], [email], [password], [account_type]) VALUES (3, N'mustafa', N'abc@gmaill.com', N'123456', N'star')
INSERT [dbo].[customers] ([id], [last_name], [email], [password], [account_type]) VALUES (8, N'akhtar', N'akhtar@gmail.com', N'123456', N'normal')
INSERT [dbo].[customers] ([id], [last_name], [email], [password], [account_type]) VALUES (9, N'newperson', N'newperson@gmail.com', N'123456', N'normal')
INSERT [dbo].[customers] ([id], [last_name], [email], [password], [account_type]) VALUES (10, N'newperson', N'newperson@gmail.com', N'123456', N'normal')
INSERT [dbo].[customers] ([id], [last_name], [email], [password], [account_type]) VALUES (11, N'anas', N'anas@gmail.com', N'123456', N'normal')
INSERT [dbo].[customers] ([id], [last_name], [email], [password], [account_type]) VALUES (14, N'anas', N'abc@gmail.com', N'123qweQ.', N'normal')
INSERT [dbo].[customers] ([id], [last_name], [email], [password], [account_type]) VALUES (15, N'a', N'b', N'c', N'star')
INSERT [dbo].[customers] ([id], [last_name], [email], [password], [account_type]) VALUES (16, N'b', N'd', N'c', N'normal')
INSERT [dbo].[customers] ([id], [last_name], [email], [password], [account_type]) VALUES (17, N'anas', N'newuser@gmail.com', N'Anasking123.', N'normal')
INSERT [dbo].[customers] ([id], [last_name], [email], [password], [account_type]) VALUES (18, N'a', N'r', N's', N'star')
SET IDENTITY_INSERT [dbo].[customers] OFF
GO
INSERT [dbo].[delivery areas] ([city], [area], [country], [postal_code], [charges], [isPossible]) VALUES (N'London', N'Westminster', N'UK', N'SW1A 0AA', 4.5, 1)
INSERT [dbo].[delivery areas] ([city], [area], [country], [postal_code], [charges], [isPossible]) VALUES (N'New York', N'Manhattan', N'USA', N'10001', 5.99, 1)
INSERT [dbo].[delivery areas] ([city], [area], [country], [postal_code], [charges], [isPossible]) VALUES (N'Paris', N'Le Marais', N'France', N'75003', 6.75, 1)
INSERT [dbo].[delivery areas] ([city], [area], [country], [postal_code], [charges], [isPossible]) VALUES (N'Sydney', N'CBD', N'Australia', N'2000', 7.25, 1)
GO
SET IDENTITY_INSERT [dbo].[orders] ON 

INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (34, 1, CAST(N'2023-12-08' AS Date), CAST(120.50 AS Decimal(10, 2)), N'Credit Card                                       ', N'Shipped                                           ', CAST(N'2023-12-10' AS Date), N'Post', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (35, 1, CAST(N'2023-12-08' AS Date), CAST(120.50 AS Decimal(10, 2)), N'Credit Card                                       ', N'Shipped                                           ', CAST(N'2023-12-10' AS Date), N'Post', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (36, 2, CAST(N'2023-12-09' AS Date), CAST(95.25 AS Decimal(10, 2)), N'PayPal                                            ', N'Processing                                        ', CAST(N'2023-12-12' AS Date), N'Leopards', 2)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (37, 3, CAST(N'2023-12-10' AS Date), CAST(200.00 AS Decimal(10, 2)), N'Debit Card                                        ', N'Delivered                                         ', CAST(N'2023-12-14' AS Date), N'Leopards', 2)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (38, 8, CAST(N'2023-12-11' AS Date), CAST(150.75 AS Decimal(10, 2)), N'Cash on Delivery                                  ', N'Pending                                           ', CAST(N'2023-12-16' AS Date), N'TCS', 4)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (39, 16, CAST(N'2023-12-08' AS Date), CAST(19.99 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (40, 16, CAST(N'2023-12-08' AS Date), CAST(19.99 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (41, 16, CAST(N'2023-12-08' AS Date), CAST(19.00 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (42, 16, CAST(N'2023-12-08' AS Date), CAST(19.00 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (43, 16, CAST(N'2023-12-08' AS Date), CAST(19.00 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (44, 16, CAST(N'2023-12-09' AS Date), CAST(29.84 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (45, 16, CAST(N'2023-12-09' AS Date), CAST(24.99 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (46, 16, CAST(N'2023-12-09' AS Date), CAST(29.84 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (47, 16, CAST(N'2023-12-09' AS Date), CAST(19.00 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (48, 16, CAST(N'2023-12-09' AS Date), CAST(24.99 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (49, 16, CAST(N'2023-12-09' AS Date), CAST(19.00 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (50, 16, CAST(N'2023-12-09' AS Date), CAST(29.84 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (51, 16, CAST(N'2023-12-09' AS Date), CAST(29.84 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (52, 16, CAST(N'2023-12-09' AS Date), CAST(24.99 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (53, 16, CAST(N'2023-12-09' AS Date), CAST(34.79 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (54, 16, CAST(N'2023-12-09' AS Date), CAST(9.94 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (55, 16, CAST(N'2023-12-09' AS Date), CAST(24.99 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (56, 16, CAST(N'2023-12-09' AS Date), CAST(34.79 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (57, 16, CAST(N'2023-12-09' AS Date), CAST(9.94 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (58, 16, CAST(N'2023-12-09' AS Date), CAST(29.84 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (59, 16, CAST(N'2023-12-09' AS Date), CAST(24.99 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (60, 16, CAST(N'2023-12-09' AS Date), CAST(34.79 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (61, 16, CAST(N'2023-12-09' AS Date), CAST(9.94 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
INSERT [dbo].[orders] ([order_id], [customer_id], [order_date], [total_amount], [payment_method], [status], [shipDate], [shipVia], [shipperID]) VALUES (62, 16, CAST(N'2023-12-09' AS Date), CAST(29.84 AS Decimal(10, 2)), N'cash                                              ', N'pending                                           ', NULL, N'PAKISTAN POST', 1)
SET IDENTITY_INSERT [dbo].[orders] OFF
GO
INSERT [dbo].[product_brand] ([product_id], [brand_id]) VALUES (24, 1)
INSERT [dbo].[product_brand] ([product_id], [brand_id]) VALUES (25, 2)
INSERT [dbo].[product_brand] ([product_id], [brand_id]) VALUES (26, 3)
INSERT [dbo].[product_brand] ([product_id], [brand_id]) VALUES (27, 4)
INSERT [dbo].[product_brand] ([product_id], [brand_id]) VALUES (28, 5)
INSERT [dbo].[product_brand] ([product_id], [brand_id]) VALUES (57, 1)
GO
SET IDENTITY_INSERT [dbo].[products] ON 

INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (24, N'Blue baby Shirt', 1, N'Blue shirt for boys', N'M  ', N'Blue', 19.99, 0.99, 50)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (25, N'Pink Dress', 3, N'Pink floral dress', N'S  ', N'Pink', 29.99, 0.15, 75)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (26, N'Black Pants', 2, N'Black pants for boys', N'L  ', N'Black', 24.99, 0, 100)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (27, N'Red Shoes', 4, N'Red sneakers for kids', N'M  ', N'Red', 34.99, 0.2, 30)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (28, N'Hair Clips', 5, N'Set of cute hair clips', N'XL ', N'Multi-color', 9.99, 0.05, 80)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (35, N'Kids T-Shirt', 1, N'Cute cotton t-shirt for kids', N'M  ', N'Blue', 12.99, 0, 50)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (36, N'Girls Dress', 3, N'Beautiful dress for little girls', N'L  ', N'Pink', 24.99, 5, 30)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (37, N'Boys Jeans', 2, N'Stylish jeans for boys', N'S  ', N'Denim Blue', 19.99, 10, 40)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (38, N'Minor shoes', 4, N'Stylish shoes for children', N'S  ', N'Red', 20, 0, 20)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (39, N'Toddler Onesie', 5, N'Soft onesie for toddlers', N'ExS', N'Yellow', 9.99, 0, 20)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (41, N'nike shoes anas', 1, N'no descrition', N'L  ', N'Blue', 50, 0, 12)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (42, N'nike shoes anas', 2, N'nhi hei', N'L  ', N'Blue', 10, 0, 1)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (43, N'xhappal', 1, N'dfa', N'L  ', N'Blue', 3, 3, 3)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (44, N'anas', 1, N'no ', N'L  ', N'Blue', 22, 22, 7)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (45, N'asdfas', 1, N'asdfs', N'L  ', N'Blue', 2, 2, 2)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (46, N'falut', 1, N'adf', N'M  ', N'Blue', 2, 2, 2)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (47, N'falut', 1, N'adf', N'M  ', N'Blue', 2, 2, 2)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (48, N'new Product', 1, N'description', N'S  ', N'Red', 1.1, 1.1, 2)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (49, N'new Product', 1, N'description', N'S  ', N'Red', 1.1, 1.1, 2)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (50, N'new Product', 1, N'description', N'S  ', N'Red', 1.1, 1.1, 2)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (51, N'new Product', 1, N'description', N'S  ', N'Red', 1.1, 1.1, 2)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (52, N'nw Product', 1, N'nhi hei description', N'S  ', N'Red', 393.3, 23.23, 2)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (53, N'new Product', 1, N'description', N'S  ', N'Red', 3.3, 8.8, 2)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (54, N'new product1', 1, N'nhi hei', N'S  ', N'Red', 12.2, 12.1, 12)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (55, N'ew', 1, N'dsf', N'S  ', N'Red', 23.2, 232.23, 1)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (56, N'product', 1, N'description', N'S  ', N'Red', 23.2, 3.3, 1)
INSERT [dbo].[products] ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,]) VALUES (57, N'final product', 1, N'final', N'S  ', N'Red', 23.2, 3.3, 2)
SET IDENTITY_INSERT [dbo].[products] OFF
GO
INSERT [dbo].[shippers] ([id], [name], [contact_number], [email]) VALUES (1, N'SpeedyShip', N'+1234567890', N'info@speedyship.com')
INSERT [dbo].[shippers] ([id], [name], [contact_number], [email]) VALUES (2, N'ExpressDelivery', N'+1987654321', N'contact@expressdelivery.com')
INSERT [dbo].[shippers] ([id], [name], [contact_number], [email]) VALUES (3, N'SwiftCarriers', N'+1122334455', N'hello@swiftcarriers.com')
INSERT [dbo].[shippers] ([id], [name], [contact_number], [email]) VALUES (4, N'FastFreight', N'+1555098765', N'support@fastfreight.com')
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ_City]    Script Date: 09/12/2023 05:38:24 PM ******/
ALTER TABLE [dbo].[delivery areas] ADD  CONSTRAINT [UQ_City] UNIQUE NONCLUSTERED 
(
	[city] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[products] ADD  CONSTRAINT [DF_products_discount]  DEFAULT ((0)) FOR [discount]
GO
ALTER TABLE [dbo].[cart]  WITH CHECK ADD  CONSTRAINT [FK_cart_customers] FOREIGN KEY([entry_id])
REFERENCES [dbo].[customers] ([id])
GO
ALTER TABLE [dbo].[cart] CHECK CONSTRAINT [FK_cart_customers]
GO
ALTER TABLE [dbo].[cart]  WITH CHECK ADD  CONSTRAINT [FK_cart_products] FOREIGN KEY([product_id])
REFERENCES [dbo].[products] ([id])
GO
ALTER TABLE [dbo].[cart] CHECK CONSTRAINT [FK_cart_products]
GO
ALTER TABLE [dbo].[orders]  WITH CHECK ADD  CONSTRAINT [FK_orders_customers] FOREIGN KEY([customer_id])
REFERENCES [dbo].[customers] ([id])
GO
ALTER TABLE [dbo].[orders] CHECK CONSTRAINT [FK_orders_customers]
GO
ALTER TABLE [dbo].[orders]  WITH CHECK ADD  CONSTRAINT [FK_orders_shippers] FOREIGN KEY([shipperID])
REFERENCES [dbo].[shippers] ([id])
GO
ALTER TABLE [dbo].[orders] CHECK CONSTRAINT [FK_orders_shippers]
GO
ALTER TABLE [dbo].[product_brand]  WITH CHECK ADD  CONSTRAINT [FK_product_brand_brands] FOREIGN KEY([brand_id])
REFERENCES [dbo].[brands] ([id])
GO
ALTER TABLE [dbo].[product_brand] CHECK CONSTRAINT [FK_product_brand_brands]
GO
ALTER TABLE [dbo].[product_brand]  WITH CHECK ADD  CONSTRAINT [FK_products_product_brand] FOREIGN KEY([product_id])
REFERENCES [dbo].[products] ([id])
GO
ALTER TABLE [dbo].[product_brand] CHECK CONSTRAINT [FK_products_product_brand]
GO
ALTER TABLE [dbo].[products]  WITH CHECK ADD  CONSTRAINT [FK_products_categories] FOREIGN KEY([category])
REFERENCES [dbo].[categories] ([id])
GO
ALTER TABLE [dbo].[products] CHECK CONSTRAINT [FK_products_categories]
GO
ALTER TABLE [dbo].[selected item]  WITH CHECK ADD  CONSTRAINT [FK_selected item_products] FOREIGN KEY([item_id])
REFERENCES [dbo].[products] ([id])
GO
ALTER TABLE [dbo].[selected item] CHECK CONSTRAINT [FK_selected item_products]
GO
USE [master]
GO
ALTER DATABASE [POSHAAK] SET  READ_WRITE 
GO
