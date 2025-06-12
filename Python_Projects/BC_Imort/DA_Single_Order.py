import pymupdf, pandas, time, datetime

def create_DA_import_file(date):
    input_file = rf"Z:\GJH Order\{date}\DA\Untitled attachment 00009.pdf"
    local_time = time.localtime()
    today_date = f"{local_time.tm_mon}-{local_time.tm_mday}-{local_time.tm_year}"
    import_details = []
    column_name = ["Customer Code","Order ID", "Order Paid Time", "Product Name",
               "SKU Reference No.", "Deal Price","Quantity" ,"Discount Amount",
               "Receiver Name", "Phone Number","Delivery Address", "Country",
               "Zip Code", "Remark from buyer","Order Complete Time","Note"]

    doc = pymupdf.open(input_file)
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num).get_textpage().extractText()
        order = page.replace("\n","")
    name = order[order.index("Customer InformationName") + 26:order.index("Address")]
    order_number = "Refer to email delivery ID"
    shipping_address = order[order.index("Address") + 9:order.index(", SG")]
    contact_number = order[order.index("Contact") + 10:order.index("Email")]
    post_code = order[order.index("SG") + 4:order.index("Contact")]
    product_name =  order[order.index("(S$)") + 4:order.index("Subtotal") - 7]
    sku =  "Refer to BC"
    deal_price = "Subtotal / Quantity"
    quantity = "Refer to PO"
    
    
    import_details.append(["D035S", order_number, today_date,
                            product_name, sku, deal_price,
                            quantity, 0, name, contact_number,
                            shipping_address, "SG", post_code, 
                            "", "", ""])
    
    df = pandas.DataFrame(import_details, columns = column_name)
    df.to_excel(rf"Z:\GJH Order\{date}\BC Import\BC Import(DA).xlsx", index = False)

date = datetime.datetime.now().strftime("%d%m") + "25"
create_DA_import_file(date)