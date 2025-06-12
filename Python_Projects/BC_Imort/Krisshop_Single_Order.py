import pymupdf
import pandas
import time, datetime

date = datetime.datetime.now()
date = date.strftime("%d%m")
date = "0901"

def generate_import_file(file_list:list):
    for x in file_list:
        file_name = f"{x}.pdf"
        local_time = time.localtime()
        today_date = f"{local_time.tm_mon}-{local_time.tm_mday}-{local_time.tm_year}"
        import_details = []
        column_name = ["Customer Code","Order ID", "Order Paid Time", "Product Name",
                    "SKU Reference No.", "Deal Price","Quantity" ,"Discount Amount",
                    "Receiver Name", "Phone Number","Delivery Address", "Country",
                    "Zip Code", "Remark from buyer","Order Complete Time","Note"]

        with open (rf"Z:\GJH Order\{date}25\Krisshop\{file_name}", "r") as file:
            doc = pymupdf.open(file)
            orders = [page.get_textpage().extractText() for page in doc]
            str = orders[0]
            orders = str.split("\n")

            #Get details
            order_number = [orders[orders.index("Order number") + 1]]
            contact_number = [orders[orders.index("Email to") + 1]]
            product_name =  "Refer to PO"
            sku =  "Refer to PO"
            deal_price = ["Total amount with GST / Quantity"]
            quantity = ["Refer to PO"]
            name = [orders[orders.index("Ship to") + 1]]
            shipping_address = [orders[orders.index("Ship to") + 2]]
            post_code = [orders[orders.index("Ship to") + 3]]

            for i in range(len(order_number)):
                import_details.append(["K021S", order_number[i], today_date,
                                        product_name, sku, deal_price[i],
                                        quantity[i], 0, name[i], contact_number[i].removeprefix("P: 65 "),
                                        shipping_address[i].removesuffix(","), "SG", post_code[i].removeprefix("Singapore "), 
                                        "", "", ""])
            
            df = pandas.DataFrame(import_details, columns = column_name)
            df.to_excel(rf"Z:\GJH Order\{date}25\BC Import\BC Import(Krisshop) {x}.xlsx", index = False)

file_list = ["PO_00536911-2"]
generate_import_file(file_list=file_list)
    