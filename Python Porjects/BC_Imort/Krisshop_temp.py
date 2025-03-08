import pymupdf, os
import pandas
import time

def generate_import_file(file_list:list):
    for x in file_list:
        if ".PDF" in x:
            file_name = f"{x}"
            local_time = time.localtime()
            today_date = f"{local_time.tm_mon}-{local_time.tm_mday}-{local_time.tm_year}"
            import_details = []
            column_name = ["Customer Code","Order ID", "Order Paid Time", "Product Name",
                        "SKU Reference No.", "Deal Price","Quantity" ,"Discount Amount",
                        "Receiver Name", "Phone Number","Delivery Address", "Country",
                        "Zip Code", "Remark from buyer","Order Complete Time","Note"]

            with open (rf"C:\Users\Ng ChunPing\Desktop\PDF Testing\Krisshop\{file_name}", "r") as file:
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
                df.to_excel(rf"C:\Users\Ng ChunPing\Desktop\PDF Testing\Krisshop\BC Import(Krisshop) {x}.xlsx", index = False)

folder_path = r'C:\Users\Ng ChunPing\Desktop\PDF Testing\Krisshop'
file_list = [f for f in os.listdir(folder_path)]
print(file_list)
generate_import_file(file_list=file_list)
    