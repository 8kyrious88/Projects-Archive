import pandas, datetime

def create_Lzd_import_file(date):
    import_date = datetime.datetime.now().strftime("%m-%d-%Y")
    lzd_orders_list = pandas.read_excel(rf"Z:\GJH Order\{date}\Lzd\Lzd {date}.xlsx" )

    import_details = []
    column_name = ["Customer Code","Order ID", "Order Paid Time", "Product Name",
                "SKU Reference No.", "Deal Price","Quantity" ,"Discount Amount",
                "Receiver Name", "Phone Number","Delivery Address", "Country",
                "Zip Code", "Remark from buyer","Order Complete Time","Note"]
    
    lzd_orders_list["Quantity"] = 1
    order_number = lzd_orders_list["orderNumber"].to_list()
    product_name = lzd_orders_list["itemName"].to_list()
    sku = lzd_orders_list["sellerSku"].to_list()
    deal_price = lzd_orders_list["unitPrice"].to_list()
    quantity = lzd_orders_list["Quantity"].to_list()
    name = lzd_orders_list["customerName"].to_list()
    contact_number = lzd_orders_list["billingPhone"].to_list()
    shipping_address = lzd_orders_list["shippingAddress"].to_list()
    post_code = lzd_orders_list["shippingPostCode"].to_list()

    for i in range(len(order_number)):
            import_details.append(["L037S", order_number[i], import_date,
                                    product_name[i], sku[i], deal_price[i],
                                    quantity[i], 0, name[i], contact_number[i],
                                    shipping_address[i], "SG", post_code[i], 
                                    "", "", ""])

    df = pandas.DataFrame(import_details, columns = column_name)
    df.to_excel(rf"Z:\GJH Order\{date}\BC Import\BC Import(Lzd).xlsx", index = False)

def create_Lzd_import_file_pm(date):
    import_date = datetime.datetime.now().strftime("%m-%d-%Y")
    lzd_orders_list = pandas.read_excel(rf"Z:\GJH Order\{date}\Lzd\pm\Lzd {date} pm.xlsx" )

    import_details = []
    column_name = ["Customer Code","Order ID", "Order Paid Time", "Product Name",
                "SKU Reference No.", "Deal Price","Quantity" ,"Discount Amount",
                "Receiver Name", "Phone Number","Delivery Address", "Country",
                "Zip Code", "Remark from buyer","Order Complete Time","Note"]
    
    lzd_orders_list["Quantity"] = 1
    order_number = lzd_orders_list["orderNumber"].to_list()
    product_name = lzd_orders_list["itemName"].to_list()
    sku = lzd_orders_list["sellerSku"].to_list()
    deal_price = lzd_orders_list["unitPrice"].to_list()
    quantity = lzd_orders_list["Quantity"].to_list()
    name = lzd_orders_list["customerName"].to_list()
    contact_number = lzd_orders_list["billingPhone"].to_list()
    shipping_address = lzd_orders_list["shippingAddress"].to_list()
    post_code = lzd_orders_list["shippingPostCode"].to_list()

    for i in range(len(order_number)):
            import_details.append(["L037S", order_number[i], import_date,
                                    product_name[i], sku[i], deal_price[i],
                                    quantity[i], 0, name[i], contact_number[i],
                                    shipping_address[i], "SG", post_code[i], 
                                    "", "", ""])

    df = pandas.DataFrame(import_details, columns = column_name)
    df.to_excel(rf"Z:\GJH Order\{date}\BC Import\BC Import(Lzd) pm.xlsx", index = False)

