import pandas, datetime

def create_Shopee_import_file(date):
    import_date = datetime.datetime.now().strftime("%m-%d-%Y")
    shopee_orders_list = pandas.read_excel(rf"Z:\GJH Order\{date}\Shopee\Shopee {date}.xlsx" )

    import_details = []
    column_name = ["Customer Code","Order ID", "Order Paid Time", "Product Name",
                "SKU Reference No.", "Deal Price","Quantity" ,"Discount Amount",
                "Receiver Name", "Phone Number","Delivery Address", "Country",
                "Zip Code", "Remark from buyer","Order Complete Time","Note"]

    unimported_orders = shopee_orders_list[shopee_orders_list["Tracking Number*"].isna()]
    order_number = unimported_orders["Order ID"].to_list()
    product_name = unimported_orders["Product Name"].to_list()
    sku = unimported_orders["Parent SKU Reference No."].to_list()
    deal_price = unimported_orders["Deal Price"].to_list()
    quantity = unimported_orders["Quantity"].to_list()
    name = unimported_orders["Receiver Name"].to_list()
    contact_number = unimported_orders["Phone Number"].to_list()
    shipping_address = unimported_orders["Delivery Address"].to_list()
    post_code = unimported_orders["Zip Code"].to_list()

    for i in range(len(order_number)):
            import_details.append(["S099S", order_number[i], import_date,
                                    product_name[i], sku[i], deal_price[i],
                                    quantity[i], 0, name[i], contact_number[i],
                                    shipping_address[i], "SG", post_code[i], 
                                    "", "", ""])

    df = pandas.DataFrame(import_details, columns = column_name)
    df.to_excel(rf"Z:\GJH Order\{date}\BC Import\BC Import(Shopee).xlsx", index = False)


def create_Shopee_import_file_pm(date):
    import_date = datetime.datetime.now().strftime("%m-%d-%Y")
    shopee_orders_list = pandas.read_excel(rf"Z:\GJH Order\{date}\Shopee\pm\Shopee {date} pm.xlsx" )

    import_details = []
    column_name = ["Customer Code","Order ID", "Order Paid Time", "Product Name",
                "SKU Reference No.", "Deal Price","Quantity" ,"Discount Amount",
                "Receiver Name", "Phone Number","Delivery Address", "Country",
                "Zip Code", "Remark from buyer","Order Complete Time","Note"]

    unimported_orders = shopee_orders_list[shopee_orders_list["Tracking Number*"].isna()]
    order_number = unimported_orders["Order ID"].to_list()
    product_name = unimported_orders["Product Name"].to_list()
    sku = unimported_orders["Parent SKU Reference No."].to_list()
    deal_price = unimported_orders["Deal Price"].to_list()
    quantity = unimported_orders["Quantity"].to_list()
    name = unimported_orders["Receiver Name"].to_list()
    contact_number = unimported_orders["Phone Number"].to_list()
    shipping_address = unimported_orders["Delivery Address"].to_list()
    post_code = unimported_orders["Zip Code"].to_list()

    for i in range(len(order_number)):
            import_details.append(["S099S", order_number[i], import_date,
                                    product_name[i], sku[i], deal_price[i],
                                    quantity[i], 0, name[i], contact_number[i],
                                    shipping_address[i], "SG", post_code[i], 
                                    "", "", ""])

    df = pandas.DataFrame(import_details, columns = column_name)
    df.to_excel(rf"Z:\GJH Order\{date}\BC Import\BC Import(Shopee) pm.xlsx", index = False)
