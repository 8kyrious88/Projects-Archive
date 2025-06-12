import pandas
import time


def create_Amazon_import_file(date):
    input_file = rf"Z:\GJH Order\{date}\Amazon\Amazon {date}.xlsx"  
    content = pandas.read_excel(input_file)
    local_time = time.localtime()
    today_date = f"{local_time.tm_mon}-{local_time.tm_mday}-{local_time.tm_year}"

    content["Deal Price"] = content["item-price"] / content["quantity-purchased"]
    content["Country"] = "SG"
    content["Discount Amount"] = 0
    content["Remark from buyer"] = ""
    content["Order Complete Time"] = ""
    content["Note"] = ""
    content["Order Paid Time"] = today_date

    new_content = content.rename(columns={"order-id":"Order ID",
                            "product-name":"Product Name",
                            "sku":"SKU Reference No.",
                            "quantity-purchased":"Quantity",
                            "recipient-name":"Receiver Name",
                            "ship-phone-number":"Phone Number",
                            "ship-address-1":"Delivery Address",
                            "ship-postal-code":"Zip Code"})

    data = pandas.DataFrame(new_content[["Order ID", "Order Paid Time", "Product Name","SKU Reference No.",
                                    "Deal Price","Quantity" ,"Discount Amount","Receiver Name",
                                    "Phone Number","Delivery Address", "Country", "Zip Code",
                                    "Remark from buyer","Order Complete Time","Note"]])


    data["Customer Code"] = "A032S"
    column_name = ["Customer Code","Order ID", "Order Paid Time", "Product Name",
                "SKU Reference No.", "Deal Price","Quantity" ,"Discount Amount",
                "Receiver Name", "Phone Number","Delivery Address", "Country",
                "Zip Code", "Remark from buyer","Order Complete Time","Note"]
    data = data[column_name]

    data.to_excel(rf"Z:\GJH Order\{date}\BC import\BC_Import(Amazon).xlsx", index=False)

